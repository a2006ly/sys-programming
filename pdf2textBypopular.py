import subprocess
import os
import glob
import sys
from os import path
import codecs
path_pop=r"C:\Users\user\Downloads\poppler-0.68.0\bin"

if path_pop not in os.environ['path'].split(os.pathsep):
    os.environ["path"] +=path_pop


pdfpath =r"C:\Users\user\Desktop\txt"
#pdflist = glob.glob(pdfpath + "\*.pdf")
#for p in pdflist:
#    f_path=os.path.dirname(p)
#    f_name=os.path.basename(p)

#    cmd="pdftotext -layout {0} {1}".format(p,p+".txt")
#    #p=subprocess.Popen(cmd.split(),shell=True,
#    #                 stdin=subprocess.PIPE,
#    #                 stdout=subprocess.PIPE)

#    subprocess.call(cmd.split(),shell=True)

##p.communicate()


def pdftoText(path):
    pdflist = glob.glob(path)
    print(len(pdflist))
    for p in pdflist:
        #f_path=os.path.dirname(p)
        #f_name=os.path.basename(p)

        #cmd='pdftotext,-layout,{0},{1}'.format(p,p+".txt")
        cmd='pdftotext,-layout,{0},-,>,{1}'.format(p,p+".txt")

        ##p=subprocess.Popen(cmd.split(","),shell=True,
        ##                 stdin=subprocess.PIPE,
        ##                 stdout=subprocess.PIPE)

        
        subprocess.call(cmd.split(","),shell=True)


if len(sys.argv) < 2: sys.exit("error: no path")

f = sys.argv[1:2]

path=""
if os.path.isdir(f[0]):
    path= f[0] if f[0][-1:-2] == '\\' else f[0] + "\*.pdf"
if os.path.isfile(f[0]):
    path = f
print("PATH",path)
pdftoText(path)

 

