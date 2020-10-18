import reblite

client = reblite.Client()

# Get collection.
col = client.get_col("new_collection")

# returns all the documents in a collection
data = col.find_all()

# create a sort instance
sort = reblite.Sort(data)

# sorts the documents by the "_id" key in ascending order
sort.by_asc("_id")

# sorts the documents by the "_id" key in descending order
sort.by_desc("_id")