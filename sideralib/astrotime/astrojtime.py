from datetime import datetime

class JulianDate:
    def __init__(self, date):
        self.date = date

    def date_utc_to_julian(self) -> float:
        # Convert the date to a datetime object
        dt = datetime(self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute, self.date.second)
        # Calculate the Julian date offset
        julian_offset = 2440587.5
        
        # Calculate the number of seconds in a day
        seconds_per_day = 86400
        
        # Convert the UTC offset to seconds
        utc_offset_seconds = (self.date.utc_offset_hours * 3600) + (self.date.utc_offset_minutes * 60)
        
        # Calculate the Julian date
        julian_date = julian_offset + (dt - datetime(1970, 1, 1)).total_seconds() / seconds_per_day - utc_offset_seconds / seconds_per_day
        return julian_date
