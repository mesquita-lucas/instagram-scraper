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
```

## Installation

Clone the repository:

```bash
git clone https://github.com/mesquita-lucas/insta_scrapper.git
cd insta_scrapper
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Git Bash

```bash
python -m venv venv
source venv/Scripts/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

You can use `.env.example` as reference:

```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

The `.env` file should never be committed to Git.

## Usage

Run the scraper passing the Instagram profile as an argument:

```bash
python scrape.py hub4.bike
```

The scraper will open Chrome and attempt to authenticate using the credentials configured in `.env`.

If Instagram requests CAPTCHA, two-factor authentication, or another security checkpoint, complete the process manually in the browser.

Once authentication is complete, return to the terminal and press `Enter` to continue.

Example:

```text
Follow the authorization and/or CAPTCHA process until you are completely
logged into your account. Then press Enter.
```

The scraper will then:

```text
Open profile
    ↓
Open first post
    ↓
Collect URL + datetime
    ↓
Click Next
    ↓
Collect next post
    ↓
Repeat
```

Example output:

```text
1 | 2026-06-10T09:48:18.000Z | https://www.instagram.com/p/XXXXXXXXXXX/
2 | 2026-06-08T14:21:32.000Z | https://www.instagram.com/reel/YYYYYYYYYYY/
3 | 2026-06-05T17:42:01.000Z | https://www.instagram.com/p/ZZZZZZZZZZZ/
```

The collected data is saved as JSON.

Example:

```json
[
    {
        "url": "https://www.instagram.com/p/XXXXXXXXXXX/",
        "datetime": "2026-06-10T09:48:18.000Z"
    },
    {
        "url": "https://www.instagram.com/reel/YYYYYYYYYYY/",
        "datetime": "2026-06-08T14:21:32.000Z"
    }
]
```

## How It Works

Instead of scrolling through the entire Instagram profile, the scraper uses Instagram's post navigation.

After opening the first post, Selenium locates the `Next` button and navigates through the posts sequentially.

For each post:

- The URL is obtained directly from the browser.
- The publication date is extracted from the HTML `<time datetime="...">` element.

This avoids loading the entire profile grid through infinite scrolling.

## Notes

Instagram may request additional authentication when detecting automated browser activity.

CAPTCHA and security checkpoints are intentionally handled manually instead of attempting to bypass Instagram's security mechanisms.

Instagram's HTML structure may change over time, which can require updating the Selenium selectors used by the scraper.

## Disclaimer

This project was created for educational and personal-use purposes.

Users are responsible for ensuring that their use of this project complies with Instagram's Terms of Use and applicable laws.