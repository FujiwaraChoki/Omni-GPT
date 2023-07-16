import os
import json
import openai

from files import *
from termcolor import colored
from dotenv import load_dotenv

load_dotenv(".env")


def start():
    print(colored("I want OmniGPT to create this website: ", "magenta"), end="")
    goal = input()

    generate(goal)


def generate(goal):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    openai.Model.list()

    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""Hello ChatGPT! From now on, I just want you to give me the response I want, nothing more, nothing less. I want to create a website which can do the following: '{goal}'. Give me the file names and their contents in a JSON-Array, like this: Example Input: A website which lets users interact with ChatGPT through their own API Key. Styling should be done with TailwindCSS. Example Output:
    [
       {{
           file_name: 'index.html',
           file_contents: 'Here should be the generated file contents from you'
      }},
     {{
         file_name: 'privacy.html',
     file_contents:  'HTML file with Privacy Policy in it'
     }},
     ...
     ]

    Information for file contents:
    Do NOT EVER keep a template. Always fill out every code.
    for example: don't say:
    // Code to fetch openai
    It has to be the actual code, so:
    fetch(url).then(...)

    Fill out all information use all best practices.

    ONLY send me the JSON-Array. NOTHING else.
    """,
        max_tokens=3500,
        temperature=0.5
    )

    create_files_and_add_contents(parse_response(completion["choices"][0]))


def parse_response(choices):
    JSONChoices = json.loads(str(choices))
    text = JSONChoices["text"]

    return text
