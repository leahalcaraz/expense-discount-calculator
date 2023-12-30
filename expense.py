# Leah Alcaraz 301279925

input_name = []
input_age = []

input_amount_spent = []

for i in range(1, 4):
    while True:
        name, age = input(f"Enter the name and age of person {i}\n").split()
        if int(age) > 0:
            input_name.append(name)
            input_age.append(int(age))
            break
        else:
            print("Age should be positive, try again!")

print("\b")

for name in input_name:
    while True:
        cost = input(f"Enter the total amount spent by {name}\n")
        input_amount_spent.append(cost)
        total_cost = cost
        break

print("\b")
print("Name of the programmer: XXX XXXXXX")
print("Student ID: XXXXX")

print("%-10s" % "Name", "%-5s" % "Age", "%10s" % "Cost", "%10s" % "Discount", "%10s" % "Net Cost")
for i in range(len(input_name)):

    cost = input_amount_spent[i]
    age = input_age[i]
    cost = float(cost)

    if age >= 65 and cost > 500:
        discount = 0.30
    elif age > 65 and cost < 500:
        discount = 0.10
    elif age < 65 and cost > 500:
        discount = 0.20
    else:
        discount = 0.0

    net_cost = cost - (cost * discount)
    discount_amount = cost - net_cost

    print("%-10s" % input_name[i], "%-5d" % age, "%10.2f" % cost, "%10.2f" % discount_amount, "%10.2f" % net_cost)




