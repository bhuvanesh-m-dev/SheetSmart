import csv
def write_csv():
    file=open('sheetsmart.csv','a')
    wo=csv.writer(file)
    ans='y'
    while ans.lower()=='y':
        l=[]
        rno=int(input('Enter roll number: '))
        name=input('Enter name: ')
        eng=float(input('Enter English mark: '))
        maths=float(input('Enter Maths mark: '))
        phy=float(input('Enter Physics mark: '))
        che=float(input('Enter Chemistry mark: '))
        cs=float(input('Enter CS mark: '))
        total=eng+maths+phy+che+cs
        average=total/5
        if average >= 90:
            grade = 'A+'
        elif average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        else:
            grade = 'D'
        l=[rno,name,eng,maths,phy,che,cs,grade,average]
        wo.writerow(l)
        file.flush()
        print('Data of the',l[1],'has been written to the storage Sucessfully!!!')
        ans=input('Do you Want to Continue (y/n): ')
    file.close()
def change_csv_cs():
    rno=int(input('Enter the roll number: '))
    cs = float(input('Enter new CS mark: '))
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)    
    cs_found = False    
    for row in data:
        if str(rno)==row[0]:
                row[6] = str(cs)
                total = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6])
                row[8] = str(total / 5)
                average=total/5
                if average >= 90:
                    grade = 'A+'
                elif average >= 80:
                    grade = 'A'
                elif average >= 70:
                    grade = 'B'
                elif average >= 60:
                    grade = 'C'
                else:
                    grade = 'D'
                row[7] = grade
                cs_found = True
    if cs_found:
        with open('sheetsmart.csv', 'w', newline='\n') as file:
            wo = csv.writer(file)
            wo.writerows(data)
        print('CS mark change has been written to the storage successfully!')
    else:
        print('rno not found in the storage.')
def change_csv_eng():
    rno=int(input('Enter the roll number: '))
    eng = float(input('Enter new English mark: '))
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)    
    eng_found = False    
    for row in data:
        if str(rno)==row[0]:
                row[3] = str(eng)
                total = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6])
                row[8] = str(total / 5)
                average=total/5
                if average >= 90:
                    grade = 'A+'
                elif average >= 80:
                    grade = 'A'
                elif average >= 70:
                    grade = 'B'
                elif average >= 60:
                    grade = 'C'
                else:
                    grade = 'D'
                row[7] = grade
                eng_found = True
    if eng_found:
        with open('sheetsmart.csv', 'w', newline='\n') as file:
            wo = csv.writer(file)
            wo.writerows(data)
        print('English mark change has been written to the storage successfully!')
    else:
        print('rno not found in the storage.')
def change_csv_maths():
    rno=int(input('Enter the roll number: '))
    maths = float(input('Enter new Maths mark: '))
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)    
    maths_found = False    
    for row in data:
        if str(rno)==row[0]:
                row[4] = str(maths)
                total = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6])
                row[8] = str(total / 5)
                average=total/5
                if average >= 90:
                    grade = 'A+'
                elif average >= 80:
                    grade = 'A'
                elif average >= 70:
                    grade = 'B'
                elif average >= 60:
                    grade = 'C'
                else:
                    grade = 'D'
                row[7] = grade
                eng_found = True
    if eng_found:
        with open('sheetsmart.csv', 'w', newline='\n') as file:
            wo = csv.writer(file)
            wo.writerows(data)
        print('Maths mark change has been written to the storage successfully!')
    else:
        print('rno not found in the storage.')
def change_csv_phy():
    rno=int(input('Enter the roll number: '))
    phy = float(input('Enter new Physics mark: '))
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)    
    phy_found = False    
    for row in data:
        if str(rno)==row[0]:
                row[5] = str(phy)
                total = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6])
                row[8] = str(total / 5)
                average=total/5
                if average >= 90:
                    grade = 'A+'
                elif average >= 80:
                    grade = 'A'
                elif average >= 70:
                    grade = 'B'
                elif average >= 60:
                    grade = 'C'
                else:
                    grade = 'D'
                row[7] = grade
                eng_found = True
    if eng_found:
        with open('sheetsmart.csv', 'w', newline='\n') as file:
            wo = csv.writer(file)
            wo.writerows(data)
        print('Physics mark change has been written to the storage successfully!')
    else:
        print('rno not found in the storage.')
def change_csv_che():
    rno=int(input('Enter the roll number: '))
    che = float(input('Enter new Chemistry mark: '))
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)    
    che_found = False    
    for row in data:
        if str(rno)==row[0]:
                row[5] = str(che)
                total = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6])
                row[8] = str(total / 5)
                average=total/5
                if average >= 90:
                    grade = 'A+'
                elif average >= 80:
                    grade = 'A'
                elif average >= 70:
                    grade = 'B'
                elif average >= 60:
                    grade = 'C'
                else:
                    grade = 'D'
                row[7] = grade
                che_found = True
    if che_found:
        with open('sheetsmart.csv', 'w', newline='\n') as file:
            wo = csv.writer(file)
            wo.writerows(data)
        print('Chemistry mark change has been written to the storage successfully!')
    else:
        print('rno not found in the storage.')
def read_details_csv():
    rno=int(input('Enter roll number of student: '))
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)
    details_found = False
    for student_details in data:
        if str(rno)==student_details[0]:
            print('Name:',student_details[1])
            print('English mark:',student_details[2])
            print('Maths mark:',student_details[3])
            print('Physics mark:',student_details[4])
            print('Chemistry mark:',student_details[5])
            print('CS mark:',student_details[6])
            print('Grade:',student_details[7])
            print('Average:',student_details[8])
            details_found = True    
    if details_found:
        pass
    else:
        print('roll numer is not there in the storage.')
def remove_csv():
    rno=int(input('Enter the roll number: '))
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)    
    remove_found = False    
    for row in data:
        if str(rno)==row[0]:
                print('''Enter 'y' to confirm the permanent removal of student with roll number''', rno, '''from the storage.\nEnter 'n' to cancel.''')
                conform=input()
                if conform.lower() == 'y':
                    data.remove(row)
                    remove_found = True
                else:
                    pass
    if remove_found:
        with open('sheetsmart.csv', 'w', newline='\n') as file:
            wo = csv.writer(file)
            wo.writerows(data)
        print(rno,'has been removed from the storage successfully!')
    else:
        print('roll number not found in the storage.')
def read_csv():
    with open('sheetsmart.csv', 'r', newline='\n') as file:
        ro = csv.reader(file)
        data = list(ro)
    for row in data:
        print(row)
while True:
    print('SheetSmart.py by BHUVANESH M')
    print('1. For add student details into storage disk')
    print('2. For change mark for particular student')
    print('3. For read student deatils from storage')
    print('4. For remove student from storage')
    print('5. For read entire details of students from storage')
    print('6. For exit')
    ch=int(input('Enter your choice by number: '))
    if ch == 1:
        write_csv()
    elif ch == 2:
        print('21. For change mark in CS')
        print('22. For change mark in English')
        print('23. For change mark in Physics')
        print('24. For change mark in Chemistry')
        print('25. For change mark in Maths')
        ch=int(input('Enter Your choice by number: '))
        if ch == 21:
            change_csv_cs()
        elif ch == 22:
            change_csv_eng()
        elif ch == 23:
            change_csv_phy()
        elif ch == 24:
            change_csv_che()
        elif ch == 25:
            change_csv_maths()
        else:
            print('You Enter a Wrong number!!!')
    elif ch == 3:
        read_details_csv()    
    elif ch == 4:
        remove_csv()
    elif ch == 5:
        read_csv()
    else:
        break
