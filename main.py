# input statements
salary = float(input( "Enter your salary: "))
numDependents = float(input( "Enter the number of dependents: "))

# calculate taxes here
stateTax = salary * 0.065
fedralTax = salary * 0.28
dependentDeduction = numDependents * (salary * 0.025)
totalWithholding = stateTax + fedralTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Fedral Tax: $" + str(fedralTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))