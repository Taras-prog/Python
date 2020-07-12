from pyowm import OWM

owm = OWM('3422b886ef1861a22ccce2d7439a5504')
place = input('What city / country are you in?: ')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]

print( 'In city ' + place + ' now ' + w.detailed_status)
print('Temperature now within ' + str(temp))          

if temp < 5:
    print("Now is cold! Please, dress warmer")
elif temp < 15:
    print("Weather is good")
else:
    print('Weather is warm')

input()
input()
    