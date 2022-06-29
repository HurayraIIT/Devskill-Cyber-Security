import random
import string

with open("wp_betterdocs_search_log.csv", 'a') as f:
  for i in range(20, 5001):
    
    keyword_id = random.randint(1, 1000)
    count = random.randint(1, 100)
    not_found_count = random.randint(1, 100)
    month = random.randint(1, 6)
    day = random.randint(1, 27)
    
    val = random.randint(1, 10)
    if val % 2 == 0:
      f.write(f'\n{i},{keyword_id},0,{not_found_count},2022-{month}-{day}')
    else:
      f.write(f'\n{i},{keyword_id},{count},0,2022-{month}-{day}')
  