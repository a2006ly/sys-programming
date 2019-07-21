#!/usr/bin/python3
# -*- conding:utf-8 -*-
from pathlib import Path
import datetime
import stat
import os
import sys
 

def runls(path: str='.', all=False, showList=False, nodeNo=False):
    inode = "" 
    size = ""
    atime = ""
    owner = ""
    group = ""
    mode = ""
    nlink = ""
    filename = ""
    lsStr = ""
    p = Path(path)

    for file in p.iterdir():
        st = file.stat()
        filename = str((file.name)).strip('()')
        if nodeNo:
             inode = "{:>20}".format(st.st_ino) #inode表示
             filename = ""
        if all:
            filename = str((file.name)).strip('()')
        if not all and str(file.name).startswith('.'):
            continue
        if showList:
            size = "{:10}".format(st.st_size) #サイズ
            atime = "{:20}".format(datetime.datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S'))
            owner, group = st.st_uid, st.st_gid
            if os.name == "posix":
                owner, group = file.owner(), file.group()
            mode = stat.filemode(st.st_mode)
            nlink = st.st_nlink
            filename = file.name
       
        lsStr = "{0} {1} {2} {3} {4} {5} {6} {7}".format(inode,mode,nlink,owner,group,str(size),atime,filename)
        yield str(lsStr)

if __name__ == '__main__':
    all = False
    showList = False
    nodeNo = False
    sysArgs = ""
    path = "."
    if len(sys.argv) > 2:
        path = sys.argv[1]
        if str(sys.argv[2]) != "-":
            sysArgs = sys.argv[2]
        else:
             sysArgs = "--"
    elif len(sys.argv) > 1:
        if str(sys.argv[1]).startswith("-") and str(sys.argv[1]) != "-":
            sysArgs = sys.argv[1]
        else:
            path = sys.argv[1]
   
    if sysArgs.startswith("-"):
        for i in sysArgs[1:]: 
            if "a" == i:
                all = True
            elif "l" == i:
                showList = True
            elif "i" == i:
                nodeNo = True
            else:
                print("ls: 無効なオプション -- '{}'".format(sysArgs))
                sys.exit(1)
    
    if os.path.exists(path) :
        for st in runls(path, all, showList, nodeNo):
            print(st)
    else:
        print("ls: '{}' にアクセスできません: そのようなファイルやディレクトリはありません.".format(path))
        sys.exit(1)