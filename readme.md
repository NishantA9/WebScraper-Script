## Hacker News Story Scraper

This Python script scrapes and sorts top stories from Hacker News. It uses BeautifulSoup for parsing HTML and Requests for fetching web pages.

# Install the required libraries using pip:

        pip install beautifulsoup4
        pip install requests

# Script Overview

This script fetches the top stories from the first two pages of Hacker News, extracts relevant information (titles, links, and votes), and sorts the stories by the number of votes.

Script Details
Fetch Data from Hacker News:

Retrieves HTML content from the first and second pages of Hacker News.
Parse HTML:

Uses BeautifulSoup to parse and clean HTML content.
Extract Data:

Extracts story titles, links, and votes from the parsed HTML.
Sort Stories:

Sorts stories by the number of votes in descending order.
Filter Stories:

Only includes stories with more than 99 votes.

# Usage
Run the script to see the sorted list of top stories with their titles, links, and votes.
        python hacker_news_scraper.py



##  Made by Nishant Acharekar, under Course of Complete Python Developer 2024 by ZTM on Udemy

