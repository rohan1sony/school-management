from datetime import date
import mysql.connector as ms,pickle,os,sys,csv
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle as rect
con=ms.connect(host='localhost',user='root',passwd='rohan')
print('Successfully connected')
cu=con.cursor()
cu.execute('Create database if not exists sch')
con.commit()
cu.execute('use sch')
con.commit()
cu.execute("create table if not exists cd (CLASS varchar(3) primary key,CLSTHR int(3),CHEM int(3),ENG int(3),PHY int(3),MATH int(3),CS int(3))")
con.commit()
cu.execute("create table if not exists st (ID int(3) primary key,NAME varchar(20),FATHER varchar(15),MOTHER varchar(15),CLASS int(2),DIVI char(1),DOB date,PASS varchar(10),ENG int(2),CHEM int(2),PHY int(2),MATH int(2),CS int(2))")
con.commit()

def loginpr():
    x=input('Enter user id')
    xx=input('Enter your password')
    fh=open('pr.csv','r',newline='')
    wo=csv.reader(fh)
    for i in wo:
        if i[0]==x and i[-1]==xx:
            print('Login Successsful\n','\tWelcome Mr.',i[1].upper())
            return 0
    print('Invalid Credentials')
    return 1
def loginst():
    k=int(input('Enter id'))
    k=mysqlidcheck(k)
    kl=input('Enter password')
    cu.execute('select * from st where id=%s'%(k,))
    global i
    i=cu.fetchone()
    #if i[0]==k and i[-6]==kl:
    print('Login Successsful\n','\tWelcome Mr.',i[1].upper())
    return 0
    print('Invalid Credentials')
    return 1
def logintr(xy):
    x=int(input('Enter your id'))
    x=find2(xy,x)
    k=input('Enter password')
    while l['id']==x and l['pass']==k:
        print('Login Successsful\n\tWelcome Mr.',l['name'].upper())
        return 0
    print('Invalid Credentials')
    return 1
def genpr():
    if os.path.exists('pr.csv'):
        fh=open('pr.csv','r')
        wo=csv.reader(fh)
        for i in wo:
            pass
        return int(i[0])+1
    else:
        return 101
def genst(x):
    cu.execute('select id from %s'%(x,))
    k=cu.fetchall()
    j=100
    for i in k:
        for j in i:
            pass
    return j+1
def gente():
    if os.path.exists('te.dat'):
        fh=open('te.dat','rb')
        try:
            while True:
                l=pickle.load(fh)
        except EOFError:
            fh.close()
            return l['id']+1
    else:
        return 101
def disst():
    n=int(input('Enter id'))
    n=mysqlidcheck(n)
    cu.execute('select * from st where id="%s"'%(n,))
    f=cu.fetchone()
    print(f)
def discls():
    k=int(input('Enter the class'))
    k=find1(k,1,12)
    cu.execute('select * from st where class=%s'%(k,))
    f=cu.fetchall()
    for i in f:
        print(i)
def disdiv():
    k,kl=find6()
    cu.execute('select * from st where class=%s and divi="%s"'%(k,kl))
    f=cu.fetchall()
    for i in f:
        print(i)
def pas():
    x=input("Enter password:")
    xx=input("Confirm password:")
    while x!=xx:
        print('mismatching password')
        x=input("Enter password:")
        xx=input("Confirm password:")
    return x
def find1(x,y,z):
    while x<y or x>z:
        print('Invalid choice (',y,'-',z,')')
        x=int(input('Enter your choice'))
    return x
def find6():
    con=1
    while con==1:
        x=int(input('Enter the class'))
        x=find1(x,1,12)
        y=input('Enter the division').upper()
        cu.execute('select class from cd')
        f=cu.fetchall()
        for i in f:
            if str(x)+y in i:
                return x,y
        print('INVALID Class or Division')
def report(k):
    def find13():
        m1=str(i[4])+i[5]
        cu.execute('select * from cd where class="%s"'%(m1,))
        j=cu.fetchone()
        f1=open('te.dat','rb')
        try:
            while True:
                jk=pickle.load(f1)
                if jk['id']==j[1]:
                    return jk['name']
        except EOFError:
            f1.close()        
    def find14(z):
        mz=0
        cu.execute('select max(%s) from st where class=%s and divi="%s"'%(z,i[4],i[5]))
        f=cu.fetchone()
        return f[0]
    cu.execute('select * from st where id=%s'%(k,))
    i=cu.fetchone()
    x=sum((i[-1],i[-2]+i[-3]+i[-4]+i[-5]))
    if x>200:
        grade='A1'
    elif x>175:
        grade='A2'
    elif x>150:
        grade='B1'
    elif x>125:
        grade='B2'
    else:
        grade='C '
    students = [
    {
        "Name": i[1],
        "Class": i[4],
        "Division":i[5],
        "Roll No": i[0],
        "DOB":i[6],
        "Subjects": {},
        "TopMarks":{},
        'PreviousMarks':{},
        "Grades": {"A": 0, "B": 0,"C": 0, "D": 0,"F": 0}
    }]
    st22={"Father":i[2],
        "Mother":i[3],
        "Class_ Teacher":find13(),}
    for j in dept1:
           students[0]['Subjects'][dept1[j]]=i[-6+j]
           print(students[0]['Subjects'][dept1[j]])
           students[0]['TopMarks'][dept1[j]]=find14(dept[j])
           print(students[0]['TopMarks'][dept1[j]])
           students[0]['PreviousMarks'][dept1[j]]=i[-6+j]
           if i[-6+j]>45:
               students[0]['Grades']['A']+=1
           elif i[-6+j]>40:
               students[0]['Grades']['B']+=1
           elif i[-6+j]>35:
               students[0]['Grades']['C']+=1
           elif i[-6+j]>30:
               students[0]['Grades']['D']+=1
           else:
                students[0]['Grades']['F']+=1
    with PdfPages("Student_Report_Cards.pdf") as pdf:
        for student_info in students:
            fig = plt.figure(figsize=(15, 12))
            border=rect((.02,.02),.96,.96,fill=False,linewidth=4,edgecolor='darkblue')
            fig.add_artist(border)
            border=rect((.03,.03),.94,.94,fill=False,linewidth=2,edgecolor='darkblue')
            fig.add_artist(border)
            plt.subplots_adjust()
            fig.patch.set_facecolor('#BDF8E6')
            
            fig.suptitle(f"Report Card: {student_info['Name']}", fontsize=20, weight='bold')

            subjects = list(student_info["Subjects"].keys())
            curr_scores = list(student_info["Subjects"].values())
            print([student_info["TopMarks"]])
            top_scores = [student_info["TopMarks"][sub] for sub in subjects]
            print(top_scores)
            prev_scores = [student_info["PreviousMarks"][sub] for sub in subjects]

            # 1. Bar Chart: Student vs Topper
            plt.subplot(4, 2, 3)
            #plt.text(35,.1,"ANALYSIS",fontsize=17)
            x = np.arange(len(subjects))
            width = 0.35
            plt.bar(x - width/2, curr_scores, width, label='Student', color='skyblue')
            plt.bar(x + width/2, top_scores, width, label='Top in Class', color='orange')
            plt.xticks(x, subjects)
            plt.title("Marks Comparison",fontsize=14,pad=10)
            plt.ylabel("Marks")
            plt.ylim(0, 60)
            plt.legend()

            # 2. Pie Chart: Grade Distribution
            plt.subplot(4, 2, 6)
            grades = list(student_info["Grades"].keys())
            grade_counts = list(student_info["Grades"].values())
            plt.pie(grade_counts, labels=grades, autopct='%1.1f%%', startangle=90,radius=2, colors=['gold', 'lightgreen','silver','blue','red'])
            plt.title("Grade Distribution",x=.5,y=.4,color='darkblue' )


            # 4. Line Plot: Current vs Previous Exam
            plt.subplot(4, 2, 5)
            plt.plot(subjects, prev_scores, marker='o', label="Previous Exam", color='gray', linestyle='--')
            plt.plot(subjects, curr_scores, marker='o', label="Current Exam", color='blue')
            plt.title("Performance Over Time",c='red')
            plt.ylabel("Marks")
            plt.ylim(0, 110)
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.legend()

            # 5. Table: Current Marks vs Topper
            plt.subplot(4, 2, 4)
            plt.axis('off')
            table_data = [[sub, student_info["Subjects"][sub], student_info["TopMarks"][sub], student_info["PreviousMarks"][sub]] for sub in subjects]
            print(table_data)
            table = plt.table(cellText=table_data,
                              colLabels=["Subject", "Student Marks", "Top Marks","Previous Marks"],
                              loc='center',
                              cellLoc='center',
                              colLoc='center')
            table.scale(1, 2)
            for (row,col) , cell in table.get_celld().items():
                if row==0:
                    cell.set_facecolor('darkblue')
                    cell.set_text_props(weight='bold',color='#add8e6')
                else:
                    if row%2==0:
                        cell.set_facecolor('#B0f7fa')
                    else:
                        cell.set_facecolor('#ffffff')
                    cell.set_text_props(color='black')
                cell.set_edgecolor('gray')
            table.auto_set_font_size(False)
            table.set_fontsize(12)
            plt.title("Mark Sheet", fontsize=14, pad=10)



            # 7. Student Info
            
            plt.subplot(4, 1, 1)
            plt.axis('off')
            info_text = "\n".join([f"{key}: {value}" for key, value in student_info.items()
                                  if key not in ["Subjects", "TopMarks", "PreviousMarks", "Grades"]])
            st21 = "\n".join([f"{key}: {value}" for key, value in st22.items()
                                  if key not in ["Subjects", "TopMarks", "PreviousMarks", "Grades"]])
            plt.title("Student Details", fontsize=14,color='blue')
            plt.text(.36,1.7,"Cert-Ed Academia",fontsize=17)
            plt.text(.37,1.55," Kothamangalam",fontsize=17)
            plt.text(.38,1.47,"Come, let's learn together!",fontsize=10)
            plt.text(.4,1.35,"REPORT CARD",fontsize=17)
            plt.text(.41,1.2,"2024-2025",fontsize=17)
            plt.text(0.1, 0.3, info_text, fontsize=13)
            plt.text(0.7, 0.4, st21, fontsize=13)
            plt.title("Student Details",x=.45,y=1, fontsize=14,color='blue')
            plt.suptitle("ANALYSIS",x=.5,y=.63,fontsize=17)
            plt.tight_layout(rect=[.02,0, .96, 0.95])
            pdf.savefig(fig) # Save the current figure to PDF
            plt.close(fig)

    print("PDF report saved as 'Student_Report_Cards.pdf'")

           
def report1(k):
    
    def find13():
        m1=str(i[4])+i[5]
        cu.execute('select * from cd where class="%s"'%(m1,))
        j=cu.fetchone()
        f1=open('te.dat','rb')
        try:
            while True:
                jk=pickle.load(f1)
                if jk['id']==j[1]:
                    return jk['name']
        except EOFError:
            f1.close()        
    def find14(z):
        mz=0
        cu.execute('select max(%s) from st where class=%s and divi="%s"'%(z,i[4],i[5]))
        f=cu.fetchone()
        return f[0]
    cu.execute('select * from st where id=%s'%(k,))
    i=cu.fetchone()
    x=sum((i[-1],i[-2]+i[-3]+i[-4]+i[-5]))
    if x>200:
        grade='A1'
    elif x>175:
        grade='A2'
    elif x>150:
        grade='B1'
    elif x>125:
        grade='B2'
    else:
        grade='C '
    print(' '*48,"St.Antony's Public School")
    print(' '*48,"  Anakkal , Kanjirapally")
    print(' '*48,"CBSE AFFLICATION NO:930037")
    print("\n",' '*55,"REPORT CARD")
    print(' '*57,'2024-2025')
    print('\t\t\t\tNAME    :',i[1])
    print('\t\t\t\tCLASS   :',i[4])
    print('\t\t\t\tDIVISION:',i[5])
    print('\t\t\t\tROLL NO :',25,'\t'*4,'FATHER        :',i[2].title())
    print('\t\t\t\tADM. NO :',i[0],'\t'*4,'MOTHER        :',i[3].title())
    print('\t\t\t\tDOB     :',i[6],'\t'*3,'CLASS TEACHER :',find13())
    print('\t'*5,'_'*48,)
    print('\t'*5,'| SUBJECTS',' |','MAX.','\t','|SCORED  | TOP  |')
    print('\t'*5,'-'*46,'-|',sep='-')
    for j in dept1:
        print('\t'*5,'|',dept1[j],'\t|',50,'\t |',i[-6+j],'\t  |',find14(dept[j]),'  |')  
    print('\t'*5,'-'*46,'-|',sep='-')
    print('\t'*5,'| TOTAL','\t'*2,'|',250,'\t |',x,' GRADE:',grade,'|')
    print('\t'*5,'-'*46,'-|',sep='-')
    print('\t'*5,'Place:','Anakkal')
    print('\t'*5,'Date :',date.today())
dept={1: 'ENG', 2: 'CHEM', 3: 'PHY', 4: 'MATH', 5: 'CS'}
dept1={1: 'ENGLISH    ', 2: 'CHEMISTRY  ', 3: 'PHYSICS    ', 4: 'MATHEMATICS', 5: 'COMPUTERSC '}
report(101)
def find4():
    print('1.English\n2.Chemistry\n3.Physics\n4.Mathematics\n5.Computer Science')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,5)
    return dept1[ch]
def find40():
    print('1.English\n2.Chemistry\n3.Physics\n4.Mathematics\n5.Computer Science')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,5)
    return dept[ch]
def find7():
    y=int(input('Enter date of birth'))
    y=find1(y,1,31)
    w=int(input('Enter month number of birth'))
    w=find1(w,1,12)
    z=int(input('Enter your year of birth'))
    while len(str(z))!=4:
        z=int(input('Enter your year of birth'))
    return date(z,w,y)
def mysqlidcheck(x):
    an=1
    while an==1:
        cu.execute('select id from st')
        f=cu.fetchall()
        for i in f:
            if x in i:
                return x
        print('invalid ID')
        x=int(input('Enter ID'))
def find2(y,x):
    a=1
    while a==1:
        f1=open(y,'rb')
        found=False
        try:
            while True:
                global l
                l=pickle.load(f1)
                if l['id']==x:
                    found=True
                    f1.close()
                    return x
        except EOFError:
            if found==False:
                print('INVALID id')
                x=int(input('Enter Your id'))
                a=1
        f1.close()
def findf(cn):
    cu.execute("update st set %s='%s' where id=%s"%(cn,n,x))
    con.commit()
    print('Edited Successfully')
ans='y'
while ans=='y' or ans=='Y':
    print('\n','\t'*4,'LOGIN INTERFACE\n1.Principal\n2.Teacher\n3.Student\n4.Admin')
    ch=int(input('Enter your choice:'))
    ch=find1(ch,1,4)
    if ch==1:
        print('\n\t\t\t\tPRINCIPAL LOGIN')
        m=loginpr()
        while m==1:
            m=loginpr()
        while m==0:
            print('1.View teacher\n2.View student\n3.Data control\n4.Logout')
            ch=int(input('Enter your choice: '))
            ch=find1(ch,1,4)
            if ch==1:
                ms=0
                while ms==0:
                    print('1.View Teacher\n2.View Department\n3.View teachers\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice: '))
                    ch=find1(ch,1,5)
                    if ch in[1,2,3]:
                        if ch==1:
                            x=int(input('Enter id:'))
                        elif ch==2:
                            n=find4()
                        fh=open('te.dat','rb')
                        try:
                            while True:
                                st=pickle.load(fh)
                                if ch==1 and st['id']==x:
                                    print(st)
                                elif ch==2 and st['dept']==n:
                                    print(st)
                                elif ch==3:
                                    print(st)
                        except EOFError:
                            fh.close()
                    else:
                        if ch==4:
                            ms=1
                        elif ch==5:
                            ms=1
                            m=1
            elif ch==2:
                ms=0
                while ms==0:
                    print('1.View Division\n2.View Class\n3.View Student\n4.View All Student\n5.Back\n6.Logout')
                    ch=int(input('Enter your choice:'))
                    ch=find1(ch,1,6)
                    if ch==1:
                        disdiv()
                    elif ch==2:
                        discls()
                    elif ch==3:
                        disst()
                    elif ch==4:
                        cu.execute('select * from st')
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==5:
                        ms=1
                    else:
                        ms=1
                        m=1
            elif ch==3:
                ms=0
                while ms==0:
                    print('\n1.Assign teacher to a class\n2.Assign Remove teacher from a class\n3.Assign class teacher\n4.Remove class teacher from a class')
                    print('5.Add a Class\n6.Remove a class\n7.Back\n8.Logout')
                    ch=int(input('Enter your choice: '))
                    ch=find1(ch,1,8)
                    if ch in [1,2,3,4]:
                        k=int(input('Enter teacher ID: '))
                        x,y=find6()
                        kl=str(x)+y
                    if ch in [1,2]:
                        x=find40()
                    if ch==1:
                        cu.execute("update cd set %s=%s where Class='%s'"%(x,k,kl))
                        con.commit()
                    elif ch==2:
                        cu.execute("update cd set %s=null where Class='%s'"%(x,kl))
                        con.commit()
                    elif ch==3:
                        cu.execute("update cd set clsthr=%s where Class='%s'"%(k,kl))
                        con.commit()
                    elif ch==4:
                        cu.execute("update  set clsthr=null where Class='%s'"%(kl,))
                        con.commit()
                    elif ch==5:
                        x=int(input('Enter the class: '))
                        x=find1(x,1,12)
                        y=input('Enter the division: ').upper()
                        s="insert into cd values('%s',%s,%s,%s,%s,%s,%s)"%(str(x)+y,'null','null','null','null','null','null')
                        cu.execute(s)
                        con.commit()
                    elif ch==6:
                        x,y=find6()
                        cu.execute("Delete from cd where class='%s'"%(str(x)+y,))
                        con.commit()
                    elif ch==7:
                        ms=1
                    else:
                        ms=1
                        m=1     
            else:
                m=1
    elif ch==2:
        print('\n\t\t\t\tTEACHER LOGIN')
        m=logintr('te.dat')
        while m==1:
            m=logintr('te.dat')
        while m==0:
            print('1.View My Class\n2.View Classes\n3.Edit Marks\n4.Edit marks of a full division\n5.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,5)
            if ch==1:
                jj=0
                while jj==0:
                    print('1.View a student\n2.View Marks\n3.Print report card\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        n=int(input('Enter id'))
                        n=mysqlidcheck(n)
                        cu.execute('select * from st where id="%s"'%(n,))
                        f=cu.fetchone()
                        cu.execute('select * from cd where class="%s"'%(str(f[4])+f[5],))
                        f1=cu.fetchone()
                        if f1[1]==l['id']:
                            print('Ad.No','Name  \t','Father','Mother  ','DOB     ','Eng','Chem','Phy','Math','CS',sep=' |  ')
                            print(f[0],f[1],f[2],f[3],str(f[6]),f[-5],f[-4],f[-3],f[-2],f[-1],sep='  |  ') 
                        else:
                            print('Sorry You Have NO Access')
                    elif ch==2:
                        cu.execute('select * from cd where clsthr=%s'%(l['id'],))
                        f1=cu.fetchone()
                        if f1[1]==l['id']:
                            cu.execute('select name,eng,chem,phy,math,cs from st where class=%s and divi="%s"'%(f1[0][0:-1],f1[0][-1]))
                            f=cu.fetchall()
                            print('Name            Eng    Chem    Phy     Math     CS')
                            for i in f:
                                for j in i:
                                    if j==i[0]:
                                        j+=(15-len(j))*' '
                                    print(j,end='\t')
                                print()
                    elif ch==3:
                        ans1='y'
                        while ans1=='y' or ans1=='Y':
                            print('1.Generate report card for 1\n2.Generate for whole class\n3.Back')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,3)
                            if ch==1:
                                n=int(input('Enter id'))
                                n=mysqlidcheck(n)
                                cu.execute('select * from st where id="%s"'%(n,))
                                f=cu.fetchone()
                                cu.execute('select * from cd where class="%s"'%(str(f[4])+f[5],))
                                f1=cu.fetchone()
                                if l['id']==f1[1]:
                                    report(f[0])
                                else:
                                    print('Sorry You Have NO Access')
                            elif ch==2:
                                cu.execute('select * from cd where clsthr=%s'%(l['id'],))
                                f1=cu.fetchone()
                                if f1[1]==l['id']:
                                    cu.execute('select * from st where class=%s and divi="%s"'%(f1[0][0:-1],f1[0][-1]))
                                    f=cu.fetchall()
                                    for i in f:
                                        report(i[0])
                            else:
                                break
                            
                    elif ch==4:
                        jj=1
                    else:
                        jj=1
                        m=1
            elif ch==2:
                print('Enter your Subject')
                k=find40()
                cu.execute('select class from cd where %s=%s'%(k,l['id']))
                f=cu.fetchall()
                d={}
                n=1
                for i in f:
                    d[n]=i[0]
                    print(n,i[0],sep='.')
                    n+=1
                i=int(input('Enter your choice'))
                i=find1(i,1,n)
                i=d[i]
                print('Adm.no Name','\t'*2,k,'mark')
                cu.execute('select id,name,%s from st where class=%s and divi="%s"'%(k,i[0:-1],i[-1]))
                f=cu.fetchall()
                f=list(f)
                for j in f:
                    j=list(j)
                    while len(j[1])<24:
                        j[1]+=' '*(24-len(j[1]))
                    print(j[0],j[1],j[2],sep=' ')
            elif ch==3:
                k=find40()
                if l['dept'][:2]==k or l['dept'][:3]==k or l['dept'][:4]==k or l['dept'][:1]==k[:1]:
                    pass
                else:
                    print('\n       You CANNOT Edit\n')
                    continue
                k1=int(input('Enter id'))
                k2=eval(input('Enter new mark'))
                cu.execute('update st set %s=%s where id=%s'%(k,k2,k1))
                con.commit()
            elif ch==4:
                k=find40()
                if l['dept'][:2]==k or l['dept'][:3]==k or l['dept'][:4]==k or l['dept'][:1]==k[:1]:
                    pass
                else:
                    print('\n       You CANNOT Edit\n')
                    continue
                cu.execute('select class from cd where %s=%s'%(k,l['id']))
                f=cu.fetchall()
                d={}
                n=1
                for i in f:
                    d[n]=i[0]
                    print(n,i[0],sep='.')
                    n+=1
                if d=={}:
                    print('You are not added anywhere')
                    continue
                i=int(input('Enter your choice'))
                i=find1(i,1,n)
                i=d[i]
                cu.execute('select id,name,%s from st where class=%s and divi="%s"'%(k,i[0:-1],i[-1]))
                f=cu.fetchall()
                for i in f:
                    print('Enter "E" to stop the proccess at any moment in quotes')
                    print('Enter marks of',i[1])
                    n=eval(input('Enter new mark'))
                    if n=='E':
                        break
                    cu.execute('update st set %s=%s where id=%s'%(k,n,i[0]))
                    con.commit()
            else:
                m=1                   
    elif ch==3:
        print('\t\t\t\tSTUDENT LOGIN')
        m=loginst()
        while m==1:
            m=loginst()
        oo=i
        while m==0:
            i=oo
            print('1.View my Class and Div\n2.View Report Card\n3.View my Details\n4.View fee details')
            print('5.View class teacher\n6.View Other teachers\n7.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,7)
            if ch==1:
                print('\tClass:',i[4],'\n\tDivision:',i[5])
            elif ch==2:
                report(i[0])
            elif ch==3:
                print('Adm.No   ','Name','\t     Father   Mother')
                print(i[0],'   ',i[1],i[2],'  ',i[3])
            elif ch==4:
                print('paid')
            elif ch==5:
                cu.execute('select * from cd where class="%s"'%(str(i[4])+i[5],))
                k=cu.fetchone()
                fh=open('te.dat','rb')
                print('Name','    phone.no',sep='  \t')
                try:
                    while True:
                        l=pickle.load(fh)
                        if l['id']==k[1]:
                            print(l['name'],l['ph1'],sep='     ')
                except EOFError:
                    fh.close()
            elif ch==6:
                cu.execute('select * from cd where class="%s"'%(str(i[4])+i[5],))
                k=cu.fetchone()
                print(' Name    \tSubject\t\tPhone number')
                for i in [k[-1],k[-2],k[-3],k[-4],k[-5]]:
                    fh=open('te.dat','rb')
                    try:
                        while True:
                            l=pickle.load(fh)
                            if l['id']==i:
                                print(l['name'],'  ',l['dept'],l['ph1'],sep='\t')
                    except EOFError:
                        fh.close()
            else:
                m=1
    else:
        print('\t\t\t\tADMIN LOGIN')
        m=0
        while m==1:
            m=loginpr()
        while m==0:
            print('1.Add\n2.Edit\n3.Display\n4.Delete\n5.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,5)
            if ch==1:
                ms=0
                while ms==0:
                    print('1.Add New Teacher\n2.Add New Student\n3.Add New Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        st={}
                        st['id']=gente()
                        st['name']=input("Enter name:").title()
                        st['dept']=find4()
                        st['dob']=find7()
                        st['address']=input("Enter address:").title()
                        st['dateofjoin']=date.today()
                        st['ph1']=int(input('Enter Phone number'))
                        st['pass']=pas()
                        fh=open('te.dat','ab')
                        pickle.dump(st,fh)
                        fh.close()
                        print('Your id is',st['id'],'\n','Your password is',st['pass'])
                
                    elif ch==2:
                        i=genst('st')
                        n=input("Enter student name").title()
                        f=input("Enter father's name").title()
                        m=input("Enter mother's name").title()
                        c,d=find6()
                        dob=find7()
                        x=pas()
                        s="insert into st values(%s,'%s','%s','%s',%s,'%s','%s','%s',%s,%s,%s,%s,%s)"%(i,n,f,m,c,d,dob,x,0,0,0,0,0)
                        cu.execute(s)
                        con.commit()
                        print('Your id is',i,'\n','Your password is',x)
                    elif ch==3:
                        st=[]
                        st.append(genpr())
                        fh=open('pr.csv','a',newline='')
                        wo=csv.writer(fh)
                        p1=input("is this the first principal?if yes type 1 else 0")
                        if p1==1:
                            st=[]
                            st=['name','date of joining','login_id','password']
                            wo.writerow(st)
                        st.append(input("Enter name:"))
                        st.append(date.today())
                        st.append(pas())
                        print('Your id is',st[0],'\n','Your password is',st[-1])
                        wo.writerow(st)
                        fh.close()
                    elif ch==4:
                        ms=1
                    else:
                        ms=1
                        m=1
            elif ch==2:
                ms=0
                while ms==0:
                    print('1.Edit Student\n2.Edit Teacher\n3.Edit Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        nj=0
                        while nj==0:
                            print('1.Edit Name\n2.Date of birth\n3.Edit Class\n4.Edit Division\n5.Edit Mark')
                            print('6.Edit password\n7.Edit fathers name\n8.Edit mothers name\n9.Back\n10.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,10)
                            if ch in [1,2,3,4,5,6,7,8]:
                                x=int(input('Enter your id'))
                                x=mysqlidcheck(x)
                            if ch==1:
                                n=input('Enter new name').title()
                                findf('name')
                            elif ch==2:
                                n=find7()
                                findf('dob')
                            elif ch==3:
                                n=int(input('Enter new class'))
                                n=find1(n,1,12)
                                findf('class')
                            elif ch==4:
                                n=input('Enter new division').upper()
                                findf('divi')
                            elif ch==5:
                                for i in dept:
                                    n=int(input('Enter Mark of'+ str(dept[i])))
                                    findf(dept[i])
                            elif ch==6:
                                n=pas()
                                findf('pass')
                            elif ch==7:
                                n=input("Enter new name:").title()
                                findf('father')
                            elif ch==8:
                                n=input("Enter new name:").title()
                                findf('mother')
                            elif ch==9:
                                nj=1
                            else:
                                nj=1
                                ms=1
                                m=1
                    elif ch==2:
                        nj=0
                        while nj==0:
                            fh=open('te.dat','rb')
                            fh1=open('teachertemp.dat','ab')
                            print('1.Edit Name\n2.Edit Department')
                            print('3.Date of birth\n4.Edit  Address\n5.phone number\n6.password\n7.Back\n8.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,8)
                            if ch==1:
                                x,y='name',input("Enter Name:").title()
                            elif ch==2:
                                x,y='dept',find4()
                            elif ch==3:
                                x,y='DOB',find7()
                            elif ch==4:
                                x,y='address',input("Enter Address:").title()
                            elif ch==5:
                                x,y='ph1',int(input('Enter new Phone number'))
                            elif ch==6:
                                x,y='pass',pas()
                            elif ch==7:
                                break
                            else:
                                ms,m=1,1
                                break
                            id=int(input("Enter your id:"))
                            id,found=find2('te.dat',id),'false'
                            try:
                                while True:
                                    st=pickle.load(fh)
                                    if st['id']!=id:
                                        pickle.dump(st,fh1)
                                    else:
                                        st[x]=y
                                        found='true'
                                        pickle.dump(st,fh1)
                            except EOFError:
                                if found=='false':
                                    print("Sorry,no such record found'")
                                fh.close()
                            fh1.close()
                            os.remove('te.dat')
                            os.rename('teachertemp.dat','te.dat')
                            print('Edited Successfully')
                    elif ch==3:
                        fh=open('pr.csv','r',newline='')
                        id=int(input("Enter the id:"))
                        print("ENTER WHAT YOU WANT TO EDIT\n1.NAME\n2.PASSWORD")
                        ep=int(input())
                        if ep==1:
                            x=0
                            n=input("ENTER NEW NAME:").title()
                        else:
                            n=input("ENTER NEW PASSWORD")
                            x=3
                        temp=[]
                        st=csv.reader(fh)
                        for i in st:
                            if i[2]!=id:
                                temp.append(i)
                            else:
                                i[x]=n
                                temp.append(i)
                        fh.close()
                        fh=open('pr.csv','w',newline='')
                        wo=csv.writer(fh)
                        wo.writerows(temp)
                        fh.close()
                    elif ch==4:
                        ms=1
                    else:
                        ms=1
                        m=1
            elif ch==3:
                mn=1
                while mn==1:
                    print('1.Display all teachers\n2.Display all students\n3.Display Principal\n4.Display students of a class')
                    print('5.Display students of a division\n6.Display teachers of a department\n7.Display Students having birthday on a date')
                    print('8.View a Student\n9.Print Report Card\n10.Back\n11.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,11)
                    if ch==1:
                        fh=open('te.dat','rb')
                        try:
                            while True:
                                st=pickle.load(fh)
                                print(st)
                        except EOFError:
                            fh.close()
                    elif ch==2:
                        cu.execute('select * from st')
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==3:
                        fh=open('pr.csv','r',newline='')
                        ro=csv.reader(fh)
                        for i in ro:
                            print(i)
                        fh.close()
                    elif ch==4:
                        discls()
                    elif ch==5:
                        disdiv()
                    elif ch==6:
                        n,fh=find4(),open('te.dat','rb')
                        try:
                            while True:
                                st=pickle.load(fh)
                                if st['dept']==n:
                                    print(st)
                        except EOFError:
                            fh.close()
                    elif ch==7:
                        n=find7()
                        cu.execute('select * from st where dob="%s"'%(n,))
                        f=cu.fetchall()
                        for i in f:
                            print('\t'*3,i[1])
                    elif ch==8:
                        disst()
                    elif ch==9:
                        ans1 ='y'
                        while ans1=='y' or ans1=='Y':
                            print('1.Generate report card for 1\n2.Generate for whole class\n3.Back')
                            ch1=int(input('Enter your ch1oice'))
                            ch1=find1(ch1,1,3)
                            if ch1==1:
                                n=int(input('Enter id'))
                                cu.execute('select * from st where id="%s"'%(n,))
                                f=cu.fetchall()
                                for i in f:
                                    report(i[0])
                            elif ch1==2:
                                cu.execute('select * from st')
                                f=cu.fetchall()
                                for i in f:
                                    report(i[0])
                            else:
                                ans1=''
                    elif ch==10:
                        mn=0
                    else:
                        mn,m=0,1
            elif ch==4:
                kl=0
                while kl==0:
                    print('1.Delete Student\n2.Delete Teacher\n3.Delete Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch in [1,2,3]:
                        id=int(input("Enter the id:"))
                    if ch==1:
                        id=mysqlidcheck(id)
                        cu.execute('Delete from st where id=%s'%(id,))
                        con.commit()
                        print('Deleted Successfully')
                    elif ch==2:
                        fh,fh1,found=open('te.dat','rb'),open('teachertemp.dat','ab+'),'false'
                        try:
                            while True:
                                st=pickle.load(fh)
                                if st['id']!=id:
                                    pickle.dump(st,fh1)
                                else:
                                    found='fa'
                                    continue
                        except EOFError:
                            if found=='false':
                                print("Sorry,no such record found'")
                            else:
                                print('Deleted Successfully')
                        fh1.close(),fh.close()
                        #fh.close()
                        os.remove('te.dat')
                        os.rename('teachertemp.dat','te.dat')
                    elif ch==3:
                        fh,temp=open('pr.csv','r',newline=''),[]
                        st,n=csv.reader(fh),1
                        for i in st:
                            if i[0]!=id:
                                n=0
                                temp.append(i)
                        fh.close()
                        fh,wo=open('pr.csv','w',newline=''),csv.writer(fh)   
                        wo.writerows(temp)
                        fh.close()
                        if n==1:
                            print("Sorry,no such record found'")
                        else:
                            print('Deleted Successfully')
                    elif ch==4:
                        kl=1  
                    else:
                        kl,m=1,1
            else:
                m=1
