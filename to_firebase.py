import firebase_admin
from firebase_admin import db, credentials
import pandas as pd
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://coordinates-fb940-default-rtdb.asia-southeast1.firebasedatabase.app/"})
def add_new_data(new_data):
    coordinates_ref = db.reference('/coordinates')
    
    data = [{ "Latitude": item["Longitude"], "Longitude": item["Latitude"] } for item in new_data]
    
    coordinates_ref.set(data)
    
    print("New data added to 'coordinates' node.")

def retrieve_entire_data():
    coordinates_ref = db.reference('/coordinates')
    
    data = coordinates_ref.get()
    
    print("Data in 'coordinates' node:")
    print(data)


new_data_df = pd.read_csv("new_data.csv")

new_data_unique = new_data_df.drop_duplicates()

new_data_dict = new_data_unique.to_dict(orient='records')

add_new_data(new_data_dict)

retrieve_entire_data()
