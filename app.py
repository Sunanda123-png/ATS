from dotenv import load_dotenv

load_dotenv()
from PIL import Image
import streamlit as st
import os
import io
import base64
import pdf2image
import google.generativeai as genai



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response= model.generate_content([input, pdf_content[0],prompt])
    try:
        return response.content  # Try accessing content attribute
    except AttributeError:
        try:
            return response.text  # Try accessing text attribute
        except AttributeError:
            print("Unable to extract text from response")
            return None

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        img_bytes_arr = io.BytesIO()
        first_page.save(img_bytes_arr, format = 'JPEG')
        img_bytes_arr = img_bytes_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_bytes_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No Files Uploaded")
    
st.set_page_config(page_title = "ATS RESUME EXPERT")
st.header("ATS Tracking System")
input_text = st.text_area("JOB DESCRIPTION", key = "input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type = ["pdf"])
if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about the resume")
submit2 = st.button("How can i improve my skill")
submit3 = st.button("What are the keyword that are missing")
submit4 = st.button("Percentage match")


input_prompt1= """
You are an experienced HR with Tech Experience in the field of Python, Python developer, django, fastapi, machine learning, datascience, dataengineer,
Your task is to review the provided resume against the job description for these profiles
Please share your proffesional evaluation on whether the candidate's profile align with the highlighted the strength and weaknessof the applicant to the specified job"""

input_prompt3 = """
You are a skilled ATS (Application tracking system scanner with a deep understanding  of Python, Python developer, 
django, fastapi, machine learning, datascience, dataengineer and deep ATS functionality, Your task is evaluate the resume against the provided job description. 
give me the percentage of match if the resume matches job description. First the output should come as a percentage and then keyword missing and final thought)
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume")

