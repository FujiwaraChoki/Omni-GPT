from halo import Halo
from termcolor import colored

import os


def info(message, showIcon=True):
    if showIcon:
        print(colored(f'[i] {message}', 'blue'))
    else:
        print(colored(message, 'blue'))


def error(message, showIcon=True):
    if showIcon:
        print(colored(f'[-] {message}', 'red'))
    else:
        print(colored(message, 'red'))


def success(message, showIcon=True):
    if showIcon:
        print(colored(f'[+] {message}', 'green'))
    else:
        print(colored(message, 'green'))


def warning(message, showIcon=True):
    if showIcon:
        print(colored(f'[!] {message}', 'yellow'))
    else:
        print(colored(message, 'yellow'))


def loading(message, command="", showIcon=True, success_text=None, error_text=None):
    if showIcon:
        spinner = Halo(text=message, spinner='dots')
        spinner.start()
        # Run command, redirect all output to /dev/null
        status = os.system(command + ' > /dev/null 2>&1')
        spinner.stop()
        if status == 0:
            success(success_text)
        else:
            error(error_text)
    else:
        print(colored(message, 'cyan'))
        status = os.system(command)
        if status == 0:
            success(success)
        else:
            error(error)
