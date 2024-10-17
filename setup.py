from setuptools import setup

setup(
    name='morning_greetings',
    version='1.0.0',
    description='A python package to manage contacts and send personalized good morning messages',
    author='Naveen Vijayasanker',
    author_email='naveen.vijayasanker@gmail.com',
    packages=['morning_greetings'],
    install_requries=[],
    entry_points={
        'console_scripts': [
            'run-automation=main:main',
            ],
        }
)