from utils.status import *
from src.brain import *


def startup():
    info('Welcome to ...')
    info(open('./assets/logo.txt', 'r').read(), showIcon=False)


def install_requirement(requirement):
    loading(message=f'Installing {requirement}...', command=f'pip3 install {requirement}',
            success_text=f'Successfully installed {requirement}!', error_text=f'Failed to install {requirement}!')


def check_requirements():
    # Read requirements.txt and check if each of them is installed
    requirements = open('./requirements.txt', 'r').read().split('\n')
    for requirement in requirements:
        try:
            __import__(requirement)
        except ImportError:
            error(f'Error: "{requirement}" is not installed.')
            install_requirement(requirement)


if __name__ == '__main__':
    startup()
    check_requirements()
    success('All requirements are installed!')
    info('Starting...')
    start()
