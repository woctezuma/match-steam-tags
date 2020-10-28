import json

from .download import download_genre_and_tag_keys
from .download_tag import populate_tags
from .utils import get_file_name_for_clustering_of_app_ids_by_tag
from .utils import get_file_name_for_list_of_tags


def parse_tag_keys():
    with open(get_file_name_for_list_of_tags(), "r", encoding="utf8") as f:
        tags = [l.strip() for l in f.readlines()]

    return tags


def load_tag_keys():
    try:
        tags = parse_tag_keys()
    except FileNotFoundError:
        _, tags = download_genre_and_tag_keys()

    return tags


def load_tag_values():
    fname = get_file_name_for_clustering_of_app_ids_by_tag()

    try:
        with open(fname, "r", encoding="utf8") as f:
            tags_dict = json.load(f)
    except FileNotFoundError:
        tags = load_tag_keys()
        tags_dict = populate_tags(tags)

    return tags_dict


if __name__ == "__main__":
    tags_dict = load_tag_values()
