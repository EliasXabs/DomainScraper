import re
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("Domain_name", help="Name of the domain that will be scraped")
try :
    domain = getattr(parser.parse_args(), "Domain_name")
except :
    print ("Please enter a valid domain") 
    exit()

http_p = r"^https?:\/\/"

if not re.match(http_p, domain) :
    sec = input("Is the protocol secure? (y/n): ")
    if sec.lower() == "y" :
        domain = "https://"+domain
    elif sec.lower() == "n" :
        domain = "http://"+domain
    else:
        print("Please enter a valid answer")
        exit()

if not re.findall(r"\/www\.", domain) :
    protocol = re.match(http_p, domain).group()
    domain = protocol+"www."+re.sub(http_p, "", domain)

if not re.findall(r"\.com$", domain):
    domain = domain+".com"

print("Checking:",domain)

exists = requests.get(domain)

if exists :
    print("Exists")
else :
    print("Error : Please enter a domain that exists")
    exit()