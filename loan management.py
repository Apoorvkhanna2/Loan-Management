from datetime import datetime

def calculate_loan(amount, rate, tenure):
    monthly_rate = rate / (12 * 100)
    months = tenure * 12
    emi = (amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    total_payment = emi * months
    total_interest = total_payment - amount
    return emi, total_interest, total_payment

def apply_penalty(due_date, payment_date, amount_due):
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    payment_date = datetime.strptime(payment_date, "%Y-%m-%d")
    if payment_date > due_date:
        penalty = 0.05 * amount_due
        return penalty
    return 0

def main():
    amount = float(input("Enter loan amount: "))
    rate = float(input("Enter annual interest rate (in %): "))
    tenure = int(input("Enter loan tenure (in years): "))
    emi, total_interest, total_payment = calculate_loan(amount, rate, tenure)
    
    print(f"\nMonthly EMI: {emi:.2f}")
    print(f"Total Interest Payable: {total_interest:.2f}")
    print(f"Total Payment (Principal + Interest): {total_payment:.2f}")
    
    due_date = input("Enter due date for payment (YYYY-MM-DD): ")
    payment_date = input("Enter actual payment date (YYYY-MM-DD): ")
    penalty = apply_penalty(due_date, payment_date, emi)
    
    if penalty > 0:
        print(f"Late payment penalty applied: {penalty:.2f}")
    else:
        print("Payment made on time. No penalty.")

if __name__ == "__main__":
    main()