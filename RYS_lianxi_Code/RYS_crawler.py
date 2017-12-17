#!/usr/bin/env python
import os
import os.path

def crawl_dirname(file_path_name):
    i = os.listdir(file_path_name)
    file_path = os.path.join(file_path_name,i)
    print (file_path)
    with open("myfile.txt","wb") as fp:
            fp.write("\n".join(file_path).encode("utf-8"))
if __name__=="__main__":
    name = input("请输入要查找的路径：")
    crawl_dirname(name)