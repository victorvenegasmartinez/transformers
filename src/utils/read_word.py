import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        if para.text!='':
            fullText.append(para.text)
    return '\n'.join(fullText)

full_text=getText("/Users/victorvenegas/courses/XCS224N-A5/src/data/CCF.docx")
file = open('/Users/victorvenegas/courses/XCS224N-A5/src/data/ccf.txt', 'w')
file.write(full_text)
file.close()