input_file = open("02.txt","r")
output_file = open("r.txt", "w")

thisKey = ""
thisValue = 0.0

for line in input_file:
  data = line.strip().split('\t')
  store, amount = data

  if store != thisKey:
    if thisKey:
      # output the last key value pair result
      output_file.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
output_file.write(thisKey + '\t' + str(thisValue)+'\n')

input_file.close()
output_file.close()
print("Done")
