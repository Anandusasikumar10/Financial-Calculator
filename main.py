import math

def calculate_annuity(pmt, r, n, growth_type='monthly'):
    if growth_type == 'monthly':
        return pmt * (((1 + r)**n - 1) / r)
    elif growth_type == 'continuous':
        return pmt * (math.exp(r * n) - 1) / r
    else:
        raise ValueError("growth_type must be 'monthly' or 'continuous'")
def calculate_mortgage(P, r, n):
    monthly_rate = r / 12
    payments = n * 12
    return P * (monthly_rate * (1 + monthly_rate)**payments) / ((1 + monthly_rate)**payments - 1)
def retirement_balance(PV, pmt, r, n):
    future_value_PV = PV * ((1 + r) ** n)
    future_value_pmt = pmt * (((1 + r) ** n - 1) / r)
    return future_value_PV + future_value_pmt
def time_to_double(r):
    return math.log(2) / math.log(1 + r)
def solve_logarithmic(base, y):
    return base ** y
def to_scientific(num):
    return f"{num:.5e}"

def from_scientific(sci_str):
    return float(sci_str)



def main():
    while True:
        print("\nFinancial Calculator Menu")
        print("1. Annuity")
        print("2. Mortgage")
        print("3. Retirement")
        print("4. Time to Double")
        print("5. Solve Logarithmic")
        print("6. Scientific Notation")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            pmt = float(input("Payment per period: "))
            r = float(input("Rate per period (e.g., 0.05): "))
            n = int(input("Number of periods: "))
            t = input("Type (monthly/continuous): ").strip().lower()
            print("Future Value:", calculate_annuity(pmt, r, n, t))
        elif choice == "2":
            P = float(input("Principal loan amount: "))
            r = float(input("Annual interest rate (e.g., 0.05): "))
            n = int(input("Loan term in years: "))
            print("Monthly Payment:", calculate_mortgage(P, r, n))
        elif choice == "3":
            PV = float(input("Present value: "))
            pmt = float(input("Monthly contribution: "))
            r = float(input("Annual rate (e.g., 0.05): "))
            n = int(input("Years: "))
            print("Estimated Retirement Balance:", retirement_balance(PV, pmt, r, n))
        elif choice == "4":
            r = float(input("Interest rate (e.g., 0.05): "))
            print("Time to double:", time_to_double(r), "periods")
        elif choice == "5":
            base = float(input("Log base: "))
            y = float(input("Result of log equation: "))
            print("Solved x:", solve_logarithmic(base, y))
        elif choice == "6":
            sub = input("Type 'to' to convert to scientific, 'from' to convert from: ").strip().lower()
            if sub == "to":
                num = float(input("Enter number: "))
                print("Scientific:", to_scientific(num))
            elif sub == "from":
                sci = input("Enter scientific notation (e.g., 1.23e+04): ")
                print("Number:", from_scientific(sci))
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()


input("Press Enter to exit...")