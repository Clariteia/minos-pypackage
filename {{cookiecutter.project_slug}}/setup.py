#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_namespace_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [{%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=7.0',{%- endif %} ]

setup_requirements = ['pytest-runner',]

test_requirements = ['pytest>=3', ]

setup(
    author="Andrea Mucci",
    author_email='andrea@clariteia.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}=minos.{{ cookiecutter.project_library }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=requirements,
    long_description_content_type="text/markdown",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_namespace_packages(include=['minos.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
