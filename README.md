# Books Downloader

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [APIs Used](#apis-used)
- [Contributing](#contributing)

## Introduction

This project is a practice exercise for web scraping. It demonstrates how to utilize the Google Books API and Library Genesis to search for a book, retrieve potential authors, and download the book if available in PDF format.
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

## APIs Used

- [Google Books API](https://developers.google.com/books/docs/overview): Used to search for books and retrieve book information, including potential authors.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, please submit a pull request.

