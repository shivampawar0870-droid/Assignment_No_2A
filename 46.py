print("Enter Marks of 5 Subjects")

ds = int(input("Enter DS Marks: "))
is_marks = int(input("Enter IS Marks: "))
deld = int(input("Enter DELD Marks: "))
uhv = int(input("Enter UHV Marks: "))
ai = int(input("Enter AI Marks: "))

average = (ds + is_marks + deld + uhv + ai) / 5

print("\nAverage Marks =", average)

if average >= 80:
    print("Grade : Distinction")
elif average >= 65:
    print("Grade : First Class")
elif average >= 40:
    print("Grade : Second Class")
else:
    print("Grade : Fail")
