import requests

def get_sura(n):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ben-muhiuddinkhan-la/{n}/1.json"

    return requests.get(url).json()


def get_oyat(n, m):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ben-muhiuddinkhan-la/{n}/{m}.json"

    return requests.get(url).json()
