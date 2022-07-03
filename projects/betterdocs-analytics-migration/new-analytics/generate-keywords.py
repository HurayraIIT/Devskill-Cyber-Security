import random
import string
from faker import Faker

fake = Faker()

KEYWORD_AMOUNT = 100
SEARCH_LOG_ROWS = 100
FROM_YEAR = 2022
FROM_MONTH = 1
FROM_DATE = 1

# Generate Search Keywords
with open("wp_betterdocs_search_keyword.csv", 'w') as f:
  res = "id,keyword\n"
  for i in range(1, KEYWORD_AMOUNT+1):
    kw = fake.text()
    
    while len(kw) < 5:
      kw = fake.text()
    if len(kw) > 30:
      new_len = random.randint(5, 30)
      kw = kw[:new_len]
    res += f"{i},{kw}{i}\n"
  f.write(res)

with open("wp_betterdocs_search_log.csv", 'w') as f:
  res = f"id,keyword_id,count,not_found_count,created_at\n"
  id = 1
  for year in range(2022, 2018, -1):
    if id > SEARCH_LOG_ROWS:
      break
    for month in range(12, 0, -1):
      if id > SEARCH_LOG_ROWS:
        break
      if year == 2022 and month > 6:
        continue
      for date in range(30, 0, -1):
        if id > SEARCH_LOG_ROWS:
          break
        if month == 2 and date > 28:
          continue
        
        if year == 2022:
          keyword_id = random.randint(1, KEYWORD_AMOUNT)
          count = random.randint(40, 70)
          not_found_count = random.randint(30, 40)
        elif year == 2021:
          keyword_id = random.randint(1, KEYWORD_AMOUNT)
          count = random.randint(30, 50)
          not_found_count = random.randint(20, 30)
        elif year == 2020:
          keyword_id = random.randint(1, KEYWORD_AMOUNT)
          count = random.randint(20, 40)
          not_found_count = random.randint(10, 20)
        
        date_str = ""
        if date < 10:
          date_str = "0" + str(date)
        else:
          date_str = str(date)
        
        month_str = ""
        if month < 10:
          month_str = "0" + str(month)
        else:
          month_str = str(month)
        
        # res += f'{id},{keyword_id},0,{not_found_count},{year}-{month_str}-{date_str}\n'
        val = random.randint(1, 11)
        if val % 2 == 0:
          res += f'{id},{keyword_id},{count},{not_found_count},{year}-{month_str}-{date_str}\n'
        else:
          res += f'{id},{keyword_id},{count},{not_found_count},{year}-{month_str}-{date_str}\n'
        id += 1
    
  f.write(res)

with open("wp_betterdocs_analytics.csv", 'w') as f:
  res = "id,post_id,impressions,unique_visit,happy,sad,normal,created_at\n"
  id = 1
  posts = [11, 12, 13, 14, 15, 16, 17, 18, 41]
  for year in range(2022, 2018, -1):
    if id > SEARCH_LOG_ROWS:
      break
    for month in range(12, 0, -1):
      if id > SEARCH_LOG_ROWS:
        break
      if year == 2022 and month > 6:
        continue
      for date in range(30, 0, -1):
        if id > SEARCH_LOG_ROWS:
          break
        if month == 2 and date > 28:
          continue
        
        x = random.randint(0,len(posts)-1)
        post_id = posts[x]
        
        if year == 2022:
          impressions = random.randint(20, 30)
          unique_visit = random.randint(15, impressions)
          happy = random.randint(9, 14)
          normal = random.randint(7, 10)
          sad = random.randint(4, 7)
        elif year == 2021:
          impressions = random.randint(20, 30)
          unique_visit = random.randint(15, impressions)
          happy = random.randint(7, 12)
          normal = random.randint(5, 8)
          sad = random.randint(2, 5)
        elif year == 2020:
          impressions = random.randint(20, 30)
          unique_visit = random.randint(15, impressions)
          happy = random.randint(5, 10)
          normal = random.randint(3, 6)
          sad = random.randint(0, 3)
        
        if happy == 0:
          happy = '"0"'
        if sad == 0:
          sad = '"0"'
        if normal == 0:
          normal = '"0"'
        
        date_str = ""
        if date < 10:
          date_str = "0" + str(date)
        else:
          date_str = str(date)
        
        month_str = ""
        if month < 10:
          month_str = "0" + str(month)
        else:
          month_str = str(month)
        
        created_at = f"{year}-{month_str}-{date_str}"
        
        res += f'{id},{post_id},{impressions},{unique_visit},{happy},{sad},{normal},{created_at}\n'
        # val = random.randint(1, 11)
        # if val % 2 == 0:
        #   res += f'{id},{keyword_id},0,{not_found_count},{year}-{month_str}-{date_str}\n'
        # else:
        #   res += f'{id},{keyword_id},{count},0,{year}-{month_str}-{date_str}\n'
        id += 1
  
  f.write(res)
