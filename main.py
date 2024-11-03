def main():
    with open('books/frankenstein.txt', 'r') as file:
        data = file.read()
        print(data)

main()