from utils.status import *


def create_files_and_add_contents(filesArrayJson):
    for file in filesArrayJson:
        create_file(f'../output/{file["file_name"]}', file["file_contents"])


def create_file(file_name, file_contents):
    try:
        with open(file_name, 'w') as file:
            file.write(file_contents)
        success(f"File '{file_name}' created successfully.")
    except Exception as e:
        error(f"Error creating file '{file_name}': {str(e)}")
