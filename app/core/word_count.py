def count_words(text: str) -> dict:
    words = text.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

if __name__ == "__main__":
    sample_text = "Hello world hello"
    result = count_words(sample_text)
    print(result)