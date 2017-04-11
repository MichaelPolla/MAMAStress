import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import datetime
from collections import OrderedDict

plt.style.use('seaborn-notebook')

# Get data
commits = pd.read_csv('github_commits.csv', sep=',', parse_dates=['date'])
issues = pd.read_csv('jira_issues_bugs.csv', sep=',', parse_dates=['date'])
versions = pd.read_csv('jira_versions.csv', sep=',', parse_dates=['release_date'])

def generateFig(byFreq, filename):
	plt.figure(figsize=(20,10))

	# Print commits
	commitsGroupBy = commits.groupby(pd.Grouper(key='date', freq=byFreq)).count()
	plt.plot(commitsGroupBy, label="Number of commits")
	print type(commitsGroupBy)

	# Print issues
	issuesGroupBy = issues.groupby(pd.Grouper(key='date', freq=byFreq)).count()
	plt.plot(issuesGroupBy, label="Number of bugs", color="red")

	maxValue = commitsGroupBy.max()
	# Print versions
	for i in versions.index :
		date = versions["release_date"][i]
		name = versions["name"][i]
		released = versions["released"][i]
		if(released):
			plt.axvline(date, color='green', linewidth=0.5, label="Version")
			plt.text(date+datetime.timedelta(days=10), maxValue-maxValue/5, versions["name"][i], rotation=90, fontsize=8)

	# Print legends
	handles, labels = plt.gca().get_legend_handles_labels()
	by_label = OrderedDict(zip(labels, handles))
	plt.legend(by_label.values(), by_label.keys())

	plt.savefig(filename)

generateFig('1d', 'all_day.png')

generateFig('7d', 'all_week.png')

generateFig('1M', 'all_month.png')
