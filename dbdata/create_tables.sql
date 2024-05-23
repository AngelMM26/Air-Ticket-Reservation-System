CREATE TABLE airport(
    code VARCHAR(3),
    name VARCHAR(50),
    city VARCHAR(50),
    country VARCHAR(50),
    num_of_terminals INT,
    type VARCHAR(20),
    PRIMARY KEY(code)
);

CREATE TABLE airline(
    airline_name VARCHAR(50),
    PRIMARY KEY(airline_name)
);

CREATE TABLE airplane(
    airline_name VARCHAR(50),
    airplane_id INT,
    num_of_seats INT,
    manufacturer VARCHAR(50),
    model VARCHAR(25),
    manufacturing_date DATE,
    PRIMARY KEY(airline_name, airplane_id),
    FOREIGN KEY(airline_name) REFERENCES airline(airline_name)
);

CREATE TABLE maintenance(
    maintenance_start DATETIME,
    maintenance_end DATETIME,
    airline_name VARCHAR(50),
    airplane_id INT,
    PRIMARY KEY(maintenance_start),
    FOREIGN KEY(airline_name, airplane_id) REFERENCES airplane(airline_name, airplane_id)
);

CREATE TABLE staff(
    username VARCHAR(50),
    password VARCHAR(50),
    fname VARCHAR(50),
    lname VARCHAR(50),
    DOB DATE,
    airline_name VARCHAR(50),
    PRIMARY KEY(username),
    FOREIGN KEY(airline_name) REFERENCES airline(airline_name)
);

CREATE TABLE staff_phone(
    username VARCHAR(50),
    phone_num VARCHAR(20),
    PRIMARY KEY(username, phone_num),
    FOREIGN KEY(username) REFERENCES staff(username)
);

CREATE TABLE staff_email(
    username VARCHAR(50),
    email VARCHAR(320),
    PRIMARY KEY(username, email),
    FOREIGN KEY(username) REFERENCES staff(username)
);

CREATE TABLE flight(
    airline_name VARCHAR(50),
    flight_num VARCHAR(10),
    departure_period DATETIME,
    departure VARCHAR(3),
    arrival_period DATETIME,
    arrival VARCHAR(3),
    base_price NUMERIC(10,2),
    airplane_id INT,
    status VARCHAR(10),
    PRIMARY KEY(airline_name, flight_num, departure_period),
    FOREIGN KEY(airline_name) REFERENCES airline(airline_name),
    FOREIGN KEY(departure) REFERENCES airport(code),
    FOREIGN KEY(arrival) REFERENCES airport(code),
    FOREIGN KEY(airline_name, airplane_id) REFERENCES airplane(airline_name, airplane_id)
);

CREATE TABLE ticket(
    ticket_id VARCHAR(10),
    calculated_price NUMERIC(10,2),
    airline_name VARCHAR(50),
    flight_num VARCHAR(10),
    departure_period DATETIME,
    PRIMARY KEY(ticket_id),
    FOREIGN KEY(airline_name, flight_num, departure_period) REFERENCES flight(airline_name, flight_num, departure_period)
);

CREATE TABLE customer(
    email VARCHAR(320),
    fname VARCHAR(50),
    lname VARCHAR(50),
    password VARCHAR(50),
    building_num INT,
    street VARCHAR(50),
    apt_num VARCHAR(10),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code INT,
    passport_num INT,
    passport_exp DATE,
    passport_country VARCHAR(50),
    DOB DATE,
    PRIMARY KEY(email)
);

CREATE TABLE customer_phone(
    email VARCHAR(320),
    phone_num VARCHAR(20),
    PRIMARY KEY(email, phone_num),
    FOREIGN KEY(email) REFERENCES customer(email)
);


CREATE TABLE purchase(
    ticket_id VARCHAR(10),
    email VARCHAR(320),
    card_type VARCHAR(6),
    card_num VARCHAR(20),
    card_name VARCHAR(50),
    expiration DATE,
    fname VARCHAR(50),
    lname VARCHAR(50),
    DOB date,
    period TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(ticket_id),
    FOREIGN KEY(ticket_id) REFERENCES ticket(ticket_id)
);

CREATE TABLE review(
    email VARCHAR(320),
    airline_name VARCHAR(50),
    flight_num VARCHAR(10),
    departure_period DATETIME,
    rating INT,
    comment VARCHAR(500),
    PRIMARY KEY(email, airline_name, flight_num, departure_period),
    FOREIGN KEY(email) REFERENCES customer(email),
    FOREIGN KEY(airline_name, flight_num, departure_period) REFERENCES flight(airline_name, flight_num, departure_period)
);




