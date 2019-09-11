import os
import csv

# Establish file path for test file
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
# Establish file path for output file
output_path = os.path.join("..", "PyBank","budget_output.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    with open(output_path, 'w', newline='') as newcsv:
        csvwriter = csv.writer(newcsv,delimiter=" ")
        csvheader = next(csvfile)
        #Initial Values
        months = []
        num_months = 0
        max_profit = 0
        min_profit = 0
        max_month = None
        min_month = None
        net_prof = 0
        max_change = 0

        for row in csvreader:
            months.append(row[0])
            #Count number of months
            num_months += 1
            net_prof += int(row[1])
            #Update min/max profit
            if int(row[1]) > max_profit:
                max_profit = int(row[1])
                max_month = str(row[0])
            elif (int(row[1]) < min_profit):
                min_profit = int(row[1])
                min_month = str(row[0])

        #Average Profit
        average_prof = int(net_prof / num_months)

        #Header
        print("Financial Analysis")
        csvwriter.writerow(["Financial Analysis"])
        #Separator
        print(f"-------------------------------------------")
        csvwriter.writerow(["--------------------------"])
        #Number of months in file
        print(f"Total Months: {num_months}")
        csvwriter.writerow(["Total Months: " + str(num_months)])
        #Net Profit
        print(f"Total: ${net_prof}")
        csvwriter.writerow(["Total: $" + str(net_prof)])
        #Average Change
        print(f"Average Change: ${average_prof}")
        csvwriter.writerow(["Average Change: $" + str(average_prof)])
        #Greatest Increase
        print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
        csvwriter.writerow(["Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_profit) + ")"])
        #Greatest Decrease
        print(f"Greatest Decrease in Profits: {min_month}: (${min_profit})")
        csvwriter.writerow(["Greatest Decrese in Profits: " + str(min_month) + " ($" + str(min_profit) + ")"])

            

