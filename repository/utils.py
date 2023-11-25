from io import BytesIO
import base64
import random
import string

def convert_to_base64(file: BytesIO):
    base64_content = base64.b64encode(file.getvalue()).decode('utf-8')
    
    return base64_content

def generate_unique_code(self):
        res = ''.join(random.choices(
            string.ascii_letters +
            string.digits
            , k=8))
        
        return str(res)

accepted_months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December",
    
    "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]