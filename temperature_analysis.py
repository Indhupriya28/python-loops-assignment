# Name: INDHUPRIYA DEISIGAN
# Roll Number: 2602031
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
min = temperatures[0]
max = temperatures[0]
for temp in temperatures:
    if(temp < min):
        min = temp
    if temp > max:
        max = temp

print (f"Highest Temperature: {max}°C")
print (f"Lowest Temperature: {min}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
count=0
for temp in  temperatures:
    if temp > 30:
        count +=1
    else:
        continue

print (f"Hot Days (>30°C): {count}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
# Write your code here
hot_Days =0
for i in range(len(temperatures)):
    if temperatures[i] >= 40:
        break
    if temperatures[i] > 30:
        hot_Days += 1
    

print (f"Hot Days before alert: {hot_Days}")

print (f"Alert! Extreme temperature 40°C detected on Day {int(i)+1}")
