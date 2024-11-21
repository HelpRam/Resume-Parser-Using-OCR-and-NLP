import streamlit as st
import pytesseract
from pdf2image import convert_from_path
import re
import spacy
from io import BytesIO
from PIL import Image
from spacy.cli import download
import tempfile
# Download the model 
download("en_core_web_sm")


# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Define a sample list of common skills for matching
SKILLS = [
    "Python", "Java", "C++", "Machine Learning", "Deep Learning", "Data Analysis",
    "Natural Language Processing", "Cloud Computing", "Project Management",
    "Communication", "SQL", "Docker", "Kubernetes", "TensorFlow", "PyTorch",
    "Leadership", "Teamwork", "Analytical Thinking", "Problem Solving"
]

# Extract text from the PDF using OCR
def extract_text(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    images = convert_from_path(tmp_file_path)
    extracted_text = ""
    for i, image in enumerate(images):
        page_text = pytesseract.image_to_string(image)
        extracted_text += f"\n\nPage {i + 1}:\n{page_text}"

    return extracted_text

# Extract entities using SpaCy
def extract_entities(text):
    doc = nlp(text)
    entities = {
        "Names": [ent.text for ent in doc.ents if ent.label_ == "PERSON"],
        "Organizations": [ent.text for ent in doc.ents if ent.label_ == "ORG"],
        "Locations": [ent.text for ent in doc.ents if ent.label_ in {"GPE", "LOC"}],
        "Dates": [ent.text for ent in doc.ents if ent.label_ == "DATE"],
    }
    return entities

# Extract skills by keyword matching
def extract_skills(text):
    text_lower = text.lower()
    matched_skills = [skill for skill in SKILLS if skill.lower() in text_lower]
    return matched_skills

# Enhanced Streamlit UI
st.set_page_config(page_title="Resume Parser", page_icon="📄", layout="wide")

st.title("📄 Resume Parser: Extract and Analyze Key Information")
st.write(
    """
    **Upload your PDF resume to extract and analyze key details!**
    This application uses **OCR and NLP** to identify names, organizations, locations, and dates. 
    """
)



# File upload section
uploaded_file = st.file_uploader(
    "📤 Upload a PDF Resume", type=["pdf"], help="Only PDF files are supported."
)

if uploaded_file is not None:
    st.sidebar.success("✅ File Uploaded Successfully!")
    
    with st.spinner("🔍 Processing... Please wait."):
        extracted_text = extract_text(uploaded_file)
        entities = extract_entities(extracted_text)
        skills = extract_skills(extracted_text)

    # Display extracted text
    st.subheader("📄 Extracted Text")
    st.text_area("Extracted Text from Resume", extracted_text, height=200)

    # Highlighted Entities
    st.subheader("🔍 Extracted Entities")
    for category, items in entities.items():
        color = (
            "blue" if category == "Names"
            else "green" if category == "Organizations"
            else "orange" if category == "Locations"
            else "red" if category == "Dates"
            else "black"
        )
        st.markdown(f"### **{category}:**")
        if items:
            for item in items:
                st.markdown(
                    f"<span style='color:{color}; font-weight:bold;'>{item}</span>",
                    unsafe_allow_html=True,
                )
        else:
            st.write(f"No {category.lower()} found.")

    # Display extracted skills
    st.subheader("🛠️ Extracted Skills")
    if skills:
        for skill in skills:
            st.markdown(
                f"<span style='color:purple; font-weight:bold;'>{skill}</span>",
                unsafe_allow_html=True,
            )
    else:
        st.write("No skills found.")

    # Download Section
    st.subheader("📥 Download Results")
    with open("extracted_text.txt", "w") as f:
        f.write(extracted_text)
    st.download_button(
        label="Download Extracted Text",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain",
    )
else:
    st.warning("⚠️ Please upload a file to proceed.")