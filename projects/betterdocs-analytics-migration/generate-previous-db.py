import random
import string

def generate():
  total_impressions = 0
  _betterdocs_meta_impression_per_day_uns = ""
  _betterdocs_fellings_uns = ""
  total_entries = 0
  total_happy = 0
  total_normal = 0
  total_sad = 0

  for year in range(22, 9, -1):
    for month in range(12, 0, -1):
      if year == 22 and month > 6:
        continue
      
      for date in range(30, 0, -1):
        
        if month == 2 and date > 28:
          continue
        
        
        total_entries += 1
        impressions = random.randint(1, 100)
        happy = random.randint(1, 80)
        normal = random.randint(1, 80)
        sad = random.randint(1, 80)
        
        
        total_impressions += impressions
        total_happy += happy
        total_normal += normal
        total_sad += sad
        
        if date < 10:
          sdate = "0" + str(date)
        else:
          sdate = str(date)
        
        if month < 10:
          smonth = "0" + str(month)
        else:
          smonth = str(month)
        
        line2 = f's:10:""{sdate}-{smonth}-20{year}"";a:4:\u007bs:11:""impressions"";i:{impressions};s:5:""happy"";i:{happy};s:6:""normal"";i:{normal};s:3:""sad"";i:{sad};\u007d'
        _betterdocs_meta_impression_per_day_uns += line2

  _betterdocs_meta_impression_per_day_uns = f'"a:{total_entries}\u007b{_betterdocs_meta_impression_per_day_uns}\u007d"'

  with open("_betterdocs_meta_impression_per_day.txt", "w") as f:
    f.write(_betterdocs_meta_impression_per_day_uns)

  _betterdocs_fellings_uns = f'"a:3:\u007bs:5:""happy"";i:{total_happy};s:6:""normal"";i:{total_normal};s:3:""sad"";i:{total_sad};\u007d"'

  with open("_betterdocs_feelings.txt", "w") as f:
    f.write(_betterdocs_fellings_uns)

  with open("_betterdocs_meta_views.txt", "w") as f:
    f.write(str(total_impressions))
  
  return total_impressions, _betterdocs_meta_impression_per_day_uns, _betterdocs_fellings_uns



# Generate The DB import file

doc_ids = []
for i in range(5, 15):
  doc_ids.append(i)
for i in range(26, 42):
  doc_ids.append(i)
  
print(doc_ids)
  
with open("_betterdocs_pre_migration_db.csv", "w") as f:
  db = "meta_id,post_id,meta_key,meta_value\n"
  
  content = ""
  line = ""
  meta_id = 1
  total_impressions, _betterdocs_meta_impression_per_day_uns, _betterdocs_fellings_uns = generate()
  
  for id in doc_ids:
    
    
    line = f"{meta_id},{id},_betterdocs_meta_views,{total_impressions}\n"
    meta_id += 1
    
    line += f'{meta_id},{id},_betterdocs_meta_impression_per_day,{_betterdocs_meta_impression_per_day_uns}\n'
    meta_id += 1
    
    line += f'{meta_id},{id},_betterdocs_feelings,{_betterdocs_fellings_uns}\n'
    meta_id += 1
    
    content += line
    
  db += content
  f.write(db)


# For search data
def get_random_string(length):
  # choose from all letter
  letters = string.ascii_letters
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

def string_data_generator():
  
  total_strings = 10000
  result = "option_id,option_name,option_value,autoload\n"
  main_string = ""
  base_string = ""
  
  for i in range(total_strings):
    search_keyword = get_random_string(random.randint(4, 30))
    search_amount = random.randint(1, 30)
    base_string += f's:{len(search_keyword)}:""{search_keyword}"";i:{search_amount};'
  
  mid_string = f'a:{total_strings}:\u007b{base_string}\u007d'
  main_string = f'"s:{len(mid_string)}:""{mid_string}"";"'
  result += f'205,betterdocs_search_data,{main_string},yes\n'
  with open("search_data_previous_db.csv", "w") as f:
    f.write(result)

string_data_generator()


    