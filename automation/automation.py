import time
import playsound
def alltasks():
    result = True
    while(result):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if(current_time>"06:00:00" and current_time<"07:00:00"):
            print('its your walking time go and walk in river!!')
        if(current_time>"07:00:00" and current_time<"08:00:00"):
            print('its your linch time and bathing,brushing,clothing etc!!')
        if(current_time>"08:00:00" and current_time<"12:00:00"):
            print('its your playing time!')
        if(current_time>"12:00:00" and current_time<"12:30:00"):
            print('its your breakfast time!')
        if(current_time>"12:30:00" and current_time<"16:00:00"):
            print('its your studying time !')
        if(current_time>"16:00:00" and current_time<"18:00:00"):
            print('its playing time!')   
        if(current_time>"18:00:00" and current_time<"22:00:00"):
            print('its your coding time!')
        if(current_time>"22:00:00" and current_time<"06:00:00"):
            print('I am sleeping zzzzzzz....')
        if(current_time =="05:50:00"):
            print('Good Morning!')
            playsound.playsound('alarm.mp3')
            result = False
            print('run program again to shedule today')
alltasks()