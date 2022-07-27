# Election Audit Analysis

## Overview of Election Audit
Election Audit project is focus on using Python and Visual Studio Code to process the Colorado Board of Elections dataset and implement data audit. In the election audit, we perform data analysis and submit the election results to the election commission. Besides, we deliever additional audited information as requested: 

- The voter turnout for each county
- The percentage of votes from each county out of the total count 
- The county with the highest turnout.

### Analysis Results Information including:
```
1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The total number of votes each candidate received.
4. The percentage of votes each candidate won.
5. The winner of the election based on popular vote.
```
### Resources
- Data Source: election_results.csv
- Data Results: election_analysis.txt
- Software:Python 3.7.6, Visual Studio Code, 1.63.2
- Insights: https://docs.google.com/presentation/d/1Bobs88Gls6hcqK675tICyev8ht5DJKNzrECC_Et2wM8/edit?usp=sharing

## Election-Audit Results
### Candidate Result
The analysis of the election shows that:
- There were **"369,711"** votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Athony Doane
- The candidate results were:
   - Charles Casper Stockham received *"23.0%"* of the vote and *"85,213"* number of votes.
   - Diana DeGette received *"73.8%"* of the vote and *"272,989"* number of votes.
   - Raymon Athony Doane received *"3.1%"* of the vote and *"11,606"* number of votes.
 - The winner of the election was:
   - Diana DeGette, who received **"73.8%"** of the vote and **"272,989"** number of votes.
### County Result
The analysis of the election shows that:
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson has *"10.5%"* out of the total votes count and *"38,855"* votes to turnout.
  - Denver has *"82.8%"* out of the total votes count and *"306,055"* votes to turnout.
  - Arapahoe has *"6.7%"* out of the total votes count and *"24,801"* votes to turnout.
- The county with the highest turnout was:
  - Denver, where has **"6.7%"** of the total county turnout and county turnout votes is **"306,055"**.

## Election-Audit Summary
We have total votes 369,711 cast in this congressional election. In this election, there are three candidates paticipated, and three counties have votes turnout. Amount the three counties, Denver has the largest number of votes. And candidate Diana DeGette has won the election with total votes 272,892 and 73.8% of the total votes. 
### Challenge Summary
We use Python to generate our dataset and write codes. When we process our auditing work, we used Visual Studio Code to modify our script and run Python files in the terminal. The script in this election we audited can be used for any election because it helps us to determine the winning candidate, vote counts and percentage. For example, we use the decision statement to compare the candidates' votes and counties votes turnout, which can be applied to other elections as needed. For instance, we use loop structure with operators to extract data for all ballets, and this script can avoid duplicate counts our votes.  

________________________________________________________________________________________________________________________________

Project Contributor: Phoebe J. Miao
Email: phoebem2021data@gmail.com
