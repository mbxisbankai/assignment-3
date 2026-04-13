
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
temperatures = []

print("Enter temperature for days of the week")
for day in days:
    temp = float(input(f"{day}: "))
    temperatures.append(temp)

lowest = min(temperatures)
highest = max(temperatures)
average = sum(temperatures) / len(temperatures)

print("\nWeekly Temperature Summary")
print(f"\n{'Day':<12} {'Temperature (°C)':>15}")
print("-" * 30)

for day, temp in zip(days, temperatures):
    print(f"{day:<12} {temp:>15.2f}")

print("-" * 30)
print(f"\n{'Lowest':<12} {lowest:>15.2f}")
print(f"{'Highest':<12} {highest:>15.2f}")
print(f"{'Average':<12} {average:>15.2f}")





