#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os
import csv

# Joining path
election_data = os.path.join("/Users/yara/Resources", "election_data.csv")

# Open and read CSV
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  

# intializing as dictionary    
    candidate_votes = {}
    
# Read through each row of data 
    for row in csvreader:
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate thee total votes, winner and winner percantage
    total_votes = sum(candidate_votes.values())
    winner = max(candidate_votes, key=candidate_votes.get)
    winner_percentage = candidate_votes[winner] / total_votes * 100

# print results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")

    for candidate, votes in candidate_votes.items():
        percentage = votes / total_votes * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")

    print("----------------------------")
    print(f"Winner: {winner} ({winner_percentage:.3f}%)")
    print("----------------------------")

# Output to txt file
    with open('/users/yara/desktop/Python-Challenge/PyPoll/Analysis/PyPoll.txt', 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write("----------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("----------------------------\n")

        for candidate, votes in candidate_votes.items():
            percentage = votes / total_votes * 100
            output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        output_file.write("----------------------------\n")
        output_file.write(f"Winner: {winner} ({winner_percentage:.3f}%)\n")
        output_file.write("----------------------------\n")


# In[ ]:




