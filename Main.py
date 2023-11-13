import os
import Validation
import FileActions

# Clear the console screen
os.system("clear")

# This runs the input gathering, and input validation
validationResponse = Validation.Validate()

# Set fileAction variable to the "Value" of the Key called "FileAction", within the validationResponse Dictionary object
fileAction = validationResponse["FileAction"]

# If FileAction = Copy or Move, then Set Source/Destination variables to the "Value" of the 
# Key called "Source", and "Destination", from within the validationResponse Dictionary object
if fileAction in ["copy", "move"]:
    source      = validationResponse["Source"]
    destination = validationResponse["Destination"]

# If FileAction = Delete, then Set filePath variable to the "Value" of the 
# Key called "FilePath], from within the validationResponse Dictionary object
if fileAction == "delete":
    filePath = validationResponse["FilePath"]

# Route the FileAction type, to the specific FileAction function to handle it
if   fileAction == "copy"   : FileActions.Copy(source, destination)
elif fileAction == "move"   : FileActions.Move(source, destination)
elif fileAction == "delete" : FileActions.Delete(filePath)
