import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import nest_asyncio

nest_asyncio.apply()


session = HTMLSession()

url1="https://www.exmapleurl.com/login"
url2="https://www.exmapleurl.com"

payload = {
    'email' : '*****************',
    'password' : '**********',
}
headers={
    "referer": "https://www.exmapleurl.com/login",
    "origin": "hhttps://www.exmapleurl.com/login"
}


with requests.Session() as s:
    post = s.post(url1, data=payload, headers={"referer": "https://www.exmapleurl.com/login"})
    r=s.get(url2)

    print(r.text)
    print(r.html.render())
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())