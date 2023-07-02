import sys
import json

import requests

from secrets import api_key


class outfit():

    # initialize and take in zip code
    def __init__(self):
        self.zip = str(sys.argv[0])
        self.faren = 0
        self.shirt = ''
        self.pants = ''
        self.accessories = ''

    # get temperature data
    def get_temp_data(self):
        req_url = 'https://api.openweathermap.org/data/2.5/weather?lat=18.538539&lon=73.789743&appid={}'.format(api_key)
        response = requests.get(req_url)
        data_dictionary = response.json()
        self.kelvin = data_dictionary['main']['feels_like']

    # convert temperature to farenheit
    def kelvin_to_celsius(self):
        self.get_temp_data()
        self.celsius = (self.kelvin - 273)

    # recommend shirt
    def get_shirt(self,gender):
        c = int(self.celsius)
        if gender == 'm':
            if c > 20:
                self.shirt = ('Full sleeve shirt')
            elif c > 30 and c <= 20:
                self.shirt = ('Sweat shirt/Pull overs')
            elif c >= 40 and c <= 50:
                self.shirt = ('short sleeves')
            else:
                self.shirt = ('sweater')
        elif gender == 'f':
            if c > 20:
                self.shirt = ('Turtle neck')
            elif c > 30 and c <= 20:
                self.shirt = ('Sweatshirt')
            elif c >= 30 and c <= 45:
                self.shirt = ('Tshirts')
            else:
                self.shirt = ('Jackets')
        else:
            print("Wrong input")
    # recommend pants
    def get_pants(self,gender):
        c = int(self.celsius)
        if gender == 'm':
            if c > 30:
                self.pants = ('shorts')
            else:
                self.pants = ('long pants')
        elif gender == 'f':
            if c > 28:
                self.pants = ('Straight fit jeans')
            else:
                self.pants = ('Slimfit sweat pant')



    # recommend accessories
    def get_accessories(self):
        c = int(self.celsius)
        if c < 40 and c > 32:
            self.accessories = ('hat')
        elif c <= 32:
            self.accessories = ('hat and gloves')
        else:
            self.accessories = ''

    # consolidate and print out recommendations
    def assemble_outfit(self,gender):
        self.kelvin_to_celsius()
        self.get_shirt(gender)
        self.get_pants(gender)
        self.get_accessories()
        print('')
        print('temperature feels like ' + str(self.celsius) + ' C')
        print(self.shirt)
        print(self.pants)
        print(self.accessories)
def getOutfit():
    gender=input("Enter your gender: ")
    print(gender)

    my_outfit = outfit()
    my_outfit.assemble_outfit(gender)

if __name__ == "__main__":
    getOutfit()

