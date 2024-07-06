interest_rate = float(input("Enter the interest rate (per month): E.g 40\n>> ")) / 100
fund = float(input("Enter the fund:\n>> "))
maturity = int(input("Enter the maturity period as days:\n>> "))

output_money = fund * (1 + interest_rate) ** (maturity / 30)
profit = output_money - fund

print(f"Profit: {profit}")
print(f"Final money: {output_money}")
