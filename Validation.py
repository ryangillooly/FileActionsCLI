import os
import sys

# The validate function will perform the File Action Input validation, and the
# File Action Configuration validation (based on the chosen FileAction). It will 
# then return a Dictionary object, with the FileAction type, and any configuration data
def Validate():
    fileActionsInput  = ValidateFileActionsInput()
    fileActionsConfig = ValidateFileActionsConfiguration(fileActionsInput)

    return {
        "FileAction": fileActionsInput,
        **fileActionsConfig
    }

# This will validate the inputs when selecting a file action to perform
def ValidateFileActionsInput():
    fileActions = ["copy", "move", "delete"]
    fileActionsString = ", ".join(fileActions)

    while True:
        print("\nSelect a file action from the following options:")
        for action in fileActions:
            print(f"- {action}")

        fileActionInput = input(f"\nEnter your choice: ").lower()

        if fileActionInput in fileActions: 
            return fileActionInput
        else:
            print("Invalid input. Please enter a valid file action.")

# This will validate the configuration inputs for each different file action
# and then will return the configuration inputs
def ValidateFileActionsConfiguration(fileActionInput):
    if fileActionInput in ["copy", "move"]: 
        input = ValidateCopyMoveActionInput()

    elif fileActionInput == "delete":  
        input = ValidateDeleteActionInput()

    return input

# This validates the inputs for the Copy and Move FileAction's
def ValidateCopyMoveActionInput():
    while True:
        # Source Path Validation
        sourcePathInput = input("Enter the full path of the file to copy: ")

        # TODO: add extra validation to make sure it's parsing the file exists, not directory
        validSoucePath = os.path.exists(sourcePathInput)
        if not validSoucePath:
            print("That path is not valid. Please enter a valid file path.")
        else:
            break

    while True:
        # Destination Path Validation
        destinationPathInput  = input("Enter the full path of the new file: ")
        destinationFolderPath = os.path.dirname(destinationPathInput)
        validDestinationPath  = os.path.exists(destinationFolderPath)
        if not validDestinationPath:
            print("That path directory is not valid. Please enter a valid directory path.")
        else:
            break

    return {
        "Source":      sourcePathInput,
        "Destination": destinationPathInput
    }

# This validates the input for the Delete FileAction
def ValidateDeleteActionInput():
    while True:
        # Source Path Validation
        sourcePathInput = input("Enter the full path of the file to delete: ")
        validSoucePath = os.path.exists(sourcePathInput)
        if not validSoucePath:
            print("That path is not valid. Please enter a valid file path.")

        confirmationInput = input("Are you sure you want to delete this file?: ").lower()
        shouldNotProceed = confirmationInput != "yes"

        if shouldNotProceed:
            sys.exit()

        return { "FilePath": sourcePathInput }