from flask import Blueprint, render_template, request, session, url_for, redirect
from utils import db, loginRequired, loginSatisfied, customerOnly, staffOnly, insertPhone, insertEmail
from datetime import datetime, timedelta
import hashlib
from decimal import Decimal

views = Blueprint(__name__, "view")

@views.route("/")
@loginSatisfied
def homePage():
    return render_template('index.html')

@views.route("/flightInfo", methods=["GET"])
def getFlightInfo():
    srcAirport = request.args.get("src")
    dstAirport = request.args.get("dst")
    deptDate = request.args.get("departure_date")
    arrivalDate = request.args.get("arrival_date")
    cursor = db.cursor()
    query = "SELECT * FROM flight WHERE departure = %s AND arrival = %s AND departure_period LIKE %s"
    query2 = "SELECT * FROM flight WHERE departure = %s AND arrival = %s AND arrival_period LIKE %s"
    cursor.execute(query, (srcAirport, dstAirport, deptDate + "%"))
    flightData = cursor.fetchall()
    roundTrip = ()
    if(arrivalDate):
        cursor.execute(query2, (dstAirport, srcAirport, arrivalDate + "%"))
        roundTrip = cursor.fetchall()
    cursor.close()
    if "username" in session:
        if(session.get("role") == "customer"):
            return render_template('customerHome.html', fname=session["fname"], flightRequest=True, flightData=flightData, roundTrip=roundTrip)
    return render_template('index.html', flightRequest=True, flightData=flightData, roundTrip=roundTrip)
    
@views.route("/flightStatus", methods=["GET"]) 
def getFlightStatus():
    airline = request.args.get("airline")
    flight = request.args.get("flight")
    deptDate = request.args.get("departure_date")
    cursor = db.cursor()
    query = "SELECT * FROM flight WHERE airline_name = %s AND flight_num = %s AND departure_period LIKE %s"
    cursor.execute(query, (airline, flight, deptDate + "%"))
    statusData = cursor.fetchone()
    cursor.close()
    if "username" in session:
        if(session.get("role") == "customer"):
            return render_template('customerHome.html', fname=session["fname"], statusRequest=True, statusData=statusData)
        return render_template('staffHome.html', fname=session["fname"], statusRequest=True, statusData=statusData)
    return render_template('index.html', statusRequest=True, statusData=statusData)

@views.route("/login")
@loginSatisfied
def login():
    return render_template('login.html')

@views.route("/loginAuth", methods=["POST"])
def loginAuth():
    username = request.form.get("username")
    password = request.form.get("password")
    person = request.form.get("selection")
    passwordHash = hashlib.md5(password.encode()).hexdigest()
    cursor = db.cursor()
    if(person == "customer"):
        query = "SELECT fname FROM customer WHERE email = %s AND password = %s"
    else:
        query = "SELECT fname FROM staff WHERE username = %s AND password = %s"
    cursor.execute(query, (username, passwordHash))
    data = cursor.fetchone()
    cursor.close()
    if(data):
        session["username"] = username
        session["fname"] = data[0]
        if(person == "customer"):
            session["role"] = "customer"
            return redirect(url_for('views.customerHome'))
        else:
            session["role"] = "staff"
            query2 = "SELECT airline_name FROM staff WHERE username = %s"
            cursor2 = db.cursor()
            cursor2.execute(query2, (username,))
            airline = cursor2.fetchone()[0]
            session["airline"] = airline
            cursor2.close()
            return redirect(url_for('views.staffHome'))
    else:
        error = "Incorrect username/password"
        return render_template('login.html', error=error)


@views.route("/customerReg")
@loginSatisfied
def customerReg():
    return render_template('customerReg.html')

@views.route("/customerRegAuth", methods=["POST"])
def customerRegAuth():
    email = request.form.get("email")
    cursor = db.cursor()
    check = "SELECT * FROM customer WHERE email = %s"
    cursor.execute(check, (email,))
    alrExists = cursor.fetchone()
    if(alrExists):
        cursor.close()
        error = "User already exists"
        return render_template('customerReg.html', error=error)
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        password = request.form.get("password")
        phone = request.form.get("phone")
        buildNum = request.form.get("buildNum")
        street = request.form.get("street")
        apt = request.form.get("apt")
        city = request.form.get("city")
        state = request.form.get("state")
        zipNum = request.form.get("zip")
        passNum = request.form.get("passNum")
        passExp = request.form.get("passExp")
        passCountry = request.form.get("passCountry")
        dob = request.form.get("DOB")
        passwordHash = hashlib.md5(password.encode()).hexdigest()
        query = "INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        query2 = "INSERT INTO customer_phone VALUES(%s, %s);"
        cursor.execute(query, (email, fname, lname, passwordHash, buildNum, street, apt, city, state, zipNum, passNum, passExp, passCountry, dob))
        cursor.execute(query2, (email, phone))
        db.commit()
        cursor.close()
        session["username"] = email
        session["fname"] = fname
        session["role"] = "customer"
        return redirect(url_for('views.customerHome'))

@views.route("/staffReg")
@loginSatisfied
def staffReg():
    return render_template('staffReg.html')

@views.route("/staffRegAuth", methods=["POST"])
def staffRegAuth():
    username = request.form.get("username")
    cursor = db.cursor()
    check = "SELECT * FROM staff WHERE username = %s"
    cursor.execute(check, (username,))
    alrExists = cursor.fetchone()
    if(alrExists):
        cursor.close()
        error = "User already exists"
        return render_template('staffReg.html', error=error)
    else:
        email = request.form.get("email")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        password = request.form.get("password")
        phone = request.form.get("phone")
        airline = request.form.get("airline")
        dob = request.form.get("DOB")
        passwordHash = hashlib.md5(password.encode()).hexdigest()
        query = "INSERT INTO staff VALUES(%s, %s, %s, %s, %s, %s);"
        query2 = "INSERT INTO staff_phone VALUES(%s, %s);"
        query3 = "INSERT INTO staff_email VALUES(%s, %s)"
        cursor.execute(query, (username, passwordHash, fname, lname, dob, airline))
        cursor.execute(query2, (username, phone))
        cursor.execute(query3, (username, email))
        db.commit()
        cursor.close()
        session["username"] = username
        session["fname"] = fname
        session["role"] = "staff"
        session["airline"] = airline
        return redirect(url_for('views.staffHome'))

@views.route("/customerHome")
@loginRequired
@customerOnly
def customerHome():
    return render_template('customerHome.html', fname=session["fname"])

@views.route("/staffHome")
@loginRequired
@staffOnly
def staffHome():
    return render_template('staffHome.html', fname=session["fname"])

@views.route("/logout")
@loginRequired
def logout():
    session.clear()
    return redirect(url_for('views.login'))

@views.route("/viewFlights", methods=["GET"])
@loginRequired
@customerOnly
def viewFlights():
    currentTime = datetime.now()
    cursor = db.cursor()
    query = """SELECT T.ticket_id, F.airline_name, F.flight_num, F.departure_period, F.departure, F.arrival_period, F.arrival 
            FROM flight AS F NATURAL JOIN ticket AS T NATURAL JOIN purchase WHERE email = %s AND departure_period > %s ORDER BY departure_period"""    
    cursor.execute(query, (session.get("username"), currentTime))
    viewData = cursor.fetchall()
    cursor.close()
    return render_template('customerHome.html', fname=session["fname"], viewRequest=True ,viewData=viewData)

@views.route("/purchasePage", methods=["GET"])
@loginRequired
@customerOnly
def purchasePage():
    airline = request.args.get("airline")
    flight = request.args.get("flight")
    deptDate = request.args.get("departure_period")
    airline2 = request.args.get("airline2")
    flight2 = request.args.get("flight2")
    deptDate2 = request.args.get("departure_period2")
    cursor = db.cursor()
    query = """SELECT ticket_id, calculated_price FROM ticket WHERE airline_name = %s AND flight_num = %s AND departure_period = %s AND 
            ticket_id NOT IN (SELECT ticket_id FROM purchase)"""
    cursor.execute(query, (airline, flight, deptDate))
    available = cursor.fetchall()
    available2 = ()
    if(airline2):
        cursor.execute(query, (airline2, flight2, deptDate2))
        available2 = cursor.fetchall()
    cursor.close()
    return render_template('purchasePage.html', available=available, airline=airline, flight=flight, departure_period=deptDate, available2=available2, airline2=airline2, flight2=flight2, departure_period2=deptDate2)

@views.route("/purchase", methods=["POST"])
@loginRequired
@customerOnly
def purchase():
    ticket = request.form.get("ticket")
    ticket2 = request.form.get("ticket2")
    cardType = request.form.get("selection")
    cardNum = request.form.get("cardNum")
    cardName = request.form.get("cardName")
    exp = request.form.get("exp")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    dob = request.form.get("DOB")
    airline = request.form.get("airline")
    flight = request.form.get("flight")
    deptDate = request.form.get("departure_period")
    airline2 = request.form.get("airline2")
    flight2 = request.form.get("flight2")
    deptDate2 = request.form.get("departure_period2")
    cursor = db.cursor()
    query = """INSERT INTO purchase(ticket_id, email, card_type, card_num, card_name, expiration, fname, lname, DOB) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (ticket, session.get("username"), cardType, cardNum, cardName, exp, fname, lname, dob))
    query2 = """SELECT COUNT(ticket_id) FROM ticket WHERE airline_name = %s AND flight_num = %s AND departure_period = %s AND 
            ticket_id NOT IN (SELECT ticket_id FROM purchase)"""
    cursor.execute(query2, (airline, flight, deptDate))
    ticketLeft = cursor.fetchone()[0]
    query3 = """SELECT base_price, COUNT(ticket_id) FROM flight NATURAL JOIN ticket WHERE airline_name = %s AND flight_num = %s AND departure_period = %s"""
    cursor.execute(query3, (airline, flight, deptDate))
    info = cursor.fetchone()
    base = info[0]
    totalTickets = info[1]
    if(0.2*(totalTickets) >= ticketLeft):
        newPrice = (base*Decimal(0.25)) + base
        query4 = """UPDATE ticket SET calculated_price = %s WHERE airline_name = %s AND flight_num = %s AND departure_period = %s AND 
                 ticket_id NOT IN (SELECT ticket_id FROM purchase)"""
        cursor.execute(query4, (newPrice, airline, flight, deptDate))
    if(ticket2):
        cursor.execute(query, (ticket2, session.get("username"), cardType, cardNum, cardName, exp, fname, lname, dob))
        cursor.execute(query2, (airline2, flight2, deptDate2))
        ticketLeft = cursor.fetchone()[0]
        cursor.execute(query3, (airline2, flight2, deptDate2))
        info = cursor.fetchone()
        base = info[0]
        totalTickets = info[1]
        if(0.2*(totalTickets) >= ticketLeft):
            newPrice = (base*Decimal(0.25)) + base
            cursor.execute(query4, (newPrice, airline2, flight2, deptDate2))
    db.commit()
    cursor.close()
    purchase="Purchase complete."
    return render_template('customerHome.html', fname=session["fname"], purchase=purchase)
    
@views.route("/cancel", methods=["POST"])
@loginRequired
@customerOnly
def cancel():
    ticket = request.form.get("ticket")
    deptDate = request.form.get("departure_period")
    currentTime = datetime.now()
    deptDate = datetime.strptime(deptDate, "%Y-%m-%d %H:%M:%S")
    query = "DELETE FROM purchase WHERE ticket_id = %s"
    if((deptDate - currentTime) > timedelta(hours=24)):
        airline = request.form.get("airline")
        flight = request.form.get("flight")
        cursor = db.cursor()
        cursor.execute(query, (ticket,))
        query2 = """SELECT COUNT(ticket_id) FROM ticket WHERE airline_name = %s AND flight_num = %s AND departure_period = %s AND 
                 ticket_id NOT IN (SELECT ticket_id FROM purchase)"""
        cursor.execute(query2, (airline, flight, deptDate))
        ticketLeft = cursor.fetchone()[0]
        query3 = """SELECT base_price, COUNT(ticket_id) FROM flight NATURAL JOIN ticket WHERE airline_name = %s AND flight_num = %s AND departure_period = %s"""
        cursor.execute(query3, (airline, flight, deptDate))
        info = cursor.fetchone()
        base = info[0]
        totalTickets = info[1]
        if(0.2*(totalTickets) < ticketLeft):
            query4 = """UPDATE ticket SET calculated_price = %s WHERE airline_name = %s AND flight_num = %s AND departure_period = %s AND 
                    ticket_id NOT IN (SELECT ticket_id FROM purchase)"""
            cursor.execute(query4, (base, airline, flight, deptDate))
        db.commit()
        cursor.close()
        return render_template('customerHome.html', fname=session["fname"])
    cancel = "Flight cancellations are not permitted within 24 hours of departure."
    return render_template('customerHome.html', fname=session["fname"], cancel=cancel)

@views.route("/potReview", methods=["GET"])
@loginRequired
@customerOnly
def potReview():
    currentTime = datetime.now()
    cursor = db.cursor()
    query = """SELECT DISTINCT airline_name, flight_num, departure_period FROM purchase NATURAL JOIN ticket WHERE email = %s AND 
            departure_period < %s AND (email, airline_name, flight_num, departure_period) NOT IN (SELECT email, airline_name, 
            flight_num, departure_period FROM review)"""
    cursor.execute(query,(session.get("username"), currentTime))
    reviewData = cursor.fetchall()
    return render_template('customerHome.html', fname=session["fname"], reviewRequest=True, reviewData=reviewData)
    
@views.route("/reviewPage", methods=["GET"])
@loginRequired
@customerOnly
def reviewPage():
    airline = request.args.get("airline")
    flight = request.args.get("flight")
    deptDate = request.args.get("departure_period")
    return render_template('reviewPage.html', airline=airline, flight=flight, departure_period=deptDate)

@views.route("/review", methods=["POST"])
@loginRequired
@customerOnly
def review():
    airline = request.form.get("airline")
    flight = request.form.get("flight")
    deptDate = request.form.get("departure_period")
    rating = request.form.get("rating")
    comment = request.form.get("comment")
    cursor = db.cursor()
    query = "INSERT INTO review VALUES(%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (session.get("username"), airline, flight, deptDate, rating, comment))
    db.commit()
    cursor.close()
    review = "Review submitted."
    return render_template('customerHome.html', fname=session["fname"], review=review)
    
@views.route("/trackSpending", methods=["GET"])
@loginRequired
@customerOnly
def track():
    start = request.args.get("start")
    end = request.args.get("end")
    query = "SELECT SUM(calculated_price) AS total FROM purchase NATURAL JOIN ticket WHERE email = %s AND DATE(period) BETWEEN %s AND %s"
    query2 = """SELECT DATE_FORMAT(period, '%Y-%m') AS month, SUM(calculated_price) AS total FROM purchase NATURAL JOIN ticket 
             WHERE email = %s AND DATE(period) BETWEEN %s AND %s GROUP BY MONTH"""
    if(start == "" and end == ""):
        end = datetime.now().date()
        start = end - timedelta(days=180)
        if(start.year < end.year):
            start = datetime(end.year, 1, 1).date()
    if((start == "" and end != "") or (start != "" and end == "")):
        error = "Specify both a start and end date, or utilize the default track option."
        return render_template('customerHome.html', fname=session["fname"], trackError=error)
    cursor = db.cursor()
    cursor.execute(query, (session.get("username"), start, end))
    total = cursor.fetchone()
    cursor.execute(query2, (session.get("username"), start, end))
    monthlyData = cursor.fetchall()
    cursor.close()
    return render_template('customerHome.html', fname=session["fname"], trackRequest= True, total=total, monthlyData=monthlyData, start=start, end=end)

@views.route("/airlineFlights", methods=["GET"])
@loginRequired
@staffOnly
def airlineFlights():
    start = request.args.get("start")
    end = request.args.get("end")
    query = "SELECT flight_num, departure_period FROM flight WHERE airline_name = %s AND departure_period BETWEEN %s AND %s"
    if((start == "" and end != "") or (start != "" and end == "")):
        error = "Specify both a start and end date, or utilize the default view option."
        return render_template('staffHome.html', fname=session["fname"], viewError=error)
    if(start == "" and end == ""):
        start = datetime.now()
        end = start + timedelta(days=30)
    else:
        start += " 00:00:00"
        end += " 00:00:00"
    cursor = db.cursor()
    cursor.execute(query, (session.get("airline"), start, end))
    flightData = cursor.fetchall()
    cursor.close()
    return render_template('staffHome.html', fname=session["fname"], flightRequest=True, flightData=flightData)

@views.route("/flightCustomers", methods=["GET"])
@loginRequired
@staffOnly
def flightCustomers():
    flight = request.args.get("flight")
    deptDate = request.args.get("departure_period")
    cursor = db.cursor()
    query = """SELECT DISTINCT C.email, C.fname, C.lname FROM ticket AS T NATURAL JOIN purchase AS P JOIN customer AS C 
            WHERE P.email = C.email AND T.airline_name = %s AND T.flight_num = %s AND T.departure_period = %s"""
    cursor.execute(query, (session.get("airline"), flight, deptDate))
    customerData = cursor.fetchall()
    cursor.close()
    return render_template('staffHome.html', fname=session["fname"], customerData=customerData, airline=session.get("airline"), flight=flight, deptDate=deptDate)

@views.route("/changeStatus", methods=["POST"])
@loginRequired
@staffOnly
def changeStatus():
    flight = request.form.get("flight")
    deptDate = request.form.get("departure_period")
    status = request.form.get("selection")
    cursor = db.cursor()
    query = "UPDATE flight SET status = %s WHERE airline_name = %s AND flight_num = %s AND departure_period = %s"
    cursor.execute(query, (status, session.get("airline"), flight, deptDate))
    db.commit()
    cursor.close()
    return redirect(url_for('views.staffHome'))

@views.route("/createFlight", methods=["POST"])
@loginRequired
@staffOnly
def createFlight():
    src = request.form.get("src")
    dst = request.form.get("dst")
    cursor = db.cursor()
    check = "SELECT type, country FROM airport WHERE code = %s"
    query = "INSERT INTO flight VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(check, (src,))
    data = cursor.fetchone()
    error = "Error: Enter a valid code"
    if(data):
        srcType = data[0]
        srcCountry = data[1]
    else:
        return render_template('staffHome.html', fname=session["fname"], flightError=error)
    cursor.execute(check, (dst,))
    data = cursor.fetchone()
    if(data):
        dstType = data[0]
        dstCountry = data[1]
    else:
        return render_template('staffHome.html', fname=session["fname"], flightError=error)
    if(srcType == "Domestic" and dstType == "International"):
        cursor.close()
        error = "Error: Cannot have a Domestic flight to an International airport"
        return render_template('staffHome.html', fname=session["fname"], flightError=error)
    elif(srcType == "International" and dstType == "Domestic"):
        cursor.close()
        error = "Error: Cannot have a International flight to an Domestic airport"
        return render_template('staffHome.html', fname=session["fname"], flightError=error)
    else:
        if(((srcType == "Domestic") or (srcType == "Both" and dstType == "Domestic")) and (srcCountry != dstCountry)):
            error = "Error: Cannot have a Domestic flight to anther country"
            return render_template('staffHome.html', fname=session["fname"], flightError=error)
        flight = request.form.get("flight")
        deptDate = request.form.get("departure_period")
        arrivalDate = request.form.get("arrival_period")
        price = request.form.get("price")
        airplaneID = request.form.get("airplaneID")
        status = request.form.get("status")
        check2 = """SELECT maintenance_start, maintenance_end FROM maintenance WHERE airline_name = %s AND airplane_id = %s AND ((%s BETWEEN maintenance_start 
                 AND maintenance_end) OR (%s BETWEEN maintenance_start AND maintenance_end) OR (maintenance_start >= %s AND maintenance_end <= %s));"""
        cursor.execute(check2, (session.get("airline"), airplaneID, deptDate, arrivalDate, deptDate, arrivalDate))
        conflict = cursor.fetchone()
        if(conflict):
            cursor.close()
            error = f"Error: Cannot schedule a flight during maintenance ({conflict[0]} - {conflict[1]})"
            return render_template('staffHome.html', fname=session["fname"], flightError=error)
        cursor.execute(query, (session.get("airline"), flight, deptDate, src, arrivalDate, dst, price, airplaneID, status))
        db.commit()
        cursor.close()
        message = "Successfully created flight"
        return render_template('staffHome.html', fname=session["fname"], flightMessage=message)

@views.route("/addPlane", methods=["POST"])
@loginRequired
@staffOnly
def addPlane():
    airplaneID = request.form.get("airplaneID")
    check = "SELECT * FROM airplane WHERE airline_name = %s AND airplane_id = %s"
    cursor = db.cursor()
    cursor.execute(check, (session.get("airline"), airplaneID))
    airplaneExists = cursor.fetchone()
    if(airplaneExists):
        error = f"Error: AirplaneID {airplaneExists[1]} already exists"
        return render_template('staffHome.html', fname=session["fname"], airplaneError=error)
    numSeats = request.form.get("numSeats")
    manufacturer = request.form.get("man")
    model = request.form.get("model")
    manDate = request.form.get("manDate")
    query = "INSERT INTO airplane VALUES(%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (session.get("airline"), airplaneID, numSeats, manufacturer, model, manDate))
    db.commit()
    cursor.close()
    message = "Successfully added"
    return render_template('staffHome.html', fname=session["fname"], airplaneMessage=message)

@views.route("/addPort", methods=["POST"])
@loginRequired
@staffOnly
def addPort():
    code = request.form.get("code")
    check = "SELECT * FROM airport WHERE code = %s"
    cursor = db.cursor()
    cursor.execute(check, (code,))
    airportExists = cursor.fetchone()
    if(airportExists):
        error = "Error: Airport already exists"
        return render_template('staffHome.html', fname=session["fname"], airportError=error)
    name = request.form.get("name")
    city = request.form.get("city")
    country = request.form.get("country")
    terminals = request.form.get("terminals")
    airportType = request.form.get("type")
    query = "INSERT INTO airport VALUES(%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (code, name, city, country, terminals, airportType))
    db.commit()
    cursor.close()
    message = "Successfully added"
    return render_template('staffHome.html', fname=session["fname"], airportMessage=message)

@views.route("/viewReviews", methods=["GET"])
@loginRequired
@staffOnly
def viewReviews():
    flight = request.args.get("flight")
    deptDate = request.args.get("departure_date")
    cursor = db.cursor()
    query = """SELECT AVG(R.rating) FROM flight AS F NATURAL JOIN review AS R WHERE F.airline_name = %s AND F.flight_num = %s AND 
            DATE(F.departure_period) = %s AND TIME(F.departure_period) LIKE %s GROUP BY F.airline_name, F.flight_num, F.departure_period"""
    query2 = """SELECT C.email, C.fname, C.lname, R.rating, R.comment FROM flight AS F NATURAL JOIN review AS R NATURAL JOIN customer AS C 
            WHERE F.airline_name = %s AND F.flight_num = %s AND DATE(F.departure_period) = %s AND TIME(F.departure_period) LIKE %s"""
    cursor.execute(query, (session.get("airline"), flight, deptDate[0:10], deptDate[11:] + "%"))
    avgRating = cursor.fetchone()
    cursor.execute(query2, (session.get("airline"), flight, deptDate[0:10], deptDate[11:] + "%"))
    reviews = cursor.fetchall()
    cursor.close()
    flightReview = f"Flight {flight} with departure {deptDate}"
    return render_template('staffHome.html', fname=session["fname"], reviewRequest=True, flightReview=flightReview, avgRating=avgRating, reviews=reviews)

@views.route("/maintenance", methods=["POST"])
@loginRequired
@staffOnly
def maintenance():
    mainID = request.form.get("mainID")
    check = "SELECT * FROM maintenance WHERE maintenance_id = %s"
    cursor = db.cursor()
    cursor.execute(check, (mainID,))
    idExists = cursor.fetchone()
    if(idExists):
        cursor.close()
        error = "Error: MaintenanceID already exists, try a different one"
        return render_template('staffHome.html', fname=session["fname"], maintenanceError=error)
    airplaneID = request.form.get("airplaneID")
    start = request.form.get("start")
    end = request.form.get("end")
    query = "INSERT INTO maintenance VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (mainID, start, end, session.get("airline"), airplaneID))
    db.commit()
    cursor.close()
    message = f"Successully scheduled maintenance for Airplane {airplaneID}"
    return render_template('staffHome.html', fname=session["fname"], mainMessage=message)

@views.route("/frequentCustomer", methods=["GET"])
@loginRequired
@staffOnly
def frequentCustomer():
    currDate = datetime.now().date()
    yearAgo = datetime(currDate.year, 1, 1).date()
    cursor = db.cursor()
    query = "SELECT email, COUNT(*) AS flights FROM ticket NATURAL JOIN purchase WHERE airline_name = %s AND departure_period BETWEEN %s and %s GROUP BY email ORDER BY flights DESC LIMIT 1"
    cursor.execute(query, (session.get("airline"), yearAgo, currDate))
    mostFrequent = cursor.fetchone()
    cursor.close()
    if(mostFrequent):
        return render_template('staffHome.html', fname=session["fname"], mostFrequent=mostFrequent)
    message = "No most frequent customer"
    return render_template('staffHome.html', fname=session["fname"], messageFrequent=message)

@views.route("/viewCustomerFlights", methods=["GET"])
@loginRequired
@staffOnly
def viewCustomerFlights():
    customer = request.args.get("customer")
    cursor = db.cursor()
    query = "SELECT flight_num, departure_period FROM ticket NATURAL JOIN purchase WHERE airline_name = %s AND email = %s"
    cursor.execute(query, (session.get("airline"), customer))
    customerFlights = cursor.fetchall()
    cursor.close()
    if(customerFlights):
        return render_template('staffHome.html', fname=session["fname"], customerFlights=customerFlights, customer=customer)
    customerFlightError = f"Error: Customer with email: {customer} does not exist or been on any flights"
    return render_template('staffHome.html', fname=session["fname"], customerFlightError=customerFlightError)

@views.route("/viewRevenue", methods=["GET"])
@loginRequired
@staffOnly
def viewRevenue():
    currDate = datetime.now()
    monthAgo = datetime(currDate.year, currDate.month, 1).date()
    yearAgo = datetime(currDate.year, 1, 1).date()
    cursor = db.cursor()
    query = "SELECT SUM(calculated_price) AS total FROM ticket NATURAL JOIN purchase WHERE airline_name = %s AND period BETWEEN %s AND %s"
    cursor.execute(query, (session.get("airline"), monthAgo, currDate))
    monthTotal = cursor.fetchone()
    cursor.execute(query, (session.get("airline"), yearAgo, currDate))
    yearTotal = cursor.fetchone()
    cursor.close()
    print(monthTotal, yearTotal)
    return render_template('staffHome.html', fname=session["fname"], revenueRequest=True, monthTotal=monthTotal, yearTotal=yearTotal)

@views.route("/addPhone", methods=["POST"])
@loginRequired
def addPhone():
    role = session.get("role")
    username = session.get("username")
    phone = request.form.get("phone")
    commited = insertPhone(role, username, phone)
    if(role == "customer"):
        if(commited):
            return render_template('customerHome.html', fname=session["fname"], addRequest=f"Successfully added {phone} as a contact")
        else:
            return render_template('customerHome.html', fname=session["fname"], addRequestError=f"{phone} is already registered as a contact")
    else:
        if(commited):
            return render_template('staffHome.html', fname=session["fname"], addContactRequest=f"Successfully added {phone} as a contact")
        else:
            return render_template('staffHome.html', fname=session["fname"], addContactError=f"{phone} is already registered as a contact")
    
@views.route("/addEmail", methods=["POST"])
@loginRequired
@staffOnly
def addEmail():
    username = session.get("username")
    email = request.form.get("email")
    commited = insertEmail(username, email)
    if(commited):
        return render_template('staffHome.html', fname=session["fname"], addContactRequest=f"Successfully added {email} as a contact")
    else:
        return render_template('staffHome.html', fname=session["fname"], addContactError=f"{email} is already registered as a contact")
   

    


    

    


