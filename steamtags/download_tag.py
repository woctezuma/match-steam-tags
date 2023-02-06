import json
import time

from steamtags.steamspy import download_tag
from steamtags.utils import get_file_name_for_clustering_of_app_ids_by_tag


def populate_tags(tags):
    print("Downloading clusters of appIDs for each tag.")

    tags_dict = {}

    for counter, current_tag in enumerate(tags):
        data = download_tag(tag=current_tag)

        tags_dict[current_tag] = [int(app_id) for app_id in data]

        # Allowed poll rate - 4 requests per second.
        # Reference: https://steamspy.com/api.php
        if counter % 4 == 0:
            print(f"{counter}/{len(tags)}")
            time.sleep(1)

    fname = get_file_name_for_clustering_of_app_ids_by_tag()

    with open(fname, "w", encoding="utf8") as f:
        json.dump(tags_dict, f)

    return tags_dict
