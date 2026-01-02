import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import uvicorn
import logging
import json

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    from config import GEMINI_API_KEY
    api_key = GEMINI_API_KEY
except ImportError:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No API Key found! Set GEMINI_API_KEY environment variable.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

class CodeRequest(BaseModel):
    code: str
    task: str = "fix"  # Default to 'fix' so it works with old & new frontends

    @field_validator('code')
    def check_code_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Code cannot be empty/blank!')
        return v

@app.get("/")
def greet():
    return {"message": "Gemini AI Server is Running 🟢"}

# --- THE CORE LOGIC ---
@app.post("/review")
def review_code(request: CodeRequest):
    logging.info(f"Received Request: {request.task} (Length: {len(request.code)})")
    
    # Dynamic Prompting (Ready for your future upgrade)
    instruction = "Fix the bugs in this code."
    if request.task == "convert_to_java":
        instruction = "Convert this code to production-ready Java."
    elif request.task == "convert_to_python":
        instruction = "Convert this code to clean Python."

    prompt = f"""
    You are a Senior Developer. {instruction}
    Return ONLY a JSON object with this format:
    {{ "fixed_code": "YOUR_CODE_HERE" }}
    
    The Code:
    {request.code}
    """
    
    attempts = 0
    max_retries = 2
    
    while attempts < max_retries:
        try:
            logging.info(f"Attempt {attempts+1}...")
            response = model.generate_content(prompt)
            
            # Clean and Parse
            cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned_text)
            return data

        except Exception as e:
            logging.error(f"Attempt {attempts+1} failed: {e}")
            attempts += 1
            # We DO NOT return here. We let the loop run again.

    # If we exit the loop, it means we failed all retries
    return {"fixed_code": "# Error: Server busy. Please try again."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))