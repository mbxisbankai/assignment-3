days = ["Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday","Sunday"]
temperatures = []

print("Enter temperature for days of the week")
for day in days:
    temp = float(input(f"{day}:"))
    temperatures.append(temp)

lowest = min(temperatures)
highest = max(temperatures)
total = sum(temperatures)
average = total/len(temperatures)

print("\n Weekly Temperature Summary ")
print(f"\n{'Day':<12} {'Temperature':<12}°C")
print("-" * 27)

for day, temp in zip(days,temperatures):
    print(f"{day:<12} {temp:>12.2f}")

print("-" *27)

print(f"\n{'Lowest':<12} {lowest:>12.2f}°C")
print(f"{'Highest':<12} {highest:>12.2f}°C")
print(f"{'Sum':<12} {total :>12.2f}°C")
print(f"{'Average':<12} {average :>12.2f}°C")