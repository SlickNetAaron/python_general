temps = [221, 234, 340, 230] # These values are stored w/o decimal to save disk

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# Same thing as List Comprehension

new_temps = [temp / 10 for temp in temps] #Inline loop does the same thing
# also don't need to create the list ahead of time like the first way

print(new_temps)

##################################################

temps = [221, 234, 340, -9999, 230]
# observation may be missing data and a placeholder is inserted
# We don't want to include it in list comprehension
new_temps2 = [temp / 10 for temp in temps if temp != -9999]

print(new_temps2)

# If you need else, the position changes
new_temps3 = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps3)