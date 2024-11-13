# opening the book
book_path = "books/frankenstein.txt"
with open(book_path, 'r') as f:
    # Read the file's content
    file_contents = f.read()

    # Print the content
    print(file_contents)

# Count how many words the book contains
num_words = 0

with open(book_path, 'r') as f:
    # Grab each line
    for line in f:
        words = line.split()

        # Add the number of elements per line to the count
        num_words = num_words + len(words)

print(f"There are {num_words} words in the book!")
    