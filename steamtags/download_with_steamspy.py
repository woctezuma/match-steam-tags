import json
import time

import steamspypi

from .utils import get_file_name_for_clustering_of_app_ids_by_genre
from .utils import get_file_name_for_clustering_of_app_ids_by_tag
from .utils import get_file_name_for_list_of_genres
from .utils import get_file_name_for_list_of_tags


def download_genre_and_tag_keys(data_source='top100in2weeks', num_apps=100):
    # Genres and tags downloaded from SteamSpy API

    print('Downloading lists of genres and tags for {}.'.format(data_source))

    # Retrieve top 100 games played in the past 2 weeks

    data_request = dict()
    data_request['request'] = data_source

    data = steamspypi.download(data_request)

    # Aggregate genres and tags

    genres = set()
    tags = set()

    for counter, app_id in enumerate(data):

        data_request = dict()
        data_request['request'] = 'appdetails'
        data_request['appid'] = app_id

        data_app_id = steamspypi.download(data_request)

        current_genres = set(s.strip() for s in data_app_id['genre'].split(','))
        current_tags = set(data_app_id['tags'].keys())

        genres.update(current_genres)
        tags.update(current_tags)

        # Allowed poll rate - 4 requests per second.
        # Reference: https://steamspy.com/api.php
        if counter % 4 == 0:
            print('{}/{}'.format(counter, len(data)))
            time.sleep(1)

    genres = sorted(genres)
    tags = sorted(tags)

    with open(get_file_name_for_list_of_genres(), 'w', encoding='utf8') as f:
        print('\n'.join(genres), file=f)

    with open(get_file_name_for_list_of_tags(), 'w', encoding='utf8') as f:
        print('\n'.join(tags), file=f)

    return genres, tags


def populate_genres(genres):
    print('Downloading clusters of appIDs for each genre.')

    genres_dict = dict()

    for counter, current_genre in enumerate(genres):

        data_request = dict()
        data_request['request'] = 'genre'
        data_request['genre'] = current_genre

        data = steamspypi.download(data_request)

        genres_dict[current_genre] = list(int(app_id) for app_id in data.keys())

        # Allowed poll rate - 4 requests per second.
        # Reference: https://steamspy.com/api.php
        if counter % 4 == 0:
            print('{}/{}'.format(counter, len(genres)))
            time.sleep(1)

    with open(get_file_name_for_clustering_of_app_ids_by_genre(), 'w', encoding='utf8') as f:
        json.dump(genres_dict, f)

    return genres_dict


def populate_tags(tags):
    print('Downloading clusters of appIDs for each tag.')

    tags_dict = dict()

    for counter, current_tag in enumerate(tags):

        data_request = dict()
        data_request['request'] = 'tag'
        data_request['tag'] = current_tag

        data = steamspypi.download(data_request)

        tags_dict[current_tag] = list(int(app_id) for app_id in data.keys())

        # Allowed poll rate - 4 requests per second.
        # Reference: https://steamspy.com/api.php
        if counter % 4 == 0:
            print('{}/{}'.format(counter, len(tags)))
            time.sleep(1)

    with open(get_file_name_for_clustering_of_app_ids_by_tag(), 'w', encoding='utf8') as f:
        json.dump(tags_dict, f)

    return tags_dict


def download(data_source='top100in2weeks'):
    genres, tags = download_genre_and_tag_keys(data_source)

    genres_dict = populate_genres(genres)
    tags_dict = populate_tags(tags)

    return genres_dict, tags_dict
