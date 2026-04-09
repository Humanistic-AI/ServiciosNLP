import nltk
import json
import openpyxl
from openai import OpenAI
from app.core.config import OPENAI_API_KEY

nltk.download('punkt_tab')

client = OpenAI(api_key=OPENAI_API_KEY)


def split_into_sentences(text: str) -> list:
    """
    Divides text into sentences using NLTK.
    """
    sentences = nltk.sent_tokenize(text.replace("\n", " "))
    return sentences

def classify_sentences(sentences: list, categories: list[str], examples: str) -> list:
    """
    Sends all sentences to OpenAI in a single request
    and returns the classified results.
    """
    categories_text = "\n".join(f"- {c}" for c in categories)

    numbered_sentences = ""
    for i, sentence in enumerate(sentences):
        numbered_sentences += f"{i+1}. {sentence}\n"

    user_prompt = f"""
        Classify each of the following sentences according to the defined categories.
        Return ONLY a valid JSON object with this exact format, no additional text:
        {{"classifications": [{{"number": 1, "sentence": "text", "classes": ["category1"]}}]}}
        If a sentence does not belong to any category, return "classes": [].

Sentences:
{numbered_sentences}
"""

    system_prompt = f"""
You are a sentence classifier in Spanish.
The available categories are:
{categories_text}

Examples to guide your classification:
{examples}

Respond ONLY with valid JSON, no explanations.
"""

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model="gpt-4o-mini",
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)

def export_to_excel(results: list, categories: list[str], filename: str) -> str:
    """
    Converts classification results to an Excel file.
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    headers = ["sentence"] + categories
    ws.append(headers)

    for item in results:
        row = [item["sentence"]]
        for c in categories:
            row.append(c in item["classes"])
        ws.append(row)

    wb.save(filename)
    return filename

def process_text(text: str, categories: list[str], examples: str, filename: str) -> str:
    """
    Main function that orchestrates the full classification pipeline.
    """
    sentences = split_into_sentences(text)
    response = classify_sentences(sentences, categories, examples)
    results = response["classifications"]    
    export_to_excel(results, categories, filename)
    return filename