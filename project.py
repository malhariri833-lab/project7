total_cost = float(input("What is the total cost? "))
people = int(input("How many people? "))

cost_per_person = total_cost / people
print("Cost per person:", cost_per_person)

items = int(input("How many items? "))

if items % people == 0:
    print("The items can be shared equally.")
else:
    print("The items cannot be shared equally.")
    print("Items left over:", items % people)

week1 = float(input("Week 1: "))
week2 = float(input("Week 2: "))
week3 = float(input("Week 3: "))
wrong_week = float(input("Wrong figure: "))
correct_week = float(input("Correct figure: "))

average = (week1 + week2 + week3 + correct_week) / 4
print("Weekly average:", average)

store1 = float(input("Local store 1: "))
store2 = float(input("Local store 2: "))
store3 = float(input("Local store 3: "))

if average < store1 and average < store2 and average < store3:
    print("The average is cheaper than all three stores.")
elif average < store1 or average < store2 or average < store3:
    print("The average is cheaper than some stores.")
else:
    print("The average is not cheaper than the stores.")

print("SUMMARY")
print("Cost per person:", cost_per_person)
print("Weekly average:", average)