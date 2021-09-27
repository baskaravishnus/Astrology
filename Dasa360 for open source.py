# This is program to calculate Dasa and Bhukti based on 360 days system
import datetime

birth_moon_position =322.756771388888887   # From 0 to 360 degree 
birth_year=2000
birth_month=5
birth_day=27


print("\n\n\n\n\nDasa-360 program starts\n")


gndo=["KETU","VENUS","SUN","MOON","MARS","RAHU","JUPITER","SATURN","MERCURY"]
dy=[7,20,6,10,7,18,16,19,17]
dyg=[6,10,7,17,16,20,19,18,7]
dasa_lords=[8,5,0,1,2,7,4,6,3]
db = [[0 for i in range(12)] for j in range(12)]
nakL= [8,5,0,1,2,7,4,6,3,8,5,0,1,2,7,4,6,3,8,5,0,1,2,7,4,6,3]
birth_star = int(birth_moon_position / (13.0 + (20.0 / 60.0)))
start_dasaLord_Atbirth = nakL[birth_star]


for i in range(9):
    for j in range(i,(i+9)):                                
        dasa=i%9
        bhukti=j%9                          
        db[dasa][bhukti]=(dy[dasa]*dy[bhukti]*360)/(120)
        # print("db["+gndo[dasa]+"]["+gndo[bhukti]+"]="+str(db[dasa][bhukti]))


dasa_days_overBirth=(((birth_moon_position*60.0)%800)/800)*dyg[start_dasaLord_Atbirth]*360
# print(dasa_days_overBirth)
today=datetime.date.today()
# print(today)
birth_day = datetime.date(birth_year, birth_month, birth_day)
# print(birth_day)

dasa=bhukti=antara=dasa_lords.index(start_dasaLord_Atbirth)      
# print("start dasa=",dasa)

tdelta = datetime.timedelta(days=dasa_days_overBirth)
start_date_dasaAtBirth=birth_day-tdelta
# print("start_date_dasaAtBirth=",start_date_dasaAtBirth)

dasac=dasa
start_date=start_date_dasaAtBirth
for i in range(9):
    tdeltay=datetime.timedelta(days=(dy[dasac]*360))
    end_date=start_date+tdeltay
    print(f"The {gndo[dasac]:7} Dasa start at {start_date} and ends at {end_date}")
    start_date=end_date
    dasac=(dasac+1)%9



dasac=dasa
bhuktic=bhukti
start_date=start_date_dasaAtBirth
for i in range(9):
    print(f"\n\nThe {gndo[dasac]:7} Dasa -Bhukti details")
    for j in range(9):
        tdeltay=datetime.timedelta(days=db[dasac][bhuktic])
        end_date=start_date+tdeltay
        print(f"The {gndo[bhuktic]:7} Bhukti start at {start_date} and ends at {end_date}")
        start_date=end_date
        bhuktic=(bhuktic+1)%9 
    dasac=(dasac+1)%9
    bhuktic=dasac 



