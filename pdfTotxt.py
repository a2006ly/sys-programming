from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from glob import glob
import os

inpath = r'C:\Users\user\Desktop\workspace\doc\�ω�\��V�X4'
file_list = glob(inpath + '\*.pdf') # PDF�t�@�C����荞��
print(len(file_list))
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    laparams.detect_vertical = True # True�ɂ��邱�Ƃ��Y��Ƀe�L�X�g�𒊏o�ł���
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    maxpages = 0
    caching = True
    pagenos=set()
    fstr = ''
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        str = retstr.getvalue()
        fstr += str

    fp.close()
    device.close()
    retstr.close()
    return fstr

result_list = []
for item in file_list:
    dirp = os.path.dirname(item)
    dirn = os.path.basename(item)
    print(item)
    result_txt = convert_pdf_to_txt(item)
    result_list.append(result_txt)
    allText = ','.join(result_list) # PDF���Ƃ̃e�L�X�g���z��Ɋi�[����Ă���̂ŘA������
    file = open(dirp + '\\'+ dirn +'.txt', 'w',encoding="utf-8")  #�������݃��[�h�ŃI�[�v��
    file.write(allText)

file.close()