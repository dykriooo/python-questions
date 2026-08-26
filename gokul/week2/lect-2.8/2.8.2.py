# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB
yob=int(input())
age=2026-yob
if age>=18:
    print("yes")
else:
    print("no")
