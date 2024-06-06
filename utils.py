from flask import  session, url_for, redirect
import mysql.connector
from functools import wraps

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