import os  

def list_files(directory):

    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")  
        return

    items = os.listdir(directory)

    files = []
    
    for item in items:
        full_path = os.path.join(directory, item)


        if os.path.isfile(full_path):
            files.append(item)  

    print(f"Files in '{directory}':")
    for file in files:
        print(f"  {file}")  

directory_path = input("Enter the path of the directory to list files and directories: ")

list_files(directory_path)

