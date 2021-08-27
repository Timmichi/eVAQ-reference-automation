import os

def get_file_info(curr_directory):
    # thisdir = os.getcwd() # gets current working directory
    for root, directories, files in os.walk(curr_directory):
        file_name = list(filter(lambda f: f[-3:] == "pdf" and "Reference" not in f, files))
        file_name = file_name[0]
        file_path = os.path.join(root, file_name)
        return file_name, file_path

if __name__ == "__main__":
    directory_path = "..\\test"
    for root, directories, files in os.walk(directory_path):
        for directory in directories:
            if "eVAQ" in directory:
                curr_directory = os.path.join(root,directory)
                print(get_file_info(curr_directory))
    