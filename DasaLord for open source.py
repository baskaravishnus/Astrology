import datetime

birth_moon_position =322.756771388888887   # From 0 to 360 degree 
birth_year=2000
birth_month=5
birth_day=27



nakL= [8,5,0,1,2,7,4,6,3,8,5,0,1,2,7,4,6,3,8,5,0,1,2,7,4,6,3]
birth_star = int(birth_moon_position / (13.0 + (20.0 / 60.0)))
start_dasaLord_Atbirth = nakL[birth_star]
gndo=["KETU","VENUS","SUN","MOON","MARS","RAHU","JUPITER","SATURN","MERCURY"]
dy=[7,20,6,10,7,18,16,19,17]
dyg=[6,10,7,17,16,20,19,18,7]
dasa_lords=[8,5,0,1,2,7,4,6,3]
dbas = [[[[0 for i in range(12)] for j in range(12)] for k in range(12)] for m in range(12)]

for i in range(9):
    for j in range(i,(i+9)):
        for k in range(j,(j+9)):
            for m in range(k,(k+9)):             
                dasa=i%9
                bhukti=j%9
                antara=k%9
                sookshma=m%9
                dbas[dasa][bhukti][antara][sookshma]=(dy[dasa]*dy[bhukti]*dy[antara]*dy[sookshma]*360)/(120*120*120)
                # print("dbas["+gndo[dasa]+"]["+gndo[bhukti]+"]["+gndo[antara]+"]["+gndo[sookshma]+"]="+str(dbas[dasa][bhukti][antara][sookshma]))


dasa_days_overBirth=(((birth_moon_position*60.0)%800)/800)*dyg[start_dasaLord_Atbirth]*360
# print(dasa_days_overBirth)
today=datetime.date.today()
# print(today)
birth_day = datetime.date(birth_year, birth_month, birth_day)
# print(birth_day)

numberOf_days_fromBirthDay=(today-birth_day).days
# print(numberOf_days_fromBirthDay)

total_days=numberOf_days_fromBirthDay+dasa_days_overBirth
# print(total_days)
dasa=bhukti=antara=sookshma=dasa_lords.index(start_dasaLord_Atbirth)      
# print("start dasa=",dasa)
i=j=k=m=0
while(total_days>0) :
    total_days=total_days-dbas[dasa][bhukti][antara][sookshma]
    sookshma_before=sookshma
    antara_before=antara
    bhukti_before=bhukti
    dasa_before=dasa
    m+=1   
    sookshma=sookshma+1
    sookshma=sookshma%9
    if(m==9):
        m=0
        k+=1             
        antara=antara+1
        antara=antara%9
        sookshma=antara
    if(k==9):
        k=0
        m=0
        j+=1
        bhukti=bhukti+1
        bhukti=bhukti%9
        antara=bhukti
        sookshma=bhukti
    if(j==9):
        j=0
        k=0
        m=0
        i+=1
        dasa+=1
        dasa%=9
        bhukti=dasa
        antara=dasa
        sookshma=dasa
    if(i==9):
        j=0
        k=0
        m=0
        i=0
        dasa=bhukti=antara=sookshma=dasa_lords.index(start_dasaLord_Atbirth)       
    
dasa=dasa_before
bhukti=bhukti_before
antara=antara_before
sookshma=sookshma_before

print("Dasa lord="+gndo[dasa])
print("Bhukti lord="+gndo[bhukti])
print("Antara lord="+gndo[antara])
print("Sookshma lord="+gndo[sookshma])

