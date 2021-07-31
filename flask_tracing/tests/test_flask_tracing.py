from app import app


def test_index():
    client = app.test_client()
    header = 'x-b3-traceid'
    expected = 'abdc'

    response = client.get('/', headers={header: expected})

    headers = response.json['headers']
    actual = None
    for key in headers:
        if key.lower() == header:
            actual = headers[key]
            break
    assert actual == expected
