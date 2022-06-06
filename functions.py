def multi_print(word1, print_count=1, tab_count=0):
  outstring = ""
  for b in range(tab_count):
    outstring = outstring +"\t"
  outstring = outstring + word1
  for a in range(print_count):
    print(outstring)

multi_print("Hello",tab_count=3, print_count=5)
