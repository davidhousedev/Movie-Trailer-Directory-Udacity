

import SimpleHTTPServer
import SocketServer

from movie import Movie
from tvshow import TvShow

# borrowed MyRequestHandler syntax from: http://stackoverflow.com/questions/10607621/a-simple-website-with-python-using-simplehttpserver-and-socketserver-how-to-onl
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
        	self.path = '/test.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000

Handler = MyRequestHandler
httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
