def print_avtaler():
    fil= open("demofile2.txt","r")
    linje=fil.readline
    for linje in fil:
        print(linje)
print_avtaler()