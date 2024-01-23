import os
import shutil

def secure_delete():
    folder_path = r"C:\Users\marke\Desktop\New folder"  # Hardcoded path for Windows

    try:
        # Recursively delete the contents of the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)

        # Remove the empty folder
        shutil.rmtree(folder_path)

        print(f"Folder '{folder_path}' securely deleted.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    secure_delete()
