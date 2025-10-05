# 🧾 Documentation: Text Summarizer using Hugging Face API

This document records every step I took while building my AI-powered **Text Summarizer** app — including what I tried, what failed, and how I finally got it working.

---

## 🧩 Project Overview

**Goal:** Build a small AI-powered app that summarizes long text into 2–3 concise sentences.  
**Final Tool Used:** Hugging Face API  
**Deployment Platform:** Render  

---

## 🧠 Step-by-Step Journey

### 🧰 Step 1: Setting Up the Environment
- Installed **Python 3.10** on my system.  
- Created a virtual environment to manage dependencies:
  ```bash
  python -m venv venv
  source venv/bin/activate   # or venv\Scripts\activate on Windows
  ```
- Installed basic libraries:
  ```bash
  pip install requests streamlit python-dotenv
  ```

---

### ⚙️ Step 2: Exploring the OpenAI API (First Attempt)
- I initially tried to use the **OpenAI API** for text summarization.  
- Generated an API key and wrote a Python script using the `openai` package.  
- However, when I ran the program, I received an **“Quota Exceeded”** error — the free tier limit was reached.  
- I searched for alternative APIs and found **Hugging Face Inference API** to be a great free alternative.

**Result:** ❌ Failed due to OpenAI quota limits.

---

### 🤖 Step 3: Switching to Hugging Face API
- Signed up on [Hugging Face](https://huggingface.co).  
- Generated a new **Hugging Face API key**.  
- Updated my Python code to use the following endpoint:
  ```
  https://api-inference.huggingface.co/models/facebook/bart-large-cnn
  ```
- Sent requests using the `requests` library:
  ```python
  response = requests.post(API_URL, headers={"Authorization": f"Bearer {API_KEY}"}, json={"inputs": text})
  ```
- Parsed the summary successfully.

**Result:** ✅ Success — working text summarization with Hugging Face API.

---

### 💻 Step 4: Adding a Simple User Interface
- Decided to use **Streamlit** for a minimal and interactive UI.  
- Created an `app.py` file with an input box for text and a button to generate a summary.  
- Ran it locally:
  ```bash
  streamlit run app.py
  ```
- Verified that the summarizer worked perfectly in the browser.

**Result:** ✅ Local Streamlit app running smoothly.

---

### ☁️ Step 5: Deployment Attempts

#### 🧩 Attempt 1 – GitHub Pages
- Tried deploying using GitHub Pages.  
- Found out it only supports static websites (HTML/CSS/JS).  
- Since Streamlit requires a Python backend, it wasn’t suitable.

**Result:** ❌ Not compatible for Streamlit apps.

#### 🤗 Attempt 2 – Hugging Face Spaces
- Tried using Hugging Face Spaces for deployment.  
- Required YAML configuration and sometimes build errors occurred during model loading.  
- Decided it was too complex for this small project.

**Result:** ⚠️ Complicated setup.

#### 🌐 Attempt 3 – Render (Final Choice)
- Render provides **free hosting for Python web apps**.  
- Created a new Web Service on [Render](https://render.com).  
- Uploaded the project and added my Hugging Face API key as an environment variable.  
- Used this **Start Command**:
  ```bash
  streamlit run app.py --server.port $PORT --server.address 0.0.0.0
  ```
- Deployment succeeded and the app was live.

**Result:** ✅ Successfully deployed using Render.

---

### ✅ Step 6: Final Testing
- Tested the summarizer with a few paragraphs and news articles.  
- Output was concise, accurate, and worked consistently.  
- Verified that API requests were handled within limits.

---

## 🔍 Summary of Tools & Decisions

| Step | Tool/Platform | Result | Notes |
|------|----------------|---------|-------|
| OpenAI API | Text generation | ❌ Failed | Exceeded free quota |
| Hugging Face API | Summarization | ✅ Success | Free and stable |
| GitHub Pages | Deployment | ❌ Failed | Only supports static sites |
| Hugging Face Spaces | Deployment | ⚠️ Complex | Required setup YAML |
| Render | Deployment | ✅ Success | Simple and works perfectly |

---

## 📦 Final Project Structure
```
text-summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
├── README.md
└── Documentation.md
```

---

## 🏁 Conclusion
This project taught me how to:
- Integrate AI APIs like OpenAI and Hugging Face.  
- Handle API errors and switch to alternatives.  
- Deploy an AI app easily using Render.  

Overall, it was a great learning experience in both **AI integration** and **deployment**.

---

**Author:** [Ankit Sengupta]  
**Intern Assignment:** Build a Tiny AI-Powered App  
**Deployed on:** [Render](https://render.com)
