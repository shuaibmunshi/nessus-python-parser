#Shuaib Munshi - 23/06/2018

#!/usr/bin/python3
import pandas as pd
import numpy as np

df = pd.read_csv('test.csv', encoding='utf-8', usecols=['Plugin ID', 'Host', 'Name', 'Solution'], sep=',', quotechar='"', quoting=2)
#df['Host'].describe()
df["Duplicated"]=df.duplicated(['Plugin ID'], keep=False) #Adds is_duplicated collumn
#pd.concat(g for _, g in df.groupby("Host") if len(g) > 1)
df.sort_values(by=['Plugin ID'], inplace=True) #Sorts by Plugin ID
dict = df.to_dict('records') #Make Dict from csv data

####################
# Use this to validate data: df.loc[df['Plugin ID'] == 31705.0, ['Host']]
###################

tmplist = []
tmpid = 0

def output(x):
        print("| **Vulnerability** | **Solution** |") #Output ticket table
        print("| :-------- | :-------- |")
        print("|{} {} | {} |".format(dict[x]['Plugin ID'],str(dict[x]['Name']).replace('\n', ""), str(dict[x]['Solution']).replace('\n', ""))) #str().replace() replaces extraneous newline characters
        for i in tmplist:
                print(" - [ ] {}".format(i)) #Output Checkboxes

        print("\n")
        print("---------------")
        print("\n")

for x in range(len(dict)): #Iterate through dict
        #print(x)
        #print(dict[x]['Plugin ID']) # DEBUGGING CODE, PRINTS HOST LIST AS IT IS BUILT
        #print("@@@@@@@@@@@@")
        #for p in tmplist:
        #       print(p)
        #print("@@@@@@@@@@@@")
        if tmpid == 0: #To prevent initial iteration from failing
                tmpid = dict[x]['Plugin ID']
        if tmpid == dict[x]['Plugin ID']: #Checks to see if the Plugin ID is still repeating
                #if dict[x]['Plugin ID'] != dict[tmpxminus1]['Plugin ID'] and dict[x]['Plugin ID'] != dict[tmpxplus1]['Plugin ID']:
                        #tmplist[:] = []
                #if dict[x]['Host'] not in tmplist:
                if dict[x]['Host'] not in tmplist: #Append host to list if it is not already there, prevent duplicate hosts
                        tmplist.append(dict[x]['Host'])
        else:
                if dict[x]['Host'] not in tmplist:
                        tmplist.append(dict[x]['Host'])
                tmpindex = x - 1 #Get previous index positon because it is the last of the set of duplicate Plugin IDs
                output(tmpindex)
                tmpid = dict[x]['Plugin ID'] #Sets check variable for next iteration's plugin ID check
                tmplist[:] = [] #Clear tmp list for next set of hosts


