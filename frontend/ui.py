import streamlit as st
from backend.qa_agent import QAAgent 
from backend.utils import allowed_file, save_uploaded_file

def app_ui():
    st.set_page_config(page_title="AI QA Agent", layout="wide")
    st.title("AI-Powered Document QA Agent")

    qa_agent = QAAgent()
    file_path=r"C:\Users\akash\Desktop\Assignments\stewert_assignment\Stewart_QA_Agent_V11\data\data.xlsx"

    # uploaded_file = st.file_uploader("Upload a document", type=['xlsx', 'csv', 'pdf'])

  
    qa_agent.load_excel(file_path)

    question = st.text_input("Enter your question:")
    if st.button("Get Answer") and question:
        answer = qa_agent.answer_question(file_path, question)
        st.write("**Answer:**", answer)
