import csv
import os
# Initialize variables to store the analysis results
total_votes = 0
candidate_votes = {}
candidates = []

# Path to the dataset CSV file

csv_path = os.path.join('Resources','election_data.csv') 

# Open and read the CSV file
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    header = next(csv_reader)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Extract candidate name from the current row
        candidate_name = row[2]
        
        # Count the total number of votes
        total_votes += 1
        
        # Update candidate votes count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
            candidates.append(candidate_name)

# Initialize variables to store the winner information
winning_candidate = ""
winning_votes = 0

# Iterate through the candidate votes dictionary
for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes each candidate won
    percentage = (votes / total_votes) * 100
    
    # Print the candidate's name, percentage of votes, and total votes
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if this candidate has more votes than the current winner
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate

# Print the election results
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Save the results to a text file
output_file = 'election_results.txt'
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winning_candidate}\n")
    file.write("-------------------------\n")

print("Results saved to 'election_results.txt'")
