[![Version](https://img.shields.io/pypi/v/fbiter.svg)][https://pypi.python.org/pypi/fbiter] [![License](https://img.shields.io/pypi/l/fbiter.svg)][https://pypi.python.org/pypi/fbiter]

# fbiter

`fbiter` is a simple Python library for iterating through paginated Facebook API endpoints.

## Installation

```sh
pip install fbiter
```

## Usage

```python
import fbiter
import os

endpoint = fbiter.Endpoint("v2.10/BuzzFeedNews/posts", params={
    "access_token": os.environ["FB_ACCESS_TOKEN"],
    "limit": 10
})

print(endpoint.get(max_results=15))
```

## `fbiter.Endpoint`

This is `fbiter`'s core class. It takes __two parameters__:

- `path`: The API endpoint path, including the API version number, but excluding `https://graph.facebook.com/`.
- `params`: A `dict` containing the relevant API params, the only required one of which is `access_token`.

`fbiter.Endpoint` also has the following __methods__:

- `.iter_results(max_results=None)`: Returns a Python iterator object that returns one result item at a time, up to `max_results` result items.
- `.get(max_results=None)`: Returns all result items as a list, after paginating through each available page, up to `max_results` result items.

## Errors

The library tries to handle HTTP errors in the following ways:

- `HTTP 400` and `HTTP 404`: Returns `{ "data": [] }`
- All other errors: Sleeps 10 seconds and then tries again.

