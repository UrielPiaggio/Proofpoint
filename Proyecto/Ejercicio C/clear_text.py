import string

def normalize_text(text):
    
    
    text = text.lower()
    #remove special characters
    text = text.translate(str.maketrans("", "", string.punctuation))
    #remove strage signs
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    # remove much spaces
    text = " ".join(text.split())
    return text
    
    
    
    