import logging
import re
import requests
# from ..requests import requests
import azure.functions as func



# /ssrf?url=https://www.google.com&header_name=test&header_value=value
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    header_name = req.params.get('header_name')
    header_value = req.params.get('header_value')

    if url:
        if header_name or header_value:
            x = requests.get(url)
        else:
            x = requests.get(url, headers={header_name: header_value})
        return func.HttpResponse(x, status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a url in the query string or in the request body for a personalized response.",
             status_code=200
        )
