# ANYWAY Data Science

Welcome to ANYWAY's Data Science Team!

## About ANYWAY

ANYWAY is a volunteer based project acting under the umbrella of the Public Knowledge Workshop (“HASADNA”) that aims to reduce road accidents by:
1. Raising public awareness of existing road hazards, thereby leading towards safer road behaviour.
2. Collaborating with authorities in order to assist and drive them to find solutions in light of Vision Zero. Such solutions will improve road infrastructure and behavioural problems in attempt to prevent road fatalities.

## Our Challenge

Our current challenge is forming an automatic generator of infographics to empower and serve journalists, bloggers, public opinion leaders, community leaders etc. in the era of data journalism. The generated infographics will enhance reporting and news writing with the use of statistics. Each infographic will be created for a real-time road accident related news flash and will provide a deeper insight into the story based on historical data. This, we believe, will increase both the quantity and quality of articles dealing with road accidents, and will result in raising public awareness and creating pressure on decision makers to initiate infrastructure improvements in light of Vision Zero.

Please see [ANYWAY's main repository](https://github.com/hasadna/anyway) to read more about our vision, collaborations and previous projects :-)

## Communication:

Via Slack. Ask any member for an invite by email.  
Please join channels #anyway, #anyway_data_science, #anyway_news_report and #general.


## Teams and Code:

There are several teams in the Anyway project:  
Front End, Back End, Data Engineering, Data Science, etc.

Similarly there are several “anyway” Github repositories too:  
https://github.com/hasadna?q=anyway

The repo that we, the Data Scientists, work with is:  
https://github.com/hasadna/anyway-data-science

We mainly add jupyter notebooks to it, for two purposes:  
  - Share useful Data Explorations  
  - Perform task PoC’s (Proof of Concepts)  
  - To later be integrated into production by DS and\or BE team  

At the moment it mainly contains these three folders:  
  - `/analysis_notebooks` : Mostly used for PoC’s and other things worth considering  
  - `/learning_notebooks` : Mostly used for Data Explorations  
  - `/tasks` : specific tasks related notebooks  


## Getting Started:

First-timers are advised to browse through (or play with) some notebooks in the repo.  
They contain pieces of code and data you may find useful.  

When you feel ready to take on a task, assign yourself one. (see “Tasks:” for more info)

Task owners shouldn’t deal with production-related overhead. When possible, keep it simple.  
To that end we’ve gathered here a few tips:  
  - Notebook: Use JupyterLab, or Colab if you have trouble installing packages  
  - Database: Use the offline CSVs (rather then connecting to the DB)  
  - Location: Find “close” records using Euclidean distance  
    Without root is ok too: (x_db - x_news)**2 + (y_db - y_news)**2  


## Data Resources:

### Offline Data
First, send a permission request to view the [data directory](https://drive.google.com/drive/folders/1k5bLQDN0VcyUdPqZ7oTxUE-eMOfD_E5E)  
Then, make sure you check out the Data Index file  


### Online Data
[Redash](https://app.redash.io/hasadna/queries?q=anyway) (an online platform to query our tables using SQL)  
[Get some inspiration from the world](https://docs.google.com/document/d/1GvfiFXkN7-80TBsvpEFEUB6z03VaBhHHa6ye_DBrQFA/edit?usp=sharing) - Accident data from different places in the world and data analysis  


## Tasks:

Tasks are added as Github Issues in our repo:  
https://github.com/hasadna/anyway-data-science/issues

Feel free to assign yourself a task to let the others know someone’s working on it.  

Feel free to also create an issue yourself if you think of a new task, or want to report a problem (You may need repo permissions to do so).  


## GitHub and Git:

If you haven’t already, install Git.  
  
Enter our repo  
If you haven’t already, click “Fork” on the top right to create your own copy of the code.    
On the right, click “Clone or download” and then the “copy” icon.  
  
Find a path to create a folder called “src”.  
Open a terminal (or “command prompt”) and change to that directory:  
`cd my_folder`  
`cd src`  
  
Paste the link after these two words and run it:  
`git clone <the-link-that-you-copied>`  
  
Enter the cloned repo:  
`cd anyway-data-science`  
  
Create your own branch:  
`git checkout -b task_1234`  
  
For each file you wanna add, run this:  
`git add my_notebook.ipynb`  
  
Wrap it all up in a commit:  
`git commit -m “Add my awesome notebook for task #1234”`  
  
Push it to your repo on Github’s website:  
`git push`  

this might print an error message with a suggested command, copy and run it  
  
On your fork (copy) on Github, go to “branches” and select “New pull request” for your branch.

### How to merge changes from the original repository to your fork?

Set the remote repository as your “upstream” repo:  
`git remote add upstream https://github.com/hasadna/anyway-data-science.git`  
  
Fetch the upstream:  
`git fetch upstream`  
  
Check out your fork’s local master branch:  
`git checkout master`  
  
Merge the changes from upstream’s master to your local master:  
`git merge upstream/master`  

Push the changes from your local master to your fork’s master in Github:  
`Git push`
