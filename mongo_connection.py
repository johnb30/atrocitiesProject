def add_entry(database, text, url, date, website):
    collection = database[website]
    toInsert = {"url" : url, 
                "source" : website, 
                "date" : date, 
                "content" : text}
    if collection.find_one({"url" : url}):
        pass
    else:
        object_id = collection.insert(toInsert)
