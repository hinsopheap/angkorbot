Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> import requests
... from bs4 import BeautifulSoup
... 
... # URL of the website you want to scrape
... url = 'https://www.dgdemy.org'
... 
... # Send a GET request to the website
... response = requests.get(url)
... 
... # Check if the request was successful
... if response.status_code == 200:
...     # Parse the HTML content of the page
...     soup = BeautifulSoup(response.content, 'html.parser')
...     
...     # Example: Extract the title of the page
...     title = soup.title.string
...     print(f"Title of the page: {title}")
...     
...     # Example: Extract all the headings (h1, h2, etc.)
...     headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
...     for heading in headings:
...         print(f"{heading.name}: {heading.text.strip()}")
...     
...     # Example: Extract all the links on the page
...     links = soup.find_all('a', href=True)
...     for link in links:
...         print(f"Link text: {link.text.strip()}, URL: {link['href']}")
... else:
...     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
