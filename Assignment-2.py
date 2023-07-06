# 1. Sum of all even numbers in a given List

myList1 = input("Enter a list of numbers separated by spaces (Even no.): ")
myList1 = [int(x) for x in myList1.split()]

print("\nGiven list to find even sum is: ", myList1)

sum = 0
for i in myList1:
    if (i % 2 == 0):
        sum +=i
print("Sum of all \"Even\" numbers in given list: ", sum, "\n")



# 2. Count number of occurrence of each element in a List

myList2 = input("Enter a list of numbers separated by spaces (Occurrence of each element): ")
myList2 = [int(x) for x in myList2.split()]

print("\nGiven list to find occurrence of each element is: ", myList2)

count = {}
for i in myList2:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print("No. of occurrence of each element in a list is as: ", count, "\n")



# 3. Check if a tuple contains only Unique elements

myList3 = input("Enter a tuple of numbers separated by spaces (uniqueness of element): ")
myList3 = [int(x) for x in myList3.split()]

myTuple = tuple(myList3)

print("Tuple is: ", myTuple)

def unique(myTuple):
    if len(myTuple) == len(set(myTuple)):
        return True
    else:
        return False
if_unique = unique(myTuple)

print("If the tuple contains unique elements ? ", if_unique)




# 4. Removing Duplicates from the list using a Set

myList4 = input("Enter a list of no's separated by spaces (Remove duplicate): ")

myList4 = [int(x) for x in myList4.split()]

print("\nList which may contain duplicates: ", myList4)

mySet = set(myList4)
newList = list(mySet)

print("New List with no duplicates: ",newList, "\n")

