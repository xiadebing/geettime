import requests
# from jsonpath import jsonpath
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

def test_get():
    # s = requests.Session()
    # s.mount('https://',
    #       HTTPAdapter(max_retries=Retry(total=5, method_whitelist=frozenset(['GET', 'POST']))))  # 设置 post()方法进行重访问
    r = requests.get("https://httpbin.ceshiren.com/get")
    print(r.text)
    print(r.json())

def test_post_data():
    s = requests.Session()
    s.mount('https://',
            HTTPAdapter(max_retries=Retry(total=5, method_whitelist=frozenset(['GET', 'POST']))))  # 设置 post()方法进行重访问
    r = s.post(
        "https://httpbin.ceshiren.com/post",
        data="hello world")
    assert r.status_code == 200
    print(r.text)

def test_post_form():
    r = requests.post(
        "https://httpbin.ceshiren.com/post",
        data={"f1": 1, "f2": 2}
    )
    assert r.status_code == 200
    print(r.text)

def test_post_json():

    r = requests.post(
        "http://httpbin.ceshiren.com/post",
        # json={"j1": 1, "j2": 2},
        # headers={"h1": "test"},
        # cookies={"c1": "cookie test"}
    )
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    # print(r.json())
    # assert r.status_code == 200
    # assert r.json()["json"]["j1"] == 1
    # assert "1" in jsonpath(r.json(), '$..j1')
    print(r.text)