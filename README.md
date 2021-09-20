# MAS-2122 Repository

> Repository for coding exercises - MAS in Architecture and Digital Fabrication at ETH Zürich.

## Requirements

Install the following tools:

- [Anaconda](https://www.anaconda.com/products/individual)
- [Visual Studio Code](https://code.visualstudio.com/) and extensions: [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) and [editorconfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [Github Desktop](https://desktop.github.com/)

## Getting started

Create a environment using `Anaconda prompt`:

    cd FOLDER_OF_REPO
    conda env create -n NAME_OR_TITLE -f environment.yml

Activate the environment:

    conda activate NAME_OR_TITLE
    python -m compas_rhino.install
    
Optionally, you could provide a Rhino version number (6.0, 7.0). The default is 6.0.

    python -m compas_rhino.install -v 7.0


Open folder in Visual Studio Code:

    code .

Select your environment from the lower left area in Visual Studio Code.

## Additional ideas

A few additional things to try:

1. On Visual Studio Code, press `Ctrl+Shift+P`, `Select linter` and select `flake8`
1. To auto-format code, `right-click`, `Format document...`
1. (Windows-only) Change shell: press `Ctrl+Shift+P`, `Select Default Shell` and select `cmd.exe`
1. Try git integration: commit, pull & push are all easily available from Visual Studio Code.
