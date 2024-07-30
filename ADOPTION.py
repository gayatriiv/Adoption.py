# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:31:58 2022

@author: Student
"""

import mysql.connector as sql
myconn=sql.connect(host="localhost",user='root',password="",database="Adoption_Centre")
if myconn.is_connected:
    print("Successfully connected.")
else:
    print("Error connecting to mySQL database.")

cursor=myconn.cursor()
    


print('*****************************--ADOPTION APP --*****************************')
print("")
print("")
print("")
print('1.REGISTER')
print("")
print('2.LOGIN')
print("")
n=int(input("Enter your choice:"))
if n==1:
    name=input('Enter username:')
    passwd=input("Enter password:")
    print()
    st="insert into user_id values('{}','{}')".format(name,passwd)
    cursor=myconn.cursor()
    cursor.execute(st)
    myconn.commit()
    print()
    print('USER created succesfully')
    c=input("Do you want to enter details(y/n)")
elif n==2 :
     name=input('Enter username:')
     print()
     passwd=int(input('Enter Password:'))
     st1="select * from user_id where password='"+str (passwd)+"' and name=  ' " +name+ " ' "
     cursor.execute(st1)
     data=cursor.fetchall()
     for row in data:
         print(row)
elif cursor.fetchone() is  None:
     print()
     print('Invalid username or password')
else:
    print()
          

c=input("Do you want to enter details(y/n)")
while c=='y':
          print('_______________________WELCOME   TO ADOPTION  SERVICE  _______________')        
          print("")
          print("")
          print("1.Parent details")
          print("")
          print('2.Child details')
          print("")
          print("3.Eligibility criteria for prospective parents")
          print("")
          print("4.Funds Donation")
          print("")
          print("5.Exit")
          print("")
          
          choice=int(input('Enter the choice:'))
          
          if choice == 1 :
               a=input('Name:')
               b=int(input('Age:'))
               c=input('Gender:')
               d=int(input('Family income:'))
               e=input('Profession:')
               f=input('Marital status:')
               g=input('Residential address:')
               h=int(input('Phone_no:'))
               i=input('Any disability:')
               
               cursor=myconn.cursor()
               sql_insert="INSERT INTO parent_details values( '{}',{},'{}',{},'{}','{}','{}',{},'{}')".format(a,b,c,d,e,f,g,h,i)
               cursor.execute(sql_insert)
               myconn.commit()
               print ('Data inserted')
               c=input('Do you want to continue (y/n):')
               if c =='y' :
                       continue
               else:
                       break
          elif choice==2:
               a=input("Preferred sex:")
               b=input("Preferred age")
               
               cursor=myconn.cursor()
               sql_insert="SELECT * FROM child_details where sex=a and age=b "
               cursor=myconn.cursor()
               cursor.execute(sql_insert)
               myconn.commit()
               c=input("Do you want to continue(y/n):")
               if c=='y' :
                   continue
               else:
                   break
          elif choice==3:
               print("The prospective parents ")
               print("")
               print("")
               print("1.The prospective adoptive parents shall be physically, mentally and emotionally stable, financially capable and shall not have any life threatening medical condition.")
               print("2.Any prospective adoptive parents, irrespective of his marital status and whether or not he has biological child, can adopt a child subject to following, namely:-")
               print("a.the consent of both the spouses for the adoption shall be required, in case of a married couple;")
               print("b.a single female can adopt a child of any gender;")
               print("c.a single male shall not be eligible to adopt a girl child;")
               print("3.No child shall be given in adoption to a couple unless they have at least two years of stable marital relationship.")
               print("4.The age of prospective adoptive parents, as on the date of registration, shall be counted for deciding the eligibility and the eligibility of prospective adoptive parents to apply for children of different age groups shall be as under:-")
               print("5.In case of couple, the composite age of the prospective adoptive parents shall be counted.")
               print("6.The minimum age difference between the child and either of the prospective adoptive parents shall not be less than twenty-five years.")
               print("7.The age criteria for prospective adoptive parents shall not be applicable in case of relative adoptions and adoption by step-parent.")
               print("8.Couples with three or more children shall not be considered for adoption except in case of special need children as defined in sub-regulation (21) of regulation 2, hard to place children as mentioned in regulation 50 and in case of relative adoption and adoption by step-parent..")
               print("9.Section 12,Hindu Adoption & Maintenance Act,1956 states that the child adopted has the same right as the biological parents.Neither the adoptive parents nor child can overturn a valid adoption.")
               print("10.The prospective parents shall be called for a meeting with the child and the adoption management and the adoption deed to be signed by the prospective parents where in the legal rights of the child are transferred from parents to adoptive parents,Birth certificate will be handed over.")
               
               c=input("Do you want to continue(y/n):")
               if c=='y':
                   continue
               
               else:
                   break
               
          elif choice==4:
               print("Support us by donating a small amount")
               print()
               print("Your contribution has the power to uplift children in dire situations. We’re working towards a nation where its children live a secure life, full of opportunities for growth and development.")
               print()
               print("A small amount can change the life of a child as it can help provide education, nutrition, and protection. With this kind of support, children in need can lead normal lives.")
               print("Come, play your part. Come, donate.")
               print("Be the change")
               print("Please fill out the below form to make your contribution.")
               
               #-------------------------------REGISTRATION FORM-------------------#
               from tkinter import*  
               base = Tk() 
               base.geometry('500x500')  
               base.title("Registration Form")  

               labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
               labl_0.place(x=90,y=53)  
   
  
               labl_1 = Label(base, text="FullName",width=20,font=("bold", 10))  
               labl_1.place(x=80,y=130)  
  
               entry_1 = Entry(base)  
               entry_1.place(x=240,y=130)  
  
               labl_2 = Label(base, text="Email",width=20,font=("bold", 10))  
               labl_2.place(x=68,y=180)  
  
               entry_02 = Entry(base)  
               entry_02.place(x=240,y=180)  
  
               labl_3 = Label(base, text="Mode of payment",width=20,font=("bold", 10))  
               labl_3.place(x=70,y=230)
               vars=IntVar()
               Radiobutton(base, text="Offline",padx = 5, variable=vars, value=1).place(x=235,y=230)  
               Radiobutton(base, text="Online",padx = 20, variable=vars, value=2).place(x=290,y=230)  
  
               labl_4 = Label(base, text="Amount:",width=20,font=("bold", 10))  
               labl_4.place(x=70,y=280) 
 
               entry_03 = Entry(base) 
               entry_03.place(x=240,y=280)  

               Button(base, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)  
               # it will be used for displaying the registration form onto the window  
               base.mainloop()  
               print("Registration form is created seccussfully...")  
               c=input("Do you want to continue(y/n):")
               if c=='y':
                   continue
               else:
                   break
          elif choice==5:
           print("THANK YOUU")
           break
          else:
              print("Invalid Choice!!!")


