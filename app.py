import pandas as pd

df = pd.read_csv('./csv/data.csv')
df_1 = pd.read_csv('./csv/data1.csv')


for index, row in df.iterrows():

    # location is a dataframe having the whole matched row inside it!
    location_match_for_repo_name = df_1.loc[df_1.index[df_1[' Repo Name']
                                                       == row[" Repo Name"]]]
    location_match_for_last_commit = df_1.loc[df_1.index[df_1[' Last Commit']
                                                         == row[" Last Commit"]]]

    if location_match_for_repo_name.empty:

        print('Execute some APIs!')
        df_1.loc[df_1.index[df_1[' Repo Name'] == row[" Repo Name"]],
                 '  Collaborators'] = 'Replace this with desired string value!'
        df_1.to_csv('./csv/some-new-file.csv')

    else:

        print('Now checking if Last commit is same or not in both CSVs!')

        if location_match_for_last_commit.empty:  # if last commit is not same in both CSVs

            print('Execute some APIs!')
            df_1.loc[df_1.index[df_1[' Repo Name'] == row[" Repo Name"]],
                     '  Collaborators'] = 'Replace this with desired string value!'
            df_1.to_csv('./csv/some-new-file.csv')

        else:                                     # if last commit is same in both CSVs

            print('Ignoring the repo!')
