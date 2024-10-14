#
class Temparature:
    def __init__(self, celcius, farenheit):
        self.celcius=celcius
        self.farenheit=farenheit
    def convertFarenhiet(self):
        return (self.celcius * 9/5)+32
    def convertCelcius(self):
        return (self.farenheit -32) * 5/9
        
    
celcius=int(input("Degree"))
farenheit=int(input("Farenheit"))
temp= Temparature(celcius, farenheit)

print(f"The farenhiet is {temp.convertFarenhiet()}")
print(f"The degree is {temp.convertCelcius()}")
        