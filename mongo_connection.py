def add_entry(collection, text, title, url, date, website):
    toInsert = {"url": url,
                "title": title,
                "source": website,
                "date": date,
                "content": text}
    if collection.find_one({"url": url}):
        pass
    else:
        object_id = collection.insert(toInsert)
        return object_id
