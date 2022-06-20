import mysql.connector 
import pandas as pd

database_connection = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    password='********',
    database='Constantia_Insurance_Assessment'
)

# this is an instance of a connection to the data base
mycursor = database_connection.cursor()


# This is an api on how to add data on the tables I have created
add_policy = ("INSERT INTO policy \
    (policy_number,policy_holder_first_name,policy_holder_last_name,policy_inception_date) \
        VALUES (%s,%s,%s,%s)")

add_policy_items = (
    "INSERT INTO policy_item\
        (policy_number,policy_item_number,section,sum_insured)\
            VALUES (%s,%s,%s,%s)"
)

add_claims = (
    "INSERT INTO claim\
        (claim_number,policy_number,date_of_loss,claim_rate_reported)\
            VALUES (%s,%s,%s,%s)"
)

    
#reading in the data
claims = pd.read_excel('CLAIM.xlsx')
#transforming the data to match the table
claims.date_of_loss=claims.date_of_loss.apply(lambda x: x.date())
claims.claim_date_reported=claims.claim_date_reported.apply(lambda x: x.date())

policy = pd.read_excel('POLICY.xlsx')
#transforming the data to match the table
policy.policy_inception_date=policy.policy_inception_date.apply(lambda x: x.date())

policy_items = pd.read_excel('POLICY_ITEM.xlsx')

for row in policy.values:
    mycursor.execute(add_policy, tuple(row))

for row in policy_items.values:
    mycursor.execute(add_policy_items, tuple(row))

for row in claims.values:
    mycursor.execute(add_claims, tuple(row))

database_connection.commit() # I commit so that the changes made are saved

print('\n\n')
filteredByPolicy_number = policy_items.groupby('policy_number ').mean() # I got the average sum of insured per policy number
print('Policy_number   Average_Sum_Insured')
for policy_number, avg_sum in zip(filteredByPolicy_number.index, filteredByPolicy_number.values):
    print(policy_number, '          ',avg_sum[0])