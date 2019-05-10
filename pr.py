import sys, os
def make():
#    import sys
    z = input("Write name of new file:")
    f = open(z, 'tx', encoding='utf-8')
    value = input("Enter the text\n")
    f.write(value)
    f.close()
#    print ("Name :", str(nome.get()), "Telephone No :", str(celular.get()))

def show():
    arr = os.listdir()
    print(arr)

def read():
    show()
    o = input("Write name of file:")
    f = open(o, 'r')
    t = f.read()
    print(t)

def delete():
    show()
    o = input("Write name of file:")
    os.remove(o)

while True:
    x = int(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChoose option:\n 1 - make and write to fille,\n 2 - open fille,\n 3 - delete fille,\n 4 - QUIT\n"))

    if x==1:
        make()
    elif x==2:
        read()
    elif x==3:
        delete()
    elif x==4:
        break
    elif x==5:
        show()
