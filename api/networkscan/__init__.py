import logging
import socket

import azure.functions as func

# /networkscan?dst_ip=0.0.0.0
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    dst_ip = req.params.get('dst_ip')
    output = ''
    # dst_ip = 'x.x.x.x'
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((dst_ip, port))
        if result == 0:
            output += 'Port {} is open\n'.format(port)
        s.close()

    return func.HttpResponse(
            output,
            status_code=200
    )

