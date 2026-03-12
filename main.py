import os
import sys
import re
from collections import Counter


def get_words(text: str):
    text = text.lower()

    words = re.findall(r"\b\w+\b", text)

    return words


def analyze_frequency(file_path: str):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = get_words(text)

    counter = Counter(words)

    top_words = counter.most_common(10)

    print("\n--Top 10 most frequent words:\n")

    for i, (word, count) in enumerate(top_words, start=1):
        print(f"{i:>2}. {word:<15} {count}")


def main():

    # si se pasó un archivo como argumento
    if len(sys.argv) >= 2:
        file_path = sys.argv[1]

    else:
        # intetnar usar input.txt por defecto
        default_file = "input.txt"

        if os.path.exists(default_file):
            file_path = default_file
            print("No input file provided. Using default: input.txt")
        else:
            print("Usage: python main.py input.txt")
            sys.exit(1)

    print(f"Analyzing word frequency in: {file_path}")

    analyze_frequency(file_path)


if __name__ == "__main__":
    main()