import requests


def check_link(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        return response.status_code

    except Exception:

        return None