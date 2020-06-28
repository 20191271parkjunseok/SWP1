from wsgiref.simple_server import make_server
from calc import application

httpd = make_server (
        '',
        8051,
        application
)

httpd.serve_forever()

