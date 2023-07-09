# Books-downloader
# Book Search and Download

This Python script allows you to search for a book using the Google Books API and download it from the Library Genesis website if available in PDF format.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [APIs Used](#apis-used)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Book Search and Download script is a Python application that leverages the Google Books API and Library Genesis to search for books and provide a direct download link if a PDF version is available on Library Genesis.

The script prompts the user to enter a book name, performs a search using the Google Books API to retrieve potential authors, and then searches Library Genesis for the book. If the book is found, it opens the download link in the default web browser.

## Features

- Search for books using the Google Books API
- Retrieve potential authors from the Google Books API
- Search for the book on Library Genesis
- Provide a direct download link for books available in PDF format on Library Genesis

## Prerequisites

To run this script, you need the following:

- Python 3.x installed on your system
- Required Python packages: `beautifulsoup4`, `requests`, `webbrowser`

## Installation

1. Clone this repository to your local machine using the following command:
   

