import logging
import json
import subprocess
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    x = []
    logging.info('Python HTTP trigger function processed a request. Download sec testing tools')
    if not os.path.exists("linpeas.sh"):
        subprocess.check_output("curl -L https://github.com/carlospolop/PEASS-ng/releases/download/20220710/linpeas.sh -o linpeas.sh", shell=True)
        x.append("linpeas")
    if not os.path.exists("cdk_linux_386"):
        subprocess.check_output("curl -L https://github.com/cdk-team/CDK/releases/download/v1.3.0/cdk_linux_386 -o cdk_linux_386", shell=True)
        x.append("cdk")
    if not os.path.exists("nmap"):
        # subprocess.check_output("curl https://nmap.org/dist/nmap-7.92.tar.bz2 -o nmap-7.92.tar.bz2", shell=True)
        # subprocess.check_output("bzip2 -cd nmap-7.92.tar.bz2 | tar xvf -", shell=True)
        # subprocess.check_output("./nmap-7.92/configure", shell=True)
        # subprocess.check_output("./nmap-7.92/make", shell=True)
        # subprocess.check_output("./nmap-7.92/make install", shell=True)
        subprocess.check_output("curl https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/nmap -o nmap", shell=True)
        x.append("nmap")
    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Downloaded "+str(x),
            status_code=200
        )



