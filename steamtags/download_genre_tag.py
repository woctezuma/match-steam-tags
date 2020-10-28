import time

from .steamspy import download_top100, download_appdetails
from .utils import get_file_name_for_list_of_genres
from .utils import get_file_name_for_list_of_tags


def find_corresponding_genres_and_tags(app_ids):
    genres = set()
    tags = set()

    for counter, app_id in enumerate(app_ids):
        data_app_id = download_appdetails(appid=app_id)

        current_genres = {s.strip() for s in data_app_id["genre"].split(",")}
        current_tags = set(data_app_id["tags"].keys())

        genres.update(current_genres)
        tags.update(current_tags)

        # Allowed poll rate - 4 requests per second.
        # Reference: https://steamspy.com/api.php
        if counter % 4 == 0:
            print("{}/{}".format(counter, len(app_ids)))
            time.sleep(1)

    genres = sorted(genres)
    tags = sorted(tags)

    return genres, tags


def download_genre_and_tag_keys(data_source="top100in2weeks"):
    print("Downloading lists of genres and tags for {}.".format(data_source))

    # Retrieve top 100 games played in the past 2 weeks
    data = download_top100(request=data_source)

    # Aggregate genres and tags
    genres, tags = find_corresponding_genres_and_tags(app_ids=data)

    with open(get_file_name_for_list_of_genres(), "w", encoding="utf8") as f:
        print("\n".join(genres), file=f)

    with open(get_file_name_for_list_of_tags(), "w", encoding="utf8") as f:
        print("\n".join(tags), file=f)

    return genres, tags


if __name__ == "__main__":
    genres, tags = download_genre_and_tag_keys(data_source="top100in2weeks")
