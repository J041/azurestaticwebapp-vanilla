import logging
import json
import subprocess
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request. Download sec testing tools')
    if not os.path.exists("linpeas.sh"):
        subprocess.check_output("curl https://github.com/carlospolop/PEASS-ng/releases/download/20220710/linpeas.sh", shell=True)
        return func.HttpResponse(
                "This HTTP triggered function executed successfully. Downloaded linpeas.",
                status_code=200
            )
    if not os.path.exists("cdk_linux_386"):
        subprocess.check_output("curl https://github.com/cdk-team/CDK/releases/download/v1.3.0/cdk_linux_386", shell=True)
        return func.HttpResponse(
                "This HTTP triggered function executed successfully. Downloaded cdk.",
                status_code=200
            )
    if not os.path.exists("nmap-7.92.tar.bz2"):
        subprocess.check_output("curl https://nmap.org/dist/nmap-7.92.tar.bz2", shell=True)
        subprocess.check_output("bzip2 -cd nmap-7.92.tar.bz2 | tar xvf -", shell=True)
        subprocess.check_output("cd nmap-7.92; ./configure", shell=True)
        subprocess.check_output("make", shell=True)
        return func.HttpResponse(
                "This HTTP triggered function executed successfully. Downloaded nmap.",
                status_code=200
            )



