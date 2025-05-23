import setuptools


with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "text_summarizer_project"
AUTHOR_USER_NAME = "hyrun2005"
SRC_REPO = f"{REPO_NAME}/src"
AUTHOR_EMAIL = "yurii.hyrun@gmail.com"	

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization tool",
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': 'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)