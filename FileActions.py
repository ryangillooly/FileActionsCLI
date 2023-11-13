import shutil
import os

# Define the "Copy" function
def Copy(sourcePath, destinationPath):
    destinationFileExists = os.path.exists(destinationPath)
    dontOverride = False

    if destinationFileExists:
        confirmation = input("The destination file already exists. Should it be overwritten?: ")
        dontOverride = confirmation != "Yes"

    if dontOverride:
        print(f"User selected NOT to override {destinationPath}. The program will exit.")
        return
    
    try:    
        copyResponse = shutil.copy(sourcePath, destinationPath)
        print(f"Source file {sourcePath} was copied to {destinationPath}")
    except:
        print(f"An error occured. The file was not successfully copied to {destinationPath}")
            
    return

# Define the "Move" function
def Move(sourcePath, destinationPath):
    destinationFileExists = os.path.exists(destinationPath)
    dontOverride = False

    if destinationFileExists:
        confirmation = input("The destination file already exists. Should it be overwritten?: ")
        dontOverride = confirmation != "Yes"

    if dontOverride:
        print(f"User selected NOT to override {destinationPath}. The program will exit.")
        return

    try:    
        copyResponse = shutil.move(sourcePath, destinationPath)
        print(f"Source file {sourcePath} was moved to {destinationPath}")
    except:
        print(f"An error occured. The file was not successfully moved to {destinationPath}")
            
    return

# Define the "Delete" function
def Delete(filePath):
    try:    
        deleteResponse  = os.remove(filePath)
        fileStillExists = os.path.exists(filePath)
        if fileStillExists:
            print(f"File was marked as removed, but still exists...")
        else:
            print(f"File {filePath} has been deleted")
    except:
        print(f"An error occured. The file {filePath} was not deleted.")
            
    return