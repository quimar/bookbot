with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    count = len(words)
    print(f"{count} words found in the document") 