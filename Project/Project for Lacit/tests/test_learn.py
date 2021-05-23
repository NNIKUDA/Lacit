import subprocess
from urllib.request import urlopen, Request  # для отправки запросов сервисам
import json  # для конвертации данных



def Learn(samples):


    data = json.dumps(samples).encode('utf-8')

    req = Request('http://localhost:8000 ',
                  headers={'Contest-Type': 'application/json'},
                  data=data,
                  method='POST')

    try:
        with urlopen(req) as resp:
            resp_bytes = resp.read()

            resp_str=resp_bytes.decode('utf-8')

            return resp_str

    except IOError as e:

        print(e,'\nОтвет от сервера не получен.')

def test_start1():
    assert '"OK"'==Learn({'x':[[0.1,0.2], [0.2,0.3]], 'y':[1,0]})


def test_start2():
    assert 'OK'==Learn({'x': [],
                 'y': []})


def test_start3():
    assert 'OK'==Learn({'x':[0.1, 0.2], 'y':[10]})


def test_start4():
    assert 'OK'==Learn({'x':[[0.1, 0.2]]})



