import re

def is_valid_html_regex(html_string):
    
    tag_re = re.compile(r'<[^>]+>')
    return bool(tag_re.search(html_string))


html_string = "<html><head><title>Test</title></head><body><h1>Header</h1></body></html>"
print(is_valid_html_regex(html_string))  

invalid_html_string = "This is not HTML"
print(is_valid_html_regex(invalid_html_string))  
