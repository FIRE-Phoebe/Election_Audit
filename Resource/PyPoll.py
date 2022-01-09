file_to_load='Resource\election_results.csv'
election_data = open(file_to_load,'r')
#close the file.
election_data.close()
with open(file_to_load) as elcetion_data:
    print(election_data)
import csv
import os
#Assign variable for the fie to load and the path.
file_to_load=os.path.join('Resource','election_results.csv')
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #print the file object.
    print(election_data)

#Create a file name variable to a direct or indirect fath to the file.
file_to_save=os.path.join('analysis','election_analysis.txt')
#Use the open statement to open the file as a text file.
outfile=open(file_to_save,'w')
#Write some data to the file
outfile.write('Hello World')
#Close the file
outfile.close()
#Using the with statetment open the file as a text file.
with open(file_to_save,'w') as txt_file:
    #Write some data to the file.
    txt_file.write('Counties in the Eletion\n--------------------\nArapahoe\nDenver\nJefferson')

#Re-organize code
import csv
import os
file_to_load=os.path.join('Resource','election_results.csv')
file_to_save=os.path.join('analysis','election_analysis.txt')
election_data=open(file_to_load,'r')
#open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

