def add_entry(collection, text, url, date, website):
    toInsert = {"url" : url, 
                "source" : website, 
                "date" : date, 
                "content" : text}
    if collection.find_one({"url" : url}):
        pass
    else:
        object_id = collection.insert(toInsert)
        print object_id
