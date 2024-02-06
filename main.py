def sort_fn(item: dict[str, int]) -> int:
    return item["count"]


def print_report(stats: dict[str, int]) -> None:
    lst = []
    for key, value in stats.items():
        lst.append({"letter": key, "count": value})
    lst.sort(reverse=True, key=sort_fn)
    for item in lst:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item["letter"]}' character was found {item["count"]} times")


def count_characters(text: str) -> dict[str, int]:
    count_dict = {}

    for char in text:
        lower_char = char.lower()
        count_dict[lower_char] = (
            count_dict[lower_char] + 1 if lower_char in count_dict else 1
        )

    return count_dict


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def main():
    with open("./books/frankenstein.txt") as file:
        content = file.read()
        # print(count_words(content))
        # print(count_characters(content))
        count = count_characters(content)
        print_report(count)


main()
