import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Gemini Code Doctor", page_icon="🩺", layout="centered")

# Header
st.title("🩺 Gemini Code Doctor")
st.write("### AI-Powered Python Debugger")
st.info("Built with FastAPI, Streamlit, and Google Gemini 2.5")

# Input Area
code_input = st.text_area("Paste your broken Python code here:", height=250)

# Action Button
if st.button("Analyze & Fix 🚑", type="primary"):
    if not code_input:
        st.warning("⚠️ Please paste some code first!")
    else:
        with st.spinner("🤖 AI is analyzing your logic..."):
            try:
                # connecting to the local backend
                response = requests.post(
                    "https://gemini-api-swaraj.onrender.com/review", 
                    json={"code": code_input, "task": "fix"}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    fixed_code = data.get("fixed_code", "# No code returned")
                    
                    st.success("✅ Analysis Complete!")
                    st.subheader("Your Fixed Code:")
                    st.code(fixed_code, language="python")
                else:
                    st.error(f"❌ Server Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"❌ Connection Failed. Is the backend running?\nError: {e}")