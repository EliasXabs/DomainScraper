import re
import argparse
import requests

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

# if not re.findall(r"\/www\.", domain) :
#     protocol = re.match(http_p, domain).group()
#     domain = protocol+"www."+re.sub(http_p, "", domain)

# if not re.findall(r"\.com$", domain):
#     domain = domain+".com"

print("Checking:",domain)


try :
    exists = requests.get(domain)
except :
    print("Error : Please enter a domain that exists")
    exit()


subdomains = open("./Potential/potential_subdomains.bat", "r")
s_output = open("./Output/subdomains_output.bat", "w")
count = 0
with subdomains as line:
    l = line.readline()
    while (l):
        swapped = swapsubdomain(domain, l.rstrip())
        try :
            test = requests.get(swapped)
            s_output.write(swapped+"\n")
            print("Found", count)
        except :
            print("not Found")

        print ("Next Line", count)
        count += 1

        l = line.readline()

