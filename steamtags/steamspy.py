import steamspypi


def download_top100(request="top100in2weeks"):
    data_request = {"request": request}
    data = steamspypi.download(data_request)

    return data


def download_appdetails(appid):
    data_request = {"request": "appdetails", "appid": appid}
    data = steamspypi.download(data_request)

    return data


def download_genre(genre):
    data_request = {"request": "genre", "genre": genre}
    data = steamspypi.download(data_request)

    return data


def download_tag(tag):
    data_request = {"request": "tag", "tag": tag}
    data = steamspypi.download(data_request)

    return data
