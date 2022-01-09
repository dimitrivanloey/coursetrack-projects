months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
suffixes = ['st', 'nd', 'rd', 'th']
suffix = ''

def date_maker(date):
    year = date[0:4]
    month = months[int(date[4:6]) - 1]
    day = int(date[6:8])
    print(day)
    if day == 1 or day == 21 or day == 31:
        suffix = suffixes[0]
    elif day == 2 or day == 22:
        suffix = suffixes[1]
    elif day == 3 or day == 23:
        suffix = suffixes[2]
    else:
        suffix = suffixes[3]


    return f"{day}{suffix} {month} {year}"
    
