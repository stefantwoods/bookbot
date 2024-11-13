import string

def main():
    book_path = "books/frankenstein.txt"
    #print_book(book_path)
    word_count = print_num_words(book_path)
    my_dict = count_chars(book_path)
    print(f"*****Begin report of {book_path}*****")
    for key, value in my_dict.items():
        print(f"The {key} character was found {value} times!!!")
    print("*****END OF REPORT*****")

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

    return num_words

def count_chars(book_path):
    char_count = {letter: 0 for letter in string.ascii_lowercase}
    # Grab the characters of the book
    with open(book_path, 'r') as f:
        for line in f:
            for word in line:
                for char in word:
                    check = char.lower()
                    # Check if the char is in the dict
                    if check in char_count:
                        char_count[check] = char_count[check] + 1
    return char_count


main()
    