# Secure-Deleter
 The Python script performs secure deletion of a specified folder on a Windows system. 

 Script Overview:

Import Statements:

import os: Provides a way to interact with the operating system, including file and directory operations.
import shutil: Offers high-level file operations, such as file copying and removal.
Function Definition (secure_delete):

def secure_delete():: Defines a function named secure_delete that encapsulates the secure deletion logic.
Hardcoded Folder Path:

folder_path = r"C:\path\to\your\folder": Hardcodes the path to the folder you want to securely delete. Modify this path to match the actual folder path.
Try-Except Block:

try: and except Exception as e:: Encloses the main logic within a try-except block to catch and handle any exceptions that might occur during execution.
Secure Deletion Logic:

for root, dirs, files in os.walk(folder_path):: Iterates through the contents of the specified folder using os.walk.
for file in files:: Iterates through the files in each directory.
file_path = os.path.join(root, file): Constructs the full path of each file.
os.remove(file_path): Deletes each file using os.remove.
shutil.rmtree(folder_path): Removes the empty folder using shutil.rmtree.
Print Statements:

print(f"Folder '{folder_path}' securely deleted."): Prints a success message after the secure deletion process.
Exception Handling:

except Exception as e:: Catches and handles any exceptions that might occur during the execution, printing an error message.
Main Block (if __name__ == "__main__":):

if __name__ == "__main__":: Ensures that the script's main logic is executed only if the script is run directly (not imported as a module).
Function Invocation (secure_delete()):

secure_delete(): Calls the secure_delete function when the script is executed.
Note:

Ensure that you have the necessary permissions to delete files and directories.
Modifying hardcoded paths and understanding the consequences of secure deletion is crucial.
The script assumes a Windows environment; adjustments may be needed for other operating systems.
