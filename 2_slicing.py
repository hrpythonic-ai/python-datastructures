#-----------------------------------------------------
#slicing:slice out substrings,sublists,sutuples using indexes
#-----------------------------------------------------

x='computer'
#________________________________
print(x[0:])#print complete string
print(x[:])#print complete string
print(x[::])#print complete string
print(x[0:len(x)])#print complete string
#________________________________

print(x[1:])#cut first letter of the string and print remaining all.
print(x[2:])#cut first two letters of the string and print remaining all. 
print(x[0:4])#start from first character and print first four characters 0,1,2,3 and notice that 4 is exclusive means not include
print(x[0:6:2])#print first 6 characters and jump of two 0,1,2,3,4,5 means by jump of two values 0,2 and 4 are printed.
#_________________________________

print(x[:1])#print first letter of the string
print(x[:2])#print first two letters of the string
#_________________________________

#negative slicing
print(x[-1:])#print last letter
print(x[-2:])#print last 2 letters
print(x[:-1])#cut last letter and print remaining all
print(x[:-2])#cut last two letters and print remaining all


#remind these 3
print(x[:])#print complete string
print(x[0])#print first letter
print(x[-1])#print last letter
