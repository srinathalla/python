def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
    availableTimeSlots = getFreeSlotsInCalendar(mergedCalendar, meetingDuration)

    return convertAvailableSlotsToTimeFormat(availableTimeSlots)

def convertAvailableSlotsToTimeFormat(availableTimeSlots):
    return list(map(lambda entry : [minutesToTime(entry[0]), minutesToTime(entry[1])], availableTimeSlots))

def getFreeSlotsInCalendar(calendar, meetingDuration):
    prevCalendar = calendar[0]
    result = []
    i = 1
    while (i < len(calendar)):
        currCalendar = calendar[i]

        if (currCalendar[0] <= prevCalendar[1]):
            prevCalendar[1] = max(prevCalendar[1], currCalendar[1])
        else:
            if (currCalendar[0] - prevCalendar[1] >= meetingDuration):
                result.append([prevCalendar[1], currCalendar[0]])   
            prevCalendar = currCalendar   
        i +=1
    return result

def mergeCalendars(calendar1, calendar2):
    i = 0
    j = 0
    mergedCalendar = []
    while (i < len(calendar1) and j < len(calendar2)):
        if (calendar1[i][0] < calendar2[j][0]):
            mergedCalendar.append(calendar1[i])
            i  +=1
        else:
            mergedCalendar.append(calendar2[j])
            j +=1

    while (i < len(calendar1)):
        mergedCalendar.append(calendar1[i])
        i  +=1
   
    while (j < len(calendar2)):
        mergedCalendar.append(calendar2[j])
        j +=1
   
    return mergedCalendar


def updateCalendar(calendar, dailyBounds):
    [startTime, endTime] = dailyBounds

    updatedCalendar = [
        ["0:0", startTime], *calendar, [endTime, "23:59"]
    ]

    return list(map(lambda entry : [timeToMinutes(entry[0]), timeToMinutes(entry[1])], updatedCalendar))



def timeToMinutes(time):
    [hours, minutes] = list(map(int,time.split(':')))
    return hours * 60 + minutes


def minutesToTime(minutesTime):
    hours = int(minutesTime / 60)
    minutes = minutesTime % 60

    return (str(hours) +
        ":" +
        ('0' + str(minutes) if minutes < 10  else str(minutes)))


calendar1 = [
    ['9:00', '10:30'],
    ['12:00', '13:00'],
    ['16:00', '18:00']
]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [
    ['10:00', '11:30'],
    ['12:30', '14:30'],
    ['14:30', '15:00'],
    ['16:00', '17:00'],
]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 45

print(calendarMatching(
    calendar1,
    dailyBounds1,
    calendar2,
    dailyBounds2,
    meetingDuration,
))
