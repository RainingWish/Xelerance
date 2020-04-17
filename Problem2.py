#use dataframe, need to install pandas
#pip install pandas
import pandas as pd 

#use dataframe to read csv file
file = "address.csv"
all_address_df = pd.read_csv(file)

#create a new dataframe only store the province == ontario
ontario_df = all_address_df.loc[all_address_df['Province'] == 'Ontario']

#print out the answer
print("Ontario residents are listed below:")
print(ontario_df)
