import re

def is_valid_ip(ip):
  
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    if re.match(pattern, ip):
        octets = ip.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)
    return False