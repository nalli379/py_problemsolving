def time_24conversion(start_time):
    #turn 12 hour clock to 24 hour clock by splitting time into hours, minutes, ampm
    time, ampm = start_time.split()
    hours, mins = (int(i) for i in time.split(":"))
    if ampm == 'PM': hours += 12
    
    return hours, mins


def duration_conversion(duration):
    #split duration into hours/minutes
    dhours, dmins = (int(i) for i in duration.split(':'))
    return dhours, dmins

def calc_mins(cmins, cdur_mins):
    #calculate new time minutes from current time (mins) and duration minutes
    #create new value for additional hours if minutes > 60
    add_hours = 0
    new_mins = cmins + cdur_mins
    
    if new_mins >= 60:
        add_hours += (new_mins //60)
        new_mins = new_mins % 60
    
    return add_hours, new_mins


def calc_hours(hours, dur_hours, add_hours):
    #calculate new time hours from current time (hours) and duration hours.
    #create new value for additional days if hours > 24
    day_count = 0
    new_hours = hours + dur_hours + add_hours
    
    if new_hours >= 24:
        day_count +=(new_hours // 24)
        new_hours = new_hours % 24
    
    return new_hours, day_count


def time_12conversion_str(nhours, nmins):
    #convert time from 24 hour to 12 hour clock by calculating if new time hours > 12
    
    str_ampm = 'AM'
    
    if nhours == 0: nhours += 12
            
    elif nhours >= 12:
        str_ampm = 'PM'
        if nhours == 12:
            pass
        else:
            nhours -= 12
    
    #format minute integer to double digits string  
    if nmins < 10:
        nmins = '0' + str(nmins)
    
    return f"{str(nhours)}:{nmins} {str_ampm}"


def get_key(val, calendar):
    #retrieve keys from values in calendar dictionary
    for key, value in calendar.items():
         if val == value:
             return key
    return "key doesn't exist"


def calc_calendar(day, day_count):
    
    calendar = {"Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 7}
    
    if not day: stat_wkday = None
    
    #if weekday is given, calculate weekday
    if day:
        try:
            day = day.title()
            curr_day = calendar[day]
            
        except Exception as e:
            print(type(e))
        
        stat_wkday = get_key(((curr_day + day_count) % 7), calendar)
    
    if not day_count: stat_day = None
    
    #if day count is not 0, calculate n days later
    if day_count:
        if day_count == 1:
            stat_day = f"next day"
        else:
            stat_day = f"{day_count} days later"
    
    #adjust statement based on stat_wkday and not stat_day variables having a value
    if not stat_wkday and not stat_day: stat = ''
    elif stat_wkday and not stat_day: stat = f", {stat_wkday}"
    elif not stat_wkday and stat_day: stat = f" ({stat_day})"
    elif stat_wkday and stat_day: stat = f", {stat_wkday} ({stat_day})"

    return stat


def add_time(start, duration, day=False):
    
    #converts 12 hour time into 24 hour time
    hours, mins = time_24conversion(start)
    
    #converts duration time into hours and minutes
    dur_hours, dur_mins = duration_conversion(duration)
    
    #calculates hours added, new minutes
    add_hours, new_mins = calc_mins(mins, dur_mins)
    
    #calculates hours, days added
    new_hours, day_count = calc_hours(hours, dur_hours, add_hours)

    #turn 24 hour clock into 12 hour clock
    str_12time = time_12conversion_str(new_hours, new_mins)

    #calendar days calculated
    new_day  = calc_calendar(day, day_count)
    
    if not new_day:
        new_time = f"{str_12time}"
    else:
        new_time = f"{str_12time}{new_day}"
    
    return new_time
