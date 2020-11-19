def prepare_text(text):
    import re
    text = text.lower()
    text = text.translate(text.maketrans('','','()@^`~*'))
    text = re.sub(r'<br/>', ' ', text)
    text = re.sub(r'</?strong>',' ',text)
    text = re.sub(r'</?em>',' ',text) 
    text = re.sub(r'</?p>', ' ', text)
    text = re.sub(r'</?br>', ' ', text)
    text = re.sub(r'</?ul>', ' ', text)
    text = re.sub(r'</?li>', ' ', text)
    text = re.sub(r'</?sup>', ' ', text)
    text = re.sub(r'</?small>', ' ', text)
    text = re.sub(r'/', ',', text)
    text = re.sub(r'\\', ' ', text)
    text = re.sub(r'(\s\d+[,\.\/\-x]*\d*)\s*(m?c?l)[\W]',r'\1\2 ',text)
    text = re.sub(r'(\s\d+[,\.\/\-x]*\d*)\s*(m?c?l)$',r'\1\2 ',text)
    text = re.sub(r'(\s\d+[,\.\/\-x]*\d*)\s*(m?k?g)[\W]',r'\1\2 ',text)
    text = re.sub(r'(\s\d+[,\.\/\-x]*\d*)\s*(m?k?g)$',r'\1\2 ',text)
    text = re.sub(r'([ø\s]\d+[,\.\/\-x]*\d*)\s*(m?c?m)$',r'\1\2 ',text)
    text = re.sub(r'([ø\s]\d+[,\.\/\-x]*\d*)\s*(m?c?m)[\W]',r'\1\2 ',text)
    text = re.sub(r'\s+\.','.',text)
    text = re.sub(r'\.+','.',text)    
    text = re.sub(r'&nbsp','',text)
    text = re.sub(r'é','e',text)
    text = re.sub(r'<br/>', '', text)
    text = re.sub(r'</?strong>','',text)
    text = re.sub(r'</?em>','',text)
    text = re.sub(r'é','e',text)
    text = re.sub(r'®',' ',text)
    text = re.sub(r'\s\s+', ' ', text)
    text = text.strip()
    return text