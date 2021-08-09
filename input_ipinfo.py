import urllib.request
import ipinfo
import json
import os

DATA = dict(Result=list())
token = input ("Insert your token: ");
handler = ipinfo.getHandler(token)

ip = input ("Insert an IP: ");
file = open("ip.txt", "w")
file.write(ip)
file.close()
ips = open('ip.txt', 'r')

for ipAddress in ips:
    result = handler.getDetails(ipAddress)
    
    item = {  
        "ip": result.all.get('ip', None),
        "city": result.all.get('city', None),
        "region": result.all.get('region', None),
        "country": result.all.get('country', None),
        "loc": result.all.get('loc', None),
        "postal": result.all.get('postal', None),
        "timezone": result.all.get('timezone', None),
        "hosting_provider": result.all.get('org',None),
        "reverse_dns": result.all.get('hostname', None)
    }

    DATA['Result'].append(item), '\n'

    with open('ip_info.json', 'w') as outfile:
        json.dump(DATA, outfile, indent=4)


    if os.path.exists("ip.txt"):
        os.remove("ip.txt")
    else:
        os.remove("ip.txt")
        