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

if not re.match(r"^https?:\/\/", domain) :
    sec = input("Is the protocol secure? (y/n): ")
    if sec.lower() == "y" :
        domain = "https://"+domain
    elif sec.lower == "n" :
        domain = "http://"+domain
    else:
        print("Please enter a valid answer")

exists = requests.get(domain)

if exists :
    print("Exists")
else :
    print("Error : Please enter a domain that exists")
    exit()