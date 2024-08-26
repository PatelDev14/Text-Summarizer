import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR = "PatelDev14"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "devp1400@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A Text Summarizer using BERT model",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected this line
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",  # Updated URL to reflect the correct repo name
    package_dir={"": "src"},  # Corrected key 'package_dir'
    packages=setuptools.find_packages(where="src")  # Find packages within 'src' directory
)

    
   
