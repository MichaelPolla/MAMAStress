import matplotlib
# Force matplotlib to not use any Xwindows backend. To fix
#     _tkinter.TclError: no display name and no $DISPLAY environment variable
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import datetime
import sys
from collections import OrderedDict
import os

PATH = 'csv_data/'
if(len(sys.argv) > 1):
	PATH=sys.argv[1]

if not os.path.exists(PATH):
	os.makedirs(PATH)

# Wait for other docker container
while os.path.exists(PATH+'github_retriever.txt')!= True:
	pass
while os.path.exists(PATH+'jira_retriever.txt')!= True:
	pass
os.remove(PATH+'github_retriever.txt')
os.remove(PATH+'jira_retriever.txt')

plt.style.use('seaborn-notebook')

# Get data
commits = pd.read_csv(PATH+'github_commits.csv', sep=',', parse_dates=['date'])
issues = pd.read_csv(PATH+'jira_issues_bugs.csv', sep=',', parse_dates=['date'])
versions = pd.read_csv(PATH+'jira_versions.csv', sep=',', parse_dates=['release_date'])


def generateFig(byFreq, filename, figurename, dateBegin=None, dateEnd=None, realDate=None):
  f,ax = None,None
  if(dateBegin == None):
    f=plt.figure(figsize=(20,10))
  else:
    f=plt.figure(figsize=(5,5))
  
  commitsCutted = commits
  issuesCutted = issues

  if(dateBegin <> None):

    # Cut
    commitsCutted = commitsCutted.loc[(commitsCutted['date'] >= dateBegin) & (commitsCutted['date'] <= dateEnd)]
    issuesCutted = issuesCutted.loc[(issuesCutted['date'] >= dateBegin) & (issuesCutted['date'] <= dateEnd)]

  # Print commits and commits
  commitsGroupBy= commitsCutted.groupby(pd.Grouper(key='date', freq=byFreq)).count()
  issuesGroupBy = issuesCutted.groupby(pd.Grouper(key='date', freq=byFreq)).count()

  #fill_in_missing_dates
  if dateBegin<>None:
    idx = pd.date_range(start=dateBegin, end=dateEnd, freq="D")
    for d in idx:
      try: 
        a = commitsGroupBy.loc[d]  
      except :
        commitsGroupBy.loc[d] = 0
      """try: 
        a = issuesGroupBy.loc[d]  
      except :
        issuesGroupBy.loc[d] = 0"""
    
  commitsGroupBy.sort_index()
  issuesGroupBy.sort_index()

  ax = commitsGroupBy.plot(color='blue', legend=False, sharex=True)
  try:
    issuesGroupBy.plot(ax = ax, color='red', legend=False, sharex=True)
  except:
    print "Nothing"
   
  maxValue = commitsGroupBy.max()
  if(dateBegin == None):
    # Print versions
    for i in versions.index :
      date = versions["release_date"][i]
      name = versions["name"][i]
      released = versions["released"][i]
      if(released):
        plt.axvline(date, color='green', linewidth=0.5, label="Version")
        plt.text(date+datetime.timedelta(days=4), maxValue-maxValue/5, versions["name"][i], rotation=90, fontsize=8)
  else:
    plt.axvline(realDate, color='green', linewidth=0.5, label="Deadline")

  f.autofmt_xdate()
  
  # Print legends
  handles, labels = plt.gca().get_legend_handles_labels()
  by_label = OrderedDict(zip(labels, handles))
  plt.suptitle(figurename, fontsize=20)
  if(dateEnd <> None):
    plt.figtext(.5,.905, realDate.strftime("%d/%m/%Y"), fontsize=10, ha='center')
  plt.legend(['Commits', 'Bugs', 'Deadlines'], loc='upper left')
  plt.savefig(filename)

# Generate general graphics
generateFig('1d', PATH+'all_day.png', "Par jour")
generateFig('7d', PATH+'all_week.png', "Par semaine")
generateFig('1M', PATH+'all_month.png', "Par mois")

# Generate graphics foreach release
for i in versions.index :
  date = versions["release_date"][i]
  name = versions["name"][i]
  released = versions["released"][i]
  if(released):
    beginDate = date - datetime.timedelta(days=14)
    print name + " from:"+str(beginDate) + " to:" + str(date)
    dateEnd = date + datetime.timedelta(days=14)
    generateFig('1d', PATH+'' + name+'.png', name, beginDate, dateEnd, date)
