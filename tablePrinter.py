#table Printer function
#Takes a list of list of lists of strings and displays them in
#a well organized table with each column right-justified.
#Assumes all inner lists contain the same number of strings.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             


def findMax(listNames):
    for i in range(len(listNames)):
	    current_len=len(listNames[i])
	    maxLen=len(max(listNames,key=len))
	    if current_len == maxLen:
		    return current_len 

def printTable(lists):
    colWidths = [0] * len(lists)
    for j in range(len(lists[0])):
        for i in range(len(lists)):
            colWidths= findMax(lists[i])
            print(lists[i][j].rjust(colWidths) + ' ',end='')
        print('') 

printTable(tableData)



    















