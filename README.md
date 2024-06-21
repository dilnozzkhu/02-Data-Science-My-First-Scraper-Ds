# My First Scraper Ds

## Description

This project is a simple web scraper that extracts the top repositories from the GitHub Trending page and formats the data into a CSV-like format.

## Features

- Sends a GET request to the GitHub Trending page and retrieves the HTML content.
- Extracts the relevant HTML elements containing the repository information.
- Transforms the extracted data into a list of dictionaries, each representing a repository.
- Formats the repository data into a CSV-like string.

## Usage

To run the scraper, simply execute the main() function:

if __name__ == '__main__':
    main()

This will print the CSV-like output to the console.

## Dependencies

- requests: Used to make the HTTP GET request to the GitHub Trending page.
- BeautifulSoup: Used to parse the HTML content and extract the relevant data.

## Future Improvements

- Add error handling for the HTTP request and HTML parsing.
- Allow the user to specify the number of repositories to scrape.
- Save the CSV-like output to a file instead of printing to the console.
- Extend the scraper to extract additional information about the repositories (e.g., description, programming language, etc.).

## Contribution

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
