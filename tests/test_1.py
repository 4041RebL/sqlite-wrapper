import reblite

db = reblite.db("test.sqlite")
db.create_table(name="tab1", col="col1", dtype="TEXT")

table = reblite.Table(db, "tab1")
table.add_col("col2", "TEXT")

table.insert("col1", "something")
table.insert("col2", "another test")

table.update(data=("col1", "test"), check=("col2", "another test"))

data = table.fetch("col2", "another test")

print(data)