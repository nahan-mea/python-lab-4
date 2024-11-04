def calculate_simple_interest(principal, time, is_senior):
    rate = 12 if is_senior else 10
    return (principal * rate * time) / 100

principal = float(input("Enter principal amount: "))
time = float(input("Enter time (in years): "))
is_senior = input("Is the customer a senior citizen? (yes/no): ").strip().lower() == 'yes'
interest = calculate_simple_interest(principal, time, is_senior)
print("Simple Interest:", interest)

