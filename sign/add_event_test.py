import unittest, requests, hashlib
from time import time


class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_add_event/"
        self.api_key = "&Guest-Bugmaster"
        now_time = time()
        self.client_time = str(now_time).split('.')[0]
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_request_error(self):
        '''请求错误'''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message', 'request error'])

    def test_add_event_sign_null(self):
        '''签名参数'''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '',
                   'start_time': '', 'time': '', 'sign': ''
                   }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user sign null')

