#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import csv

# Joining path
budget_data = os.path.join("/Users/yara/Resources", "budget_data.csv")

# Open and read CSV
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  

    # Initialize lists to store profit/losses and months
    P = []
    months = []

    # Read through each row of data after header
    for row in csvreader:  
        P.append(int(row[1]))
        months.append(row[0])

    # Find revenue change
    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append(P[x] - P[x-1])  

    # Calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)

    # Calculate total length of months
    total_months = len(months)

    # Greatest increase and decrease in revenue
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)

    # Print the results
    print("Financial Analysis")
    print("....................................................................................")
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum(P)}")
    print(f"Average Change: ${revenue_average:.2f}")
    print(f"Greatest Increase in Profits: {months[revenue_change.index(greatest_increase) + 1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {months[revenue_change.index(greatest_decrease) + 1]} (${greatest_decrease})")

    # Output to a text file
   
    with open("/Users/yara/desktop/Python-Challenge/PyBank/analysis/PyBank.txt", "w") as file:
        file.write("Financial Analysis\n")
        file.write("....................................................................................\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${sum(P)}\n")
        file.write(f"Average Change: ${revenue_average:.2f}\n")
        file.write(f"Greatest Increase in Profits: {months[revenue_change.index(greatest_increase) + 1]} (${greatest_increase})\n")
        file.write(f"Greatest Decrease in Profits: {months[revenue_change.index(greatest_decrease) + 1]} (${greatest_decrease})\n")


# In[ ]:




