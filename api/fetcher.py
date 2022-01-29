import requests

def states_acccessor():
    # Go through the doc api examples!
    url = f"https://opensky-network.org/api/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())