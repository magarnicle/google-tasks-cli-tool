import setuptools
import pathlib

try:
    import docutils.core
    from docutils.writers import manpage
except ImportError:
    docutils = None
    manpage = None


with open("README.md", encoding="utf-8") as fd:
    long_description = fd.read()


with open("LICENSE", encoding="utf-8") as fd:
    licensetext = fd.read()


setuptools.setup(
    name="google_tasks_cli_tool",
    version="00.01",
    description="Console UI to manage your Google Tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "google-api-python-client",
        "google-auth-oauthlib",
        # dotenv
    ],
    python_requires=">=3.10",
)
