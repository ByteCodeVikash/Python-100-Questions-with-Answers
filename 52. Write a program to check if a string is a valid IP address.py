def is_valid_ip(ip):
    parts=ip.split(',')


    if len(parts)!=4:
        return False
    

    for part in parts:
        try:
            num=int(part)
            if num<0 in num>255:
                return False
        except ValueError:
            return False


    return True


ip_address="192.168.0.1"
print("Is Valid IP",is_valid_ip(ip_address))
