MongoDB: update_one (thorin_oakenshield)
result = db.pytech.update_one(("student_id" : 1007)), ("$set": {"last_name": "Oakenshield_II"})

MongoDB: find()
docs = docs = db.pytech.find({"student_id"})

MongoDB: find_one(student_id)
doc = db.pytech.find_one({"student_id": "1007"})
