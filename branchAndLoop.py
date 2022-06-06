odd_list = [[1,2],["Hello", "Mother", "Hello", "Father"],[1,2,3,4,5,6],[1,[1,2]], "Dog"]

# 1. Loop through each entry in odd_list and print it out you should get five items

for item in odd_list:
  print(item)

# 2. Loop through each entry in odd_list, print it out, count each item as you go and use an else to print out the count


count=0
for item in odd_list:
  count += 1
  print(item)
else:
  print(count)

# 3. You can check to see if something is a list using
# if isinstance(x, list):   
# use this and if an item is a list print out all the items in the list individually rather than just printing the list

for item in odd_list:
  if isinstance(item, list):       
    for item2 in item:
      print(item2)
  else:
    print(item)
