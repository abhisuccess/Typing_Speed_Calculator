from time import *
import random as r
def mistake(partest,usertest):
     error=0
     for i in range(len(partest)):
         try:
             if partest[i] != usertest[i]:
                error=error+1
         except:
             error= error+1
     return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)

 # Paste your text below (inside test variable ) , which you want to type & check speed
test="My name is abhi success, i am your repositary"

print("********* Typing speed calculator ***********")
print()
print()
time1=time()
testinput=input("Enter the text : ")
time2=time()
print("Speed : ", speed_time(time1,time2,testinput) , "words/sec")
print("Error : " ,  mistake(test,testinput) )
