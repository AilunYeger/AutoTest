import requests, os
from utils.sourceLoad import data
from utils.logger import logger
import json as complexjson

class HttpRequests():

    def send(self, url, method, data=None, json=None, **kwargs):
        url = self.host + url
        headers = dict(**kwargs).get('headers')
        params = dict(**kwargs).get('params')
        files = dict(**kwargs).get('files')
        cookies = dict(**kwargs).get('cookies')

        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == 'GET':
            return self.session.get(url, data, json, **kwargs)
        if method == 'POST':
            return self.session.post(url, data, json, **kwargs)
        if method == 'DELETE':
            return self.session.delete(url, data, json)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))

if __name__ == '__main__':
    RQ = HttpRequests()
    RQ.send('/pay/single/pay', 'GETT')





