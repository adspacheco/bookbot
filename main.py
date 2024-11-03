def main():
    file_path = 'books/frankenstein.txt'
    data = read_file(file_path)
    words_count = count_words(data)
    print(data)
    print(f'Total words in file: {words_count}')

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def count_words(data):
    words = data.split()
    return len(words)

main()