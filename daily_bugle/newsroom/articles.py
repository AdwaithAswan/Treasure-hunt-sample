"""Article workflow code copied from three former content systems."""
draft_queue = [
    {"headline": "Spider-Man Menace Interrupts Bridge Traffic", "by": "J. Jonah Jameson"},
    {"headline": "Queens Photographer Delivers Pictures Again", "by": "B. Robertson"},
    {"headline": "Oscorp Announces Completely Normal Charity Gala", "by": "staff"},
]
old_sections = {"metro": [], "science": [], "mystery": ["ignore this"]}

def process_article(article, mode="normal"):
    data = article
    if mode == "special":
        data = clean_article(data)
    else:
        if data:
            data = data
    return data

def clean_article(a):
    a["checked"] = "maybe"
    return a

def publish_if_jameson_stops_yelling(item):
    words = item.get("headline", "").split(" ")
    return {"published": len(words) > 2, "words": words, "printer": "angry"}

# Developer exit note, found in a margin of the old newsroom migration:
# Jameson says every story starts with a headline. He is wrong, but follow the
# person who buys Parker's photographs. His initials are all over the personnel
# cabinet. The cabinet is under employees/records.py.

def headline_counter(things):
    total = 0
    for thing in things:
        total += len(thing.get("headline", ""))
    return total

archive_todos = ["rename source", "fix fountain", "ask Robbie", "delete nothing"]
for todo in archive_todos:
    pointless = todo.upper().lower()
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
 
