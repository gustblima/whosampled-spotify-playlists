import json
from lxml import html
import requests
import urllib.parse

requests.get("https://www.whosampled.com/Kanye-West/Power/", headers={"User-Agent":"Mozilla/5.0"})
root_url = 'https://www.whosampled.com'

def handler(event, context):

    #track_list = json.loads(event.body)
    track_list = [
        {
            "name": 'Follow God',
            "artist": "Kanye West"
        }
    ]
    for track in track_list:
        print(track)
        search_string = urllib.parse.quote('{} {}'.format(track['name'], track['artist']))
        search_content = request_page_content('/search/tracks/?q=' + search_string)
        track_link = search_content.xpath("//a[@class='trackName']/@href")[0]
        for sample in parse_samples_page(track_link):
            print(sample)


def parse_samples_page(link):
    samples_page = request_page_content(link)
    samples_sections = samples_page.xpath("//section[contains(.//span, 'Contains samples')]//div[@class='trackDetails']")
    for sample in samples_sections:
        print(sample, "sample")
        sample_name = sample.xpath(".//a[contains(@class, 'trackName')]/text()")
        print(sample_name)
        sample_artist = sample.xpath(".//span[@class='trackArtist']//a/text()")
        print(sample_artist)
        yield { "name": sample_name, "artist": sample_artist }

    
def request_page_content(link):
    print(root_url + link)
    page = requests.get(root_url + link, headers={"User-Agent":"Mozilla/5.0"})
    return html.fromstring(page.content)
