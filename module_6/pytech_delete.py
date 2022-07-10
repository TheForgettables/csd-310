MongoDB: find()
docs = db.pytech.find({"student_id"})

MongoDB: insert_one(john)
john = {
    "first_name" : "john"
    "last_name" : "Doe"
    'studnet_id" : "1010"
}

MongoDB: find_one(1010)
docs = db.pytech.find_one({"student_id": "1010"})

MongoDB: delete_one(1010)
docs = db.pytech.delete_one({"student_id" : "1010"})
