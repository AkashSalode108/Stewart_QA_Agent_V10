# AI QA Agent

## Overview
This project builds an AI agent to answer questions based on uploaded documents. Uses OpenAI GPT models for natural language understanding.

## Setup
1. Create a Python virtual environment:

python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

2. Install dependencies:


pip install -r requirements.txt

3. Add your OpenAI API key to a `.env` file:


OPENAI_API_KEY="your_api_key_here"

4. Run the Streamlit app:


streamlit run frontend/app.py


## Folder Structure
- `backend/` → Core QA logic and helpers
- `frontend/` → Streamlit UI
- `data/` → Uploaded/shared documents
