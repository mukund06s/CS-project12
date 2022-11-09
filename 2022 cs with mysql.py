import random
import mysql.connector
con = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "Hawaairlines")

L = []
ch = 'y'
c = 'y'

while ch=='y':
    print("1. Ticket Booking")
    print("2. Total Ticketamount")
    print("3. Food")
    print("4. Search Record")
    n = int(input("Enter the choice : "))
    
    if n==1:
        print("1. View flight Class")
        print("2. Payment")
        
        m = int(input("Enter the choice : "))
        if m==1:
            if con.is_connected():
                print("Established")
            else:
                print("no")
            cur = con.cursor()
#             x = "Create table records(ticket  int(6) primary key , N  varchar(20) ,  A  varchar(30) , Date  int(20) , sor   varchar(20) )"
#             cur.execute(x)
            pas = int(input("No. of passengers : "))
            ticket = random.randint(1,6)
#             for i in ticket:
#                 print("Ticket no:  " , i ,"")
            print(ticket)
            for i in range(pas):
                N = input("Your Name : ")
                A = input("Your Address : ")
            Date = input("Your Date of journey : ")
            sor = print("Source point : " , "Indore")
            print("Destitation point : ")
            print("1. Mumbai")
            print("2. Delhi")
            print("3. Goa")
            D = int(input("Enter the choice : "))
 
            cur.execute("insert into records values( {} )", format(ticket))
            con.commit()
            x = "select * from records"
            cur.execute(x)
            data = cur.fecthall()
            for i in data:
                print(i)
            L_list = [ticket , N , A , Date , sor , D]
            L.append(L_list)
       
        elif m==2:
            if D==1:
                print("We Have the following rooms for : ")
                print("1 . FIRST CLASS---------> 5500Rs : ")
                print("2 . BUSINESS CLASS------> 4500Rs : ")
                print("3 . ECONOMY CLASS-------> 3500Rs : ")
                u = int(input("Enter the choice : "))
            
                if u==1:
                    print("you have taken FIRST CLASS seat")
                    print("Your seat rent is 5500Rs")
                    ch = input("Want to continue press 'y'")
                    hg = 5500  
                
                elif u==2:
                    print("you have taken BUSINESS CLASS seat")
                    print("Your seat rent is 4500Rs")
                    ch = input("Want to continue press 'y'")
                    hg = 4500
                    
                elif u==3:
                    print("you have taken ECONOMY CLASS seat")
                    print("Your seat rent is 3500Rs")
                    ch = input("Want to continue press 'y'")
                    hg = 3500
               
                else:
                    print("Wrong option")
                        
                    
            elif D==2:
                print("We Have the following rooms for : ")
                print("1 . FIRST CLASS---------> 5800Rs : ")
                print("2 . BUSINESS CLASS------> 4000Rs : ")
                print("3 . ECONOMY CLASS-------> 3500Rs : ")
                u = int(input("Enter the choice : "))
            
                if u==1:
                    print("you have taken FIRST CLASS seat")
                    print("Your seat rent is 5800Rs")
                    hg = 5800    
                    ch = input("Want to continue press 'y'")
                    
                elif u==2:
                    print("you have taken BUSINESS CLASS seat")
                    print("Your seat rent is 4000Rs")
                    hg = 4000   
                    ch = input("Want to continue press 'y'")
                        
                elif u==3:
                    print("you have taken ECONOMY CLASS seat")
                    print("Your seat rent is 3500Rs")
                    hg = 3500    
                    ch = input("Want to continue press 'y'")
                    
                else:
                    print("wrong option")
                 
            
            elif D==3:
                print("We Have the following rooms for : ")
                print("1 . FIRST CLASS---------> 5000Rs : ")
                print("2 . BUSINESS CLASS------> 4000Rs : ")
                print("3 . ECONOMY CLASS-------> 3000Rs : ")
                u = int(input("Enter the choice : "))
            
                if u==1:
                    print("you have taken FIRST CLASS seat")
                    print("Your seat rent is 5000Rs")
                    hg = 5000    
                    ch = input("Want to continue press 'y'")
                    
                elif u==2:
                    print("you have taken BUSINESS CLASS seat")
                    print("Your seat rent is 4000Rs")
                    hg = 4000   
                    ch = input("Want to continue press 'y'")
                        
                elif u==3:
                    print("you have taken ECONOMY CLASS seat")
                    print("Your seat rent is 3000Rs")
                    hg = 3000    
                    ch = input("Want to continue press 'y'")
                    
                else:
                    print("wrong option")
                 
            
            
    elif n==2:
        print("total amount of tickets ---->" ,pas*hg, "Rs")
        lbw = pas * hg 
        lugage = print("lugage cost ----------------> 500 Rs")
        food = print("food bill ------------------> 150 Rs")
        lugage = 500
        food = 150
        print("total cost------------------>" , lugage + food + lbw,"Rs")
        
'''        
    elif n==3:
        print("1. Edable ")
        print("2. Drinks ")
        j = int(input("Enter your choice: "))
        if j==1:
            print("1.Breakfast /n2.Lunch /n3.Dinner")

 
    elif n==4:
        flag = 0
        Name = input("Enter the Name to be searched : ")
        for i in range (len(L)) :
            if L[i][0]==Name :
                print("*******Details are here*******")
                print("Name : ", L[i][0])
                print("Address : ", L[i][1])
                print("Date of booking : ", L[i][2])
                print("Source point : ", "Indore")
                print("Destination point : ", D)
                print("******************************")
                flag = 1
        if flag == 0 :
            print("Not Found !")
'''           
con.close()            
            