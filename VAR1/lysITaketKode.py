#class for interior light

class interiorLight:
    def getSpeeds(self,speed_file):
        speed1 = open(speed_file,'r')
        speed=[]
        for line in speed1: #legger inn 1 nar bilen har fart, og 0 naar bilen star stille
            if line.strip() != str(0):
                speed.append(1) #bil har fart
            else:
                speed.append(0) #bil har ikke fart
        return speed
    #the method returns flase if everything is OK (no notifications), if not, it returns flase
    def taklys(self,l, d, s): #take in value for light, door and speed (1 or 0)
        if l == 1 and d == 0 and s == 0: #the only time it is ok for the light to be on
            return False
        elif l==1: #light is on, but dor is open or/and the car has a speed
            return True
        else:
            return False #the light is off, no notification necessary

