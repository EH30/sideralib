from sideralib import astrochart, astrodata

def degree_minute_second_st(deg, minute, second):
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
    kundli = astrochart.Chart(data.planets_rashi()).lagnaChart() # returns list with all the houses in Lagna Chart
    deg_min_sec= degree_minute_second_st(kundli[0].asc_signlon, kundli[0].asc_minute, kundli[0].asc_second)
    print(deg_min_sec)
