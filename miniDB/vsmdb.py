from database import Database
# create db with name "smdb"
db = Database('vsmdb', load=False)
# create a single table named "classroom"
db.create_table('classroom', ['building', 'room_number', 'capacity'], [str,str,int])
# insert 5 rows
db.insert('classroom', ['c1', '101', '500'])
db.insert('classroom', ['b1', '514', '10'])
db.insert('classroom', ['papei', '3128', '70'])
db.insert('classroom', ['building2', '100', '30'])
db.insert('classroom', ['building1', '120', '50'])
db.insert('classroom', ['building1', '120', '55'])

