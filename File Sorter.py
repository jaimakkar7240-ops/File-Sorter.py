import os
import shutil

file_path = input("Enter folder/directory path:\n")
categories = {
'Documents' : ['.pdf', '.docx', '.txt'],
'Images' : ['.png', '.jpg', '.jpeg'],
'Audio' : ['.mp3', '.m4a', '.aac', '.wav'],
}

if os.path.isfile(file_path):
    print("Please enter a Directory.")

elif os.path.exists(file_path):
    entries = os.listdir(file_path)
    print("Valid Path: The path exists.")

    if os.path.isdir(file_path):
        print("This is a directory.")
        print(f"The entries in this folder/directory are:\n {entries}")
    
    with os.scandir(file_path) as data:
        for entry in data:

            if entry.is_dir():
                continue

            if entry.is_file():
                name, ext = os.path.splitext(entry.name)
                file_ext = ext.lower() 
                
                print(f"File: {entry.name} | Extension: {file_ext}")
                
                category = "Others"
            
            for category_name, extensions in categories.items():
                if file_ext in extensions : 
                    category = category_name
                    break
            
            source_path = os.path.join(file_path, entry.name)
            dest_folder = os.path.join(file_path, category)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(source_path, dest_folder)

            print(f"Moved: {entry.name} -> {category}")
            
else:
    print("Invalid Path: The path does not exist.")
 



 




 







 




