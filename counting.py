import csv
import sqlite3

import pandas as pd
import pandas_alive

import datetime

""" """
registered = dict()
voter_hasvoted= list()
voter_password = dict()
candidate_votes = dict()
header = ["Candidate", "Date", "Votes"]
candidate_votes["Dongmo Naomie"] = 0
candidate_votes["Mocto Steeve"] = 0
candidate_votes["None"] = 0
nao_ani = list()
moc_ani = list()
no_ani = list()
today = datetime.date.today()
d1 = today.strftime("%Y-%m-%d")
sqlstr = 'SELECT * FROM Student'

"""MAIN PROGRAM"""
conn = sqlite3.connect('registration.db')
with conn:
      cursor=conn.cursor()
for row in cursor.execute(sqlstr):
    if(row[1] == None):
        continue
    registered[str(row[0])] = str(row[1]) 
"""FETCH AND PARSE THE DATA FROM THE CSV FILE"""   
with open("election.csv","r") as file:
    my_reader = csv.reader(file,)
    for row in my_reader:
        #Check if the registration number belongs
        if(str(row[1]) in list(registered)):
            #check if the password corresponds
            if(str(row[2]) == registered[str(row[1])]):
                #check if you have not yet voted
                if(str(row[1]) not in voter_hasvoted):
                    voter_hasvoted.append(str(row[1]))
                    candidate_votes[str(row[3])] += 1
        continue
i = 0
while (i <= candidate_votes["Dongmo Naomie"]):
    nao_ani.append(i**2 + i)
    i +=1
i = 0
while (i <= candidate_votes["Mocto Steeve"]):
    moc_ani.append(i**2 + i)
    i +=1
i = 0
while (i <= candidate_votes["None"]):
    no_ani.append(i**2 + i )
    i +=1
i = 0

while(len(nao_ani) != len(moc_ani) or len(nao_ani) != len(no_ani)):
    if(len(nao_ani) != len(moc_ani)):
        moc_ani.append(moc_ani[-1])
    if(len(nao_ani) != len(no_ani)):
        no_ani.append(no_ani[-1])

with open("votes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    writer.writerow(header)
    for i in range (len(nao_ani)) :
        writer.writerow(["Dongmo Naomie",d1,nao_ani[i]])
        writer.writerow(["Mocto Steeve",d1,moc_ani[i]])
        writer.writerow(["None",d1,no_ani[i]])
        

df_election = pd.read_csv("votes.csv")
df_election.plot_animated("ELECTION.gif",period_fmt="%Y-%m", title="PKFIE ELECTION")

