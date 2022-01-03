from bs4 import BeautifulSoup
import requests


class Songs:
    url: str = "https://www.billboard.com/charts/hot-100/"
    date: str = ""

    def __init__(self, date):
        self.date = date

    def scrap_songs(self):
        main_url = f"{self.url}{self.date}/"
        html = requests.get(main_url)
        html.raise_for_status()
        soup = BeautifulSoup(html.text, "html.parser")
        tmp_list = soup.findAll("div", class_="o-chart-results-list-row-container")
        for tag in tmp_list:
            song_tag = tag.find_all("h3")[0]
            song_name = song_tag.next_element.text.strip()
            singer = song_tag.find_next("span").text.strip()
            yield song_name, singer
