import RPi.GPIO as GPIO
import time#importing time library
from RPLCD.gpio import CharLCD #to ise lcd functions
import haversine as hs #to convert long and lat difference to meters
from haversine import Unit #units for converstion
import random #random function for choosing random roads
 
def getloc():
    from urllib.request import urlopen
    url = 'http://api.thingspeak.com/channels/1435023/field/1/last.txt'#to read latitude
    file = urlopen(url)
    loc1 = file.read().decode()
    url = 'http://api.thingspeak.com/channels/1435023/field/2/last.txt'#to read longitude
    file = urlopen(url)
    loc2 = file.read().decode()#decodeding the data
    return(loc1,loc2)#returning the decoded data
    
def getambsts():
    from urllib.request import urlopen
    url = 'http://api.thingspeak.com/channels/1435023/field/4/last.txt'#
    file = urlopen(url)
    ambsts = file.read().decode()
    return(ambsts)

def locdis():
    [lat,longi]=getloc()#calling latitude longitude calculating function
    print(lat)#printing on console
    print(longi)
    loc1=(float(lat),float(longi))#assigning location of ambulance
    loc2=(13.9612179,75.5062619)#(lat,longi) location of traffic signal
    return(hs.haversine(loc1,loc2,unit=Unit.METERS))

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)#disabling warnings
#assigning pins
r1=40#red
r2=38
r3=36
r4=32

y1=37#yellow
y2=35
y3=33
y4=31

g1=29#green
g2=13
g3=5
g4=11
buzz=8#buzzer
#defining output pins
GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(r3, GPIO.OUT)
GPIO.setup(r4, GPIO.OUT)
GPIO.setup(y1, GPIO.OUT)
GPIO.setup(y2, GPIO.OUT)
GPIO.setup(y3, GPIO.OUT)
GPIO.setup(y4, GPIO.OUT)
GPIO.setup(g1, GPIO.OUT)
GPIO.setup(g2, GPIO.OUT)
GPIO.setup(g3, GPIO.OUT)
GPIO.setup(g4, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)

#test condition to off all leds
def allledoff():
    GPIO.output(g1,0)
    GPIO.output(g2,0)
    GPIO.output(g3,0)
    GPIO.output(g4,0)
    GPIO.output(r1,0)
    GPIO.output(r2,0)
    GPIO.output(r3,0)
    GPIO.output(r4,0)
    GPIO.output(y1,0)
    GPIO.output(y2,0)
    GPIO.output(y3,0)
    GPIO.output(y4,0)
    
lcd = CharLCD(pin_rs = 15, pin_rw=18, pin_e=16, pins_data= [21,22,23,24],numbering_mode = GPIO.BOARD, cols=16, rows=2, dotsize=8)#assigning the lcd pins
lcd.clear()#to clear led content
lcd.write_string("Smart Geo Fencing")#writing to led
lcd.cursor_pos = (1, 0)#setting cursor to line 2
lcd.write_string("For Ambulance")
time.sleep(2)#delay
#roads
rr1=0
rr2=0
rr3=0
rr4=0
rs=1#road select
ambsts1=0#default ambulance condition
#resetting
allledoff()

while(1):#traffic functionality starts
    while(rr1<30 or rs==1):#road1
        if(rr1<20 ):#distance less than 20 meters
            GPIO.output(g1,1)
            GPIO.output(g2,0)
            GPIO.output(g3,0)
            GPIO.output(g4,0)
            GPIO.output(r1,0)
            GPIO.output(r2,1)
            GPIO.output(r3,1)
            GPIO.output(r4,1)
        else:
            GPIO.output(y1,1)
            GPIO.output(g2,0)
            GPIO.output(g3,0)
            GPIO.output(g4,0)
            GPIO.output(g1,0)
            rs=2
        rr1=rr1+1
        if(rr1>30):
            ambsts1=0  
        dis=locdis()
        ambsts=getambsts()
        if(int(dis)<20 and int(ambsts)>50 and ambsts1==0):
            ambsts1=1
            list1 = [1, 2, 3, 4]
            rs=random.choice(list1)
            rr1=0
            print(rs)
            break
        print(rr1)
    allledoff()

    while(rr2<30 and rs==2):#road2   
        if(rr2<20):#distance less than 20 meters
            GPIO.output(g1,0)
            GPIO.output(g2,1)
            GPIO.output(g3,0)
            GPIO.output(g4,0)
            GPIO.output(r1,1)
            GPIO.output(r2,0)
            GPIO.output(r3,1)
            GPIO.output(r4,1)
        else:
            GPIO.output(y2,1)
            GPIO.output(g2,0)
            GPIO.output(g3,0)
            GPIO.output(g4,0)
            GPIO.output(g1,0)
            rs=3
            
        rr2=rr2+1
        if(rr2>30):
            ambsts1=0
            
        dis=locdis()
        ambsts=getambsts()
        if(int(dis)<20 and int(ambsts)>50 and ambsts1==0):
            ambsts1=1
            list1 = [1, 2, 3, 4]
            rs=random.choice(list1)
            rr2=0
            break
    allledoff()

    while(rr3<30 and rs==3):#road3
        
        if(rr3<20):#distance less than 20 meters
            GPIO.output(g1,0)
            GPIO.output(g2,0)
            GPIO.output(g3,1)
            GPIO.output(g4,0)
            GPIO.output(r1,1)
            GPIO.output(r2,1)
            GPIO.output(r3,0)
            GPIO.output(r4,1)
        else:
            GPIO.output(y3,1)
            GPIO.output(g2,0)
            GPIO.output(g3,0)
            GPIO.output(g4,0)
            GPIO.output(g1,0)
            rs=4
        rr3=rr3+1
        if(rr3>30):
            ambsts1=0
            
        dis=locdis()
        ambsts=getambsts()
        if(int(dis)<20 and int(ambsts)>50 and ambsts1==0):
            ambsts1=1
            list1 = [1, 2, 3, 4]
            rs=random.choice(list1)
            rr3=0
            break

        print(rr3)
    allledoff()

    while(rr4<30 and rs==4):#road4
        
        if(rr4<20):#distance less than 20 meters
            GPIO.output(g1,0)
            GPIO.output(g2,0)
            GPIO.output(g3,0)
            GPIO.output(g4,1)
            GPIO.output(r1,1)
            GPIO.output(r2,1)
            GPIO.output(r3,1)
            GPIO.output(r4,0)
        else:
            GPIO.output(y4,1)
            GPIO.output(g2,0)
            GPIO.output(g3,0)
            GPIO.output(g4,0)
            GPIO.output(g1,0)
            rs=1
        rr4=rr4+1
        if(rr4>30):
            ambsts1=0
            
        dis=locdis()
        ambsts=getambsts()
        if(int(dis)<20 and int(ambsts)>50 and ambsts1==0):
            ambsts1=1
            list1 = [1, 2, 3, 4]
            rs=random.choice(list1)
            rr4=0
            break
#making all default after exiting loop
    rr1=0
    rr2=0
    rr3=0
    rr4=0
    list1 = [1, 2, 3, 4]
    rs=random.choice(list1)
    allledoff()
