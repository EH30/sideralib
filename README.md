# sideralib
     
sideralib is a simple Python package designed for astrology enthusiasts. This package empowers users to calculate charts and determine planetary positions within the zodiac signs, adhering to the sidereal system.   

# Example
```
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
    kundli = astrochart.Chart(data.planets_rashi()).lagnaChart() # returns list with all the houses in Lagna Chart
    # kundli[0] = house 1      
    # kundli[1] = house 2   
    # ...   
    # ...   
    # kundli[11] = house 12

    # kundli[0].sign_num returns rashi sign in first house.   
    # kundli[0].planets returns dict with all the planet information in first house.   
    for house in range(len(kundli)):
        if kundli[house].is_ascendant == True:
            print("Asc Signlon: ", kundli[house].asc_signlon)
            print("Asc minute: ", kundli[house].asc_minute)
            print("Asc sec: ", kundli[house].asc_second)
            print("Asc: ", kundli[house].asc_degree)
        print("house: {0} sign_num: {1} planet: {2}".format(house+1, kundli[house].sign_num, kundli[house].planets))

```   
#       
```   
# Output: 
# Asc Signlon:  7.606448680104336
# Asc minute:  36.38692080626015
# Asc sec:  23.215248375609086
# Asc:  07:36:23
# house: 1 sign_num: 2 planet: {'moon': {'signlon': 0.4326922465451801, 'minute': 25.961534792710808, 'second': 57.69208756264839, 'lon': 30.43269224654518, 'degree': '00:25:57', 'retrograde': False}}
# house: 2 sign_num: 3 planet: {}
# house: 3 sign_num: 4 planet: {'ketu': {'signlon': 12.303851305303283, 'minute': 18.231078318196978, 'second': 13.864699091818732, 'lon': 102.30385130530328, 'degree': '12:18:13', 'retrograde': True}}
# house: 4 sign_num: 5 planet: {'saturn': {'signlon': 22.758987182069518, 'minute': 45.53923092417108, 'second': 32.353855450264746, 'lon': 142.75898718206952, 'degree': '22:45:32', 'retrograde': True}}
# house: 5 sign_num: 6 planet: {}
# house: 6 sign_num: 7 planet: {}
# house: 7 sign_num: 8 planet: {}
# house: 8 sign_num: 9 planet: {'pluto': {'signlon': 9.30237002216532, 'minute': 18.142201329919203, 'second': 8.532079795152224, 'lon': 249.30237002216532, 'degree': '09:18:08', 'retrograde': False}}
# house: 9 sign_num: 10 planet: {'jupiter': {'signlon': 24.766072525924358, 'minute': 45.96435155546146, 'second': 57.86109332768774, 'lon': 294.76607252592436, 'degree': '24:45:57', 'retrograde': False}, 'rahu': {'signlon': 12.303851305303283, 'minute': 18.231078318196978, 'second': 13.864699091818732, 'lon': 282.3038513053033, 'degree': '12:18:13', 'retrograde': True}}
# house: 10 sign_num: 11 planet: {'mars': {'signlon': 17.779569685040656, 'minute': 46.77418110243934, 'second': 46.45086614636038, 'lon': 317.77956968504066, 'degree': '17:46:46', 'retrograde': False}, 'uranus': {'signlon': 29.585563853318888, 'minute': 35.13383119913328, 'second': 8.029871947996847, 'lon': 329.5855638533189, 'degree': '29:35:08', 'retrograde': False}, 'neptune': {'signlon': 1.5493690559594597, 'minute': 32.962143357567584, 'second': 57.72860145405505, 'lon': 301.54936905595946, 'degree': '01:32:57', 'retrograde': False}}
# house: 11 sign_num: 12 planet: {'sun': {'signlon': 15.606050560341089, 'minute': 36.36303362046533, 'second': 21.7820172279199, 'lon': 345.6060505603411, 'degree': '15:36:21', 'retrograde': False}, 'mercury': {'signlon': 14.595579878481658, 'minute': 35.73479270889948, 'second': 44.08756253396846, 'lon': 344.59557987848166, 'degree': '14:35:44', 'retrograde': False}, 'venus': {'signlon': 11.793622040073728, 'minute': 47.6173224044237, 'second': 37.039344265422216, 'lon': 341.7936220400737, 'degree': '11:47:37', 'retrograde': True}}
# house: 12 sign_num: 1 planet: {}
```   


#   
kundli[0] = house 1      
kundli[1] = house 2  
...   
...   
kundli[11] = house 12

kundli[0].sign_num returns rashi sign number in first house.   
kundli[0].planets returns dict with all the planet information in first house.

ayanamsa options:   
"ay_fagan_bradley"   
"ay_lahiri"   
"ay_deluce"   
"ay_raman"   
"ay_krishnamurti"  
"ay_sassanian"   
"ay_aldebaran_15tau"  
"ay_galcenter_5sag"      
   

# 
```kundli[0].sign_num```: returns sign number in the first house    
```kundli[0].asc_signlon```: returns the ascendant degree    
```kundli[0].asc_minute```: returns the ascendant minute    
```kundli[0].asc_second```: returns the ascendant second   
```kundli[0].asc_degree```: returns the ascendant degree   
```kundli[0].planets```:   returns dict with planet information in the first house   
#
```astrochart.Chart```:    
- ```astrochart.Chart(data.planets_rashi()).lagnaChart()```: returns Lagna Chart    
- ```astrochart.Chart(data.planets_rashi()).moonChart()```: returns Moon Chart   
#
```astrodata.AstroData```:
- ```astrodata.AstroData(year, month, day, hour, minute, second, utc_hour, utc_minute, latitude, longitude, ayanamsa=ayanamsa).planets_rashi()```:returns dict with planets information
- ```astrodata.AstroData(year, month, day, hour, minute, second, utc_hour, utc_minute, latitude, longitude, ayanamsa=ayanamsa).get_chiron_rashi("resources\swefiles")```: returns dict with chiron information
   
```   
# Example  
data = SiderealAstroData.AstroData(year, month, day, hour, minute, second, utc_hour, utc_minute, latitude, longitude, ayanamsa=ayanamsa)
data.get_chiron_rashi("resources\swefiles") # returns dict with chiron information
kundli = AstroChart.Chart(data.planets_rashi()).lagnaChart() # returns list with all the houses in Lagna Chart
```   



# Installl
```   
pip install sideralib
```   
or    
download the files from https://github.com/EH30/sideralib   
then cd to the folder and enter the command:    

```   
pip install .
```   
