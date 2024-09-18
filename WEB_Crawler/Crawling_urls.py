from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

app = Flask(__name__)

crawled_urls = set()

# Function to extract forms from a page
def extract_form(soup, url):
    forms = soup.find_all('form')
#    print(f'Found {len(forms)} form(s) on {url}')
    form_details = []  # Initialize this list here
    for form in forms:
        action = form.get('action')
        method = form.get('method', 'get').lower()
        inputs = form.find_all('input')
        input_names = [input.get('name') for input in inputs if input.get('name')]
        form_details.append({'action': action, 'method': method, 'inputs': input_names})
    return form_details


# Function to extract URLs with query parameters
def extract_links_with_parameters(url, soup):
    url_with_params = []
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if '?' in href:
            full_urls = urljoin(url, href)
            url_with_params.append(full_urls)
    return url_with_params


def crawl_website(url, depth=2):
    if url in crawled_urls or depth == 0:
        return
    crawled_urls.add(url)
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"Status code is not 200 for {url}"
        soup = BeautifulSoup(response.text, 'html.parser')

        # Pass 'url' to extract_form function
        forms = extract_form(soup, url)
        url_with_params = extract_links_with_parameters(url, soup)
        links = soup.find_all('a', href=True)
        Other_than_URL_parameters = []
        
        for link in links:
            href = link['href']
            if href != '?':
                next_url = urljoin(url, href)
                Other_than_URL_parameters.append(next_url)
                if urlparse(next_url).netloc == urlparse(url).netloc:
                    crawl_website(next_url, depth-1)
    
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return [],[],[]
    return forms or [], url_with_params or [],Other_than_URL_parameters or []

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/find_urls', methods=['POST'])
def find_urls():
    website = request.form['website']
    forms, url_with_params, Other_than_URL_parameters = crawl_website(website)
    
    return render_template('index.html',website=website, forms=forms, url_with_params=url_with_params, Other_than_URL_parameters=Other_than_URL_parameters)
# Example usage
if __name__ == '__main__':
    app.run(debug=True)
#start_url = 'https://monkeytype.com/'
#crawl_website(start_url)
