import mysql.connector
import os
import time
#CONNECTING TO DATABASE , CHANGE PASSWORD WHICH YOU HAVE GIVEN
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
    )

my_cur = mydb.cursor()
#CREATING DATABSE AIRPLANE
my_cur.execute("CREATE DATABASE IF NOT EXISTS AIRPLANE")
my_cur.execute("USE AIRPLANE")
#CREATING TABLE FOR USERS AND FLIGHT BOOKING TABLE
my_cur.execute("CREATE TABLE IF NOT EXISTS users(name VARCHAR(255) , address VARCHAR(255) , phone_num INTEGER(10) , user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cur.execute("CREATE TABLE IF NOT EXISTS flight_book1(seat_no VARCHAR(10) , user_id VARCHAR(255))")
my_cur.execute("CREATE TABLE IF NOT EXISTS flight_book2(seat_no VARCHAR(10) , user_id VARCHAR(255))")
my_cur.execute("CREATE TABLE IF NOT EXISTS flight_book3(seat_no VARCHAR(10) , user_id VARCHAR(255))")
my_cur.execute("CREATE TABLE IF NOT EXISTS flight_book4(seat_no VARCHAR(10) , user_id VARCHAR(255))")
my_cur.execute("CREATE TABLE IF NOT EXISTS flight_book5(seat_no VARCHAR(10) , user_id VARCHAR(255))")
#my_cur.execute("INSERT INTO users (name, address , phone_num) SELECT * FROM (SELECT 'KUMAR', 'CHENNAI', '12345678') AS tmp WHERE NOT EXISTS ( SELECT name FROM users WHERE name = 'KUMAR') LIMIT 1")
#my_cur.execute("DELETE FROM AIRPLANE.flight_book")

#CREATING TBALE FOR FLIGHTS AND INSERTING INTO THEM
my_cur.execute("CREATE TABLE IF NOT EXISTS flights(f_name VARCHAR(255) , starting_point VARCHAR(255) , end_point VARCHAR(255) , departure DOUBLE , arrival DOUBLE , flight_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cur.execute("INSERT INTO flights (f_name, starting_point , end_point , departure , arrival) SELECT * FROM (SELECT 'SPICEJET', 'CHENNAI', 'GOA' , '18.00' , '19.25') AS tmp WHERE NOT EXISTS ( SELECT f_name FROM flights WHERE f_name = 'SPICEJET') LIMIT 1")
my_cur.execute("INSERT INTO flights (f_name, starting_point , end_point , departure , arrival) SELECT * FROM (SELECT 'INDIGO', 'CHENNAI', 'LAS VEGAS' , '15.00' , '17.45') AS tmp WHERE NOT EXISTS ( SELECT f_name FROM flights WHERE f_name = 'INDIGO') LIMIT 1")
my_cur.execute("INSERT INTO flights (f_name, starting_point , end_point , departure , arrival) SELECT * FROM (SELECT 'JET AIRWAYS', 'CHENNAI', 'MUMBAI' , '9.00' , '10.55') AS tmp WHERE NOT EXISTS ( SELECT f_name FROM flights WHERE f_name = 'JET AIRWAYS') LIMIT 1")
my_cur.execute("INSERT INTO flights (f_name, starting_point , end_point , departure , arrival) SELECT * FROM (SELECT 'AIR ASIA', 'CHENNAI', 'MALAYSIA' , '11.00' , '15.30') AS tmp WHERE NOT EXISTS ( SELECT f_name FROM flights WHERE f_name = 'AIR ASIA') LIMIT 1")
my_cur.execute("INSERT INTO flights (f_name, starting_point , end_point , departure , arrival) SELECT * FROM (SELECT 'VISTARA', 'CHENNAI', 'BANGALORE' , '6.55' , '8.00') AS tmp WHERE NOT EXISTS ( SELECT f_name FROM flights WHERE f_name = 'VISTARA') LIMIT 1")


#INSERTING FLIGHT NAME INTO FLIGHT BOOK TABLE
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT1') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT1')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT2') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT2')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT3') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT3')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT4') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT4')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT5') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT5')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT6') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT6')LIMIT 1 ")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT7') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT7')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT8') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT8')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT9') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT9')LIMIT 1")
my_cur.execute("INSERT INTO flight_book1(seat_no) SELECT * FROM(SELECT 'SEAT10') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book1 WHERE seat_no = 'SEAT10')LIMIT 1")

#INSERTING FLIGHT NAME INTO FLIGHT BOOK TABLE2
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT1') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT1')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT2') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT2')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT3') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT3')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT4') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT4')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT5') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT5')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT6') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT6')LIMIT 1 ")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT7') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT7')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT8') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT8')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT9') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT9')LIMIT 1")
my_cur.execute("INSERT INTO flight_book2(seat_no) SELECT * FROM(SELECT 'SEAT10') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book2 WHERE seat_no = 'SEAT10')LIMIT 1")

#INSERTING FLIGHT NAME INTO FLIGHT BOOK TABLE3
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT1') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT1')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT2') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT2')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT3') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT3')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT4') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT4')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT5') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT5')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT6') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT6')LIMIT 1 ")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT7') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT7')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT8') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT8')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT9') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT9')LIMIT 1")
my_cur.execute("INSERT INTO flight_book3(seat_no) SELECT * FROM(SELECT 'SEAT10') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book3 WHERE seat_no = 'SEAT10')LIMIT 1")

#INSERTING FLIGHT NAME INTO FLIGHT BOOK TABLE4
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT1') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT1')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT2') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT2')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT3') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT3')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT4') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT4')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT5') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT5')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT6') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT6')LIMIT 1 ")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT7') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT7')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT8') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT8')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT9') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT9')LIMIT 1")
my_cur.execute("INSERT INTO flight_book4(seat_no) SELECT * FROM(SELECT 'SEAT10') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book4 WHERE seat_no = 'SEAT10')LIMIT 1")

#INSERTING FLIGHT NAME INTO FLIGHT BOOK TABLE
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT1') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT1')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT2') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT2')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT3') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT3')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT4') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT4')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT5') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT5')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT6') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT6')LIMIT 1 ")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT7') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT7')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT8') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT8')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT9') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT9')LIMIT 1")
my_cur.execute("INSERT INTO flight_book5(seat_no) SELECT * FROM(SELECT 'SEAT10') AS tmp WHERE NOT EXISTS (SELECT seat_no FROM flight_book5 WHERE seat_no = 'SEAT10')LIMIT 1")
mydb.commit()

while(True):
    print("==============================================================================================")
    print("                           WECOME TO AIRLINES COMPANY                                         ")

    a = int(input("Enter your choice \n1. LOGIN \n2. SIGNUP\n3. EXIT\n"))
    if(a==1):
        u_id = input("Enter your user id\t")
        name = input("Enter your name\t")
        my_cur.execute("SELECT * FROM AIRPLANE.users WHERE user_id = %s and name = %s" , [u_id , name])
        myresult = my_cur.fetchall()
        if(myresult == []):
            print("-------NO SUCH USER--------PLEASE RETRY OR SIGNUP-----------")
            continue
        else:
            while(True):
                print("==============================================================================================")
                print("------------------------------------- WELCOME "+ name +" -----------------------------------------------USER ID "+ u_id)
                b = int(input("What do you want to do \n 1. View FLights \n 2. Book Flights\n 3. LOGOUT\n"))
                if(b==1):
                    my_cur.execute("SELECT * FROM flights")
                    result = my_cur.fetchall()
                    print("FLIGHT NAME \t FROM \t TO \t DEPARTURE \t ARRIVAL \t FLIGHT ID")
                    for i in result:
                        for j in i:
                            print(j , end = "\t   ")
                        print("\n")
                        continue
                if((b!=2)&(b!=3)&(b!=1)):
                    print("Invalid number")
                    continue
                if(b==2):
                    my_cur.execute("SELECT * FROM flights")
                    result = my_cur.fetchall()
                    print("FLIGHT NAME \t FROM \t TO \t DEPARTURE \t ARRIVAL \t FLIGHT ID")
                    for i in result:
                        for j in i:
                            print(j , end = "\t   ")
                        print("\n")
                    f = input("WHICH FLIGHT WOULD YOU WANT TO CHOOSE , TYPE THE FLIGHT NAME EG. SPICEJET\t")
                    if(f == "SPICEJET"):
                        my_cur.execute("SELECT * FROM AIRPLANE.flight_book1 WHERE user_id is NULL")
                        print("AVAILABLE SEATS")
                        res = my_cur.fetchall()
                        for x in res:
                            print(x)
                        ticket_no = int(input("HOW MANY TICKETS DO YOU WANT\t"))
                        if(len(res)<ticket_no):
                            print("Sorry , you have entered too much seats")
                        else:  
                            print("Your seats have been reserved , Are you sure to continue and book tickets")
                            cont = int(input("Press 1 to continue and 0 to exit"))
                            if(cont == 0):
                                break
                            else:
                                for i in range(ticket_no):
                                    my_cur.execute("UPDATE AIRPLANE.flight_book1 SET user_id = %s WHERE user_id IS NULL LIMIT 1" % (u_id))

                                file = open("TICKET.txt" , 'w+')
                                file.write("******************************** AIRLINES COMPANY********************************")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("Hello :" + name + "               User id :" + u_id)
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("        YOUR TICKET IS SUCCESSFULLY BOOKED        ")
                                file.write("Total number of passengers :" + str(ticket_no))
                                
                                my_cur.execute("SELECT * FROM AIRPLANE.flights")
                                res = my_cur.fetchall()
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                FLIGHT DETAILS                    ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("FLIGHT NAME \t FROM \t TO \t DEPARTURE \t ARRIVAL \t FLIGHT ID")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                data = res[0]
                                file.write(str(data))
                                file.close()
                                mydb.commit()
                                time.sleep(2)
                                print("Your ticket is stored in this location:" ,os.path.abspath("TICKET.txt"))
                                print("TICKET BOOKED SUCCESSFULLY")
                                break
                    elif(f=="INDIGO"):
                        my_cur.execute("SELECT * FROM AIRPLANE.flight_book2 WHERE user_id is NULL")
                        print("AVAILABLE SEATS")
                        res = my_cur.fetchall()
                        for x in res:
                            print(x)
                        ticket_no = int(input("HOW MANY TICKETS DO YOU WANT\t"))
                        if(len(res)<ticket_no):
                            print("Sorry , you have entered too much seats")
                        else:  
                            print("Your seats have been reserved , Are you sure to continue and book tickets")
                            cont = int(input("Press 1 to continue and 0 to exit"))
                            if(cont == 0):
                                break
                            else:
                                for i in range(ticket_no):
                                    my_cur.execute("UPDATE AIRPLANE.flight_book2 SET user_id = %s WHERE user_id IS NULL LIMIT 1" % (u_id))
                                file = open("TICKET.txt" , 'w+')
                                file.write("******************************** AIRLINES COMPANY********************************")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("Hello :" + name + "               User id :" + u_id)
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("        YOUR TICKET IS SUCCESSFULLY BOOKED        ")
                                file.write("Total number of passengers :" + str(ticket_no))
                                my_cur.execute("SELECT * FROM AIRPLANE.flights")
                                res = my_cur.fetchall()
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                FLIGHT DETAILS                    ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("FLIGHT NAME \t FROM \t TO \t DEPARTURE \t ARRIVAL \t FLIGHT ID")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                data = res[1]
                                file.write(str(data))
                                file.close()
                                mydb.commit()
                                time.sleep(2)
                                print("Your ticket is stored in this location:" ,os.path.abspath("TICKET.txt"))
                                print("TICKET BOOKED SUCCESSFULLY")
                                break
                                   
                    elif(f=="JET AIRWAYS"):
                        my_cur.execute("SELECT * FROM AIRPLANE.flight_book3 WHERE user_id is NULL")
                        print("AVAILABLE SEATS")
                        res = my_cur.fetchall()
                        for x in res:
                            print(x)
                        ticket_no = int(input("HOW MANY TICKETS DO YOU WANT\t"))
                        if(len(res)<ticket_no):
                            print("Sorry , you have entered too much seats")
                        else:  
                            print("Your seats have been reserved , Are you sure to continue and book tickets")
                            cont = int(input("Press 1 to continue and 0 to exit"))
                            if(cont == 0):
                                break
                            else:
                                for i in range(ticket_no):
                                    my_cur.execute("UPDATE AIRPLANE.flight_book3 SET user_id = %s WHERE user_id IS NULL LIMIT 1" % (u_id))
                                file = open("TICKET.txt" , 'w+')
                                file.write("******************************** AIRLINES COMPANY********************************")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("Hello :" + name + "               User id :" + u_id)
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("        YOUR TICKET IS SUCCESSFULLY BOOKED        ")
                                file.write("Total number of passengers :" + str(ticket_no))
                                my_cur.execute("SELECT * FROM AIRPLANE.flights")
                                res = my_cur.fetchall()
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                FLIGHT DETAILS                    ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("FLIGHT NAME \t FROM \t TO \t DEPARTURE \t ARRIVAL \t FLIGHT ID")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                data = res[2]
                                file.write(str(data))
                                file.close()
                                mydb.commit()
                                time.sleep(2)
                                print("Your ticket is stored in this location:" ,os.path.abspath("TICKET.txt"))
                                print("TICKET BOOKED SUCCESSFULLY")
                                break

                    elif(f=="AIR ASIA"):
                        my_cur.execute("SELECT * FROM AIRPLANE.flight_book4 WHERE user_id is NULL")
                        print("AVAILABLE SEATS")
                        res = my_cur.fetchall()
                        for x in res:
                            print(x)
                        ticket_no = int(input("HOW MANY TICKETS DO YOU WANT\t"))
                        if(len(res)<ticket_no):
                            print("Sorry , you have entered too much seats")
                        else:  
                            print("Your seats have been reserved , Are you sure to continue and book tickets")
                            cont = int(input("Press 1 to continue and 0 to exit"))
                            if(cont == 0):
                                break
                            else:
                                for i in range(ticket_no):
                                    my_cur.execute("UPDATE AIRPLANE.flight_book4 SET user_id = %s WHERE user_id IS NULL LIMIT 1" % (u_id))
                                file = open("TICKET.txt" , 'w+')
                                file.write("******************************** AIRLINES COMPANY********************************")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("Hello :" + name + "               User id :" + u_id)
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("        YOUR TICKET IS SUCCESSFULLY BOOKED        ")
                                file.write("Total number of passengers :" + str(ticket_no))
                                my_cur.execute("SELECT * FROM AIRPLANE.flights")
                                res = my_cur.fetchall()
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                FLIGHT DETAILS                    ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("FLIGHT NAME \t FROM \t TO \t DEPARTURE \t ARRIVAL \t FLIGHT ID")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                data = res[3]
                                file.write(str(data))
                                file.close()
                                mydb.commit()
                                time.sleep(2)
                                print("Your ticket is stored in this location:" ,os.path.abspath("TICKET.txt"))
                                print("TICKET BOOKED SUCCESSFULLY")
                                break

                    elif(f=="VISTARA"):
                        my_cur.execute("SELECT * FROM AIRPLANE.flight_book5 WHERE user_id is NULL")
                        print("AVAILABLE SEATS")
                        res = my_cur.fetchall()
                        for x in res:
                            print(x)
                        ticket_no = int(input("HOW MANY TICKETS DO YOU WANT\t"))
                        if(len(res)<ticket_no):
                            print("Sorry , you have entered too much seats")
                        else:  
                            print("Your seats have been reserved , Are you sure to continue and book tickets")
                            cont = int(input("Press 1 to continue and 0 to exit"))
                            if(cont == 0):
                                break
                            else:
                                for i in range(ticket_no):
                                    my_cur.execute("UPDATE AIRPLANE.flight_book5 SET user_id = %s WHERE user_id IS NULL LIMIT 1" % (u_id))
                                file = open("TICKET.txt" , 'w+')
                                file.write("******************************** AIRLINES COMPANY********************************")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("Hello :" + name + "               User id :" + u_id)
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("        YOUR TICKET IS SUCCESSFULLY BOOKED        ")
                                file.write("Total number of passengers :" + str(ticket_no))
                                my_cur.execute("SELECT * FROM AIRPLANE.flights")
                                res = my_cur.fetchall()
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                FLIGHT DETAILS                    ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("FLIGHT NAME \t FROM \t TO \t DEPARTURE \t ARRIVAL \t FLIGHT ID")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                file.write("                                                  ")
                                data = res[4]
                                file.write(str(data))
                                file.close()
                                mydb.commit()
                                time.sleep(2)
                                print("Your ticket is stored in this location:" ,os.path.abspath("TICKET.txt"))
                                print("TICKET BOOKED SUCCESSFULLY")
                                break
                    else:
                        print("ENTER THE CORRECT NAME (ALL CAPS)")                    
                if(b==3):
                    break
                
    if(a==2):
        new_name = input("Enter your name\t")
        new_address = input("Enter your address\t")
        new_phone = int(input("Enter your phone number\t"))
        sql2 = "INSERT INTO AIRPLANE.users(name , address , phone_num) VALUES ('%s','%s','%s')" % (new_name , new_address , new_phone)
        my_cur.execute(sql2)
        mydb.commit()
        print("---------------------------USER SUCCESFULLY REGISTERED----------------------------------------")
        print("Please try logging in again with your name and given User ID")
        my_cur.execute("SELECT user_id FROM AIRPLANE.users WHERE name = %s and address = %s and phone_num = %s" , (new_name , new_address , new_phone))
        result = my_cur.fetchall()
        print("YOUR USER ID is : " , result[0])
    if(a==3):
        break
    if((a!=1)&(a!=2)&(a!=3)):
        print("INVALID")
        continue

