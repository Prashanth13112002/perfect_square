def s(n):
    
    i=1
    while(i*i<=n):
        i+=1
        if(i*i==n):
            return True
        else:
            return False
print(s(int(input())))