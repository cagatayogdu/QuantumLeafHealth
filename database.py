from pymongo import MongoClient
from necessary import mongodbURI, DB_NAME

class AtlasClient ():
   def __init__ (self):
       self.mongodb_client = MongoClient(mongodbURI)
       self.database = self.mongodb_client[DB_NAME]
       print (f"[SYSTEM] Veritabanına ile bağlantı sağlandı.")

   def ping (self):
       self.mongodb_client.admin.command('ping')

   def get_collection (self, collection_name):
       collection = self.database[collection_name]
       return collection
   
   def insert(self, collection_name, data):
        collection = self.database[collection_name]
        if isinstance(data, list):
            result = collection.insert_many(data)
            return result.inserted_ids
        else:
            result = collection.insert_one(data)
            return result.inserted_id
        
   def get_treatment_by_name(self, collection_name, name_value):
        collection = self.get_collection(collection_name)
        if collection is not None:  # Bu şekilde kontrol yapın
            try:
                result = collection.find_one({"name": name_value})
                if result:
                    return result.get("tedavi"), result.get("ilac"), result.get("oneri")
                else:
                    print(f"No record found with name: {name_value}")
                    return None, None, None
            except Exception as e:
                print(f"Error fetching data from {collection_name}: {e}")
        return None, None, None

   
if __name__ == "__main__":
    atlas_client = AtlasClient()

    atlas_client.ping()
    
    treatment, ilac, oneri = atlas_client.get_treatment_by_name("Hastalik", "apple_black_rot")
    if treatment:
        print(f"Tedavi: {treatment}, Ilac: {ilac}, Oneri: {oneri}")