#Q1 
team = int(input("Number of team members"))
months= int(input("Number of months"))
monthly_salary = float(input("Monthly salary "))
cloud_cost = float(input("enter total cloud"))


salary_cost = team * months * monthly_salary
subtotal = salary_cost + cloud_cost
vat = subtotal * 0.14
total = subtotal + vat

print(f" Salary Cost: {salary_cost:,.2f} Subtotal{subtotal:,.2f} VAT (14%): {vat:,.2f} total: {total:,.2f} ")





######################################################################

#Q2
message = str(input("Customer message:"))
hours = int(input("Hours open"))


if  "payment" in  message:
    print("Billing")


elif "delivery" in message:
    print("logistics")

elif "error" in message:
    print("Tech")

else:
    print("General")     


if hours >= 24 :
    print("High")

else:
    print("Normal")