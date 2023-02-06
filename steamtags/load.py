from steamtags.load_genre import load_genre_values
from steamtags.load_tag import load_tag_values


def load():
    genres_dict = load_genre_values()
    tags_dict = load_tag_values()

    return genres_dict, tags_dict
