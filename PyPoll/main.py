# Modules
import os
import csv


# set up vote counter and candidates
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

# Set path for file
filepath = os.path.join("..", "Resources", "election_data.csv")
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # tally votes
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# calculate vote percentage and identify winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person            


# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
          
# Output file
output_file = os.path.join("Election_Results_Summary.txt")       

with open(output_file,"w", newline="") as file:
    file.write("-------------------------" + "\n")
    file.write(f"Total Votes: {total_votes}" + "\n")
    file.write("-------------------------" + "\n")
    for person, vote_count in candidate_votes.items():
        file.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
    file.write("-------------------------" + "\n")
    file.write(f"Winner: {winner}" + "\n")
    file.write("-------------------------" + "\n")