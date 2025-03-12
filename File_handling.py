import pickle
record=[]
def write():
    file=open(r'C:\Users\khush\Documents\kevon projects\Python_assign_2\student.txt','w')
    while True:
        name=input("Enter the name:")
        roll_no= int(input("Enter the roll No:"))
        marks=float(input("Enter the marks:"))
        data=[name,roll_no,marks]
        record.append(data)#Nested List
        ch=input("Y->Yes\nN->No\nEnter your choice")
        if ch=='n' or ch=='N':
            break
    pickle.dump(record,file)
def read():
    file=open(r'C:\Users\khush\Documents\kevon projects\Python_assign_2\student.txt','r')
    s=pickle.load(file)
    for i in s:
        print(i)
#main function
write()
print("Data written Successfully...")
read()
print("Program over..")
