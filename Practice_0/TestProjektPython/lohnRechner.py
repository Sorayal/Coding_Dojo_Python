def is_float(value):
    try:
        float(value)
        return True
    except ValueError as e:
        print(str(e))
        return False


def calculate_workhours_month(workhours_per_week, weekfactor):
    return weekfactor * workhours_per_week


def calculate_brutto_sum(workhours_per_month, hourly_wage):
    return workhours_per_month * hourly_wage


workHoursPerWeek = 0.0
workHoursPerMonth = 0.0
hourlyWage = 0.0
# For Germany workHoursPerMonth = workHoursPerWeek * weekFactor
weekFactor = 4.35
valueErrorMessage = "Falsches Eingabeformat"

while True:
    hourlyWage = input('Bitte geben Sie den Stundenlohn an: ')
    if is_float(hourlyWage) and float(hourlyWage) >= 0.0:
        hourlyWage = float(hourlyWage)
        break
    else:
        print(valueErrorMessage)

while True:
    workHoursPerWeek = input('Bitte geben Sie die Wochenstunden an: ')
    if is_float(workHoursPerWeek) and 0.0 <= float(workHoursPerWeek) <= 168.0:
        workHoursPerWeek = float(workHoursPerWeek)
        break
    else:
        print(valueErrorMessage)


workHoursPerMonth = calculate_workhours_month(workHoursPerWeek, weekFactor)
bruttoSum = calculate_brutto_sum(workHoursPerMonth, hourlyWage)
print("Arbeitsstunden pro Monat: " + str(workHoursPerMonth))
print("Bruttolohn pro Monat: " + str(bruttoSum))
print("Bruttolohn pro Jahr: " + str(bruttoSum * 12))
input('Bitte drücken Sie eine Taste...')
