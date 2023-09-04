import os
import json
import openai

from halo import Halo
from utils.status import *
from termcolor import colored
from dotenv import load_dotenv

load_dotenv(".env")


def start():
    print(colored("I want OmniGPT to create this website: ", "magenta"), end="")
    goal = input()

    generate(goal)


def generate(goal):
    spinner = Halo(text="Creating your website\n", spinner='dots')
    spinner.start()

    # Usually
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # New
    '''
    openai.api_base = "https://api.nova-oss.com/v1"
    openai.api_key = os.getenv("NOVAAI_API_KEY")
    '''

    completion = openai.Completion.create(
        model="davinci",
        prompt=f"""Hello ChatGPT! From now on, I just want you to give me the response I want, nothing more, nothing less. I want to create a website which can do the following: '{goal}'. Give me the file names and their contents in a JSON-Array, like this: Example Input: A website which lets users interact with ChatGPT through their own API Key. Styling should be done with TailwindCSS. Example Output:
    [
       {{
           "file_name": "",
           "file_contents": ""
      }},
     ...
     ]

    It can either be a static HTML-Site or a website using a specific framework/library, like Next.js or React.
     
    Put the directory names in front inside of each filename, leave out the directory if none is needed.

    Information for file contents:
    Do NOT EVER keep a template. Always fill out every code.
    for example: don't say:
    // Code to fetch openai
    It has to be the actual code, so:
    fetch(url).then(...)

    The website needs at least the following:
    * Navbar
    * Working Links
    * Data in form of Text (Not Lorem Ipsum, But Actual Text)
    * Footer

    Fill out both with filler data if no data is provided from my side.

    Fill out all information use all best practices.
    Don't leave any unterminated strings and always use double quotes.
    Be creative with the files, generate multiple files.

    MAKE SURE THERE ARE NO JSON-related errors. Use single quotes if you need to quote something in the file contents string.

    ONLY send me the JSON-Array. NOTHING else.
    """,
        max_tokens=3500,
        temperature=0.5
    )

    create_files_and_add_contents(
        parse_response(completion["choices"][0]))

    spinner.stop()
    success(
        "Successfully created your website!")

    info("Would you like to run a webserver to see your new website? (y/n)")
    run_webserver(input())


def run_webserver(choice):
    if choice.lower() == "y":
        # Run a webserver in output directory
        spinner = Halo(
            text="Started HTTP-Server on Port 8080: http://localhost:8080")
        spinner.start()
        os.chdir("output")
        os.system("python3 -m http.server 8080 > /dev/null 2>&1")
        spinner.stop()
        info("Stopped webserver!")
    else:
        info("Aborting...")
        exit(0)


def parse_response(choices):
    JSONChoices = json.loads(str(choices))
    text = JSONChoices["text"]

    with open('file_structures.json', 'w') as file:
        file.write(text)

    return text


def create_files_and_add_contents(filesArrayJson):
    for file in json.loads(filesArrayJson):
        create_file(file["file_name"], file["file_contents"])


def create_file(file_name, file_contents):
    # Check if output directory exists, if not create one
    if not os.path.exists("output"):
        os.makedirs("output")

    file_path = os.path.join("output", file_name)

    try:
        with open(file_path, 'w') as file:
            file.write(file_contents)
        success(f"File '{file_name}' created successfully.")
    except Exception as e:
        error(f"Error creating file '{file_name}': {str(e)}")
