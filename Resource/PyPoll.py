import csv
import os
file_to_load=os.path.join('Resource','election_results.csv')
file_to_save=os.path.join('analysis','election_analysis.txt')

#Initialize a total vote counter.
total_votes=0
#candidate options
candidate_options=[]
#declare the empty dictionary.
candidate_votes={}
#winning candidate and winning count tracker
winning_candidate=''
winning_count=0
winning_percentage=0


#Open the election results and read file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    headers=next(file_reader)
    print(headers)
   
   #print each row in the csv file.
    for row in file_reader:
        total_votes+=1

        #print candidate name form each row.
        candidate_name=row[2]

        #if the candidate does not match an existing candidate
        if candidate_name not in candidate_options:

        #add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

        #begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

        candidate_votes[candidate_name]+=1
#determine the percentage of votes for each candidate by looping through the counts.
# 1. iterate through the candidate list.
for candidate_name in candidate_votes:
    #2. Retriveve vote count of a candidate.
    votes=candidate_votes[candidate_name]
    #3. calculate the percentage votes.
    vote_percentage=float(votes)/float(total_votes)*100

    #To-do: print out each candidate's name, vote count, and percentage of
    #votes to the terminal.

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count.
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        #if true then set winning_count=votes and winning_percentage=
        #vote_percentage.
        winning_count=votes
        winning_percentage=vote_percentage
        #And, set the winning_candidate equal to the candidate's name
        winning_candidate=candidate_name

#To do:print out the winning candidate, vote count and percentage to
#   terminal.
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

winning_candidate_summary=(
    f'-----------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-----------------------\n')
print(winning_candidate_summary)


        