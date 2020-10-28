import json

from .download import download_genre_and_tag_keys
from .download_genre import populate_genres
from .utils import get_file_name_for_clustering_of_app_ids_by_genre
from .utils import get_file_name_for_list_of_genres


def parse_genre_keys():
    with open(get_file_name_for_list_of_genres(), "r", encoding="utf8") as f:
        genres = [l.strip() for l in f.readlines()]

    return genres


def load_genre_keys():
    try:
        genres = parse_genre_keys()
    except FileNotFoundError:
        genres, _ = download_genre_and_tag_keys()

    return genres


def load_genre_values():
    fname = get_file_name_for_clustering_of_app_ids_by_genre()

    try:
        with open(fname, "r", encoding="utf8") as f:
            genres_dict = json.load(f)
    except FileNotFoundError:
        genres = load_genre_keys()
        genres_dict = populate_genres(genres)

    return genres_dict


if __name__ == "__main__":
    genres_dict = load_genre_values()
