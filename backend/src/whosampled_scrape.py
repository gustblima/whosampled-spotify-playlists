import json
from lxml import html
import requests
import urllib.parse

root_url = 'https://www.whosampled.com'

def create_samples_list (track_list):
    for track in track_list:
        search_string = urllib.parse.quote(track)
        search_content = request_page_content('/search/tracks/?q=' + search_string)
        track_link = search_content.xpath("//a[@class='trackName']/@href").pop()
        if track_link:
            for sample in parse_samples_page(track_link):
                yield sample


def parse_samples_page(link):
    samples_page = request_page_content(link)
    samples_sections = samples_page.xpath("//section[contains(.//span, 'Contains samples')]//div[@class='trackDetails']")
    for sample in samples_sections:
        sample_name = sample.xpath(".//a[contains(@class, 'trackName')]/text()").pop()
        sample_artist = sample.xpath(".//span[@class='trackArtist']//a/text()").pop()
        yield { "name": sample_name, "artist": sample_artist }


def request_page_content(link):
    page = requests.get(root_url + link, headers={"User-Agent":"Mozilla/5.0"})
    return html.fromstring(page.content)
