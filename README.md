# Match Steam Tags

[![PyPI status][pypi-image]][pypi]
[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

This repository contains Python code to match Steam tags with appIDs.

## Installation

The code is packaged for [PyPI](https://pypi.org/project/steamtags/), so that the installation consists in running:

```bash
pip install steamtags
```

## Usage

### Load genres and tags from a local cache, if available. Otherwise, download them.

```python
import steamtags

genres_dict, tags_dict = steamtags.load()
```

### Download genres and tags based on Top 100 games, with respect to the number of players in the last two weeks.

```python
import steamtags

genres_dict, tags_dict = steamtags.download(data_source='top100in2weeks')
```

### Download genres and tags based on Top 100 games, with respect to the number of players since March 2009.

```python
import steamtags

genres_dict, tags_dict = steamtags.download(data_source='top100forever')
```

### Download genres and tags based on Top 100 games, with respect to the estimated number of owners.

```python
import steamtags

genres_dict, tags_dict = steamtags.download(data_source='top100owned')
```

## References

-   An exhaustive list of tags can be found in [`steam-labs-recommender`](https://github.com/woctezuma/steam-labs-recommender).
-   [`gamedatacrunch`][gamedatacrunch-api]@[PyPI][gamedatacrunch-pypi]: an API to download data through [GameDataCrunch API][gamedatacrunch].
-   [`steamspypi`][steamspy-api]@[PyPI][steamspy-pypi]: an API to download data through [SteamSpy API][steamspy-api-docs].

<!-- Definitions -->

[gamedatacrunch-api]: <https://github.com/woctezuma/gamedatacrunch>
[gamedatacrunch-pypi]: <https://pypi.org/project/gamedatacrunch/>
[gamedatacrunch]: <https://www.gamedatacrunch.com>

[steamspy-api]: <https://github.com/woctezuma/steamspypi>
[steamspy-pypi]: <https://pypi.org/project/steamspypi/>
[steamspy-api-docs]: <https://steamspy.com/api.php>

[pypi]: https://pypi.python.org/pypi/steamtags
[pypi-image]: https://badge.fury.io/py/steamtags.svg

[build]: <https://github.com/woctezuma/match-steam-tags/actions>
[build-image]: <https://github.com/woctezuma/match-steam-tags/workflows/Python package/badge.svg?branch=master>
[publish-image]: <https://github.com/woctezuma/match-steam-tags/workflows/Upload Python Package/badge.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/match-steam-tags/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/match-steam-tags/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/match-steam-tags/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/match-steam-tags>
[codecov-image]: <https://codecov.io/gh/woctezuma/match-steam-tags/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/match-steam-tags>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/99ed16e3606947e391ace1e1910305c4>
