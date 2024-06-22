from flask import  session, url_for, redirect
import mysql.connector
from functools import wraps
from decimal import Decimal

db = mysql.connector.connect(host= 'localhost',
                          user= 'root',
                          password='',
                          database='ticket_reservation')

def loginRequired(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for('views.login'))
        return route(*args, **kwargs)
    return wrapper

def loginSatisfied(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if "username" in session:
            if(session.get("role") == "customer"):
                return redirect(url_for('views.customerHome'))
            else:
                return redirect(url_for('views.staffHome'))
        return route(*args, **kwargs)
    return wrapper

def customerOnly(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if(session.get("role") == "staff"):
            return redirect(url_for('views.staffHome'))
        return route(*args, **kwargs)
    return wrapper

def staffOnly(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if(session.get("role") == "customer"):
            return redirect(url_for('views.customerHome'))
        return route(*args, **kwargs)
    return wrapper

def insertPhone(role, username, phone):
    cursor = db.cursor()
    if(role == "customer"):
        query = "INSERT INTO customer_phone VALUES (%s, %s)"
    else:
        query = "INSERT INTO staff_phone VALUES (%s, %s)"
    try:
        cursor.execute(query, (username, phone))
        db.commit()
        cursor.close()
        return 1
    except:
        cursor.close()
        return 0
    
def insertEmail(username, email):
    cursor = db.cursor()
    query = "INSERT INTO staff_email VALUES (%s, %s)"
    try:
        cursor.execute(query, (username, email))
        db.commit()
        cursor.close()
        return 1
    except:
        cursor.close()
        return 0
    
def insertTicket(ticketID, price, airline, flight, deptDate):
    cursor = db.cursor()
    query = "INSERT INTO ticket VALUES (%s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, (ticketID, price, airline, flight, deptDate))
        db.commit()
        cursor.close()
        return 1
    except:
        cursor.close()
        return 0
    
def updatePrice(cursor, airline, flight, deptDate):
    query = """SELECT COUNT(ticket_id) FROM ticket WHERE airline_name = %s AND flight_num = %s AND departure_period = %s AND 
            ticket_id NOT IN (SELECT ticket_id FROM purchase)"""
    cursor.execute(query, (airline, flight, deptDate))
    ticketLeft = cursor.fetchone()[0]
    print(ticketLeft)
    query2 = """SELECT base_price, COUNT(ticket_id) FROM flight NATURAL JOIN ticket WHERE airline_name = %s AND flight_num = %s AND departure_period = %s"""
    cursor.execute(query2, (airline, flight, deptDate))
    info = cursor.fetchone()
    base = info[0]
    totalTickets = info[1]
    print(totalTickets)
    query3 = """UPDATE ticket SET calculated_price = %s WHERE airline_name = %s AND flight_num = %s AND departure_period = %s AND 
                ticket_id NOT IN (SELECT ticket_id FROM purchase)"""
    if(0.2*(totalTickets) >= ticketLeft):
        newPrice = (base*Decimal(0.25)) + base
        cursor.execute(query3, (newPrice, airline, flight, deptDate))
    else:
        cursor.execute(query3, (base, airline, flight, deptDate))

        
        