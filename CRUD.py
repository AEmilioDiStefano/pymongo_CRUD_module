from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31782
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# The create() method implements the C in CRUD.
    def create(self, data):
        # If nothing is passed into the data parameter,
        if data is None:
            # then raise an exception stating that the parameter was left empty.
            raise Exception("Nothing to save, because data parameter is empty.")
        else:
            # If the data passed into the data parameter is not of type dict,
            if type(data) is not dict:
                # then raise an exception stating that the data was not of type dict.
                raise Exception("Your entry must be in the form of a dictionary.")
            # Otherwise,
            else:
                # insert the animal object with the specified data into the database.
                self.database.animals.insert_one(data)
                return True

# The read() method implements the R in CRUD.
    def read(self, data):
        # If nothing is passed into the data parameter,
        if data is None:
            # then raise an exception stating that the query was left blank.
            raise Exception("Your query was left blank.")
        else:
            # If the data passed into the data parameter is not of type dict,
            if type(data) is not dict:
                # then raise an exception stating that the query was not of type dict.
                raise Exception("Your query must be in the form of a dictionary.")
            # Otherwise,
            else:
                # find data based on the query (turn results of find() function into a list).
                results = list(self.collection.find(data))
                # Print each item in the results list.
                for item in results:
                    print(item)

# The update() method implements the U in CRUD.
    def update(self, data, new_data):
        # If nothing is passed into the data parameter,
        if data is None:
            # then raise an exception stating that the query was left blank.
            raise Exception("Your query was left blank.")
        # Otherwise, if nothing is passed into the new_data parameter,
        elif new_data is None: 
            # then raise an exception stating that no new data was specified for the update.
            raise Exception("You did not specify any new data for the update.")
        else: 
             # If the data passed into the data parameter is not of type dict (dictionary),
            if type(data) is not dict:
                # then raise an exception stating that the query was not of type dict.
                raise Exception("Your query must be in the form of a dictionary.")
            # Otherwise, if the data passed into the new_data parameter is not of tyype dict,
            elif type(new_data) is not dict:
                # then raise an exception stating that the data for the update was not of type dict.
                raise Exception("The data for your update must be in the form of a dictionary.")
            # Othewise,
            else:
                # find data based on the query (turn results of find() function into a list).
                results = list(self.collection.find(data))
                results_length = len(results)
                # If the results list contains less than one result (no results),
                if results_length < 1:
                    # then tell the user that no changes were made.
                    print ("No changes were made to the database.")
                    return
                # Otherwise, if the results list contains exactly one result,
                elif results_length == 1:
                    # then set multi to false.
                    multi = False
                #Otherwise,
                else:
                    # set multi to true.
                    multi = True
                # If multi is set to false (if there is only one result),
                if multi == False:
                    # then use update_one() to update the one result.
                    self.database.animals.update_one(data, {"$set": new_data})
                    # Tell the user how many files were updated.
                    print("One file was modified.")
                # Otherwise (if multi is set to true),
                else:
                    # then use update_many() to opdate the results.
                    self.database.animals.update_many(data, {"$set": new_data})
                    # Tell the user how many files were updated.
                    print(str(results_length) + " files were modified.")
    
# The delete() method implements the D in CRUD.
    def delete(self, data):
        # If nothing is passed into the data parameter,
        if data is None:
            # then raise an exception stating that the query was left blank.
            raise Exception("Your query was left blank.")
        else: 
             # If the data passed into the data parameter is not of type dict (dictionary),
            if type(data) is not dict:
                # then raise an exception stating that the query was not of type dict.
                raise Exception("Your query must be in the form of a dictionary.")
            else:
                # find data based on the query (turn results of find() function into a list).
                results = list(self.collection.find(data))
                results_length = len(results)
                # If the results list contains less than one result (no results),
                if results_length < 1:
                    # then tell the user that no changes were made.
                    print ("No changes were made to the database.")
                    return
                # Otherwise, if the results list contains exactly one result,
                elif results_length == 1:
                    # then set multi to false.
                    multi = False
                #Otherwise,
                else:
                    # set multi to true.
                    multi = True
                # If multi is set to false (if there is only one result),
                if multi == False:
                    # then use delete_one() to update the one result.
                    self.database.animals.delete_one(data)
                    # Tell the user how many files were deleted.
                    print("One file was deleted.")
                # Otherwise (if multi is set to true),
                else:
                    # then use delete_many() to opdate the results.
                    self.database.animals.delete_many(data)
                    # Tell the user how many files were deleted.
                    print(str(results_length) + " files were deleted.")



