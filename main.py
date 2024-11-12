# opening the book
book_path = "books/frankenstein.txt"
with open(book_path, 'r') as f:
    # Read the file's content
    file_contents = f.read()

    # Print the content
    print(file_contents)