from scrapping import Scrapping
import requests

if __name__ == '__main__':
    urls = Scrapping.scrap_data()
    for link, address, price in urls:
        data = {
                "entry.489572553": link,
                "entry.443167855": address,
                "entry.123820490": price
        }
        response = requests.post(
        "https://docs.google.com/forms/d/e/1FAIpQLScOnJndCwGeVDpnSnx3if4iPpKrghWx0AzoYKrHKGtHgJcUiw/formResponse",
            data=data)
    print("Done")
