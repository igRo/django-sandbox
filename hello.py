def wsgi_hello(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    body = []
    for param in environ["QUERY_STRING"].split('&'):
        body.append(param + '\n')
    start_response(status, response_headers)
    return [ body ]
