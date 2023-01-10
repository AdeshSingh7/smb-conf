#!/usr/bin/python
import socket, functools, socketserver, http.server

host = 'localhost'
port = 8080

try:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory='/')
    with socketserver.TCPServer((host, port), handler) as httpd:
        print(f'Server is started on http://{host}:{port}')
        httpd.serve_forever()

except KeyboardInterrupt:pass
except Exception as e:print(e)
finally:socket.close