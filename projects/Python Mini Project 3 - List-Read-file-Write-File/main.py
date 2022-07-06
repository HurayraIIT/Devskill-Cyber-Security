# Abu Hurayra
with open("friends.txt", 'r') as f:
  names = f.read().split()
  names_modified = ""
  for name in names:
    names_modified += name + "@gmail.com\n"

with open("friends_modified.txt", "w") as f:
  f.write(names_modified)

"""
Contents of friends.txt:

takibul reduan mahin
rizu shaon

Contents of friends_modified.txt:

takibul@gmail.com
reduan@gmail.com
mahin@gmail.com
rizu@gmail.com
shaon@gmail.com
"""