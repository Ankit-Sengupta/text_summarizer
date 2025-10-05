import streamlit as st
import requests
import os
from dotenv import load_dotenv


load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"  
}


st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")
st.title("📝 AI Text Summarizer (Powered by Hugging Face)")
st.write("Paste any article, blog, or text below to get a concise summary in seconds.")


text = st.text_area("Enter text to summarize:", height=300)


def summarize_text(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)

 
    if response.status_code != 200:
        return f"⚠️ Error {response.status_code}: {response.text}"

    data = response.json()
    if isinstance(data, list) and "summary_text" in data[0]:
        return data[0]["summary_text"]
    else:
        return "❌ Unable to generate summary. Please try again later."


if st.button("Summarize"):
    if not text.strip():
        st.warning("⚠️ Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary... ⏳"):
            summary = summarize_text(text)
            st.subheader("📄 Summary:")
            st.write(summary)
