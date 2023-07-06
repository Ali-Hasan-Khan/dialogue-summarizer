import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.1"

REPO_NAME = "text-summarizer-demo"
AUTHOR = "Ali-Hasan-Khan"
EMAIL = "alihasank86@gmail.com"
SRC_REPO = "textSummarizer"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    description="A demo app for text summarization",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues"
    }
)