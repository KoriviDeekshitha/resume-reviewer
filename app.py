import streamlit as st
from groq import Groq

st.set_page_config(page_title="Resume Reviewer", page_icon="📄")
st.title("📄 AI Resume Reviewer")
st.caption("Paste your resume and get instant AI feedback!")

api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

resume_text = st.text_area("Paste your resume here 👇", height=300, placeholder="Copy and paste your full resume text here...")

if st.button("Review My Resume 🚀"):
    if not api_key:
        st.warning("⚠️ Please enter your Groq API key in the sidebar!")
    elif not resume_text:
        st.warning("⚠️ Please paste your resume text!")
    else:
        client = Groq(api_key=api_key)

        with st.spinner("Analyzing your resume..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert resume reviewer with 10 years of experience in HR and recruitment.
                        Review the resume and give feedback in this exact format:

                        ⭐ OVERALL RATING: X/10

                        ✅ STRENGTHS:
                        - Point 1
                        - Point 2
                        - Point 3

                        ❌ WEAKNESSES:
                        - Point 1
                        - Point 2
                        - Point 3

                        💡 IMPROVEMENTS:
                        - Point 1
                        - Point 2
                        - Point 3

                        🎯 FINAL VERDICT:
                        Write 2-3 lines summary here."""
                    },
                    {
                        "role": "user",
                        "content": f"Please review this resume:\n\n{resume_text}"
                    }
                ]
            )

            feedback = response.choices[0].message.content

        st.success("Review Complete! 🎉")
        st.markdown(feedback)