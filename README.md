# 🩺 Gemini Code Doctor - https://aicodereviewer-swaraj.streamlit.app/

**An AI-powered Microservice for Automated Code Debugging.**
*Deployed with FastAPI (Backend) and Streamlit (Frontend).*

## 🏗️ Architecture
This project demonstrates a production-grade **Microservices Architecture**:
* **The Brain (Backend):** A FastAPI server that handles validation (Pydantic), error handling, and LLM orchestration (Google Gemini 2.5).
* **The Face (Frontend):** A Streamlit interface that consumes the backend API via HTTP requests.
* **Resilience:** Implements a custom retry mechanism with exponential backoff to handle transient API failures.

## 🛠️ Tech Stack
- **Python 3.10+**
- **FastAPI** (High-performance API)
- **Pydantic** (Data Validation)
- **Streamlit** (UI/UX)
- **Google Generative AI** (LLM)


## 🚀 Quick Start
1.  **Clone the repo:**
    `git clone https://github.com/swarajp8020/AI_Code_Reviewer.git`
2.  **Install dependencies:**
    `pip install -r requirements.txt`
3.  **Run the System:**
    * Backend: `python backend/server.py`
    * Frontend: `streamlit run frontend/app.py`

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
