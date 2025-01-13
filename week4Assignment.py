def file_read_write():
    try:
        # Ask the user for the filename
        input_filename = input("Enter the name of the file to read from: ").strip()
        
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Modify the content (e.g., add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        # Ask for the output filename
        output_filename = input("Enter the name of the file to write to: ").strip()
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content successfully written to {output_filename}!")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please try again.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_read_write()
