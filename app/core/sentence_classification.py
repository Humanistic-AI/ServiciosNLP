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

def classify_sentences(sentences: list, classes: list) -> list:
    """
    Sends all sentences to OpenAI in a single request
    and returns the classified results.
    """
    # Build the classes section of the system prompt
    prompt_classes = ""
    for clase in classes:
        prompt_classes += f"\nClass: {clase['nombre']}\n"
        prompt_classes += f"Description: {clase['descripcion']}\n"
        prompt_classes += f"Examples: {clase['ejemplos']}\n"

    # Build the numbered list of sentences
    numbered_sentences = ""
    for i, sentence in enumerate(sentences):
        numbered_sentences += f"{i+1}. {sentence}\n"

    user_prompt = f"""
Classify each of the following sentences according to the defined classes.
Return ONLY a valid JSON with this format, no additional text:
[{{"number": 1, "sentence": "text", "classes": ["class1"]}}, ...]
If a sentence does not belong to any class, return "classes": [].

Sentences:
{numbered_sentences}
"""

    system_prompt = f"""
You are a sentence classifier in Spanish.
The available classes are:
{prompt_classes}
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

def export_to_excel(results: list, classes: list, filename: str) -> str:
    """
    Converts classification results to an Excel file.
    Returns the filename.
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    # Build header row
    headers = ["sentence"] + [c["nombre"] for c in classes]
    ws.append(headers)

    # Build data rows
    for item in results:
        row = [item["sentence"]]
        for c in classes:
            row.append(c["nombre"] in item["classes"])
        ws.append(row)

    wb.save(filename)
    return filename

def process_text(text: str, classes: list, filename: str) -> str:
    """
    Main function that orchestrates the full classification pipeline.
    Returns the filename of the generated Excel.
    """
    sentences = split_into_sentences(text)
    results = classify_sentences(sentences, classes)
    export_to_excel(results, classes, filename)
    return filename