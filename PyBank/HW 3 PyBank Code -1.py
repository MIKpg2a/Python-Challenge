import csv
import os
# Initialize variables to store the analysis results
total_months = 0
total_profit_losses = 0
previous_month_profit_loss = 0
profit_loss_changes = []
dates = []

# Path to the dataset CSV file
csv_path = os.path.join('Resources','budget_data.csv') 

# Open and read the CSV file
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    header = next(csv_reader)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Extract date and profit/loss value from the current row
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate the total number of months
        total_months += 1
        
        # Calculate the net total amount of profit/losses
        total_profit_losses += profit_loss
        
        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            profit_loss_change = profit_loss - previous_month_profit_loss
            profit_loss_changes.append(profit_loss_change)
            dates.append(date)
        
        # Update the previous month's profit/loss for the next iteration
        previous_month_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)

# Find the corresponding dates for the greatest increase and decrease
increase_date = dates[profit_loss_changes.index(greatest_increase)]
decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Losses: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# Save the results to a text file
output_file = 'financial_analysis.txt'
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total Profit/Losses: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

print("Results saved to 'financial_analysis.txt'")
