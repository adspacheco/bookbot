def main():
    file_path = 'books/frankenstein.txt'
    data = read_file(file_path)
    words_count = count_words(data)
    chars_count = count_characters(data)
    print(f'Total words in file: {words_count}')
    print(f'Characters count: {chars_count}')
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def count_words(data):
    words = data.split()
    return len(words)

def count_characters(data):
    counter = {}
    for char in data.lower():
        if char.isalnum():
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter

main()