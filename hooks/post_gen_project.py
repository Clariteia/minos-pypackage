#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    

if __name__ == '__main__':

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('minos', '{{ cookiecutter.project_library }}', 'cli.py')
        remove_file(cli_file)

        cli_file = os.path.join('tests', 'test_{{ cookiecutter.project_library }}', 'test_cli.py')
        remove_file(cli_file)
