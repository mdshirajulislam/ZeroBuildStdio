import json

def send_json_response(handler, status_code, data):
    handler.send_response(status_code)
    handler.send_header('Content-type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(data).encode('utf-8'))

def parse_request_body(handler):
    content_length = int(handler.headers.get('Content-Length', 0))
    if content_length > 0:
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode('utf-8'))
    return {}
