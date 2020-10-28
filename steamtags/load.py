import json

from .download import download_genre_and_tag_keys, populate_genres, populate_tags
from .utils import get_file_name_for_clustering_of_app_ids_by_genre
from .utils import get_file_name_for_clustering_of_app_ids_by_tag
from .utils import get_file_name_for_list_of_genres
from .utils import get_file_name_for_list_of_tags


def load_genre_keys():
    try:
        with open(get_file_name_for_list_of_genres(), 'r', encoding='utf8') as f:
            genres = [l.strip() for l in f.readlines()]

    except FileNotFoundError:
        genres, _ = download_genre_and_tag_keys()

    return genres


def load_tag_keys():
    try:
        with open(get_file_name_for_list_of_tags(), 'r', encoding='utf8') as f:
            tags = [l.strip() for l in f.readlines()]
    except FileNotFoundError:
        _, tags = download_genre_and_tag_keys()

    return tags


def load_genre_values():
    try:
        with open(get_file_name_for_clustering_of_app_ids_by_genre(), 'r', encoding='utf8') as f:
            genres_dict = json.load(f)
    except FileNotFoundError:
        genres = load_genre_keys()
        genres_dict = populate_genres(genres)

    return genres_dict


def load_tag_values():
    try:
        with open(get_file_name_for_clustering_of_app_ids_by_tag(), 'r', encoding='utf8') as f:
            tags_dict = json.load(f)
    except FileNotFoundError:
        tags = load_tag_keys()
        tags_dict = populate_tags(tags)

    return tags_dict


def load():
    genres_dict = load_genre_values()
    tags_dict = load_tag_values()

    return genres_dict, tags_dict


if __name__ == '__main__':
    genres_dict, tags_dict = load()
