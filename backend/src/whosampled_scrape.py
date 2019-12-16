import json
from lxml import html
import requests
import urllib.parse

class WhoSampledScrape:
    
    __url = 'https://www.whosampled.com'
    
    def get_samples_from_track_search (self, search):
        search_string = urllib.parse.quote(search)
        search_content = self.__request_page_content('/search/tracks/?q=' + search_string)
        track = search_content.xpath("//span[@class='trackDetails']").pop(0)
        track_link = track.xpath(".//a[@class='trackName']/@href").pop(0)
        if track_link:
            track_details = self.__get_track_information(track)
            samples = list(self.__parse_samples_page(track_link))
            return { "name": track_details['name'], "artist": track_details['artist'], "samples": samples }
    
    def __get_track_information(self, track_element):
        track_name = track_element.xpath(".//a[contains(@class, 'trackName')]/text()").pop(0)
        track_artist = track_element.xpath(".//span[@class='trackArtist']//a/text()")
        return { "name": track_name, "artist": track_artist }


    def __parse_samples_page(self, link):
        samples_page = self.__request_page_content(link)
        samples_sections = samples_page.xpath("//section[contains(.//span, 'Contains samples')]//div[@class='trackDetails']")
        for sample in samples_sections:
            yield self.__get_track_information(sample)


    def __request_page_content(self, link):
        page = requests.get(self.__url + link, headers={"User-Agent":"Mozilla/5.0"})
        return html.fromstring(page.content)
