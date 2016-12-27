tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)
colNum = len(colWidths)
#Assume each column has equal rows
rowNum = len(tableData[0])

tableClean = ['' for i in range(rowNum)]

#iterates from 0 to 2
for i in range(len(tableData)):
    #iterates from 0 to 3
    for j in range(len(tableData[i])):
        if len(tableData[i][j]) > colWidths[i]:
            colWidths[i] = len(tableData[i][j])
"""
 string columns
 0 to colWidths[0]+1 to colwidths[1] + 1 to colwidths[2]
 - +1 between for spacing
 - Create formatted strings in a list. do one column at a time
"""

#fill formatted table, col by col
for i in range(len(tableData)):
    #and row by row
    for j in range(len(tableData[i])):
        if i == 0:
            tableClean[j] = tableData[i][j].rjust(colWidths[i])
        else:
            stringFormat = tableData[i][j].rjust(colWidths[i])
            tableClean[j] = ' '.join([tableClean[j], stringFormat])

for i in range(len(tableClean)):
    print(tableClean[i])

        
        
        

        
