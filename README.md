# Instagram Scraper

A simple Instagram post scraper built with Python and Selenium.

The scraper navigates through the posts of an Instagram profile and collects
the URL and publication datetime of each post.

This project was created primarily for learning and personal automation.

## Features

- Instagram authentication using Selenium
- Support for manual CAPTCHA / checkpoint verification
- Opens the first post of a profile automatically
- Navigates between posts using Instagram's `Next` button
- Collects:
  - Post URL
  - Publication datetime
- Supports regular posts and Reels
- Prevents duplicate URLs during scraping
- Exports collected posts to JSON
- Accepts the Instagram profile through the command line
- Credentials are loaded through environment variables

## Technologies

- Python
- Selenium
- python-dotenv

## Project Structure

```text
instagram-scraper/
│
├── scrape.py
├── session.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md