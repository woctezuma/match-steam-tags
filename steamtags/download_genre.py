import json
import time

from .steamspy import download_genre
from .utils import get_file_name_for_clustering_of_app_ids_by_genre


def populate_genres(genres):
    print("Downloading clusters of appIDs for each genre.")

    genres_dict = {}

    for counter, current_genre in enumerate(genres):
        data = download_genre(genre=current_genre)

        genres_dict[current_genre] = [int(app_id) for app_id in data.keys()]

        # Allowed poll rate - 4 requests per second.
        # Reference: https://steamspy.com/api.php
        if counter % 4 == 0:
            print("{}/{}".format(counter, len(genres)))
            time.sleep(1)

    fname = get_file_name_for_clustering_of_app_ids_by_genre()

    with open(fname, "w", encoding="utf8") as f:
        json.dump(genres_dict, f)

    return genres_dict
