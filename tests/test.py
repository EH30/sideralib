from sideralib import astrochart, astrodata

if __name__ == "__main__":
    # Example UTC: +5:30 which is used by India
    # Example Location Mumbai India latitude: 19.0760 and Longitude: 72.8777 
    # Year: 2009 Month: 3  Day: 30 Hour: 9 Minute: 36 Second: 0 utc_hour: 5 utc_minute: 30 latitude: 19.0760 Longitude: 72.8777 ayanamsa: ay_lahiri 
    year  = 2009
    month = 3
    day = 30
    hour = 9
    minute = 36
    second = 0
    utc_hour = 5
    utc_minute = 30
    latitude = 19.0760
    longitude =  72.8777
    ayanamsa = "ay_lahiri"
    data = astrodata.AstroData(year, month, day, hour, minute, second, utc_hour, utc_minute, latitude, longitude, ayanamsa=ayanamsa)
    planet_data = data.planets_rashi() # get planet data  
    kundli = astrochart.Chart(planet_data).lagnaChart() # returns list with all the houses in Lagna Chart
    # kundli[0] = house 1      
    # kundli[1] = house 2   
    # ...   
    # ...   
    # kundli[11] = house 12

    # kundli[0].sign_num returns rashi sign in first house.   
    # kundli[0].planets returns dict with all the planet information in first house.   
    for house in range(len(kundli)):
        if kundli[house].is_ascendant == True:
            print("Asc lon: ", kundli[house].asc_lon)
            print("Asc Signlon: ", kundli[house].asc_signlon)
            print("Asc minute: ", kundli[house].asc_minute)
            print("Asc sec: ", kundli[house].asc_second)
            print("Asc: ", kundli[house].asc_degree)
        print("house: {0} sign_num: {1} planet: {2}".format(house+1, kundli[house].sign_num, kundli[house].planets))
