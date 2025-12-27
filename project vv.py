import mysql.connector as m
import datetime as dt
import tkinter as tk
from tkinter import ttk
con=m.connect(host='localhost',user='root',passwd='123@123')
cur=con.cursor()
cur.execute('create database if not exists sunshine_cabs')
cur.execute('use sunshine_cabs')
con=m.connect(host='localhost',user='root',passwd='123@123',database='sunshine_cabs')
cur=con.cursor()
#MADE BY PARIKSHIT SHARMA
def insert(a):
    if a.lower()=='employee':
        cur.execute('select MAX(Emp_id) from employee')
        d1=cur.fetchone()
        for lm in d1:
            s=lm
        eid=1+s
        while True:
            ename=input('Enter employee name : ')
            if len(ename)<=25 and type(ename)==str:
                break
            else:
                print('name should be less than 25')
        while True:
            try:
                year=int(input('Enter the year of joining : '))
            except ValueError:
                print('invalid year')
                continue
            if len(str(year))==4:
                if year>=2018:
                    break
                else: 
                    print('the company started in 2018 so invalid')
            else:
                print('invalid enter in format YYYY')
        while True:
            try:
                month=int(input('enter month  of joining in numerics: '))
            except ValueError:
                print('invalid month')
                continue
            if month>0 and month<=12 :
                break
            else:
                print('invalid month')
        while True:
            try:
                dat=int(input('enter Date of joining  :'))
            except ValueError:
                print('invalid date')
                continue
            if month in (1,3,5,7,8,10,12) and dat<=31 and dat>0 :
                break
            elif month in (4,6,9,11) and dat<=30 and dat>0 and type(dat)==int:
                break
            elif month==2 and dat<=29 and dat>0 and type(dat)==int and year%4==0:
                break
            elif month==2 and dat<=28 and dat>0 and type(dat)==int and year%4!=0:
                break
            else:
                print('invalid date')
        date=dt.date(year,month,dat)
        while True:
            try:
                sal=int(input('enter salary of employee: '))
            except ValueError:
                print('invalid salary')
                continue
            if sal>0 and type(sal)==int:
                break
            else:
                print('invalid')
        dep=input('enter the department of employee : ')
        cur.execute("INSERT INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (%s, %s, %s, %s, %s)",(eid, ename, date, sal, dep))
        con.commit()
    elif a.lower()=='drivers':
        cur.execute('select MAX(Driver_id) from drivers')
        d1=cur.fetchone()
        for lm in d1:
            s=lm
        did=1+s
        while True:
            dname=input('Enter Driver name : ')
            if len(dname)<=25:
                break
            else:
                print('name should be less than 25')
        while True:
            try:
                year=int(input('Enter the year of joining : '))
            except ValueError:
                print('invalid year')
                continue
            if len(str(year))==4 and type(year)==int:
                if year>=2018:
                    break
                else: 
                    print('the company started in 2018 so invalid')
            else:
                print('invalid enter in format YYYY')
        while True:
            try:
                month=int(input('enter month  of joining in numerics: '))
            except ValueError:
                print('invalid month')
                continue
            if month>0 and month<=12:
                break
            else:
                print('invalid month')
        while True:
            try:
                dat=int(input('enter Date of joining  :'))
            except ValueError:
                print('invalid date')
                continue
            if month in (1,3,5,7,8,10,12) and dat<=31 and dat>0 :
                break
            elif month in (4,6,9,11) and dat<=30 and dat>0:
                break
            elif month==2 and dat<=29 and dat>0 and year%4==0:
                break
            elif month==2 and dat<=28 and dat>0 and year%4!=0:
                break
            else:
                print('invalid date')
        date=dt.date(year,month,dat)
        while True:
            sal=int(input('enter salary of Driver: '))
            if sal>0 :
                break
            else:
                print('invalid')
        cur.execute("INSERT INTO Drivers (Driver_id, Name, Date_of_joining, Salary) VALUES (%s, %s, %s, %s)",(did, dname, date, sal))
        con.commit()
        print('record inserted successfully')
    elif a.lower()=='cars':
        cur.execute('select MAX(Car_id) from cars')
        d1=cur.fetchone()
        for lm in d1:
            s=lm
        cid=1+s
        while True:
            try:
                cname=input('Enter Car name : ')
            except ValueError:
                print('invalid name')
                continue
            if len(cname)<=50 :
                break
            else:
                print('name should be less than 50')
        while True:
            try:
                year=int(input('Enter the year of Commission : '))
            except ValueError:
                print('invalid year')
                continue
            if len(str(year))==4 and type(year)==int:
                if year>=2018:
                    break
                else: 
                    print('the company started in 2018 so invalid')
            else:
                print('invalid enter in format YYYY')
        while True:
            try:
                month=int(input('enter month  of commission in numerics: '))
            except ValueError:
                print('invalid month')
                continue
            if month>0 and month<=12 and type(month)==int:
                break
            else:
                print('invalid month')
        while True:
            try:
                dat=int(input('enter Date of Commission  :'))
            except ValueError:
                print('invalid date')
                continue
            if month in (1,3,5,7,8,10,12) and dat<=31 and dat>0:
                break
            elif month in (4,6,9,11) and dat<=30 and dat>0:
                break
            elif month==2 and dat<=29 and dat>0 and year%4==0:
                break
            elif month==2 and dat<=28 and dat>0  and year%4!=0:
                break
            else:
                print('invalid date')
        date=dt.date(year,month,dat)
        while True:
            try:
                trp=int(input('enter no. of trips of car: '))
            except ValueError:
                print('invalid')
                continue
            if trp>=0 :
                break
            else:
                print('invalid')
        while True:
            try:
                year1=int(input('Enter the year of Service (enter DOC if no service) : '))
            except ValueError:
                print('invalid year')
                continue
            if len(str(year1))==4 and type(year1)==int:
                if year1>=2018:
                    break
                else: 
                    print('the company started in 2018 so invalid')
            else:
                print('invalid enter in format YYYY')
        while True:
            try:
                 month1=int(input('enter month  of service in numerics: '))
            except ValueError:
                print('invalid month')
                continue
            if month1>0 and month1<=12 and type(month1)==int:
                break
            else:
                print('invalid month')
        while True:
            try:
                dat1=int(input('enter Date of service  :'))
            except ValueError:
                print('invalid date')
                continue
            if month1 in (1,3,5,7,8,10,12) and dat1<=31 and dat1>0 :
                break
            elif month1 in (4,6,9,11) and dat1<=30 and dat1>0 :
                break
            elif month1==2 and dat1<=29 and dat1>0 and year1%4==0:
                break
            elif month1==2 and dat1<=28 and dat1>0 and year1%4!=0:
                break
            else:
                print('invalid date')
        date1=dt.date(year1,month1,dat1)
        while True:
            try:
                plat=int(input('Enter plate no in 6 digits: '))
            except ValueError:
                print('invalid plate no')
                continue
            if len(str(plat))==6 and type(plat)==int:
                break
            else:
                print('invalid')
        cur.execute("INSERT INTO cars (Car_id, plate_no,car_name,Date_of_commission, no_of_trips,last_service) VALUES (%s, %s, %s, %s, %s,%s)",(cid, plat,cname,date,trp, date1))
        con.commit()
    elif a.lower()=='customers':
        cur.execute('select MAX(cust_id) from customers')
        d1=cur.fetchone()
        for lm in d1:
            s=lm
        cuid=1+s
        while True:
            cuname=input('Enter Customer name : ')
            if len(cuname)<=15 and type(cuname)==str:
                break
            else:
                print('name should be less than 15')
        date=dt.date.today()
        cur.execute("INSERT INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (%s, %s, %s)",(cuid, cuname, date))
        con.commit()
    elif a.lower()=='trips':
        cur.execute('select MAX(trip_id) from trips')
        d1=cur.fetchone()
        for lm in d1:
            s=lm
        trid=1+s
        while True:
            try:
                cuid=int(input('Enter the  Customer id (from 1): '))
            except ValueError:
                print('invalid id')
                continue
            cur.execute('select cust_id from customers')
            f=cur.fetchall()
            c1=0
            for h in f:
                for j in h:
                    if cuid==j:
                        c1=1
                    else:
                        c1+=0
            if c1==1:
                break
            else:
                print('this is invalid')
        while True:
            try:
                crid=int(input('Enter the Car id (from 401): '))
            except ValueError:
                print('invalid id')
                continue
            cur.execute('select Car_id from cars')
            f1=cur.fetchall()
            c2=0
            for h1 in f1:
                for j1 in h1:
                    if crid==j1:
                        c2=1
                    else:
                        c2+=0
            if c2==1:
                break
            else:
                print('this is invalid id ')
        while True:
            try:
                Drid=int(input('Enter the Driver id (from 101) : '))
            except ValueError:
                print('invalid id')
                continue
            cur.execute('select Driver_id from Drivers')
            f2=cur.fetchall()
            c3=0
            for h2 in f2:
                for j2 in h2:
                    if Drid==j2:
                        c3=1
                    else:
                        c3+=0
            if c3==1:
                break
            else:
                print('this is invalid')
        while True:
            try:
                ch=int(input('enter Choice as 1 if you want to use current date for booking \n enter Choice as 2 if you want to use custom date :'))
            except ValueError:
                print('invalid choice')
                continue
            if ch==1:
                date=dt.date.today()
                break

            elif ch==2:
                while True:
                    try:
                        year=int(input('Enter the year of booking : '))
                    except ValueError:
                        print('invalid year')
                        continue
                    if len(str(year))==4 and type(year)==int:
                        if year>=2018:
                            break
                        else: 
                            print('the company started in 2018 so invalid')
                    else:
                        print('invalid enter in format YYYY')
                while True:
                    try:
                        month=int(input('enter month  of booking in numerics: '))
                    except ValueError:
                        print('invalid month')
                        continue
                    if month>0 and month<=12 and type(month)==int:
                        break
                    else:   
                        print('invalid month')
                while True:
                    try:
                        dat=int(input('enter Date of Booking  :'))
                    except ValueError:
                        print('invalid date')
                        continue
                    if month in (1,3,5,7,8,10,12) and dat<=31 and dat>0 and type(dat)==int:
                        break
                    elif month in (4,6,9,11) and dat<=30 and dat>0 and type(dat)==int:
                        break
                    elif month==2 and dat<=29 and dat>0 and type(dat)==int and year%4==0:
                        break
                    elif month==2 and dat<=28 and dat>0 and type(dat)==int and year%4!=0:
                        break
                    else:
                        print('invalid date')
                date=dt.date(year,month,dat)
                break
            else:
                print('invalid choice')
        while True:
            st=input('enter starting point : ')
            if len(st)<=50 and type(st)==str:
                break
            else:
                print('name should be less than 50')
        while True:
            dest=input('enter destination point : ')
            if len(dest)<=50 and type(dest)==str:
                break
            else:
                print('name should be less than 50')
        while True:
            try:
                dist=int(input('enter distance travelled in kms : '))
            except ValueError:
                print('invalid distance')
                continue
            if dist>0 and type(dist)==int:
                break
            else:
                print('invalid')
        fare=dist*15
        cur.execute("INSERT INTO trips (trip_id, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(trid, cuid, crid, Drid, date, st, dest, dist, fare))
        con.commit()
        print('record inserted successfully')
    else:
        print('invalid table name')
def Del(a1):
    a=a1.lower()
    if a=='employee':
        while True:
            try:
                eid=int(input('enter employee id to delete record : '))
            except ValueError:
                print('invalid id')
                continue
            if eid>=201 :
                break
            else:
                print('invalid id')
        cur.execute('delete from employee where Emp_id={}'.format(eid))
        con.commit()
        print('record deleted successfully')
    elif a=='drivers':
        while True:
            try:
                did=int(input('enter Driver id to delete record : '))
            except ValueError:
                print('invalid id')
                continue
            if did>=101:
                break
            else:
                print('invalid id')
        cur.execute('delete from Drivers where Driver_id={}'.format(did))
        con.commit()
        print('record deleted successfully')    
    elif a=='cars':
        while True:
            try:
                cid=int(input('enter Car id to delete record : '))
            except ValueError:
                print('invalid id')
                continue
            if cid>=401:
                break
            else:
                print('invalid id')
        cur.execute('delete from cars where Car_id={}'.format(cid))
        con.commit()
        print('record deleted successfully')
    elif a=='customers':
        while True:
            try:
                cuid=int(input('enter Customer id to delete record : '))
            except ValueError:
                print('invalid id')
                continue
            if cuid>=1 and type(cuid)==int:
                break
            else:
                print('invalid id')
        cur.execute('delete from customers where cust_id={}'.format(cuid))
        con.commit()
        print('record deleted successfully')    
    elif a=='trips':
        while True:
            try:
                trid=int(input('enter Trip id to delete record : '))
            except ValueError:
                print('invalid id')
                continue
            if trid>=1 :
                break
            else:
                print('invalid id')
        cur.execute('delete from trips where trip_id={}'.format(trid))
        con.commit()
        print('record deleted successfully')
    else:
        print('invalid choice')
def sel(a1):
    a=a1.lower()
    if a=='employee':
        cur.execute('select * from employee')
        f=cur.fetchall()
        for h in f:
            print(h)
    elif a=='drivers':
        cur.execute('select * from Drivers')
        f=cur.fetchall()
        for h in f:
            print(h)
    elif a=='cars':
        cur.execute('select * from cars')
        f=cur.fetchall()
        for h in f:
            print(h)
    elif a=='customers':
        cur.execute('select * from customers')
        f=cur.fetchall()
        for h in f:
            print(h)
    elif a=='trips':
        cur.execute('select * from trips')
        f=cur.fetchall()
        for h in f:
            print(h)
    else:
        print('invalid choice')
def rat():
    cur.execute('create table if not exists ratings ( Driver_id int, rating int)')
    while True:
        try:
            x=int(input('enter Driver id to rate : '))
        except ValueError:
            print('invalid id')
            continue
        if x>=101 :
            break
        else:
            print('invalid id')
    while True:
        try:       
            x1=int(input('enter rating out of 5 : '))
        except ValueError:
            print('invalid rating')
            continue
        if x1>=1 and x1<=5 and type(x1)==int:
            break
        else:
            print('invalid rating')
    cur.execute('insert into ratings (Driver_id, rating) values ({},{})'.format(x,x1))
    con.commit()
    cur.execute('select avg(rating) from ratings where Driver_id={}'.format(x))
    x2=cur.fetchall()
    for h in x2:
        for j in h:
            x3=j
    cur.execute('update Drivers set Rating={} where Driver_id={}'.format(x3,x))
    con.commit()
def trip(a1):
    a=a1.lower()
    if a=='customer id':
        while True:
            try:
                x=int(input('enter Customer id to view trips : '))
            except ValueError:
                print('invalid id')
                continue
            if x>=1:
                break
            else:
                print('invalid id')
        cur.execute('select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where trips.cust_id={};'.format(x))
        f=cur.fetchall()
        if not f:
            print('No trips found for this customer ID')
        else:
            for h in f:
                print(h)
    elif a=='driver id':
        while True:
            try:
                x=int(input('enter Driver id to view trips : '))
            except ValueError:
                print('invalid id')
                continue
            if x>=101 and type(x)==int:
                break
            else:
                print('invalid id')
        cur.execute('select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where trips.Driver_id={};'.format(x))
        f=cur.fetchall()
        if not f:
            print('No trips found for this Driver ID')
        else:
            for h in f:
                print(h)
    elif a=='car id':
        while True:
            try:
                x=int(input('enter Car id to view trips : '))
            except ValueError:
                print('invalid id')
                continue
            if x>=401 and type(x)==int:
                break
            else:
                print('invalid id')
        cur.execute('select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where trips.Car_id={};'.format(x))
        f=cur.fetchall()
        if not f:
            print('No trips found for this Car ID')
        else:
            for h in f:
                print(h)
    elif a=='trip id':
        while True:
            try:
                x=int(input('enter Trip id to view trip details : '))
            except ValueError:
                print('invalid id')
                continue
            if x>=1:
                break
            else:
                print('invalid id')
        cur.execute('select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where trips.trip_id={};'.format(x))
        f=cur.fetchall()
        if not f:
            print('No trip found for this Trip ID')
        else:
            for h in f:
                print(h)
    elif a=='customer name':
        while True:
            x=input('enter Customer name to view trips : ')
            if len(x)<=15 and type(x)==str:
                break
            else:
                print('invalid name')
        cur.execute("select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where customers.Cust_name='{}';".format(x))
        f=cur.fetchall()
        if not f:
            print('No trips found for this Customer name')
        else:
            for h in f:
                print(h)
    elif a=='driver name':
        while True:
            x=input('enter Driver name to view trips : ')
            if len(x)<=25 and type(x)==str:
                break
            else:
                print('invalid name')
        cur.execute("select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where drivers.Name='{}';".format(x))
        f=cur.fetchall()
        if not f:
            print('No trips found for this Driver name')
        else:
            for h in f:
                print(h)
    elif a=='car name':
        while True:
            x=input('enter Car name to view trips : ')
            if len(x)<=50 and type(x)==str:
                break
            else:
                print('invalid name')
        cur.execute("select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where cars.car_name='{}';".format(x))
        f=cur.fetchall()
        if not f:
            print('No trips found for this Car name')
        else:
            for h in f:
                print(h)
    elif a=='all trips':
        cur.execute('select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id;')
        f=cur.fetchall()
        if not f:
            print('No trips found')
        else:
            for h in f:
                print(h)
    elif a=='date range':
        while True:
            print('Enter start date of range:')
            y=int(input('Enter year in YYYY format: '))
            m=int(input('Enter month in MM format: '))
            d=int(input('Enter day in DD format: '))
            try:
                start_date=dt.date(y,m,d)
                break
            except ValueError:
                print('Invalid date, please try again.')
        while True:
            print('Enter end date of range:')
            year=int(input('Enter year in YYYY format: '))
            month=int(input('Enter month in MM format: '))
            day=int(input('Enter day in DD format: '))
            try:
                end_date=dt.date(year,month,day)
                if end_date>=start_date:
                    break
                else:
                    print('End date must be after start date.')
            except ValueError:
                print('Invalid date, please try again.')
        cur.execute("select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where trips.Date_of_booking between '{}' and '{}';".format(start_date,end_date))
        f=cur.fetchall()
        if not f:
            print('No trips found in this date range')
        else:
            for h in f:
                print(h)
    elif a=='total fare range':
        while True:
            try:
                min_fare=int(input('Enter minimum fare: '))
            except ValueError:
                print('Invalid fare, please try again.')
                continue
            try:
                max_fare=int(input('Enter maximum fare: '))
            except ValueError:
                print('Invalid fare, please try again.')
                continue
            if min_fare>=0 and max_fare>=min_fare:
                break
            else:
                print('Invalid fare range, please try again.')
        cur.execute("select trips.trip_id,customers.Cust_name,trips.Date_of_booking,trips.Start_location,trips.Destination,trips.total_km,trips.total_fare,cars.car_name,drivers.Name As Driver_Name,drivers.Rating from trips inner join cars on trips.Car_id=cars.Car_id inner join customers on trips.Cust_id=customers.Cust_id inner join drivers on trips.Driver_id=drivers.Driver_id where trips.total_fare between {} and {};".format(min_fare,max_fare))
        f=cur.fetchall()
        if not f:
            print('No trips found in this fare range')
        else:
            for h in f:
                print(h)
c1=0

def chh(): 
    global c1
    while True:
        o=input('enter Password : ')
        if o=='123@123':
            c1+=0
            while True:
                print('Enter Choice as 1 to Insert Record \n Enter Choice as 2 to Delete Record \n Enter Choice as 3 to View Records \n Enter Choice as 4 to View a Trip record \n Enter choice as 5 to exit')
                try:
                    ch2=int(input('Enter your choice  to function  : '))
                except ValueError:
                    print('invalid choice')
                    continue
                if ch2==1:
                    while True:
                        b=input('Enter table name to insert record (employee/drivers/cars/customers/trips): ')
                        if b in ('employee','drivers','cars','customers','trips'):
                            insert(b)
                            break
                        else:
                            print('invalid choice')
                elif ch2==2:
                    while True:
                        b=input('Enter table name to delete record (employee/Drivers/cars/customers/trips): ')
                        if b in ('employee','drivers','cars','customers','trips'):
                            Del(b)
                            break
                        else:
                            print('invalid choice')
                elif ch2==3:
                    while True:
                        b=input('Enter table name to view records (employee/drivers/cars/customers/trips): ')
                        if b in ('employee','drivers','cars','customers','trips'):
                            sel(b)
                            break
                        else:
                            print('invalid choice')
                elif ch2==4:
                    while True:
                        b=input('Enter choice to view trips by (customer ID/driver ID/car ID/trip ID/customer name/driver name/car name/all trips/date range/total fare range): ')
                        if b in ('customer ID','driver ID','car ID','trip ID','customer name','driver name','car name','all trips','date range','total fare range'):
                            trip(b)
                            break
                        else:
                            print('invalid choice')
                elif ch2==5:
                    break
                else:
                    print('invalid choice')
            break
        else :
            print('incorrect password')
            c1+=1
            if c1==3:
                print('Too many incorrect attempts. Exiting.')
                break

def chh2():
    while True:
            print('Enter Choice as 1 to Rate a Driver \n Enter Choice as 2 to View a Trip record \n Enter choice as 3 to exit')
            try:
                chh3=int(input('Enter your choice : '))
            except ValueError:
                print('invalid choice')
                continue
            if chh3==1:
                rat()
            elif chh3==2:
                while True:
                    b=input('Enter choice to view trips by (customer ID/driver ID/car ID/trip ID/customer name/driver name/car name/all trips/date range/total fare range): ')
                    if b in ('customer ID','driver ID','car ID','trip ID','customer name','driver name','car name','all trips','date range','total fare range'):
                        trip(b)
                        break
                    else:
                        print('invalid choice')
            elif chh3==3:
                break
            else:
                print('invalid choice')
#inserting Dummy data 
cur.execute('create table if not exists employee ( Emp_id int primary key, Name varchar(25) NOT NULL, Date_of_joining date NOT NULL, Salary int NOT NULL, Dept varchar(20) NOT NULL)')
cur.execute('create table if not exists Drivers ( Driver_id int primary key, Name varchar(25) NOT NULL, Date_of_joining date NOT NULL, Salary int NOT NULL, Rating decimal(3,2) NOT NULL DEFAULT 0.00)')
cur.execute('create table if not exists cars ( Car_id int primary key, plate_no int NOT NULL, car_name varchar(50) NOT NULL, Date_of_commission date NOT NULL, no_of_trips int NOT NULL, last_service date NOT NULL)')
cur.execute('create table if not exists customers ( cust_id int primary key, Cust_name varchar(15) NOT NULL, Date_of_registration date NOT NULL)')
cur.execute('create table if not exists trips ( trip_ID int primary key, cust_id int NOT NULL, Car_id int NOT NULL, Driver_id int NOT NULL, Date_of_booking date NOT NULL, Start_location varchar(50) NOT NULL, Destination varchar(50) NOT NULL, total_km int NOT NULL, total_fare DECIMAL(7,2) NOT NULL)')
cur.execute('insert IGNORE into employee (Emp_id, Name, Date_of_joining, Salary, Dept) values (201, "Alice Johnson", "2019-03-15", 50000, "HR") ')
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (201, 'Rajesh Kumar', '2018-05-12', 55000, 'Operations')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (202, 'Priya Sharma', '2018-07-20', 60000, 'HR')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (203, 'Amit Patel', '2019-01-15', 52000, 'Finance')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (204, 'Sneha Gupta', '2019-03-10', 58000, 'Operations')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (205, 'Vikram Singh', '2019-06-22', 65000, 'IT')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (206, 'Anjali Verma', '2020-02-14', 50000, 'HR')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (207, 'Rohit Desai', '2020-08-05', 62000, 'Operations')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (208, 'Neha Chopra', '2021-01-18', 54000, 'Finance')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (209, 'Arjun Nair', '2021-05-30', 59000, 'Operations')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (210, 'Divya Iyer', '2022-03-12', 56000, 'IT')")
cur.execute("INSERT IGNORE INTO employee (Emp_id, Name, Date_of_joining, Salary, Dept) VALUES (211, 'Karan Malhotra', '2022-09-20', 61000, 'Operations')")
con.commit()
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (101, 'Suresh Reddy', '2018-04-10', 35000, 4.8)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (102, 'Ramesh Rao', '2018-06-15', 34000, 4.6)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (103, 'Mohan Lal', '2018-09-20', 36000, 4.9)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (104, 'Harish Joshi', '2019-02-12', 33000, 4.5)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (105, 'Deepak Bhatt', '2019-05-18', 35500, 4.7)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (106, 'Arun Kumar', '2019-08-25', 34500, 4.4)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (107, 'Sanjay Singh', '2020-01-10', 37000, 4.8)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (108, 'Praveen Nair', '2020-04-22', 35000, 4.6)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (109, 'Nitin Chopra', '2020-07-30', 36500, 4.9)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (110, 'Vikram Desai', '2021-02-14', 34000, 4.5)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (111, 'Ashok Verma', '2021-06-20', 38000, 4.7)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (112, 'Ravi Patel', '2021-11-05', 35500, 4.8)")
cur.execute("INSERT IGNORE INTO Drivers (Driver_id, Name, Date_of_joining, Salary, Rating) VALUES (113, 'Manish Iyer', '2022-03-18', 37500, 4.6)")
con.commit()
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (401, 123456, 'Honda City', '2018-05-10', 450, '2023-02-15')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (402, 234567, 'Maruti Swift', '2018-07-20', 380, '2023-01-20')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (403, 345678, 'Toyota Innova', '2019-02-15', 520, '2023-03-10')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (404, 456789, 'Hyundai Creta', '2019-04-22', 410, '2023-02-25')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (405, 567890, 'Skoda Rapid', '2019-08-10', 390, '2023-01-30')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (406, 678901, 'MG Hector', '2020-01-18', 470, '2023-03-05')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (407, 789012, 'Kia Seltos', '2020-03-25', 430, '2023-02-18')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (408, 890123, 'Tata Nexon', '2020-06-12', 360, '2023-01-15')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (409, 901234, 'Mahindra XUV500', '2020-09-30', 510, '2023-03-20')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (410, 112345, 'Renault Kwid', '2021-02-14', 340, '2023-02-10')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (411, 223456, 'Ford EcoSport', '2021-05-20', 420, '2023-03-15')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (412, 334567, 'Nissan Kicks', '2021-08-15', 380, '2023-01-25')")
cur.execute("INSERT IGNORE INTO cars (Car_id, plate_no, car_name, Date_of_commission, no_of_trips, last_service) VALUES (413, 445678, 'Citroen C5', '2022-01-10', 290, '2023-02-20')")
con.commit()
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (1, 'Rahul Sharma', '2018-06-10')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (2, 'Pooja Singh', '2018-08-15')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (3, 'Arjun Verma', '2018-10-20')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (4, 'Neha Gupta', '2019-01-12')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (5, 'Vikram Patel', '2019-03-18')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (6, 'Anjali Kumar', '2019-05-25')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (7, 'Rohan Desai', '2019-07-30')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (8, 'Priya Nair', '2019-09-14')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (9, 'Karan Singh', '2020-01-20')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (10, 'Divya Reddy', '2020-03-12')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (11, 'Aditya Joshi', '2020-05-18')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (12, 'Sneha Iyer', '2020-07-25')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (13, 'Harsh Malhotra', '2020-09-10')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (14, 'Isha Chopra', '2020-11-15')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (15, 'Siddharth Rao', '2021-01-22')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (16, 'Ananya Singh', '2021-03-30')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (17, 'Nikhil Verma', '2021-05-14')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (18, 'Megha Patel', '2021-07-20')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (19, 'Rajat Kumar', '2021-09-25')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (20, 'Simran Desai', '2021-11-10')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (21, 'Varun Nair', '2022-01-18')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (22, 'Shreya Chopra', '2022-03-25')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (23, 'Abhishek Iyer', '2022-05-12')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (24, 'Riya Malhotra', '2022-07-20')")
cur.execute("INSERT IGNORE INTO customers (cust_id, Cust_name, Date_of_registration) VALUES (25, 'Akshay Reddy', '2022-09-15')")
con.commit()
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (1, 1, 401, 101, '2018-06-15', 'MG Road', 'Whitefield', 25, 375)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (2, 2, 402, 102, '2018-08-20', 'Indiranagar', 'Koramangala', 18, 270)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (3, 3, 403, 103, '2018-10-25', 'Bangalore Central', 'Airport', 35, 525)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (4, 4, 404, 104, '2019-01-15', 'Hebbal', 'Domlur', 22, 330)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (5, 5, 405, 105, '2019-03-22', 'Banjara Hills', 'Gachibowli', 28, 420)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (6, 6, 406, 106, '2019-05-18', 'Secunderabad', 'HITEC City', 32, 480)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (7, 7, 407, 107, '2019-07-30', 'Jubilee Hills', 'Madhapur', 20, 300)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (8, 8, 408, 108, '2019-09-14', 'Kondapur', 'Kukatpally', 24, 360)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (9, 9, 409, 109, '2019-11-20', 'Ameerpet', 'Dilsukhnagar', 26, 390)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (10, 10, 410, 110, '2020-01-25', 'Lakdi Ka Pool', 'Nampally', 15, 225)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (11, 11, 411, 111, '2020-03-18', 'Begum Bazaar', 'Kachiguda', 12, 180)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (12, 12, 412, 112, '2020-05-22', 'Charminar', 'Abids', 8, 120)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (13, 13, 413, 113, '2020-07-30', 'Hyderabad Central', 'Shamshabad', 40, 600)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (14, 14, 401, 101, '2020-09-12', 'Rajendra Nagar', 'Mehdipatnam', 18, 270)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (15, 15, 402, 102, '2020-11-18', 'Chaderghat', 'Tarnaka', 22, 330)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (16, 16, 403, 103, '2021-01-25', 'Panjagutta', 'Fateh Gunj', 19, 285)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (17, 17, 404, 104, '2021-03-30', 'Moghal Pura', 'Moghalpura Station', 14, 210)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (18, 18, 405, 105, '2021-05-14', 'Falaknuma', 'Malakpet', 16, 240)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (19, 19, 406, 106, '2021-07-22', 'Golconda', 'Himayat Nagar', 30, 450)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (20, 20, 407, 107, '2021-09-10', 'Somajiguda', 'Yousufguda', 11, 165)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (21, 21, 408, 108, '2021-11-15', 'Secunderabad Junction', 'Paradise', 23, 345)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (22, 22, 409, 109, '2022-01-20', 'Lakdikapool', 'Yellareddyguda', 27, 405)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (23, 23, 410, 110, '2022-03-25', 'Osman Nagar', 'Vanasthalipuram', 34, 510)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (24, 24, 411, 111, '2022-05-18', 'Qutb Shahi Tomb', 'Disha', 31, 465)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (25, 25, 412, 112, '2022-07-22', 'Taramati Baradari', 'Mir Alam Tank', 21, 315)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (26, 1, 413, 113, '2022-09-10', 'Aparna Arcade', 'Bandlaguda', 38, 570)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (27, 2, 401, 101, '2022-11-14', 'Gowliguda', 'Charminar Road', 13, 195)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (28, 3, 402, 102, '2023-01-08', 'Saidabad', 'Hayathnagar', 36, 540)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (29, 4, 403, 103, '2023-02-15', 'Jublai Hills Road', 'Monda Market', 17, 255)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (30, 5, 404, 104, '2023-03-20', 'Tolichowki', 'Ghatikesar', 29, 435)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (31, 6, 405, 105, '2023-04-12', 'Uppal', 'Narayanguda', 26, 390)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (32, 7, 406, 106, '2023-05-18', 'Karmanghat', 'Mailardevpally', 24, 360)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (33, 8, 407, 107, '2023-06-25', 'Nagol', 'Tandoor', 33, 495)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (34, 9, 408, 108, '2023-07-30', 'Shankarpalli', 'Ibrahimpatnam', 37, 555)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (35, 10, 409, 109, '2023-08-14', 'Chevella', 'Kandukur', 42, 630)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (36, 11, 410, 110, '2023-09-20', 'Pedda Shaikpet', 'Arka Nagar', 19, 285)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (37, 12, 411, 111, '2023-10-05', 'Tellapur', 'Anjaiah Nagar', 25, 375)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (38, 13, 412, 112, '2023-11-10', 'Banasthali', 'Esha Gardens', 28, 420)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (39, 14, 413, 113, '2023-12-15', 'Adarsh Nagar', 'Rajarajeshwari Nagar', 23, 345)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (40, 15, 401, 101, '2024-01-18', 'Champapet', 'Himayathnagar', 31, 465)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (41, 16, 402, 102, '2024-02-22', 'Gachibowli', 'Aparna', 20, 300)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (42, 17, 403, 103, '2024-03-10', 'HITEC City', 'Tellapur', 27, 405)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (43, 18, 404, 104, '2024-04-15', 'Madhapur', 'L B Nagar', 35, 525)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (44, 19, 405, 105, '2024-05-20', 'Kondapur', 'Nanakramguda', 22, 330)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (45, 20, 406, 106, '2024-06-25', 'Kukatpally', 'Bachupally', 18, 270)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (46, 21, 407, 107, '2024-07-30', 'Jeedimetla', 'Miyapur', 24, 360)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (47, 22, 408, 108, '2024-08-14', 'Miyapur', 'Dhulapalli', 29, 435)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (48, 23, 409, 109, '2024-09-18', 'Shamshabad', 'Tandur', 41, 615)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (49, 24, 410, 110, '2024-10-22', 'Tandur', 'Kurnool', 45, 675)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (50, 25, 411, 111, '2024-11-10', 'Kurnool', 'Tirupati', 50, 750)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (51, 1, 412, 112, '2024-12-05', 'Tirupati', 'Renigunta', 32, 480)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (52, 2, 413, 113, '2018-06-18', 'Indiranagar', 'Whitefield', 30, 450)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (53, 3, 401, 101, '2018-09-05', 'Airport', 'HSR Layout', 28, 420)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (54, 4, 402, 102, '2019-02-14', 'Koramangala', 'Bannerghatta', 26, 390)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (55, 5, 403, 103, '2019-04-20', 'Jayanagar', 'Kundalahalli', 24, 360)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (56, 6, 404, 104, '2019-06-15', 'Yeshwantpur', 'Rajajinagar', 20, 300)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (57, 7, 405, 105, '2019-08-22', 'Ulsoor', 'Sumadhura', 22, 330)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (58, 8, 406, 106, '2019-10-30', 'Vijayanagar', 'Basaveshwara', 21, 315)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (59, 9, 407, 107, '2020-02-10', 'Vidhan Soudha', 'Mantri Square', 16, 240)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (60, 10, 408, 108, '2020-04-18', 'Kowdiar', 'Palace Road', 13, 195)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (61, 11, 409, 109, '2020-06-25', 'Mekhri Circle', 'Marathahalli', 25, 375)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (62, 12, 410, 110, '2020-08-12', 'Seshadripuram', 'Ramakrishna Nagar', 19, 285)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (63, 13, 411, 111, '2020-10-20', 'Malleswaram', 'RV Road', 15, 225)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (64, 14, 412, 112, '2020-12-10', 'Frazer Town', 'St Johns Road', 12, 180)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (65, 15, 413, 113, '2021-02-18', 'Shoolay Circle', 'Andhra Bank Road', 14, 210)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (66, 16, 401, 101, '2021-04-22', 'Cantonment Road', 'Thyagaraya Road', 17, 255)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (67, 17, 402, 102, '2021-06-15', 'Sumadhura Nagarabhavi', 'Subramanyapura', 23, 345)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (68, 18, 403, 103, '2021-08-20', 'Sajjan Nagar', 'Yelachenahalli', 27, 405)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (69, 19, 404, 104, '2021-10-14', 'Ramamurthy Nagar', 'CV Raman Nagar', 18, 270)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (70, 20, 405, 105, '2021-12-25', 'Dakshineswar', 'Sumadhura', 31, 465)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (71, 21, 406, 106, '2022-02-14', 'Gottigere', 'Banasthali', 33, 495)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (72, 22, 407, 107, '2022-04-18', 'Kengeri', 'Jnanabharathi', 28, 420)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (73, 23, 408, 108, '2022-06-22', 'Rajarajeshwari Nagar', 'Hanumanthanagar', 25, 375)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (74, 24, 409, 109, '2022-08-10', 'Hanumanthanagar', 'Nagavalli', 26, 390)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (75, 25, 410, 110, '2022-10-15', 'Nagavalli', 'Banashankari', 29, 435)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (76, 1, 411, 111, '2023-01-12', 'Banashankari', 'Peenya', 32, 480)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (77, 2, 412, 112, '2023-03-15', 'Peenya', 'Yeshwantpur', 24, 360)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (78, 3, 413, 113, '2023-05-20', 'Yeshwantpur', 'Indiranagar', 34, 510)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (79, 4, 401, 101, '2023-07-25', 'Indiranagar', 'Whitefield', 38, 570)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (80, 5, 402, 102, '2023-09-18', 'Whitefield', 'Marathahalli', 22, 330)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (81, 6, 403, 103, '2023-11-22', 'Marathahalli', 'Kundalahalli', 19, 285)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (82, 7, 404, 104, '2024-01-10', 'Kundalahalli', 'Koramangala', 26, 390)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (83, 8, 405, 105, '2024-02-14', 'Koramangala', 'Jayanagar', 21, 315)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (84, 9, 406, 106, '2024-03-18', 'Jayanagar', 'HSR Layout', 28, 420)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (85, 10, 407, 107, '2024-04-22', 'HSR Layout', 'Bannerghatta', 23, 345)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (86, 11, 408, 108, '2024-05-25', 'Bannerghatta', 'Ramamurthy Nagar', 35, 525)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (87, 12, 409, 109, '2024-06-30', 'Ramamurthy Nagar', 'CV Raman Nagar', 20, 300)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (88, 13, 410, 110, '2024-07-15', 'CV Raman Nagar', 'Marathahalli', 25, 375)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (89, 14, 411, 111, '2024-08-20', 'Marathahalli', 'Whitefield', 27, 405)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (90, 15, 412, 112, '2024-09-25', 'Whitefield', 'Sarjapur', 30, 450)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (91, 16, 413, 113, '2024-10-10', 'Sarjapur', 'Electronics City', 32, 480)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (92, 17, 401, 101, '2024-11-14', 'Electronics City', 'HSR Layout', 36, 540)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (93, 18, 402, 102, '2024-12-20', 'HSR Layout', 'Indiranagar', 28, 420)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (94, 19, 403, 103, '2019-01-10', 'Airport', 'Whitefield', 32, 480)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (95, 20, 404, 104, '2019-03-15', 'Whitefield', 'Marathahalli', 24, 360)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (96, 21, 405, 105, '2019-05-20', 'Marathahalli', 'Koramangala', 26, 390)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (97, 22, 406, 106, '2019-07-25', 'Koramangala', 'Jayanagar', 19, 285)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (98, 23, 407, 107, '2019-09-30', 'Jayanagar', 'HSR Layout', 21, 315)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (99, 24, 408, 108, '2019-11-10', 'HSR Layout', 'Bannerghatta', 25, 375)")
cur.execute("INSERT IGNORE INTO trips (trip_ID, cust_id, Car_id, Driver_id, Date_of_booking, Start_location, Destination, total_km, total_fare) VALUES (100, 25, 409, 109, '2020-01-15', 'Bannerghatta', 'Electronics City', 40, 600)")
con.commit()
w=tk.Tk()
w.geometry("1000x1000")
w.title("Sunshine Cabs Management System")
l=ttk.Label(master=w , text= 'Welcome to Sunshine Cabs Management System',font=('Brooklyn 24'))
l3=ttk.Label(w,text='Welcome',font='Brooklyn 40 bold')
l1=ttk.Label(master=w , text= 'Please select your portal below:',font=('Brooklyn 16'))
l.pack()
f=ttk.Frame(master=w)
l1.pack(side='top', pady=20)
b1=ttk.Button(master = f , text='Employee Portal', command =chh)
b2=ttk.Button(master = f , text='Customer Portal', command =chh2)
b1.pack(side='left',padx=20)
b2.pack(side='right',padx=20)
b3=ttk.Button(master = f , text='Exit', command =w.destroy)
b3.pack( side='left',pady=250)
l3.pack()
f.pack()
w.mainloop()