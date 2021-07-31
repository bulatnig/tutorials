import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    headers = {'my_header': 'abcd'}
    response = requests.get("https://httpbin.org/headers", headers=add_tracing_headers(headers))
    return response.json()


def add_tracing_headers(headers=None):
    """Append tracing headers to any headers already provided for the request.

    See https://istio.io/latest/docs/tasks/observability/distributed-tracing/
    """
    if headers is None:
        headers = {}
    for header in (
            'x-request-id',
            'x-b3-traceid',
            'x-b3-spanid',
            'x-b3-parentspanid',
            'x-b3-sampled',
            'x-b3-flags',
            'x-ot-span-context'
    ):
        value = request.headers.get(header)
        if value:
            headers[header] = value
    return headers


if __name__ == '__main__':
    app.run()
