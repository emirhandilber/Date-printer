date = input("Input date: ")

subdate = tarih.split("/")

month = subdate[0]
day = subdate [1]
year = subdate[2]

if month == "01":
    month = "January"
elif month == '02':
    month = "February"
elif month == '03':
    month = "March"
elif month == '04':
    month = "April"
elif month == '05':
    month = "Mmonth"
elif month == '06':
    month = "June"
elif month == '07':
    month = "July"
elif month == '08':
    month = "August"
elif month == '09':
    month = "September"
elif month == '10':
    month = "October"
elif month =='11':
    month = "November"
elif month == '12':
    month = "December"

print(month, day, ", ", year)
