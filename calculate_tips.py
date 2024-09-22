def calculate_tip(bill_amount, tip_percentage):
    
    return bill_amount * (tip_percentage / 100)

def main():
    try:
        bill_amount = float(input("Enter the bill amount: "))
        tip_percentage = float(input("Enter the tip percentage: "))
        
        tip = calculate_tip(bill_amount, tip_percentage)
        print(f"Tip amount: ${tip:.2f}")
        
    except ValueError:
        print("Please enter valid numbers for the bill and tip.")

if __name__ == "__main__":
    main()
