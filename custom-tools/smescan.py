# This script automates the broken link checking for smevai.
# Author: Abu Hurayra



# from cgi import test
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse


APP_URL = 'https://app.smevai.com'
TESTING_URL = 'https://testing.smevai.com'

SERVICE_USERNAME = 'wpdabh+year22sa1@gmail.com'
TRADING_USERNAME = 'wpdabh+year22ta1@gmail.com'

PASSWORD = 'pass1234'


# links = FindLinksFromWebpage(URL)
all_links = []
tested_links = []


# Check If a string is a valid URL
def is_valid(url):
    if url == None or ".smevai.com" not in url:
      return False
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# This function will login to the laravel website
def login(url, username, password):
    s = requests.Session()
    
    # Get the crsf_token first
    front = s.get(url)
    token = re.findall(r'<input type="hidden" name="_token" value="(.*)"', front.text )
    csrf_token = (token[0] if len(token)>0 else '0')
    
    # Get cookies
    cookies = s.cookies
    
    # Create the login payload
    payload = {
        'username': username,
        'password': password,
        '_token': csrf_token
    }
    
    # Send the login POST request
    res = s.post(
        url=url+'/login', 
        data=payload,
        cookies=cookies
    )
    
    print(f"Logged in? {res.status_code}")
    
    return s


# Find all links from a webpage
def FindLinksFromWebpage(session, url):
    r = session.get(url)
    if r.status_code >= 400:
        print(f'[x] Error: Code {r.status_code} on URL - {url}')
        return []
    html_page = r.text
    soup = BeautifulSoup(html_page, 'html.parser')
    
    links = []
    for link in soup.findAll('a'):
        new_link = link.get('href')
        if is_valid(new_link) and new_link not in links:
            links.append(new_link)
    
    return links


# Recursively Extract all links
def extract_links(session, link):
    
  
    if link not in all_links:
        all_links.append(link)
    if link in tested_links:
        return
    
    tested_links.append(link)
    # print(f'[+] Tested - {link}')
    
    for l in FindLinksFromWebpage(session, link):
        extract_links(session, l)


# This method will act as the main method here
def RunSmeScan(_URL, _USERNAME, _PASSWORD):
    
    URL = _URL
    USERNAME = _USERNAME
    PASSWORD = _PASSWORD
    result = ""
    
    # Login to the website
    session = login(URL, USERNAME, PASSWORD)
    
    extract_links(session, URL)
    count = 0
    # Print The links and their Status Codes
    for index, link in enumerate(sorted(all_links)):
        res = session.get(link)
        count += 1
        if res.status_code == 200:
          
          continue
          
        if index<10:
            result += f'\n0{index} - {res.status_code} > {link}'
        else:
            result += f'\n{index} - {res.status_code} > {link}'
    print(f"Tested {count} links.")
    return result


# print("Checking: APP + TRADING")
# result1 = RunSmeScan(APP_URL, "sagorace.017@gmail.com", "123456789")
# print(result1)





print("Checking: APP + TRADING")
result1 = RunSmeScan(APP_URL, TRADING_USERNAME, PASSWORD)
print(result1)

all_links = []
tested_links = []

print("Checking: APP + SERVICE")
result2 = RunSmeScan(APP_URL, SERVICE_USERNAME, PASSWORD)
print(result2)

all_links = []
tested_links = []

print("Checking: TESTING + TRADING")
result3 = RunSmeScan(TESTING_URL, TRADING_USERNAME, PASSWORD)
print(result3)

all_links = []
tested_links = []

print("Checking: TESTING + SERVICE")
result4 = RunSmeScan(TESTING_URL, SERVICE_USERNAME, PASSWORD)
print(result4)

all_links = []
tested_links = []