import requests
import re


class Categ:
    def __init__(self, name):
        self.name = name
        self.PATTERN = 'data-docid="(.*?)"'

    @property
    def app_names(self):
        pass

    def top_n_app(self, n=100):
        url = "https://play.google.com/store/apps/category/ART_AND_DESIGN/collection/topselling_free"
        things = set()
        querystring = {"authuser": "0"}
        for i in xrange((n / 100) + 1):
            payload = "start=%s&num=100&numChildren=0&ipf=1&xhr=0" % i * 100
            headers = {
                'origin': "https://play.google.com",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "zh-CN,zh;q=0.9",
                'x-chrome-uma-enabled': "1",
                'x-client-data': "CIu2yQEIpLbJAQjBtskBCPqcygEIqZ3KAQioo8oB",
                'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
                'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
                'accept': "*/*",
                'referer': "https://play.google.com/store/apps/category/ART_AND_DESIGN/collection/topselling_free",
                'authority': "play.google.com",
                'dnt': "1",
                'cache-control': "no-cache",
                'postman-token': "0db5319f-c7a8-20bb-e208-d87a74bd60d6"
            }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring, timeout=10)
            for i in re.findall(self.PATTERN, response.text):
                if i not in things:
                    things.add(i)
                    print i

    @property
    def download_top_n_app(self, n):
        pass


if __name__ == '__main__':
    print(Categ(name='ART_AND_DESIGN').top_n_app(n=100))
