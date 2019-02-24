#!/usr/bin/env python
# coding=utf-8

import time

import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer

import run
from src.conf.conf import *

HOST_NAME = HOST
PORT_NUMBER = PORT

CONIFRM_PATH = './log'


class HttpHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _get_handler(self, data):
        json_data = self._json_encode(data)

    def _post_handler(self, data):

        retVal = {}
        try:
            Runner = run.SpartanRunner()
            retVal['Ret'] = Runner.run(data)
            retVal['RetCode'] = 200
        except:
            retVal['RetCode'] = 0
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
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HttpHandler)
    print(time.asctime(), 'Server Starts')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops')
