from io import BytesIO
import base64

def convert_to_base64(file: BytesIO):
    base64_content = base64.b64encode(file.getvalue()).decode('utf-8')
    
    return base64_content