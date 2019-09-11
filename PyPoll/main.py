import os
import csv

#Establish initial values
num_votes = 0
unique_cand = []
votes = []
#File Paths
csvpath = os.path.join("..", "PyPoll", "election_data.csv")
output_path = os.path.join("..", "PyPoll","election_output.csv")
greatest_vote = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvfile)
    with open(output_path, 'w', newline='') as newcsv:
        csvwriter = csv.writer(newcsv,delimiter=" ")

        for row in csvreader:
            votes.append(str(row[2]))

        for i in votes:
            if i not in unique_cand:
                unique_cand.append(i)
        # for     
        print("Election Results")
        csvwriter.writerow(["Election Results"])
        print("----------------")
        csvwriter.writerow(["-----------------"])
        #Total Number of Votes Cast
        print(f"Total Votes: {len(votes)}")
        csvwriter.writerow(["Total Votes: " + str(len(votes))])
        #Complete List of candiates who received votes
        #Percentage of votes each candidate won
        #Total number of votes each candiate won
        print(f"Candidates who received votes:")
        csvwriter.writerow(["Candidates who received votes:"]) 
        for cand in unique_cand:
            if votes.count(cand) > greatest_vote:
                greatest_vote = votes.count(cand)
            print(str(cand) + ": " + str(int(votes.count(cand) * 100/ len(votes))) + "%" + f" ({str(votes.count(cand))})")
            csvwriter.writerow([str(cand) + ": " + str(int(votes.count(cand) * 100/ len(votes))) + "% " +  "(" +(str(votes.count(cand))) + ")"])

        for cand in unique_cand:
            #Find candidate with most votes
            if votes.count(cand) == greatest_vote:
                winner = cand
        #Winner of election based on popular vote
        print("----------------")
        csvwriter.writerow(["--------------"])
        print(f"Winner: {winner}")
        csvwriter.writerow(["Winner: " + str(winner)])
        
