import re

# Simple stopword list (can grow later)
STOPWORDS = {
    "el", "la", "los", "las",
    "un", "una", "unos", "unas",
    "y", "o", "pero",
    "de", "del",
    "que", "en",
    "por", "para",
    "con", "sin",
    "sobre", "entre",
    "al", "lo"
}


def normalize_text(text: str) -> list[str]:
    """
    Normalize text by:
    1. Lowercasing
    2. Removing punctuation
    3. Splitting into tokens
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation using regex
    text = re.sub(r"[^\w\sáéíóúüñ]", "", text)

    # Split into words
    words = text.split()

    return words


def count_words(text: str) -> dict:
    """
    Count words in text while removing stopwords.
    """

    words = normalize_text(text)
    counts = {}

    for word in words:
        # Skip stopwords
        if word in STOPWORDS:
            continue

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


if __name__ == "__main__":
    sample_text = "Hola mundo, hola mundo! El mundo es grande y el mundo es interesante."
    result = count_words(sample_text)
    print(result)