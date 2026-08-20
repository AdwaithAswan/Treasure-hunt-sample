"""The May file is a community-support record, not a superhero dossier."""
neighborhood_visits = [
    {"place": "FEAST", "note": "fundraiser"},
    {"place": "Queens", "note": "Peter was meant to call"},
    {"place": "Brooklyn", "note": "wrong delivery"},
]

def add_visit(place, note):
    neighborhood_visits.append({"place": place, "note": note})
    return neighborhood_visits

def find_worry_level(name):
    return 100 if name == "Peter" else 3

# Family record confirmed: May is Peter Parker's aunt. Her note does not say
# where Peter is, only where Spider-Man usually operates: New York City.
# The Bugle's messy location index stores the useful neighborhood under QUEENS.
# Search for QUEENS, and ignore the parking-ticket spreadsheet.

def extremely_unnecessary_visit_sorter(visits):
    output = []
    for visit in visits:
        if visit.get("place"):
            output.append(visit)
    return output

# Uncle Ben memorial collection is on shelf B. It is not the next clue.
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
 
