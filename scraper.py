import re
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("Domain_name", help="Name of the domain that will be scraped")
domain = getattr(parser.parse_args(), "Domain_name")

exists = requests.get('http://www.google.com')

if exists :
    print("Exists")
else :
    print("Error : Please enter a domain that exists")
    print("Terminating . . .")
    exit()