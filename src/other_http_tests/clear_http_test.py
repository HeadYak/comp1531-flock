import sys
sys.path.append('../')
import requests


def test_clear_http(url):
    resp = requests.delete(f"{url}/clear", json={})
    assert resp.status_code == 200

