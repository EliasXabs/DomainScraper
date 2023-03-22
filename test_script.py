import re
import argparse
import requests
from urllib.request import urlopen

def swapsubdomain(sdomain, subdomain):
    protocol = re.match(r"https?:\/\/", sdomain).group()
    sdomain = re.sub(r"https?:\/\/www\.", "", sdomain)
    return protocol+subdomain+"."+sdomain


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

print("Checking:",domain)


try :
    exists = requests.get(domain)
except :
    print("Error : Please enter a domain that exists")
    exit()


subdomains = open("./Potential/potential_subdomains.bat", "r")
s_output = open("./Output/subdomains_output.bat", "w")

trailing_spaces = r'^\s+|\s+$|[^a-zA-Z0-9\s]'

with subdomains as line:
    l = line.readline()
    while (l):
        nospace = re.sub(trailing_spaces, "", l)
        swapped = swapsubdomain(domain, nospace)
        try :
            test = requests.get(swapped)
            s_output.write(swapped+"\n")
        except :
            pass

        l = line.readline()

directories = open("./Potential/dirs_dictionary.bat", "r")
d_output = open("./Output/directories_output.bat", "w")

with directories as line:
    l = line.readline
    while (l):
        nospace= re.sub(trailing_spaces, "", l)
        swapped = domain+"/"+nospace
        try:
            test = requests.get(swapped)
            d_output.write(swapped+"\n")
        except:
            pass
        l = line.readline()
try:
    html = urlopen(domain).read().decode()
    f_output = open("./Output/files_output.bat", "w")

    link = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
    matches = re.findall(link, html)
    for link in list(matches):
        f_output.write(link)
except:
    print("Forbidden access")

print("Done")