import falcon
import io

from wsgiref import simple_server

#https://stackoverflow.com/a/6658130
class iter_to_stream(object):
    def __init__(self, bytes, times):
        self.cnt = 0
        self.bytes = bytes
        self.times = times

    #iterate and return the data to be sent, send empty bytes when completed
    def read(self, size):
        # print(f'requested size {size}') # 8192 bytes
        if self.cnt < self.times:
            self.cnt = self.cnt + 1
            return self.bytes
        return b''


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        # resp.body = ('hello world!')

        #https://docs.python.org/3.4/library/io.html?highlight=io#buffered-streams
        # resp.set_stream(io.BytesIO(b"abcdef"), 6)

        resp.set_stream(iter_to_stream(b'abc', 5), 5*3)


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()

