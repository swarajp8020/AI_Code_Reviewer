# 🩺 Gemini Code Doctor

An AI-powered automated debugging tool that fixes Python code in real-time.
Built with **FastAPI** (Backend), **Streamlit** (Frontend), and **Google Gemini 2.5** (LLM).

## 🚀 Architecture
This project uses a Microservices architecture:
- **Frontend:** Streamlit web interface for user interaction.
- **Backend:** FastAPI server that handles validation and error management.
- **AI Engine:** Google Gemini 2.5 via API for logic analysis and code correction.
- **Resilience:** Implements automatic retry logic (exponential backoff) to handle API instability.

## 🛠️ Tech Stack
- **Python 3.10+**
- **FastAPI** (High-performance API)
- **Pydantic** (Data Validation)
- **Streamlit** (UI/UX)
- **Google Generative AI** (LLM)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/AI_Code_Reviewer.git](https://github.com/YOUR_USERNAME/AI_Code_Reviewer.git)

   Install dependencies:

2. Bash

pip install -r requirements.txt
Configure API Key:

3. Create a file backend/config.py

Add your key: GEMINI_API_KEY = "your_key_here"

4. How to Run
Terminal 1 (Backend):

Bash

cd backend
python server.py
Terminal 2 (Frontend):

Bash

cd frontend
python -m streamlit run app.py

5. 📸 Screenshots
<img width="1605" height="952" alt="image" src="https://github.com/user-attachments/assets/776456be-f0a6-47f7-98df-80738b7726bd" />
