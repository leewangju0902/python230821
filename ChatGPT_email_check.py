# chatGPT_emal.py

import re

def is_valid_email(email):
    # Regular expression pattern to match a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.search(pattern, email):
        return True
    else:
        return False

# Sample email addresses
sample_emails = [
    "user@example.com",        # Valid
    "john.doe@gmail.com",      # Valid
    "invalid_email",           # Invalid
    "name123@yahoo",           # Invalid
    "contact@domain.co.uk",    # Valid
    "no_reply@example",        # Invalid
    "support@123.com",         # Valid
    "admin@site",              # Invalid
    "test.email@gmail.com",    # Valid
    "12345@domain.com",        # Valid
]

for email in sample_emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is NOT a valid email address.")


