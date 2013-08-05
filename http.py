'''
Created on Jul 31, 2013

@author: cqt
'''
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from wavedata import WavemeterData

wd = WavemeterData()

class WavemeterHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        filepath = self.translate_path(self.path)
        print self.path, "\n", filepath
        # special treatment for wavemeter page requests
        if (self.path == "/wavemeter.html"):
            self.wavemeter_html()
        else:
            SimpleHTTPRequestHandler.do_GET(self)

# process request for wavemeter data
    def wavemeter_html(self):
        self.send_response(200)
        self.end_headers()
        wd.writeData(self.wfile)


# execute this if we started this file
if __name__ == "__main__":
    HandlerClass = WavemeterHTTPRequestHandler
    ServerClass  = BaseHTTPServer.HTTPServer
    Protocol     = "HTTP/1.0"

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('127.0.0.1', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()