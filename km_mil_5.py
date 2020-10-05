
try:
    dis = input('enter km distance: ' )
    if float(dis) <= 0:
        print ('Not a valid number')
    else :
        tim = input('enter hours: ' )
        if float(tim) <= 0:
            print ('Not a valid number')
        else :
            spd = float(dis) / float(tim)
            kmh = float(spd)
            print('kmh:', kmh)
            mph = float(spd) / 1.61
            print('mph:', mph)
            if kmh > 7 and mph > 4.348:
                print('slow down!')
            elif kmh < 4.5 and mph < 2.795:
                print ('speed up!')
            else : print ('good speed')
except:
    print ('Error, please enter numeric input')
