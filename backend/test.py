from src.whosampled_scrape import create_samples_list

def test_whosampled_scrape ():
    track_list = ['Follow God Kanye West']
    result = list(create_samples_list(track_list))
    assert len(result) > 0
    assert result[0]['name'] == 'Can You Lose by Following God'
    assert result[0]['artist'] == 'Whole Truth'