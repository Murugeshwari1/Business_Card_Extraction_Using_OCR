**BUSINESS CARD DATA EXTRACTION USING OCR**


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


**FRONTEND**

![1](https://github.com/user-attachments/assets/f9fe73ca-40c1-4c10-8b3c-32e227e60a33)


**BUSINESS CARD DATA EXTRACTION USING OCR**

![2](https://github.com/user-attachments/assets/bd12532a-0c81-4d7f-b4dd-ac01ac5989ea)


![3](https://github.com/user-attachments/assets/4c5695e0-46e4-4f24-9a1f-2c05f4ba52dd)



In some cases, business cards might not include a cardholder's name, focusing solely on the company name. Our application is designed to accurately predict and extract the company name from such business cards. This ensures that even when the cardholder's name is absent, users can still obtain valuable company information efficiently.

![4](https://github.com/user-attachments/assets/735951ee-d47b-4980-bccf-38123b69af9f)

