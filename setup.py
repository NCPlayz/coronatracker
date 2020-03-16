from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='coronatracker',
    version='0.1',
    packages=['coronatracker'],
    url='https://github.com/NCPlayz/coronatracker',
    license='MIT',
    author='NCPlayz <Nadir Chowdhury>',
    author_email='chowdhurynadir0@outlook.com',
    description='A Python wrapper for Bing\'s COVID19 tracker.',
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires='requests==2.23.0',
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)