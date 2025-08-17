import os
import pandas as pd
# from openai import OpenAI
import openai
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=openai_api_key)
openai.api_key = openai_api_key
client=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
class QAAgent:
    def __init__(self):
        self.documents = {}

    def load_excel(self, file_path):
        df = pd.read_excel(file_path)
        self.documents[file_path] = df
        return df

    def answer_question(self, file_path, question):
        if file_path not in self.documents:
            return "Document not loaded."

        data_str = self.documents[file_path].to_string()
        prompt = f"Given the following data:\n{data_str}\nAnswer this question: {question}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
