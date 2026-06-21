import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(report_text: str):

    prompt = f"""
    You are a medical report assistant.

    Analyze the blood report and provide:

    1. Summary
    2. Abnormal values
    3. Possible concerns
    4. Simple explanation

    Blood Report:

    {report_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def answer_question(
    question: str,
    context: str
):

    prompt = f"""
    You are a blood report assistant.

    Use only the supplied context.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text