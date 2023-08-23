# ChatGPT_주민번호.py

import re

def validate_korean_ssn(ssn):
    ssn = re.sub(r'\D', '', ssn)
    
    if len(ssn) < 6 or len(ssn) > 7:
        return False
    
    year_digit = int(ssn[0])
    if year_digit < 0 or year_digit > 9:
        return False
    
    month = int(ssn[1:3])
    if month < 1 or month > 12:
        return False
    
    day = int(ssn[3:5])
    if day < 1 or day > 31:
        return False
    
    last_digit = int(ssn[-1])
    if last_digit < 1 or last_digit > 4:
        return False
    
    return True

ssn_examples = [
    "950101-1234567",
    "8802024567890",
    "030504-2345678",
    "761214-3456789",
    "0108101234567",
    "900531-2345678",
    "6712314567890",
    "830712-3456789",
    "0410051234567",
    "720719-2345678"
]

for ssn in ssn_examples:
    if validate_korean_ssn(ssn):
        print(f"{ssn} is a valid Korean social security number.")
    else:
        print(f"{ssn} is not a valid Korean social security number.")
