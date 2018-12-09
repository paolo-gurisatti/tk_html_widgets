import setuptools
import tk_html_widgets

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tk_html_widgets",
    version=tk_html_widgets.VERSION,
    author="Paolo Gurisatti",
    author_email="paolo@fastmail.com",
    description="HTML widgets for tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paolo-gurisatti/tk_html_widgets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4.*",
    install_requires=['Pillow>=5.3.0',],
)