from pathlib import Path


def get_data_folder():
    data_path = "data/"
    Path(data_path).mkdir(parents=True, exist_ok=True)
    return data_path


def get_file_name_for_list_of_genres():
    return get_data_folder() + "genre_keys.json"


def get_file_name_for_clustering_of_app_ids_by_genre():
    return get_data_folder() + "genre_values.json"


def get_file_name_for_list_of_tags():
    return get_data_folder() + "tag_keys.json"


def get_file_name_for_clustering_of_app_ids_by_tag():
    return get_data_folder() + "tag_values.json"
