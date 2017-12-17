#!/usr/bin/env python


def open_file():
    fp = open("RYS_name.txt","rb")
    names = fp.readlines()
    print(names)
    for i in names:
        print(i.decode('utf-8').strip())
    fp.close()

def open_wire_file():
    fp = open("RYS_wire_name.txt","wb")
    names = ["任永生","陈金","代维"]
    for i in names:
        fp.write("{}\n".format(i).encode("utf-8"))
    fp.close()

def open_with_file():
    with open("RYS_with_wire_name.txt","wb") as fp:
        names = ["任永生", "陈金", "代维"]
        for i in names:
            fp.write("{}\n".format(i).encode("utf-8"))

if __name__ == "__main__":
    open_file()
    open_wire_file()
    open_with_file()

