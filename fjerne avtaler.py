def Fjerne_avtale():
    searched = input("hvilken avtale skal fjernes") # every line containing the variable "searched" will be deleted
    
    with open("demofile2.txt","r+") as f: # open your file
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if searched not in line:
                f.write(line)
        f.truncate() 
Fjerne_avtale()