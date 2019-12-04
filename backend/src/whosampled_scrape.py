import json
from lxml import html
import requests
import urllib.parse

class WhoSampledScrape:
    
    __url = 'https://www.whosampled.com'
    
    def create_samples_list (self, track_list):
        for track in track_list:
            search_string = urllib.parse.quote(track)
            search_content = self.__request_page_content('/search/tracks/?q=' + search_string)
            track_link = search_content.xpath("//a[@class='trackName']/@href").pop()
            if track_link:
                for sample in self.__parse_samples_page(track_link):
                    yield sample


    def __parse_samples_page(self, link):
        samples_page = self.__request_page_content(link)
        samples_sections = samples_page.xpath("//section[contains(.//span, 'Contains samples')]//div[@class='trackDetails']")
        for sample in samples_sections:
            sample_name = sample.xpath(".//a[contains(@class, 'trackName')]/text()").pop()
            sample_artist = sample.xpath(".//span[@class='trackArtist']//a/text()").pop()
            yield { "name": sample_name, "artist": sample_artist }


    def __request_page_content(self, link):
        page = requests.get(self.__url + link, headers={"User-Agent":"Mozilla/5.0"})
        return html.fromstring(page.content)
