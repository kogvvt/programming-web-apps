def copy_image(input_file, output_file):
    try:
        
        with open(input_file, 'rb') as file_in:
            content = file_in.read()
            
            with open(output_file, 'wb') as file_out:
                file_out.write(content)
        
        print(f"File {input_file} has been copied to {output_file}.")
    except FileNotFoundError:
        print("Cannot find a file.")

if __name__ == "__main__":
    input_file_name = input("Enter the name of png file: ")
    output_file_name = "lab1zad1.png"
    copy_image(input_file_name, output_file_name)