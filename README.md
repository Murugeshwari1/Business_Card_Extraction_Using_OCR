**PROJECT OVERVIEW**


The objective of this project is to develop a comprehensive solution for accurately extracting the Organization 
Name and Person Name from images of business cards using Optical Character Recognition (OCR) technology. 
This solution is designed to address and handle various image quality scenarios such as different lighting 
conditions, angles, and levels of clarity to ensure that text extraction is both precise and reliable.


**APPROACH**


**1. Model Selection:** To address the OCR task, we selected EasyOCR, an open-source OCR model known for its 
high accuracy and ease of integration. EasyOCR supports multiple languages and can handle diverse text formats, 
making it suitable for business cards with different layouts and text styles.

**2. Library and Tool Selection**

**EasyOCR:** Chosen for its robustness and support for multiple languages.

**Streamlit:** Selected for building a simple and user-friendly interface to facilitate image upload and display the 
extracted information.

**OpenCV:** Used for pre-processing images to enhance text extraction accuracy. OpenCV provides various image
processing techniques such as filtering, contrast adjustment, and noise reduction.

**NumPy:** Employed for efficient handling of image arrays and numerical operations
