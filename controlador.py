def controlador(op,a,b):
    if op == 1:
        res=a+b
    elif op == 2:
        res=a-b
    elif op == 3:
        res=a*b
    elif op == 4:
        if b!=0:
            res=a/b
        else:
            print "divzion por zero"
            exit(0)
    elif op == 5:
        exit(0)
