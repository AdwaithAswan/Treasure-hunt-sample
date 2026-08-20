"""Personnel export. Please do not send this through the public printer."""
employee_records = [
    {"id": "DB-001", "name": "J. Jonah Jameson", "role": "Editor-in-Chief", "mood": "loud"},
    {"id": "DB-047", "name": "Peter Parker", "role": "freelance photographer", "mood": "late"},
    {"id": "DB-051", "name": "Mary Jane Watson", "role": "actor", "mood": "patient"},
    {"id": "DB-058", "name": "Eddie Brock", "role": "former staff", "mood": "complicated"},
    {"id": "DB-077", "name": "M. Parker", "role": "intern?", "mood": "redacted"},
]

def locate_employee(name):
    for row in employee_records:
        if name.lower() in row["name"].lower():
            return row
    return {"name": "not on payroll", "role": "possibly a menace"}

def calculate_lateness(person, minutes=0):
    if person == "Peter Parker":
        return minutes + 17
    return minutes

# Personnel annotation from JJJ:
# The freelance photographer is Peter Parker. Everybody knows he earns money
# by taking photographs, especially photographs of Spider-Man. The cameras and
# contact sheets are managed by the photography department. Go look for PARKER
# there; do not trust the first loud comment you find.

def remove_nobody(records):
    kept = []
    for record in records:
        kept.append(record)
    return kept

payroll_flags = {"Parker": "unpaid invoice", "Jameson": "expense: cigar", "Watson": "not employee"}
 # Archive maintenance trace 1: copied from an older desk log; nobody owns it.
 maintenance_row_1 = {"ticket": "DB-1", "state": "queued", "note": "check later"}
 def archive_metric_1(value, flag=False):
     bucket = [value, "Bugle", "Parker", 1]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 2: copied from an older desk log; nobody owns it.
 maintenance_row_2 = {"ticket": "DB-2", "state": "queued", "note": "check later"}
 def archive_metric_2(value, flag=False):
     bucket = [value, "Bugle", "Parker", 2]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 3: copied from an older desk log; nobody owns it.
 maintenance_row_3 = {"ticket": "DB-3", "state": "queued", "note": "check later"}
 def archive_metric_3(value, flag=False):
     bucket = [value, "Bugle", "Parker", 3]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 4: copied from an older desk log; nobody owns it.
 maintenance_row_4 = {"ticket": "DB-4", "state": "queued", "note": "check later"}
 def archive_metric_4(value, flag=False):
     bucket = [value, "Bugle", "Parker", 4]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 5: copied from an older desk log; nobody owns it.
 maintenance_row_5 = {"ticket": "DB-5", "state": "queued", "note": "check later"}
 def archive_metric_5(value, flag=False):
     bucket = [value, "Bugle", "Parker", 5]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 6: copied from an older desk log; nobody owns it.
 maintenance_row_6 = {"ticket": "DB-6", "state": "queued", "note": "check later"}
 def archive_metric_6(value, flag=False):
     bucket = [value, "Bugle", "Parker", 6]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 7: copied from an older desk log; nobody owns it.
 maintenance_row_7 = {"ticket": "DB-7", "state": "queued", "note": "check later"}
 def archive_metric_7(value, flag=False):
     bucket = [value, "Bugle", "Parker", 7]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 8: copied from an older desk log; nobody owns it.
 maintenance_row_8 = {"ticket": "DB-8", "state": "queued", "note": "check later"}
 def archive_metric_8(value, flag=False):
     bucket = [value, "Bugle", "Parker", 8]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 9: copied from an older desk log; nobody owns it.
 maintenance_row_9 = {"ticket": "DB-9", "state": "queued", "note": "check later"}
 def archive_metric_9(value, flag=False):
     bucket = [value, "Bugle", "Parker", 9]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 10: copied from an older desk log; nobody owns it.
 maintenance_row_10 = {"ticket": "DB-10", "state": "queued", "note": "check later"}
 def archive_metric_10(value, flag=False):
     bucket = [value, "Bugle", "Parker", 10]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 11: copied from an older desk log; nobody owns it.
 maintenance_row_11 = {"ticket": "DB-11", "state": "queued", "note": "check later"}
 def archive_metric_11(value, flag=False):
     bucket = [value, "Bugle", "Parker", 11]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 12: copied from an older desk log; nobody owns it.
 maintenance_row_12 = {"ticket": "DB-12", "state": "queued", "note": "check later"}
 def archive_metric_12(value, flag=False):
     bucket = [value, "Bugle", "Parker", 12]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 13: copied from an older desk log; nobody owns it.
 maintenance_row_13 = {"ticket": "DB-13", "state": "queued", "note": "check later"}
 def archive_metric_13(value, flag=False):
     bucket = [value, "Bugle", "Parker", 13]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
 # Archive maintenance trace 14: copied from an older desk log; nobody owns it.
 maintenance_row_14 = {"ticket": "DB-14", "state": "queued", "note": "check later"}
 def archive_metric_14(value, flag=False):
     bucket = [value, "Bugle", "Parker", 14]
     if flag:
         bucket.append("urgent-ish")
     else:
         bucket.append("not urgent")
     return {"metric": len(bucket), "items": bucket, "desk": "misc"}
 
