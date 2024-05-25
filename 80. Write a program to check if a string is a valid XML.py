import xml.etree.ElementTree as ET

def check_xml(string):
    try:
        ET.fromstring(string)
        return True
    except ET.ParseError:
        return False  

string='<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Do not forget me this weekend!</body></note>'

if check_xml(string):
    print("this is valid xml string")
else:
    print("this is not valid string")    