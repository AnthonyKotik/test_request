import requests

appid = 'd4edba3f805fccacc2e6d1bd34174e51'


def test_200():
    city = 'Moscow'
    payload = {}
    with open("test200.txt") as f:
        for line in f:
            (key, val) = line.split()
            payload[key] = val

    r = requests.get('https://api.openweathermap.org/data/2.5/weather?appid='+appid, params=payload)
    assert r.status_code == 200
    assert r.json()['name'] == city
    print(r.json())

def test_404():
    payload = {}
    with open("test404.txt") as f:
        for line in f:
            (key, val) = line.split()
            payload[key] = val

    s = requests.get('http://api.openweathermap.org/geo/2.0/direct?appid='+appid, params=payload)

    assert s.status_code == 404

    print(s.text)

def test_401():
    payload = {}
    with open("test401.txt") as f:
        for line in f:
            (key, val) = line.split()
            payload[key] = val

    s = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={+lat+}&lon={+long+}', params=payload)

    assert s.status_code == 401

    print(s.text)

def test_400():
    payload = {}
    with open("test400.txt") as f:
        for line in f:
            (key, val) = line.split()
            payload[key] = val

    s = requests.get('https://api.openweathermap.org/data/2.5/weather?appid='+appid, params=payload)

    assert s.status_code == 400

    print(s.text)

