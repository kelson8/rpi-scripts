import whois

# New

# https://pypi.org/project/python-whois/#description
# Basic whois lookup python

url = "https://kelsoncraft.net"
w = whois.whois(url)


print("KelsonCraft website whois info:")

print(f" {w.text}")