# files=open('content.txt', 'r')
# print(files.read())
# files.close()

# with open ('content.txt','r') as file:
#     content=file.read()
#     print(content)

# with open("content.txt", "r") as file:
#     print(file.read())        # Entire content
#     file.seek(0)              # Reset cursor to start
#     print(file.readline())    # First line
#     file.seek(0)
#     print(file.readlines())   # List of all lines

with open ('content1.txt', 'w') as file:
    file.write("I Love petite girls \n")
    file.write("This is a new file")

with open ('content1.txt', 'a') as file:
    file.write("\n Appending this line.")


# Implementing the practice problems as requested

# Problem 1: Word Counter
def word_counter(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

# Problem 2: Write and Read
def write_and_read(filename, lines):
    try:
        with open(filename, "w") as file:
            file.writelines(lines)
        with open(filename, "r") as file:
            return file.read()
    except Exception as e:
        return f"Error: {str(e)}"

# Problem 3: File Copier
def file_copier(source_filename, destination_filename):
    try:
        with open(source_filename, "r") as source, open(destination_filename, "w") as destination:
            for line in source:
                destination.write(line)
        return f"Content from '{source_filename}' copied to '{destination_filename}'."
    except FileNotFoundError:
        return f"Error: The file '{source_filename}' was not found."

# Problem 4: Search in File
def search_in_file(filename, search_word):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            result_lines = [line for line in lines if search_word in line]
            return result_lines if result_lines else f"'{search_word}' not found in the file."
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

# Testing the problems with sample data (Note: These files should exist for actual testing)

# Sample content
sample_filename = "content.txt"
with open(sample_filename, "w") as f:
    f.write("Hello World!\nThis is a sample file for testing.\nPython file handling is fun!")

# Testing Word Counter
word_count_result = word_counter(sample_filename)

# Testing Write and Read
lines_to_write = ["This is the first line.\n", "This is the second line.\n"]
write_and_read_result = write_and_read("write_and_read.txt", lines_to_write)

# Testing File Copier
file_copier_result = file_copier(sample_filename, "copied_sample.txt")

# Testing Search in File
search_word = "Python"
search_in_file_result = search_in_file(sample_filename, search_word)

# Output results
practice_results = {
    "word_counter": word_count_result,
    "write_and_read": write_and_read_result,
    "file_copier": file_copier_result,
    "search_in_file": search_in_file_result,
}

practice_results

