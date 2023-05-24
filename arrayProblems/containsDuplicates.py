'''
Contains Duplicates (Easy)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

'''
Possible Solution: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)

Simple as it goes, use a main for-loop to iterate through each element,
and have another inner for loop to iterate through each element at i + 1.
This will allow a base parsing of elements in the main 'i' for-loop to go
through the array, and then allow the 'j' for loop to combine all possible
unique combinations, the if statement compares these possibilities and will 
determine if they equal each other, if so it will return true.
If all possibilites fail, this means that there is no duplicate number,
and will return False
'''

def BruteForce(arrayValues):

	for i in range(len(arrayValues)):

		for j in range(i + 1, len(arrayValues)):

			if arrayValues[i] == arrayValues[j]:

				return True
			
	return False


'''
Possible Solution: Sort Array
Time Complexity: O(nlogn)
Space Complexity: O(n)

Sort the array before iteration in the 'i' for loop.
Then, go through the loop and determine if there is two numbers that are the 
same by seeing if the i + 1, which should be the same as i if there is a 
duplicate. If for loop ends, then simply return false.

'''

def SortArray(arrayValues):

	arrayValues = sorted(arrayValues)

	for i in range(len(arrayValues) - 1):

		if (arrayValues[i + 1] == arrayValues[i]):

			return True
		
	return False

'''
Possible Solution: Convert To Set
Time Complexity: O(n)
Space Complexity: O(n)

Convert the array into a set, and then if the lengths of the set and array
are the same, then that must mean there is no duplicate, in which we need to use
a 'not' statement to flip the meaning of the return statement.
'''

def ConvertToSet(arrayValues):

	setValues = set(arrayValues)

	return not len(setValues) == arrayValues



'''
Possible Solution: Hashmap

Time Complexity: O(n)
Space Complexity: O(n)

Implement a dictionary (hash map) to store values in a O(1) step process.
If that value has been encountered again (determined by the if statement),
then it will return true. If for loop ends, we know there is no duplicate and
we must return false.
'''

def UseHashMap(arrayValues):

	d = {}

	for i in arrayValues:

		if i in d:

			return True
		
		d[i] = True
	
	return False
