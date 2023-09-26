from typing import List

class DataHouse:
    def __init__(self):
        self.sign_num        = None
        self.is_ascendant    = False
        self.asc_signlon     = None
        self.asc_minute      = None
        self.asc_second      = None
        self.asc_degree      = None 
        self.planets          = {}

class Chart:
    def __init__(self, data:dict) :
        self.data = data
    
    def degree_minute_second_st(self, deg, minute, second) -> str:
        new_deg = ""
        new_min = ""
        new_sec = ""
        if int(deg) < 10:
            new_deg = "0"+str(int(deg))
        else:
            new_deg = str(int(deg))
        if int(minute) < 10:
            new_min = "0"+str(int(minute))
        else:
            new_min = str(int(minute))
        if int(second) < 10:
            new_sec = "0"+str(int(second))
        else:
            new_sec = str(int(second))
        return str(new_deg+":"+new_min+":"+new_sec)


    def degree_minute_second(self, lon:float) -> dict:
        """calculate degree minute and second"""
        deg = lon % 30
        minutes = (lon - int(lon)) * 60
        seconds = (lon - int(lon) - int(minutes) / 60) * 3600
        return {"signlon": deg, "minute": minutes, "second": seconds}
    
    def lagnaChart(self) -> List[DataHouse]:
        """calculate lagna chart"""
        houses = []
        planets = self.data
        temp = planets["ascendant"]["sign_num"]
        for _ in range (0, 12):
            if temp > 12:
                temp = 1
            
            data = DataHouse()
            data.sign_num = temp
            houses.append(data)
            temp += 1
        
        lagna = self.degree_minute_second(planets["ascendant"]["lon"])
        houses[0].is_ascendant = True
        houses[0].asc_signlon  = lagna["signlon"]
        houses[0].asc_minute   = lagna["minute"]
        houses[0].asc_second   = lagna["second"]
        houses[0].asc_degree   = self.degree_minute_second_st(lagna["signlon"], lagna["minute"], lagna["second"])

        for house in range(len(houses)):
            for planet in planets:
                if planet == "ascendant":
                    continue
                if planets[planet]["sign_num"] == houses[house].sign_num:
                    temp = self.degree_minute_second(planets[planet]["lon"])
                    houses[house].planets[planet] = temp
                    houses[house].planets[planet]["lon"] = planets[planet]["lon"]
                    houses[house].planets[planet]["degree"] = self.degree_minute_second_st(houses[house].planets[planet]["signlon"], 
                                                                                           houses[house].planets[planet]["minute"], 
                                                                                           houses[house].planets[planet]["second"])
                    houses[house].planets[planet]["retrograde"] = planets[planet]["retrograde"]
        
        return houses
    
    def moonChart(self) -> List[DataHouse]:
        """calculate moon chart"""
        houses  = []
        planets = self.data
        temp    = planets["moon"]["sign_num"]
        asc_house = 0
        for _ in range (0, 12):
            if temp > 12:
                temp = 1

            if temp == planets["ascendant"]["sign_num"]:
                asc_house = len(houses)
            data = DataHouse()
            data.sign_num = temp
            houses.append(data)
            temp += 1
        
        lagna = self.degree_minute_second(planets["ascendant"]["lon"])
        houses[asc_house].is_ascendant = True
        houses[asc_house].asc_signlon  = lagna["signlon"]
        houses[asc_house].asc_minute   = lagna["minute"]
        houses[asc_house].asc_second   = lagna["second"]
        houses[asc_house].asc_degree   = self.degree_minute_second_st(lagna["signlon"], lagna["minute"], lagna["second"])

        for house in range(len(houses)):
            for planet in planets:
                if planet == "ascendant":
                    continue
                if planets[planet]["sign_num"] == houses[house].sign_num:
                    temp = self.degree_minute_second(planets[planet]["lon"])
                    houses[house].planets[planet] = temp
                    houses[house].planets[planet]["lon"] = planets[planet]["lon"]
                    houses[house].planets[planet]["degree"] = self.degree_minute_second_st(houses[house].planets[planet]["signlon"], 
                                                                                           houses[house].planets[planet]["minute"], 
                                                                                           houses[house].planets[planet]["second"])
                    houses[house].planets[planet]["retrograde"] = planets[planet]["retrograde"]        
        return houses



