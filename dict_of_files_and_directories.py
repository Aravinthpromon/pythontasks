import os  

def list_files_and_directories(directory):
    if not os.path.exists(directory):  
        print(f"Directory not found: {directory}")
        return

    result = {
        "files": [],
        "directories": []
    }

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)  

        if os.path.isfile(full_path):  
            result["files"].append(item)
        elif os.path.isdir(full_path):  
            result["directories"].append(item)

    print("Files and Directories Dictionary:")
    print(result) 

directory_path = input("Enter the path of the directory to list files and directories: ")

list_files_and_directories(directory_path)
