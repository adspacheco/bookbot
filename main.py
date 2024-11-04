def main():
    file_path = "books/frankenstein.txt"
    
    data = read_file(file_path)
    
    words_count = count_words(data)
    chars_count = count_characters(data)
    sorted_chars_count = sort_dict(chars_count)

    report_layout = [
        (f"--- Begin report of {file_path} ---"),
        (f"{words_count} words found in the document"),
        ("Characters found in the document:")
    ]

    for char, count in sorted_chars_count:
        report_layout.append(f"The caracter '{char}' was found {count} times")

    report_layout.append("--- End report ---")

    print_report(report_layout)


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def count_words(data):
    words = data.split()
    return len(words)

def count_characters(data):
    counter = {}
    for char in data.lower():
        if char.isalpha():
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter

def sort_dict(dict):
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list

def print_report(report_layout):
    for line in report_layout:
        print(line)

main()