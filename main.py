def main():
    book_path = "books/frankenstein.txt"
    print_book(book_path)
    print_num_words(book_path)

# Prints the entire book
def print_book(book_path):
    with open(book_path, 'r') as f:
        # Read the file's content
        file_contents = f.read()

        # Print the content
        print(file_contents)

# Prints the number of words in a book
def print_num_words(book_path):
    with open(book_path, 'r') as f:
        num_words = 0

        # Grab each line
        for line in f:
            words = line.split()

            # Add the number of elements per line to the count
            num_words = num_words + len(words)

    print(f"There are {num_words} words in the book!")

main()
    