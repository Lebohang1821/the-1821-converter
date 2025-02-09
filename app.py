import streamlit as st
import requests
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API keys from .env file
OCR_SPACE_API_KEY = os.getenv("OCR_SPACE_API_KEY", "helloworld")  # Fallback to free key

OCR_SPACE_URL = "https://api.ocr.space/parse/image"

# Function to load chat history from session state
def load_chat_history():
    return st.session_state.get("chat_history", [])

# Function to save chat history to session state
def save_chat_history(chat_history):
    st.session_state.chat_history = chat_history

# Load chat history
chat_history = load_chat_history()

# Main content
st.title("📄 Document Converter")
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stTextInput>div>div>input {
        border: 2px solid #4CAF50;
        border-radius: 8px;
    }
    @media (max-width: 600px) {
        .main {
            padding: 10px;
        }
        .stButton>button {
            padding: 8px 16px;
            font-size: 14px;
        }
        .stTextInput>div>div>input {
            font-size: 14px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Tab layout for different conversion tools
tabs = st.tabs(["Image to Text", "PDF to Text", "Word to Text"])

# Image to Text Conversion
with tabs[0]:
    st.header("🖼️ Image to Text")
    uploaded_file = st.file_uploader("Upload an Image:", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        # OCR Processing
        with st.spinner("Extracting text... ⏳"):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            payload = {"apikey": OCR_SPACE_API_KEY}
            response = requests.post(OCR_SPACE_URL, files=files, data=payload)
            
            if response.status_code == 200:
                try:
                    extracted_text = response.json()["ParsedResults"][0]["ParsedText"]
                    st.text_area("Extracted Text", extracted_text, height=200)
                    
                    # Save conversion to history
                    chat_history.append({"title": "Image to Text", "content": extracted_text, "date": datetime.now().strftime("%Y-%m-%d")})
                    save_chat_history(chat_history)
                except (KeyError, IndexError):
                    st.error("❌ Error: Unable to extract text.")
            else:
                st.error(f"❌ API Error: {response.status_code}")

# PDF to Text Conversion (Placeholder)
with tabs[1]:
    st.header("📄 PDF to Text")
    st.write("This feature is coming soon!")

# Word to Text Conversion (Placeholder)
with tabs[2]:
    st.header("📝 Word to Text")
    st.write("This feature is coming soon!")
