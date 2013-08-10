'''
Created on Jul 31, 2013

@author: cqt
'''
import sys
import BaseHTTPServer
import SocketServer
import urlparse
from SimpleHTTPServer import SimpleHTTPRequestHandler
from wavedata import WavemeterData

class ThreadingHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

class WavemeterHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        filepath = self.translate_path(self.path)
        print self.path, "\n", filepath
        # special treatment for wavemeter page requests
        if (self.path == "/wavemeter.html"):
            self.wavemeter_html()
        elif (self.path == "/sse.html"):
            self.wavemeter_sse()
#        elif (self.path.find("/control.html") > 0):
        elif (self.path.find("/control.html") >= 0):
            self.wavemeter_control()
        else:
            SimpleHTTPRequestHandler.do_GET(self)

# process request for wavemeter data
    def wavemeter_html(self):
        self.send_response(200)
        self.end_headers()
        wd.writeData(self.wfile)

    def wavemeter_sse(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Connection", "keep-alive")
        self.send_header("Pragma", "no-cache")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write("data: Started connection\n\n")
        wd.addSSEClient(self.wfile)
        
    def wavemeter_control(self):
        self.send_response(200)
        self.end_headers()
        query  = urlparse.urlparse(self.path).query
        params = urlparse.parse_qs(query)
        try:
            ch     = params.get('ch', None)[0]
            action = params.get('action', None)[0]
            value  = params.get('value', None)[0]
            wd.controlState(int(ch), action, int(value))
        except:
            print "Error parsing parameters", sys.exc_info()
        self.wfile.write("<OK>")

# execute this if we started this file
if __name__ == "__main__":
    HandlerClass = WavemeterHTTPRequestHandler
#    ServerClass  = BaseHTTPServer.HTTPServer
    ServerClass  = ThreadingHTTPServer
    Protocol     = "HTTP/1.0"
    
    wd = WavemeterData()
    wd.start()

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
#    server_address = ('127.0.0.1', port)
    server_address = ('0.0.0.0', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)
#    httpd = ThreadingHTTPServer(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()