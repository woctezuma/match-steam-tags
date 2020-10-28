from .download_genre import populate_genres
from .download_genre_tag import download_genre_and_tag_keys
from .download_tag import populate_tags


def download(data_source="top100in2weeks"):
    genres, tags = download_genre_and_tag_keys(data_source)

    genres_dict = populate_genres(genres)
    tags_dict = populate_tags(tags)

    return genres_dict, tags_dict


if __name__ == "__main__":
    genres_dict, tags_dict = download(data_source="top100in2weeks")
