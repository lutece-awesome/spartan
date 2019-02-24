#!/usr/bin/env python
# coding=utf-8

import time
import BaseHTTPServer
import urllib
import json
import base64
import ConfigParser
cf = ConfigParser.ConfigParser()

cf.read('./src/conf/spartan.config')

HOST_NAME = str(cf.get("base", "host"))
PORT_NUMBER = int(cf.get("base", "port"))

CONIFRM_PATH = './log'

class HttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _json_encode(self, data):
        array = data.split('&')
        json_data = {}
        for item in array:
            item = item.split('=', 1)
            json_data[item[0]] = item[1]
        return json_data

    def _get_handler(self, data):
        json_data = self._json_encode(data)

    def _post_handler(self, data):
        retVal = {}
        json_data = self._json_encode(data)
        file_name = json_data['FileName']
        file_data = base64.b64decode(json_data['FileData'])
        file_path = f'{CONIFRM_PATH}/{file_name}'
        fd = open(file_path, 'w')
        fd.write(file_data)
        fd.close()
        retVal["RetCode"] = 0
        return json.dumps(retVal)

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        path = self.path
        query = urllib.splitquery(path)
        self._get_handler(query[1])

    def do_POST(self):
        self._set_headers()
        post_data = self.rfile.read(int(self.headers['content-length']))
        post_data = urllib.unquote(post_data).decode("utf-8", 'ignore')
        retStr = self._post_handler(post_data)
        self.wfile.write(retStr)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HttpHandler)
    print(time.asctime(), f'Server Starts - {HOST_NAME}:{PORT_NUMBER}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), f'Server Stops - {HOST_NAME}:{PORT_NUMBER}')