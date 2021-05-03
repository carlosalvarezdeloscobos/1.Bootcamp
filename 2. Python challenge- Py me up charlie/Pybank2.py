import os
import csv

months= []
profit=[]
changes=[]

#/Users/carlosalvarez/Desktop/Boot/3 Python Intro/Python Intro Hmwk
#pybank_csv = os.path("Users/carlosalvarez/Desktop/Boot/3 Python Intro/Python Intro Hmwk")
pybank_csv = os.path.join("..","Python Intro Hmwk", "budget_data.csv")

#open de file and use de csv module to read it
with open(pybank_csv, newline='') as csvfile_pybank:
    csvreader_pybank = csv.reader(csvfile_pybank, delimiter=",")
    # extract the information to the months and profits list
    for row in csvreader_pybank:
        months.append(row[0])
        profit.append(row[1])

#remove information to start the operations
months.remove('Date')
profit.remove('Profit/Losses')

# Format profit to integeres
profit_integer= [int(x) for x in profit]

for i in range(0,len(profit_integer)):
  changes.append(profit_integer[i] - profit_integer[i-1])

changes_integer= [int(x) for x in changes]
changes_integer.remove(changes_integer[0])

addchanges=0

for x in range(1,len(changes_integer)):
  addchanges= addchanges + changes_integer[x]


# total months, total profit, ave change, greatest & lowest profit (with dates)
total_months= len(months)
total_profit= sum(profit_integer)
avechange= addchanges/(len(changes_integer))
greatest_profit= max(profit_integer)
minimum_profit= min(profit_integer)

#Use the following to identify wich months were the greatest and minimum profit
#zip_pybank_data= zip(months,profit)
#for months,profit in zip_pybank_data:
 #   print(months,profit)

#print results
print('TOTAL MONTHS: ' + str(total_months))
print('TOTAL PROFIT: ' + str(total_profit))
print('AVERAGE CHANGE: ' + str(avechange))
print('GREATEST INCREASE profit: ' + str(greatest_profit)+ ' month: ' + str(months[25]))
print('GREATEST DECREASE profit: ' + str(minimum_profit) + ' month: '+ str(months[44]))


# Export results to a new csv file
output_path = os.path.join("..","Python Intro Hmwk", "new_PYBANK.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as new_pybank:

    # Initialize csv.writer
    csvwriter = csv.writer(new_pybank, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months: ', total_months])
    csvwriter.writerow(['Total Profit: ', total_profit] )
    csvwriter.writerow(['GREATEST INCREASE profit: ', greatest_profit,' month: ', months[25]])
    csvwriter.writerow(['GREATEST DECREASE profit: ', minimum_profit ,' month: ', months[44]])