n=int(input("enter the number of vehicles"))
TW=[]
FW=[]
for i in range(n):
    v=int(input("enter type of v (2w r 4w)"))
    if v==2:
        TW.append(v)
    else:
        FW.append(v)
total=len(TW)+len(FW)
TWW=2*len(TW)
FWW=4*len(FW)
wheels=TWW+FWW
print("no of wheels is",wheels)
print("number of two wheelers is",len(TW))
print("number of four wheelers is",len(FW))
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
