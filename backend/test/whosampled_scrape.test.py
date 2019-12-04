from src.whosampled_scrape import WhoSampledScrape

def test_whosampled_scrape ():
    track_list = ['Follow God Kanye West']
    scrape = WhoSampledScrape()
    result = list(scrape.create_samples_list(track_list))
    assert len(result) > 0
    assert result[0]['name'] == 'Can You Lose by Following God'
    assert result[0]['artist'] == 'Whole Truth'