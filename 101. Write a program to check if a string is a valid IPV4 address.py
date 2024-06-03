def is_valid_ipv4_address(ip):
    parts = ip.split(".")
    
    # Check if the IP address has exactly four parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is a number and within the range 0-255
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
        
        # Check if there are leading zeros
        if part != str(int(part)):
            return False
    
    return True

# Test cases
test_ips = [
    "192.168.0.1",
    "255.255.255.255",
    "0.0.0.0",
    "256.100.50.0",
    "192.168.0.01",
    "192.168.0",
    "192.168.0.256",
    "abc.def.ghi.jkl"
]

for ip in test_ips:
    print(f"{ip}: {is_valid_ipv4_address(ip)}")
