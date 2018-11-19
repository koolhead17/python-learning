temprature = eval(input('Enter current temprature:'))
if temprature >= 0:
    print('The current temprature is',str(temprature),'degree celcious.',sep=' ')
elif temprature == 0:
    print ('The current temprature is 0 degree celcious.')
else:
    print('The current temptature is',abs(temprature),'degree celcious below zero.',sep=' ')       