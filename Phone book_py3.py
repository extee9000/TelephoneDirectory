#CLASSES

class Account (object) :
    def __init__(self,Fname,Lname) :
        self.Fname=Fname
        self.Lname=Lname
       
class Address (object) :
    
    def __init__(self,BldgNum,StreetName,City,PIN) :
        self.BN=BldgNum
        self.SN=StreetName
        self.city=City
        self.pin=PIN

    def printaddrs (self) :
        return "Address  : "+"\n"+"Building Number : "+str(self.BN)+"\n"+"Street Name : "+str(self.SN)+"\n"+"City : "+str(self.city)+"\n"+"Pin : "+str(self.pin)


class Date (object) :

    def __init__(self,Day,Month,Year) :
        self.D=Day
        self.M=Month
        self.Y=Year

    def printdate(self) :
        return "\n"+"Date of Birth : "+"\n"+"Day : "+str(self.D)+"  "+"Month : "+str(self.M)+"  "+"Year : "+str(self.Y)


    
    
class PersonalAccnt (Account) :

    def __init__(self,Fname,Lname,HomeAddrs,Mobile,DOB) :

        self.HomeAddrs=HomeAddrs
        self.mob=Mobile
        self.dob=DOB
        Account.__init__(self,Fname,Lname)
    def __str__(self):
        return "\n"+"Name  : "+str(self.Fname)+" "+str(self.Lname)+"\n"+str((self.HomeAddrs).printaddrs())+"\n"+"Mobile Number : "+str(self.mob)+"\n"+str((self.dob).printdate())+"\n"


class OfficeAccnt (Account) :

    def __init__(self,Fname,Lname,Desig,Phone,OfficeName,OfficeAddrs="") :

        self.Desig=Desig
        self.phn=Phone
        self.OAddrs=OfficeAddrs
        self.Oname=OfficeName
        Account.__init__(self,Fname,Lname)
    def __str__(self):
        if self.OAddrs != "" :
            return "\n"+"Name  : "+str(self.Fname)+" "+str(self.Lname)+"\n"+str((self.OAddrs).printaddrs())+"\n"+"Designation :"+str(self.Desig)+"\n"+"Office Name : "+str(self.Oname)+"\n"+"Phone Number : "+str(self.phn)+"\n"
        else :
            
            return "\n"+"Name  : "+str(self.Fname)+" "+str(self.Lname)+"\n"+"Address : Not Available"+"\n"+"Designation :"+str(self.Desig)+"\n"+"Office Name : "+str(self.Oname)+"\n"+"Phone Number : "+str(self.phn)+"\n"

        
import pickle
import os


#FUNCTIONS

def add_perContact (Fname,Lname,HomeAddrs,Mobile,DOB) :
    perCont=open("PersonalContact.txt","ab+")
    offCont=open("OfficialContact.txt","ab+")
    New = PersonalAccnt(Fname,Lname,HomeAddrs,Mobile,DOB)
    pickle.dump(New,perCont)
    perCont.close()
    offCont.close()
    

def add_offContact (Fname,Lname,Desig,Phone,OfficeName,OfficeAddrs) :
    perCont=open("PersonalContact.txt","ab+")
    offCont=open("OfficialContact.txt","ab+")
    New = OfficeAccnt(Fname,Lname,Desig,Phone,OfficeName,OfficeAddrs)
    pickle.dump(New,offCont)
    offCont.close()
    perCont.close()
    
def DeletePerCont(Firstname,Lastname) :
    perCont=open("PersonalContact.txt","ab+")
    temporary=open("Temporary.txt","ab+")
    count=0
    try :
        while True :
            x=pickle.load(perCont)
            if (x.Fname).lower() != Firstname.lower() and (x.Lname).lower() != Lastname.lower() :
                pickle.dump(x,temporary)
            else :
                count+=1
            
    except EOFError :
        perCont.close()
        temporary.close()
        
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")
    else :
        print ("\n","Acoount Deleted","\n")
  
    os.remove("PersonalContact.txt")
    os.rename("Temporary.txt","PersonalContact.txt")
    
    
                
def DeleteOffCont(Fname,Lname) :
    offCont=open("OfficialContact.txt","ab+")
    temporary=open("Temporary.txt","ab+")
    count=0
    while True :
        try :
            x=pickle.load(offCont)
            if str(x.Fname).lower() != str(Fname).lower() and str(x.Lname).lower() != str(Lname).lower():
                pickle.dump(x,temporary)
                
            else :
                count+=1
                
            
        except EOFError :
            offCont.close()
            temporary.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")
    else :
        print ("\n","Acoount Deleted","\n")
    
    os.remove("OfficialContact.txt")
    os.rename("Temporary.txt","OfficialContact.txt")
        
def changeMobilenumber(Fname,Lname,NewMobileNum) :
    perCont=open("PersonalContact.txt","ab+")
    temporary=open("Temporary.txt","ab+")
    count=0
    while True :
        try :
            x=pickle.load(perCont)
            if (x.Fname).lower()==Fname.lower() and (x.Lname).lower()==Lname.lower() :
                setattr(x,"mob",NewMobileNum)
                pickle.dump(x,temporary)
                temporary.flush()
                print ("\n","Updated Contact : ")
                print (x)
                count+=1
            else :
                pickle.dump(x,temporary)
                
                
        except EOFError :
            perCont.close()
            temporary.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")
    os.remove("PersonalContact.txt")
    os.rename("Temporary.txt","PersonalContact.txt")
                        
def changePhonenumber(Fname,Lname,NewPhoneNum) :
    
    offCont=open("OfficialContact.txt","ab+")
    temporary=open("Temporary.txt","ab+")
    count=0
    while True :
        
        try :
            x=pickle.load(offCont)
            if (x.Fname).lower()==Fname.lower() and (x.Lname).lower()==Lname.lower() :
                setattr(x,"phn",NewPhoneNum)
                pickle.dump(x,temporary)
                temporary.flush()
                print ("Updated Contact : ")
                print (x)
                count+=1
            else :
                pickle.dump(x,temporary)
                
        except EOFError :
            offCont.close()
            temporary.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")

    os.remove("OfficialContact.txt")
    os.rename("Temporary.txt","OfficialContact.txt")
    
    
def searchPerCont(Firstname,Lastname) :
    
    perCont=open("PersonalContact.txt","ab+")
    count=0
    while True :
        try :
            x=pickle.load(perCont)
            if (x.Fname).lower()==Firstname.lower() and (x.Lname).lower()==Lastname.lower() :
                print (x)
                count+=1
            else :
                continue
        except EOFError :
            perCont.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")
     
    
    
def searchOffCont(Oname) :
    offCont=open("OfficialContact.txt","ab+")
    count=0
    while True :
        try :
            x=pickle.load(offCont)
            if  (x.Oname).lower()==Oname.lower():
                print (x)
                count+=1
            else :
                continue
        except EOFError :
            offCont.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")
   
    
def searchPerContPhone(Phone) :
    perCont=open("PersonalContact.txt","ab+")
                            
    count=0
    while True :
        try :
            x=pickle.load(perCont)
            if str(x.mob)==str(Phone) :
                print (x)
                count+=1
            else :
                continue
        except EOFError :
            perCont.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")
    
    
def searchPerContDOB(DOB) :
    perCont=open("PersonalContact.txt","ab+")
    count=0
    while True :
        try :
            x=pickle.load(perCont)
            if x.dob.D==DOB.D and x.dob.M==DOB.M and x.dob.Y==DOB.Y :
                print (x)
                count+=1
                
            else :
                continue
        except EOFError :
            perCont.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")
    
    
def searchOffContOffCity(Offcity) :
    offCont=open("OfficialContact.txt","ab+")

    count=0
    while True :    
        try :
            x=pickle.load(offCont)
            if  x.OAddrs != "" :
                if (x.OAddrs.city).lower()==Offcity.lower():
                    print (x)
                    count+=1
            elif x.OAddrs == "" :
                continue
            else :
                continue
        except EOFError :
            offCount.close()
            break
    if count == 0 :
        print ("\n","No Contact Matched specified Data","\n")

    
def menu():


    menu=('''                     ***PHONE DIRECTORY***

            : What would you like to do my master :

            1. Add Contact
            2. Change Phone Number of specified person 
            3. Search Contact by Name in Personal Contacts
            4. Search Contact by Office Name in Official Contacts
            5. Search by Date of Birth
            6. Search by City
            7. Search by Mobile Number in Personal Contact
            8. Delete Contact
            9. Exit
            ''')
    print (menu)

    try :
        n=input("Enter your Choice between 1 to 9 : ")
        if int(n) in [1,2,3,4,5,6,7,8,9] :
            return int(n)
        elif n=="" :
            print ("\n","Please Enter proper Option","\n")
        else  :
            print ('''              ******INVALID INPUT******
              please choose between 1 to 9 ''',2*"\n")
    except :
            print ('''              ******INVALID INPUT******
              please choose between 1 to 9 ''',2*"\n")
        
#main

while True :
    user_input=menu()

    if user_input==1 :
        
        while True :
         try :
          x=int(input(''' To add Personal Acoount Choose 1 \nTo add Official Account choose 2 \nEnter Your Choice : '''))
          if x in [1,2]:
            break
          else :
            raise ValueError
         except :
           print ("\n","Please enter proper option","\n")

        if int(x)==1 :
            
             print ("\n","You have decided to add Personal Contact","\n")
             
             while True :
                 try :
                     Fname=input("Enter First Name : ")
                     Lname=input("Enter  Last Name :")
                     if Fname=="" or Lname=="" :
                         raise ValueError
                     else :
                         break
                 except :
                     print ("\n","Please enter Name properly","\n")
             while True :
                         
                 try :
                         Mobile=int(input("Enter mobile number : "))
                         if len(str(Mobile))!=10 :
                               print ("***Mobile number should be of 10 digits :")
                               continue
                         else :
                               break                                     
                 except  :
                         print ("\n","Please enter ten digit number","\n")
                         
             while True :
                 try :
                     print ("\n",": Enter Homeaddress Details : ","\n")
                                         
                     BldgNum=input("Enter The Building Number : ")
                     StreetName=input("Enter the Street Name : ")
                     City=input("Enter the City Name : ")
                     while True :
                         try :
                             PIN=int(input("Enter the pincode : "))
                             if len(str(PIN))!=6 :
                                 print ("\n","Please enter 6 digit pin","\n")
                             else :
                                 break
                         except :
                             print ("\n","Please enter 6 digit pin","\n")
                 
                     break
                 except :
                     print ("\n","Please Enter Address details properly","\n")
                                  
             HomeAddrs=Address(BldgNum,StreetName,City,PIN)
                                                          
             print ("\n",": Enter Dirth of Birth Details :","\n")                                         
                                    
             while True :
                 try :                                 
                     Day=int(input("Enter the day : "))
                     if Day>0 and Day<=31 :
                         break
                     else :
                         raise ValueError
                 except :
                     print ("\n","Please enter a date in between 1 to 30","\n")
                        
             while True :
                try :
                     L=["January","February","March","April","May","June","July","August","September","October","November","December"]
                     Month=input("Enter the Month : ")
                     if int(Month)>0 and int(Month)<13 :
                         month=L[int(Month)-1]
                         break
                     else :
                        raise ValueError
                      
                except :
                     print ("\n"+"Please enter proper Month"+"\n")              
                 
             while True:
                 try :
                     Year=int(input("Enter the year : "))
                     break
                 except :
                     print ("\n","Please enter proper year","\n")
             DOB=Date(Day,month,Year)
                                                                   
             add_perContact(Fname,Lname,HomeAddrs,Mobile,DOB)
                                    
             print ("\n","Personal Contact added Successfully",2*"\n")

        
        elif x==2 :
            
            print ("\n","You have decided to add Official Contact ","\n")
                         
            while True :
                 try :
                     Fname=input("Enter First Name : ")
                     Lname=input("Enter  Last Name :")
                     if Fname=="" or Lname=="" :
                         raise ValueError
                     else :
                         break
                 except :
                     print ("\n","Please enter Name properly","\n")
            while True :
                         
                 try :                         
                     Phone=int(input("Enter Phone number : "))
                     if len(str(Phone))!=8 :
                           print ("***Phone number should be of 8 digits :")
                           continue
                     else :
                           break                                     
                 except  :
                         print ("\n","Please enter 8 digit number","\n")
            
                                  
            while True :
                 try :
                     x=input("Would you like to enter a Adress (yes/no) : ")
                     if x.lower() in ["yes","y"] :
                             
                         while True :
                             try :
                                 print ("\n",": Enter Office Address Details : ","\n")
                                                     
                                 BldgNum=input("Enter The Building Number : ")
                                 StreetName=input("Enter the Street Name : ")
                                 City=input("Enter the City Name : ")
                                 while True :
                                     try :
                                         PIN=int(input("Enter the pincode : "))
                                         if len(str(PIN))!=6 :
                                             print ("\n","Please enter 6 digit pin","\n")
                                         else :
                                             break
                                     except :
                                         print ("\n","Please enter 6 digit pin","\n")
                             
                                 break
                             except :
                                 print ("\n","Please Enter Address details properly","\n")
                                      
                         OfficeAddrs=Address(BldgNum,StreetName,City,PIN)
                         break
                                 
                     elif x.lower() in ["no","n"] :
                         print ("\n","You have decided not to provide Address","\n") 
                         OfficeAddrs=""
                         break

                     else :
                                  
                          print ("\n","Please choose between yes or no ","\n")
                          raise ValueError
                 except :
                     print ("\n","Please choose between yes or no","\n")
                     
            while True :
                    
                try :
                    Desig=input("Enter the person's Designation : ")
                    break
                except :
                    ("\n","Please enter proper Designation","\n")
                                
                                                      
            while True :

                try :
                    OfficeName=input("Enter the person's Office Name  : ")
                    break
                except :
                    print("\n","Please enter proper Designation","\n")

            add_offContact(Fname,Lname,Desig,Phone,OfficeName,OfficeAddrs)
                                    
            print ("\n","Official Contact added Successfully",2*"\n")
                    
           
    elif user_input==2 :
        
            print ("\n","Enter 1 if you want to change Personal Contact Number \nEnter 2 if you want to change ofiicial Phone number ")
            while True :
                try :
                    x=int(input ("Enter your choice : "))
                    if x in [1,2] :
                        break
                    else :
                        raise ValueError 
                except :
                    print ("\n","Please enter proper Value","\n")
                    
            if x==1 :
                print ("\n","You Decided to change Personal Contact Number","\n")
                while True :
                     try :
                         Fname=input("Enter First Name : ")
                         Lname=input("Enter  Last Name :")
                         if Fname=="" or Lname=="" :
                             raise ValueError
                         else :
                             break
                     except :
                         print ("\n","Please enter Name properly","\n")

                while True :
                 
                     try :
                             NewMobileNum=int(input("Enter mobile number : "))
                             if len(str(NewMobileNum))!=10 :
                                   print ("***Mobile number should be of 10 digits :")
                                   continue
                             else :
                                   break                                     
                     except  :
                             print ("\n","Please enter ten digit number","\n")
               
                changeMobilenumber(Fname,Lname,NewMobileNum)           
                
            if x==2 :
                print ("\n","You Decided to change Official Contact Number","\n")
                while True :
                     try :
                         Fname=input("Enter First Name : ")
                         Lname=input("Enter  Last Name :")
                         if Fname=="" or Lname=="" :
                             raise ValueError
                         else :
                             break
                     except :
                         print ("\n","Please enter Name properly","\n")

                while True :
                 
                     try :
                             NewPhoneNum=int(input("Enter mobile number : "))
                             if len(str(NewPhoneNum))!=8 :
                                   print ("***Mobile number should be of 8 digits :")
                                   continue
                             else :
                                   break                                     
                     except  :
                             print ("\n","Please enter 8 digit number","\n")
                 
                changePhonenumber(Fname,Lname,NewPhoneNum)           
                                                                                 
    elif user_input == 3 :
                print ("\n","You choose to Search Contact by Name in Personal Contacts","\n")
                while True :
                     try :
                         Fname=input("Enter First Name of the Contact : ")
                         Lname=input("Enter  Last Name of the Contact :")
                         if Fname=="" or Lname=="" :
                             raise ValueError
                         else :
                             break
                     except :
                         print ("\n","Please enter Name properly","\n")
                print ("\n","The reqired Contacts are : ","\n")
                searchPerCont(Fname,Lname)
                
    elif user_input==4:
                print ("\n","You choose to Search Contact by Name in Official Contacts","\n")
                while True :

                    try :
                        Oname=input("Enter the person's Office Name  : ")
                        break
                    except :
                        print("\n","Please enter proper Designation","\n")
                
                print ("\n","The reqired Contacts are : ","\n")
                searchOffCont(Oname)

    elif user_input==5 :
                    print ("\n",": Enter Dirth of Birth Details :","\n")                                         
                                        
                    while True :                
                         Day=int(input("Enter the day : "))
                         if Day>0 and Day<=31 :
                             break
                         else :
                             print ("\n","Please enter a date in between 1 to 30","\n")       

                    while True :
                        try :
                             L=["January","February","March","April","May","June","July","August","September","October","November","December"]
                             Month=input("Enter the Month : ")
                             if int(Month)>0 and int(Month)<13 :
                                 month=L[int(Month)-1]
                                 break
                             else :
                                print ("\n","Please enter month between 1 to 12","\n")
                              
                        except :
                             print ("\n"+"Please enter proper Month"+"\n")              
                         
                    while True:
                         try :
                             Year=int(input("Enter the year : "))
                             break
                         except :
                             print ("\n","Please enter proper year","\n")
                    DOB=Date(Day,month,Year)
                    searchPerContDOB(DOB)
                    

    elif user_input==6 :
                print ("\n","You choose to Search by City","\n")
                while True :
                    try :
                        Offcity=input("Enter the City Name : ")
                        break
                    except :
                        ("\n","Please Enter proper value","\n")
                searchOffContOffCity(Offcity)
                        
    elif user_input==7 :
               print ("\n","You choose to Search by Mobile Number","\n")
               while True :
                     try :  
                             Mobile=input("Enter mobile number : ")
                             if len(str(Mobile))!=10 :
                                   print ("***Mobile number should be of 10 digits :")
                                   continue
                             else :
                                   break                                     
                     except  :
                             print ("\n","Please enter ten digit number","\n")
               print ("\n","The required contacts are :","\n")
               searchPerContPhone(Mobile)
                          
    elif user_input == 8 :

                print ("\n","To Delete A Personal Contact press 1 \nTo Delete Official Contact Press 2 ","\n")
                while True :
                    try:
                        x=int(input("Enter Your Choice : "))
                        if x not in [1,2] :
                            raise ValueError
                        elif x == "" :
                            raise ValueError
                        else :
                            break    
                    except :
                        print ("Please enter proper value")
                if str(x)=="1" :
                    while True :
                         try :
                             Fname=input("Enter First Name of the contact to be Deleted : ")
                             Lname=input("Enter  Last Name of the contact to be Deleted :")
                             if Fname=="" or Lname=="" :
                                 raise ValueError
                             else :
                                 break
                         except :
                             print ("\n","Please enter Name properly","\n")
                    DeletePerCont(Fname,Lname)
                    
        
                elif str(x)=="2" :
                    
                    while True :
                         try :
                             Fname=input("Enter First Name of the contact to be Deleted : ")
                             Lname=input("Enter  Last Name of the contact to be Deleted :")
                             if Fname=="" or Lname=="" :
                                 raise ValueError
                             else :
                                 break
                         except :
                             print ("\n","Please enter Name properly","\n")
                    DeleteOffCont(Fname,Lname)           
                    
            
    elif user_input==9 :
            print ("\n","Thank You For Using ME \nHave a NICE DADY MASTER","\n")
            break
    else :
            print ("\n","PLease Enter Proper Option","\n")

            
                





                        
                
                                                                              

    
    
    


















            
    
    































        
 
