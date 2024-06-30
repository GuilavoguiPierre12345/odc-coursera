import requests
from bs4 import BeautifulSoup

"""
Fetching and parsing HTML
To start web scraping, you need to fetch the HTML content of a webpage and parse 
it using Beautiful Soup. Here's a step-by-step example:
"""

# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'
# Send an HTTP GET request to the webpage
response = requests.get(url)
if response.status_code == 200:

    # Store the HTML content in a variable
    html_content = response.text
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Display a snippet of the HTML content
    # print(html_content[:500])

    """
    NAVIGATING THE HTML STRUCTURE
    BeautifulSoup represents HTML content as a tree-like structure, allowing for easy 
    navigation. You can use methods like find_all to filter and extract specific HTML 
    elements. For example, to find all anchor tags () and print their text:

    """ 
    # Find all <a> tags (anchor tags) in the HTML
    links = soup.find_all('a')
    # Iterate through the list of links and print their text
    for link in links:
        print(link.text)


else :
    print("Error https response")


