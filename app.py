import pandas as pd

#Reading csv as dataframe
old_df = pd.read_csv('data.csv')
new_df = pd.read_csv('data1.csv')
#Converting Repo Column to List
old_repo = old_df[" Repo Name"].tolist()
new_repo = new_df[" Repo Name"].tolist()

for repo in new_repo: #Iterating Repo in New file

    if repo in old_repo: #Repo name from new file exists in old file
        new_commit = new_df.loc[new_df[' Repo Name'] == repo, ' Last Commit'].tolist()[0] #Fetcing commit cell for matched repo from new file 
        old_commit = old_df.loc[old_df[' Repo Name'] == repo, ' Last Commit'].tolist()[0] #Fetcing commit cell for matched repo from old file
        
        if new_commit == old_commit: #Comparing commit from new file and old file for found repo name
            #new_df.loc[new_df[' Repo Name'] == repo, " Collaborators"] = "Unchanged"
            pass
        else: #Commit date in old and new not same
            new_df.loc[new_df[' Repo Name'] == repo, " Collaborators"] = "Commit changed"
    
    else: #Repo name from new file not exists in old file 
        new_df.loc[new_df[' Repo Name'] == repo, " Collaborators"] = "New Entry"

#Saving dataframe
new_df.to_csv("data2.csv", index=False)
