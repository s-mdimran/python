def count_days(n,startday):
    weeks = n//7
    sunday = weeks
    remaining_days = n%7

    for i in range(remaining_days):
        if (startday+i)%7==1:
            sunday += 1

    return sunday

n = int(input("Enter the number of days: "))

startday=int(input("Enter Startdate: "))

num_sunday=count_days(n,startday)

print(f"there are {num_sunday} sundays in {n} day starting on day {startday}.")