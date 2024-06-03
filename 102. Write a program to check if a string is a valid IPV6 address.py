import re

def is_valid_ipv6_address(ip):
    # Regular expression for validating an IPv6 address
    ipv6_pattern = re.compile(r"""
        ^(?:                                      # Match the start of the string
            (?:[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7})|  # Match 1:1:1:1:1:1:1:1 format
            (?:[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,6}::[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,6})|  # Match ::1:1:1:1:1:1 format
            (?:[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})|  # Match 1::1:1:1:1:1 format
            (?:[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,4}::[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,4})|  # Match 1:1::1:1:1:1 format
            (?:[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,3}::[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,3})|  # Match 1:1:1::1:1:1 format
            (?:[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,2}::[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,2})|  # Match 1:1:1:1::1:1 format
            (?:[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4})?)|  # Match 1:1:1:1:1::1 format
            (?:[0-9A-Fa-f]{1,4}::[0-9A-Fa-f]{1,4})|  # Match 1:1:1:1:1:1:: format
            (?:[0-9A-Fa-f]{1,4}:){1,7}:            # Match 1:1:1:1:1:1:1:: format
        )$                                        # Match the end of the string
    """, re.VERBOSE)

    # Match the IPv6 address pattern
    if ipv6_pattern.match(ip):
        return True
    return False

# Test cases
test_ips = [
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "2001:db8:85a3::8a2e:370:7334",
    "::1",
    "fe80::1",
    "1200::AB00:1234::2552:7777:1313",  # Invalid
    "1200:0000:AB00:1234:O000:2552:7777:1313",  # Invalid (O instead of 0)
    "1200::AB00:1234:2552:7777:1313",
    "2001:0db8:85a3:0000:0000:8A2E:0370:7334"
]

for ip in test_ips:
    print(f"{ip}: {is_valid_ipv6_address(ip)}")
