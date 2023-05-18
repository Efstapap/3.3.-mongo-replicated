from pymongo import MongoClient, ReadPreference, WriteConcern
from pymongo.errors import ConnectionFailure
import pymongo
from tkinter import Tk, Label
import time

# Create a Tkinter window
window = Tk()

# Update the window title
window.title("MongoDB Replica Set Connection")

# Connection string for the MongoDB replica set
connection_string = "mongodb://db01:30001,db02:30002/?replicaSet=rs0"


try:
    # Create a MongoDB client
    client = MongoClient(connection_string, w=1)

    # Access the primary node of the replica set
    primary_node = client.test.my_collection
    

    # Access the secondary node of the replica set
    secondary_node =    client.test.my_collection.with_options(read_preference=ReadPreference.SECONDARY)


    # Perform an insert operation on the primary node
    document = {"name": "George", "age": 28}
    result = primary_node.insert_one(document)
    print("Inserted document ID:", result.inserted_id)

    # Perform a read operation on the primary node (find a document)
    query = {"name": "George"}
    result_primary = primary_node.find_one(query)
    print("Retrieved document from primary:", result_primary)

    
    # Perform a read operation on the secondary node (find a document)
    result_secondary = secondary_node.find_one(query)
    print("Retrieved document from secondary:", result_secondary)
    
    # Perform a delete operation on the primary node
    delete_result = primary_node.delete_one(query)
    print("Deleted document count:", delete_result.deleted_count)

    # Introduce a delay of 5 seconds before reading from the secondary node
    time.sleep(5)


    # Perform a read operation on the secondary node after deletion (find a document)
    result_secondary_after_delete = secondary_node.find_one(query)
    print("Retrieved document from secondary after deletion:", result_secondary_after_delete)


     # Display the inserted document ID and retrieved documents in the GUI
    Label(window, text="Inserted document ID: " + str(result.inserted_id)).pack()
    Label(window, text="Retrieved document from primary: " + str(result_primary)).pack()
    Label(window, text="Retrieved document from secondary: " + str(result_secondary)).pack()
    Label(window, text="Retrieved document from secondary after deletion: " + str(result_secondary_after_delete)).pack()



except ConnectionFailure as e:
    # Display the connection failure message in the GUI
    Label(window, text="Failed to connect to the MongoDB replica set: " + str(e)).pack()

# Run the Tkinter event loop
window.mainloop()    
