def copy_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file_in:
            content = file_in.read()
            
            with open(output_file, 'w') as file_out:
                file_out.write(content)
            print(f"File {input_file} has been copied to: {output_file}.")
    except FileNotFoundError:
        print("Cannot find a file with such a name.")

if __name__ == "__main__":
    input_file_name = input("Enter name of the txt file: ")
    output_file_name = "lab1zad1.txt"
    copy_file(input_file_name, output_file_name)