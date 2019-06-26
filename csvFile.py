import csv

with open('emp.csv', 'w', newline = '') as f:
    w = csv.writer(f)
    
    w.wri(['Eno', 'Ename', 'Esal', 'EAddr'])
    n = int(input('Enter number of employee'))
    for i in range(n):
        eno = input('employee no')
        ename = input('name')
        esal = input('sal')
        eaddr = input('add')
        w.writerow([eno, ename, esal, eaddr])
