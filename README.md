# Web_Crawler_For_URL_Extraction
🚀 Built a Web Crawler for Comprehensive URL Extraction 🚀

Excited to share a project I've been working on—a web crawler that extracts all URLs from a website, with three distinct outputs:
    1)Forms
    2)URLs with Query Parameters
    3)All Remaining URLs

🔧 Tech Stack:
    1)Frontend: HTML, CSS
    2)Backend: Python (Flask) with core libraries like:
        -requests: Fetches HTML pages
        -beautifulsoup: Extracts tags from the page
        -urllib.parse (urljoin): Joins subdomain URLs
        -Recursion: To repeatedly extract URLs, even from subdomains

The crawler helps in gathering all internal URLs from a site, making it an effective tool for vulnerability detection and website security auditing. It’s designed to help ensure no page is left unchecked during web assessments.

This project can be a game-changer in web security, allowing for proactive website protection after collecting all critical URLs.

**For Running this Web:**
You have to follow this path:

**/WEB_Crawler
    /static
        /style.css
    /templates
        /index.html
    Crawling_urls.py**

NOte: First you have to run the Crawling_urls.py and then in that output you get the url. Click the url you go to the website. Now just give the url of the website and wait for a few minutes to extract the urls.
