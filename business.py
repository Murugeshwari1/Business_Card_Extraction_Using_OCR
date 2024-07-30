import easyocr as ocr  # OCR for text extraction
import streamlit as st  # Web App framework
from PIL import Image  # Image processing
import numpy as np  # Numerical operations
import cv2  # OpenCV for image processing

# Set the page layout for the Streamlit app
st.set_page_config(layout="wide")

# Title of the web app
st.title(":orange[Business Card Extraction Using OCR]")
st.write(" ")

# Create columns for layout
col1, col2, col3 = st.columns([3, 0.5, 4.5])
with col1:
    # Image uploader widget
    st.write("## Upload Image")
    image = st.file_uploader(label="", type=['png', 'jpg', 'jpeg'])

# Function to load the EasyOCR model
@st.cache_resource
def load_model():
    reader = ocr.Reader(['en'])  # Initialize the OCR reader for English
    return reader

reader = load_model()  # Load the OCR model

# Function to check if there is a large vertical gap between two bounding boxes
def is_large_vertical_gap(bbox1, bbox2, threshold=20):
    return abs(bbox2[0][1] - bbox1[2][1]) > threshold

# Function for pre-processing the image to improve OCR accuracy
def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive histogram equalization to enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(blurred)
    
    # Apply bilateral filter for noise reduction while preserving edges
    denoised = cv2.bilateralFilter(enhanced, 9, 75, 75)
    
    return denoised

# Main logic to process the uploaded image
if image is not None:
    input_image = Image.open(image)  # Open the uploaded image
    input_image_np = np.array(input_image)  # Convert to numpy array for processing
    preprocessed_image = preprocess_image(input_image_np)  # Pre-process the image
    
    with col1:
        st.image(preprocessed_image, channels="GRAY")  # Display the pre-processed image
    
    # Perform OCR to extract text and bounding boxes
    result = reader.readtext(preprocessed_image, detail=1)
    result_text = [text[1].strip() for text in result]  # Extract text from OCR result
    bboxes = [text[0] for text in result]  # Extract bounding boxes from OCR result
    
    st.write("### Debug Information")
    st.write(result_text)  # Display OCR result text for debugging

    # Initialize variables for company name and card holder name
    company_name = ""
    card_holder_name = ""

    # Logic to extract company name and card holder name based on vertical gaps
    if len(result_text) > 1:
        if is_large_vertical_gap(bboxes[0], bboxes[1]):
            company_name = result_text[0]
            if len(result_text) > 2:
                card_holder_name = result_text[1]
        else:
            company_name = (result_text[0] + " " + result_text[1])
            if len(result_text) > 2:
                card_holder_name = result_text[2]

    with col3:
        # Display the extracted company name and card holder name
        st.write('##### :red[Card Holder & Company Details:]')
        if company_name:
            st.write('##### Company Name: ' + company_name)
        if card_holder_name:
            st.write('##### Card Holder: ' + card_holder_name)
