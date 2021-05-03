import os
import csv

#Create lists to append information from csv
voter_id=[]
candidates=[]
mydic1= {}
Khan_voterids= []
Correy_voterids= []
Li_voterids=[]

#Path of the file
pyroll_csv = os.path.join("..","Python Intro Hmwk", "election_data.csv")

#open de file and use de csv module to read it
with open(pyroll_csv, newline='') as csvfile_pyroll:
    csvreader_pyroll = csv.reader(csvfile_pyroll, delimiter=",")
    for row in csvreader_pyroll:
        # extract the information to the months and profits list
        voter_id.append(row[0])
        candidates.append(row[2])
        # extract the information of voter ids to lists
        if row[2] == "Khan":
            Khan_voterids.append(row[0])
        elif row[2] == "Li":
            Li_voterids.append(row[0])
        elif row[2] == "Correy":
            Correy_voterids.append(row[0])
 

voter_id.remove('Voter ID')
candidates.remove('Candidate')

#The total number of votes cast
total_votes= len(voter_id)

#A complete list of candidates who received votes
#find the unique candidates
merging= zip(candidates,voter_id)
mydic= dict(merging)
#print(mydic)

#The total number of votes each candidate wo
Khan_votes= len(Khan_voterids)
Correy_votes= len(Correy_voterids)
Li_votes= len(Li_voterids)
Otooley_votes= total_votes- Khan_votes- Correy_votes - Li_votes

winner= max(Khan_votes,Li_votes,Correy_votes,Otooley_votes)


#The percentage of votes each candidate won
Khan_percent_votes= Khan_votes/ total_votes
Correy_percent_votes= Correy_votes/ total_votes
Li_percent_votes=  Li_votes/ total_votes
Otooley_percent_votes= Otooley_votes/ total_votes

#Print results
print('TOTAL VOTES: ' + str(total_votes))
print('KHAN: ' + "{:.2%}".format(Khan_percent_votes)+ '(' +str(Khan_votes)+ ')')
print('CORREY: ' + "{:.2%}".format(Correy_percent_votes)+ '(' +str(Correy_votes)+ ')')
print('LI: ' + "{:.2%}".format(Li_percent_votes)+ '(' +str(Li_votes)+ ')')
print('OTOOLEY: ' + "{:.2%}".format(Otooley_percent_votes)+ '(' +str(Otooley_votes)+ ')')
print('Winner: Khan '+ str(winner))

# Export results to a new csv file
output_path = os.path.join("..","Python Intro Hmwk", "new_PYROLL.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as new_pyroll:

    # Initialize csv.writer
    csvwriter = csv.writer(new_pyroll, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['TOTAL VOTES: ',total_votes])
    csvwriter.writerow(['KHAN: ', Khan_percent_votes, Khan_votes ] )
    csvwriter.writerow(['CORREY ',Correy_percent_votes, Correy_votes])
    csvwriter.writerow(['LEE: ',Li_percent_votes, Li_votes ])
    csvwriter.writerow(['OTOOLEY:',Otooley_percent_votes, Otooley_votes ])
    csvwriter.writerow(['WINNER: ', 'Khan'])



