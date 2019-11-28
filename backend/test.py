from handlers.samples import create_sample_list

def test_whosampled_scrape ():
    track_list = [{
        "name": 'Follow God',
        "artist": "Kanye West"
    }]
    result = list(create_sample_list(track_list))
    assert len(result) > 0
    assert result[0]['name'] == 'Can You Lose by Following God'
    assert result[0]['artist'] == 'Whole Truth'