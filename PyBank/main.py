# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
total_months = []
net_profit = []
profit_change = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        # Skip the header row
        csv_header = next(csvreader)

        # Loop through the rows in the file
        for row in csvreader:

            # Add the total months to the list
            total_months.append(row[0])

            # Add the total profit to the list
            net_profit.append(int(row[1]))

        # Loop through the profits to get the change in profits
        for i in range(len(net_profit)-1):
            
            # Add the difference between two months and add it to the profit change list
            profit_change.append(net_profit[i+1]-net_profit[i])

# Retrieve the minimum and maximum from the profit change list  
max_change = max(profit_change)
min_change = min(profit_change)

# Retrieve the month of the max and min change by using the month list and index from max and min
# using the next month as the month of change
month_max_change = profit_change.index(max(profit_change)) + 1
month_min_change = profit_change.index(min(profit_change)) + 1

# Print summary

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[month_max_change]} (${(str(max_change))})")
print(f"Greatest Decrease in Profits: {total_months[month_min_change]} (${(str(min_change))})")
          
# Output file
output_file = os.path.join("Financial_Analysis_Summary.txt")       

with open(output_file,"w", newline="") as file:
    
    # Write methods to print to Financial_Analysis_Summary 
        file.write("Financial Analysis")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(f"Total Months: {len(total_months)}")
        file.write("\n")
        file.write(f"Total: ${sum(net_profit)}")
        file.write("\n")
        file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {total_months[month_max_change]} (${(str(max_change))})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {total_months[month_min_change]} (${(str(min_change))})")