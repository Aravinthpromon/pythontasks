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

    
    output_file = os.path.join(os.getcwd(), "file_list.txt")
    
    with open(output_file, "w") as file_writer:
        file_writer.write(f"Files in '{directory}':\n")
        for file in files:
            file_writer.write(f"  {file}\n")  
    
    print(f"File list has been written to: {output_file}")

directory_path = input("Enter the path of the directory to list files and directories: ")

list_files(directory_path)
