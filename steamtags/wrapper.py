from .download_with_steamspy import download as steamspy_download
from .load_with_steamspy import load as steamspy_load


def get_gamedatacrunch_synonyms():
    return ['gamedatacrunch', 'gdc']


def download(website='gamedatacrunch'):
    if website in get_gamedatacrunch_synonyms():
        data = None  # TODO
    else:
        data = steamspy_download()

    return


def load(website='gamedatacrunch'):
    if website in get_gamedatacrunch_synonyms():
        data = None  # TODO
    else:
        data = steamspy_load()

    return
