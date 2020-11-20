
gname = ["SUN", "MOON", "MARS","RAHU", "JUPITER", "SATURN", "MERCURY",  "KETU" , "VENUS"]
dy=[6,10,7,18,16,19,17,7,20]

i=0
j=0
for i in range(9):    
    print("\nIn Dasa(period) of ",gname[i],", the bhukti(Sub-perods) are as follows" )
    print("Bhukti period in   Years  Months   Days")
    for k in range(9):
        j=(i+k)%9
        v=(dy[i]/120)*dy[j]
        by=int(v)
        x=(v-by)*12
        bm=int(x)
        y=(x-bm)*30
        bd=round(y)
        if(bd>29):
            bm+=1
            bd=0        
        print("{:17}\t{:02}\t\t{:02}\t\t{:02}".format(gname[j],by,bm,bd))