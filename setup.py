# coding=utf8
from setuptools import setup

setup(
    name='scraper',
    version='0.1',
    description='scrapes BITS ID and Pics for students',
    url='https://github.com/Utkarsh1308/Pics-Scraper',
    author='Utkarsh Sharma',
    author_email='',
    classifiers=[  # Optional
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='BeautifulSoup scraper requests',
    packages=["scraper"],
    install_requires=[],
    extras_require={},
    entry_points={
        'console_scripts': [
            'scraper=scraper.command_line_interface:main',
        ],
    },
)
