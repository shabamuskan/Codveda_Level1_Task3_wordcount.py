def word_counter(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

# Example usage
filename = input("Enter the file name: ")
print("Word count:", word_counter(filename))
