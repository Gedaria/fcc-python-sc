def add_time(start, duration, day=""):
    start = start.replace(":", " ").split()
    # duration = duration.split(':')
    # duration = list(map(int, duration))
    duration = list(map(int, duration.split(":")))

    start_24hrs = []
    if start[2] == "PM":
        if start[0] != "12":
            start_24hrs.append(int(start[0]) + 12)
        else:
            start_24hrs.append(int(start[0]))
    if start[2] == "AM":
        if start[0] != "12":
            start_24hrs.append(int(start[0]))
        else:
            start_24hrs.append(0)
    start_24hrs.append(int(start[1]))

    duration = list(map(int, duration))

    sum_time = [start_24hrs[0] + duration[0], start_24hrs[1] + duration[1]]

    next_day_num = 0

    if sum_time[1] > 59:
        sum_time[0] = sum_time[0] + int(sum_time[1] / 60)
        sum_time[1] = sum_time[1] % 60

    if sum_time[0] > 23:
        next_day_num = int(sum_time[0] / 24)
        sum_time[0] = sum_time[0] - (24 * next_day_num)

    ampm = ""
    if sum_time[0] < 12:
        ampm = "AM"
        if sum_time[0] == 0:
            sum_time[0] = 12
    else:
        ampm = "PM"
        if sum_time[0] != 12:
            sum_time[0] = sum_time[0] - 12

    sum_time[0] = str(sum_time[0])
    sum_time[1] = str(sum_time[1])

    if len(str(sum_time[1])) == 1:
        sum_time[1] = "0" + str(sum_time[1])

    next_day_string = ""

    if next_day_num > 0 and day == "":
        if next_day_num == 1:
            next_day_string = " (next day)"
        else:
            next_day_string = " (" + str(next_day_num) + " days later)"

    if day != "":
        day = day.capitalize().strip()
        if next_day_num == 0:
            next_day_string = ", " + day
        else:
            if day == "Sunday":
                weekday_num = 1
            elif day == "Monday":
                weekday_num = 2
            elif day == "Tuesday":
                weekday_num = 3
            elif day == "Wednesday":
                weekday_num = 4
            elif day == "Thursday":
                weekday_num = 5
            elif day == "Friday":
                weekday_num = 6
            elif day == "Saturday":
                weekday_num = 7
            else:
                return "You've input an invalid weekday"

            weekday_num = (weekday_num + next_day_num) % 7
            if weekday_num == 1:
                day = "Sunday"
            elif weekday_num == 2:
                day = "Monday"
            elif weekday_num == 3:
                day = "Tuesday"
            elif weekday_num == 4:
                day = "Wednesday"
            elif weekday_num == 5:
                day = "Thursday"
            elif weekday_num == 6:
                day = "Friday"
            elif weekday_num == 7:
                day = "Saturday"

            if next_day_num == 1:
                next_day_string = ", " + day + " (next day)"
            else:
                next_day_string = ", " + day + " (" + str(next_day_num) + " days later)"

    new_time = sum_time[0] + ":" + sum_time[1] + " " + ampm + next_day_string

    return new_time
