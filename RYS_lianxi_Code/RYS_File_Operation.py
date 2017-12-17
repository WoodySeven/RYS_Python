#!/usr/bin/env pyfhon


def open_file():
    fp = open("RYS_name.txt","rb")
    names = fp.readlines()
    print(names)
    for i in names:
        print(i.decode("utf-8").strip())
    fp.close()

def open_wire_file():
    fp = open("RYS_a.txt","wb")
    a = [1,2,3,4,5,6,7,8]
    for i in a:
        fp.write("{}\n".format(i).encode("utf-8"))
    fp.close()

def open_with_wire_file():
    b = [1,2,3,4,5,6,7,8,9,10]
    with open("RYS_b.txt","wb") as fp:
        for i in b:
            fp.write("{}\n".format(i).encode("utf-8"))

if __name__=="__main__":
    open_file()
    open_wire_file()
    open_with_wire_file()