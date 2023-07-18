import os,csv

data_path= os.path.join("PyBank","Resources","budget_data.csv")
output_path = os.path.join("PyBank","Analysis", "financial_analysis.txt")

months= 0
profit_loss= 0 
changes = []
previous_profit_loss = 0   
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""


with open(data_path) as in_data:
    reader = csv.reader(in_data)
    next(reader)
    
    for row in reader:
        current_profit_loss = int(row[1])
        profit_loss += int(row[1])
        months += 1
        
        if months > 1:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
                
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        previous_profit_loss = current_profit_loss

average_change = sum(changes) / len(changes)
   
print("Financial Analysis")
print("---------------------------------------------")
print("Total Months: ", months)
print("Total: $", profit_loss)
print("Average Change ", average_change)
print("Greatest Increase in Profits:", greatest_increase_date, "($",greatest_increase,")")
print("Greatest Decrease in Profits:", greatest_decrease_date, "($",greatest_decrease,")")
print("----------------------------------------------")
        
with open(output_path, "w") as out_file:
    out_file.write("Financial Analysis\n")
    out_file.write("----------------------------\n")
    out_file.write("Total Months: " + str(months) + "\n")
    out_file.write("Total: $" + str(profit_loss) + "\n")
    out_file.write("Average Change: $" + str(round(average_change, 2)) + "\n")
    out_file.write("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")\n")
    out_file.write("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")\n")
    out_file.write("----------------------------\n")

print("Analysis exported to", output_path)    