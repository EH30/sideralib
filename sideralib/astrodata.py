import swisseph as swe
from .tools import JulianDate


SWE_AYANAMSA  = {
    "ay_fagan_bradley": 0,
    "ay_lahiri": 1,
    "ay_deluce": 2,
    "ay_raman": 3,
    "ay_krishnamurti": 5,
    "ay_sassanian": 16,
    "ay_aldebaran_15tau": 14,
    "ay_galcenter_5sag": 17
}

PLANETS = {
    "sun": swe.SUN, 
    "moon": swe.MOON, 
    "mercury": swe.MERCURY, 
    "venus": swe.VENUS, 
    "mars": swe.MARS, 
    "jupiter":swe.JUPITER, 
    "saturn": swe.SATURN, 
    "rahu": swe.MEAN_NODE,
    "uranus": swe.URANUS, 
    "pluto": swe.PLUTO,
    "neptune": swe.NEPTUNE
}

class Date:
    def __init__(self, 
                 year:int, 
                 month:int, 
                 day:int, 
                 hour:int, 
                 minute:int, 
                 second:int,  
                 utc_offset_hours:int, 
                 utc_offset_minutes:int):
        self.year   = year
        self.month  = month
        self.day    = day
        self.hour   = hour
        self.minute = minute
        self.second = second
        self.utc_offset_hours   = utc_offset_hours
        self.utc_offset_minutes = utc_offset_minutes

class AstroData:
    def __init__(self, 
                 year:int, 
                 month:int, 
                 day:int,  
                 hour:int, 
                 minute:int, 
                 second:int, 
                 utc_offset_hours:int,  
                 utc_offset_minutes:int, 
                 latitude:float, 
                 longitude:float, 
                 ayanamsa="ay_lahiri"):
        """   
        arguments: 
        - year: birth year
        - month: birth month
        - day: birth day
        - hour: birth hour
        - minute: birth minute
        - second: birth second
        - utc_offset_hour: utc offset hour example: 5
        - utc_offset_minutes: utc offset minutes example: 30
        - ayan: Ayanamsa default is lahiri.   

        Example: AstroData(2009, 3, 30, 9, 36, 0, 5, 30, 19.0760, 72.8777, ayanamsa="ay_lahiri")    
        """
        date = Date(year, month, day, hour, 
                    minute, second, utc_offset_hours, utc_offset_minutes)  
        self.juld = JulianDate.JulianDate(date).date_utc_to_julian()
        self.ayanamsa = ayanamsa.lower()
        self.latitude  = latitude
        self.longitude = longitude
    
    def get_chiron_rashi(self, swefiles) -> dict:
        """
        arguments:
        - swefiles: enter path to swisseph files for chiron      

        Example: get_chiron('resources/swefiles')    
        """
        output = {}
        planet = "chiron"
        swe.set_ephe_path(swefiles)
        swe.set_sid_mode(SWE_AYANAMSA[self.ayanamsa], 0, 0)  # Set the Ayanamsa
        flags = swe.FLG_SWIEPH + swe.FLG_SPEED + swe.FLG_SIDEREAL        
        xx, ret = swe.calc_ut(self.juld, swe.CHIRON, flags)
        rashi_number = xx[0] / 30 
        output[planet] = {
            "sign_num":int(rashi_number)+1, 
            "lon": xx[0], "retrograde": False
        }
        if xx[3] < 0:
            output["planet"]["retrograde"] = True
        return output
    
    def planets_rashi(self) -> dict:
        """calculate planet position in rashi"""
        swe.set_sid_mode(SWE_AYANAMSA[self.ayanamsa], 0, 0)  # Set the Ayanamsa
        flags = swe.FLG_SWIEPH + swe.FLG_SPEED + swe.FLG_SIDEREAL

        cusps, ascmc = swe.houses_ex(self.juld, self.latitude,
                                      self.longitude, b'B', flags)
        ascendant = ascmc[0]
        output = {}
        output["ascendant"] = {
            "sign_num":int(ascendant/30)+1, 
            "lon":ascendant
        }

        for planet in PLANETS:
            xx, ret = swe.calc_ut(self.juld, PLANETS[planet], flags)
            rashi_number = xx[0] / 30 
            output[planet] = {
                "sign_num":int(rashi_number)+1, 
                "lon": xx[0], "retrograde": False
            }  
            if xx[3] < 0:
                output[planet]["retrograde"] = True
        
        output["ketu"] = {
            "sign_num":  int(swe.degnorm(output["rahu"]["lon"]+180) / 30)+1 , 
            "lon": swe.degnorm(output["rahu"]["lon"]+180), "retrograde": False
        }
        if output["rahu"]["retrograde"] == True:
            output["ketu"]["retrograde"] = True 
        swe.close()
        return output
