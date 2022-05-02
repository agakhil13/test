import pandas as pd

df = pd.read_csv('./csv/data.csv')
df_1 = pd.read_csv('./csv/data1.csv')


for index, row in df.iterrows():
    
    location = df_1.loc[df_1.index[df_1[' Repo Name'] == row[" Repo Name"]]]    # location is a dataframe having the whole matched row inside it!

    if location.empty: 

        print('Do nothing!')

    else:

        print('Caught the match!')
        print('Match found at : ' + location)
        print('Match found at : ' + location[' Last Commit'])
        

        # Now compare location[' Last Commit'] and row[' Last Commit'] and proceed further!