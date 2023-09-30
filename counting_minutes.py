def count_minutes(time):
    time = time.split("-")
    # starttime, endtime = time
    l = []
    minutes = []
    hours = []
    totalminutes = 0
    for t in time:
        t = t.split(":")
        hour, minute = t
        if minute[-2:] == "am":
            l.append(1)
        else:
            l.append(0)
        minute = minute[:-2]
        hours.append(int(hour))
        minutes.append(int(minute))
    l = set(l)
    if not len(l) == 1:
        first_hour = 12 - hours[0]
        second_hour = hours[1]
        total_hour = first_hour + second_hour
    elif hours[0] == hours[1] and minutes[0] > minutes[1] and len(l) == 1:
        first_hour = 24 - hours[0]
        second_hour = hours[1]
        total_hour = first_hour + second_hour
    else:
        total_hour = abs(first_hour - second_hour)
    if minutes[0] > minutes[1]:
        total_hour -= 1
        totalminutes = minutes[1] + 60 - minutes[0]
        breakpoint()
    return total_hour * 60 + totalminutes


# print(count_minutes("12:30pm-12:00am"))
print(count_minutes("1:23am-1:08am"))
