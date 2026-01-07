import streamlit as st
import requests

st.set_page_config(page_title="Gemini Code Doctor", page_icon="🩺", layout="wide")

st.title("🩺 Gemini Code Doctor V2.0")
st.markdown("### AI-Powered Debugger for Python, Java, C++, and Go")

col1, col2 = st.columns([1, 3])

with col1:
    language = st.selectbox("Select Language:", ("Python 🐍", "Java ☕", "C++ 🚀", "Go 🐹"))

task_map = {
    "Python 🐍": "fix_python",
    "Java ☕": "fix_java",
    "C++ 🚀": "fix_cpp",
    "Go 🐹": "fix_go"
}

with col2:
    code_input = st.text_area("Paste your broken code here:", height=300)

if st.button("Analyze & Explain 🧠", type="primary"):
    if not code_input:
        st.warning("Please paste some code first!")
    else:
        with st.spinner(f"Analyzing {language} Logic..."):
            try:
                # Update to your RENDER URL
                response = requests.post(
                    "https://gemini-api-swaraj.onrender.com/review", 
                    json={"code": code_input, "task": task_map[language]},
                    headers={"X-Service-Token": "SWARAJ_SECURE_2026"} # <--- THE KEY
                )
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("Analysis Complete!")
                    res_col1, res_col2 = st.columns(2)
                    with res_col1:
                        st.subheader("🧐 Why it failed:")
                        st.info(data.get("bug_report", "No explanation provided."))
                    with res_col2:
                        st.subheader("✅ The Fix:")
                        st.code(data.get("fixed_code", "# Error"), language=language.split()[0].lower())
                else:
                    st.error(f"Server Error: {response.status_code}")
            except Exception as e:
                st.error(f"Connection Failed: {e}")