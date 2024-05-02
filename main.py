import sys


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_letter_counts(words: list[str]) -> dict[str, int]:
    d: dict[str, int] = {}

    for word in words:
        lower_case_word = word.lower()

        for letter in lower_case_word:
            if letter in d:
                d[letter] += 1

            else:
                d[letter] = 1

    return d


def sort_on(d: dict[str, str, str, int]) -> str:
    return d["count"]


def convert_dict(d: dict[str, int]) -> list[dict[str, str, str, int]]:
    lst = []

    for c in d:
        if c.isalpha():
            lst.append({"char": c, "count": d[c]})

    lst.sort(reverse=True, key=sort_on)

    return lst


def main() -> int:

    with open("./books/frakenstien.txt") as f:
        contents = f.read()
        word_count = count_words(contents)
        letter_dict = get_letter_counts(contents.split())

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        for count in convert_dict(letter_dict):
            c = count["char"]
            n = count["count"]

            print(f"The '{c}' character was found {n} times")

        print("--- End report ---")

    return 0


if __name__ == "__main__":
    sys.exit(main())
