import unittest

import steamtags


class TestSteamTagsMethods(unittest.TestCase):
    def test_download_top100in2weeks(self):
        data_source = "top100in2weeks"
        genres_dict, tags_dict = steamtags.download(data_source)

        sentence = "[request = {}] #genres = {} & #tags = {}"
        print(sentence.format(data_source, len(genres_dict), len(tags_dict)))

        assert len(genres_dict) > 0
        assert len(tags_dict) > 0

    def test_download_top100forever(self):
        data_source = "top100forever"
        genres_dict, tags_dict = steamtags.download(data_source)

        sentence = "[request = {}] #genres = {} & #tags = {}"
        print(sentence.format(data_source, len(genres_dict), len(tags_dict)))

        assert len(genres_dict) > 0
        assert len(tags_dict) > 0

    def test_download_top100owned(self):
        data_source = "top100owned"
        genres_dict, tags_dict = steamtags.download(data_source)

        sentence = "[request = {}] #genres = {} & #tags = {}"
        print(sentence.format(data_source, len(genres_dict), len(tags_dict)))

        assert len(genres_dict) > 0
        assert len(tags_dict) > 0

    def test_download(self):
        genres_dict, tags_dict = steamtags.download()

        sentence = "[default request] #genres = {} & #tags = {}"
        print(sentence.format(len(genres_dict), len(tags_dict)))

        assert len(genres_dict) > 0
        assert len(tags_dict) > 0

    def test_load(self):
        # Download
        assert steamtags.load()
        # Load from cache
        assert steamtags.load()


if __name__ == "__main__":
    unittest.main()
