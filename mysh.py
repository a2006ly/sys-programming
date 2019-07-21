#!/usr/bin/python3
# -*- conding:utf-8 -*-

import subprocess
import os

while True:
    print("mysh>",end="")
    cmd = input();
    if cmd == "exit":
        break
    print(cmd)
    
    pwd = os.getcwd()
    cmds = cmd.split()
    if cmds[0] == "cd":
       if len(cmds) > 1:     
           pwd = pwd + "/" + cmds[1]
           if os.path.exists(pwd):
               os.chdir(pwd)
               cmd = ""
           else:
               print("'{}' にアクセスできません: そのようなファイルやディレクトリはありません.".format(pwd))
       else:
           pass
    p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            universal_newlines=True)

    stdout_data, stderr_data = p.communicate()
    if p.returncode == 0: 
        print(str(stdout_data))
    else:
        print(str(stderr_data))
