import os
import json

def finder(path):
    if os.path.exists(path):
        print(f"The <{path}> Exist")
        if os.path.isdir(path):
            print(f"<{path}> is a Directory")
        elif os.path.isfile(path):
            print(f"<{path}> is a File")
    else:
        print(f"The <{path}> Doesn't Exist")
        
def create(path, content):
    file_path = path
    file_content = content
    with open(file_path, 'w') as file:
        file.write(file_content)
        print(f"The File <{file_path}> has been written")

def main():
    file_path = "sample.txt"
    finder(file_path)
    path = input("Input File name or File path:      ")
    content = input("Input Content:     ")
    
    create(path, content)
    
if __name__ == '__main__':
    main()