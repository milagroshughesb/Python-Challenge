import os,csv

data_path= os.path.join("PyPoll","Resources","election_data.csv")
output_path = os.path.join("PyPoll","Analysis", "financial_analysis.txt")

#Read the CSV File
with open(data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row
    data = list(csvreader)

#Calculate Total Votes
total_votes = len(data)

#Create and Populate the Candidate Votes Dictionary
candidate_votes = {}
for row in data:
    candidate_name = row[2]
    candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1

#Calculate Percentage of Votes for Each Candidate
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

#Determine the Winner
winner = max(candidate_votes, key=candidate_votes.get)

# Step 7: Print and Export the Results
with open(output_path, "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        f.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
