from bs4 import BeautifulSoup
import requests
from Day53.config import SITE_URL
import re


class Scrapping:

    @classmethod
    def scrap_data(cls):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        html = requests.get(SITE_URL, headers=headers)
        html.raise_for_status()
        soup = BeautifulSoup(html.text, "html.parser")
        tmp_list = soup.select("article")
        for tag in tmp_list:
            a = tag.find("a")
            if a:
                try:
                    href = a.attrs["href"]
                    address = a.text
                    pr = tag.find("div", class_="list-card-price")
                    price = re.match("[$]\d,\d+", pr.next.text).group(0)
                    if "http" not in href:
                        yield f"https://www.zillow.com{href}", address, price
                    else:
                        yield href, address, price
                except:
                    continue
