import reblite

client = reblite.Client()

# Get collection.
col = client.get_col("new_collection")

# Deletes a collection
col.drop()