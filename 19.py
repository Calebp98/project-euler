'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

month_to_length_no_leap = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 30,
    9: 31,
    10: 31,
    11: 30,
    12: 31,
}


month_to_length_leap = {**month_to_length_no_leap, 2: 29}


def is_leap_year(year):
    if(year % 400 == 0):
        # print("leap")
        return True
    elif(year % 100 != 0 and year % 4 == 0):
        # print("leap")
        return True
    else:
        return False


# tests
# print(is_leap_year(1600))
# print(is_leap_year(1604))
# print(is_leap_year(1603))
# print(is_leap_year(1900))
# print(is_leap_year(1904))

# takes date in [d,m,y] format and returns days since 1/1/1900


def days_since_1900(date):
    # days in month
    total_days = 0
    total_days += date[0] - 1
    # months
    if(not is_leap_year(date[2])):
        for i in range(1, date[1]):
            total_days += month_to_length_no_leap[i]
    else:
        for i in range(1, date[1]):
            total_days += month_to_length_leap[i]
    # years
    for i in range(1900, date[2]):
        # print(i)
        # print(is_leap_year(i))
        if(not is_leap_year(i)):
            total_days += 365
        else:
            total_days += 366
    return total_days


# testing
# print(days_since_1900([1,1,1900]))
# print(days_since_1900([2,1,1900]))
# print(days_since_1900([1,2,1900]))
# print(days_since_1900([31,12,1900]))
# print(days_since_1900([1, 1, 1900]))
# print(days_since_1900([1, 1, 1901]) / 1)
# print(days_since_1900([1, 1, 1902]) / 2)
# print(days_since_1900([1, 1, 1903]) / 3)
# print(days_since_1900([1, 1, 1904]) / 4)
# print((days_since_1900([1, 1, 1905]) - days_since_1900([1, 1, 1901]))/4)



# sunday returns 0
def what_day(date):
    day = days_since_1900(date)%7
    return day

def match(date):
    if (date[0]==1 and what_day(date)==6):
        return True
# print(what_day([7, 1, 1901]))
# print(what_day([15, 2, 2021]))

total = 0
for k in range(1901,2001):
    for j in range(1,13):
        if(is_leap_year(k)):
            for i in range(1,month_to_length_leap[j]+1):
                print(i,j,k,what_day([i,j,k]))
                if match([i,j,k]):
                    total+=1
                    print(i,j,k,what_day([i,j,k]))
        else:
            for i in range(1,month_to_length_no_leap[j]+1):
                if match([i,j,k]):
                    total+=1
                    print(i,j,k,what_day([i,j,k]))

print(i,j,k)
print(total)
