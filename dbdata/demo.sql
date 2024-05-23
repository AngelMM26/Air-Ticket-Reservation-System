INSERT INTO airline VALUES("United");

-- INSERT INTO staff VALUES ("admin", "e2fc714c4727ee9395f324cd2e7f331f", "Max", "Mejia", "2000-09-18", "United");
-- INSERT INTO staff_email VALUES("admin", "staff@nyu.edu");
-- INSERT INTO staff_phone VALUES("admin", "111-2222-3333");
-- INSERT INTO staff_phone VALUES("admin", "444-5555-6666");

INSERT INTO airplane VALUES("United", 1, 4, "Boeing", "B-101", "2013-05-02");
INSERT INTO airplane VALUES("United", 2, 4, "Airbus", "A-101", "2011-05-02");
INSERT INTO airplane VALUES("United", 3, 50, "Boeing", "B-101", "2015-05-02");

INSERT INTO maintenance VALUES("2024-06-27 13:25:25", "2024-06-29 07:25:25", "United", 1 );
INSERT INTO maintenance VALUES("2024-01-27 13:25:25", "2024-01-29 07:25:25", "United", 2 );

INSERT INTO airport VALUES("JFK", "JFK", "NYC", "USA", 4, "Both");
INSERT INTO airport VALUES("BOS", "BOS", "Boston", "USA", 2, "Both");
INSERT INTO airport VALUES("PVG", "PVG", "Shanghai", "China", 2, "Both");
INSERT INTO airport VALUES("BEI", "BEI", "Beijing", "China", 2, "Both");
INSERT INTO airport VALUES("SFO", "SFO", "San Fransisco", "USA", 4, "Both");
INSERT INTO airport VALUES("LAX", "LAX", "Los Angeles", "USA", 2, "Both");
INSERT INTO airport VALUES("HKA", "HKA", "Hong Kong", "China", 2, "Both");
INSERT INTO airport VALUES("SHEN", "SHEN", "Shenzhen", "China", 2, "Both");


-- INSERT INTO customer VALUES("testcustomer@nyu.edu", "Jon", "Snow", "81dc9bdb52d04dc20036dbd8313ed055", 1555, "Jay St", NULL, "Brooklyn", "New York", NULL, 54321, "2025-12-24", "USA", "1999-12-19");
-- INSERT INTO customer VALUES("user1@nyu.edu", "Alice", "Bob", "81dc9bdb52d04dc20036dbd8313ed055", 5405, "Jay Street", NULL, "Brooklyn", "New York", NULL, 54322, "2025-12-25", "USA", "1999-11-19");
-- INSERT INTO customer VALUES("user2@nyu.edu", "Cathy", "Wood", "81dc9bdb52d04dc20036dbd8313ed055", 1702, "Jay Street", NULL, "Brooklyn", "New York", NULL, 54323, "2025-10-24", "USA", "1999-10-19");
-- INSERT INTO customer VALUES("user3@nyu.edu", "Trudy", "Jones", "81dc9bdb52d04dc20036dbd8313ed055", 1890, "Jay Street", NULL, "Brooklyn", "New York", NULL, 54324, "2025-09-24", "USA", "1999-09-19");

-- INSERT INTO customer_phone VALUES("testcustomer@nyu.edu", "123-4321-4321");
-- INSERT INTO customer_phone VALUES("user1@nyu.edu", "123-4322-4322");
-- INSERT INTO customer_phone VALUES("user2@nyu.edu", "123-4323-4323");
-- INSERT INTO customer_phone VALUES("user3@nyu.edu", "123-4324-4324");

INSERT INTO flight VALUES("United", "102", "2024-02-12 13:25:25", "SFO", "2024-02-12 16:50:25", "LAX", 300.00, 3, "on-time");
INSERT INTO flight VALUES("United", "104", "2024-03-04 13:25:25", "PVG", "2024-03-04 16:50:25", "BEI", 300.00, 3, "on-time");
INSERT INTO flight VALUES("United", "106", "2024-01-04 13:25:25", "SFO", "2024-01-04 16:50:25", "LAX", 350.00, 3, "delayed");
INSERT INTO flight VALUES("United", "206", "2024-07-04 13:25:25", "SFO", "2024-07-04 16:50:25", "LAX", 400.00, 2, "on-time");
INSERT INTO flight VALUES("United", "207", "2024-08-04 13:25:25", "LAX", "2024-08-04 16:50:25", "SFO", 300.00, 2, "on-time");
INSERT INTO flight VALUES("United", "134", "2024-12-12 13:25:25", "JFK", "2024-12-12 16:50:25", "BOS", 300.00, 3, "delayed");
INSERT INTO flight VALUES("United", "296", "2024-05-30 13:25:25", "PVG", "2024-05-30 16:50:25", "SFO", 3000.00, 1, "on-time");
INSERT INTO flight VALUES("United", "715", "2024-02-28 10:25:25", "PVG", "2024-02-28 13:50:25", "BEI", 500.00, 1, "delayed");
INSERT INTO flight VALUES("United", "839", "2023-05-26 13:25:25", "SHEN", "2023-05-26 16:50:25", "BEI", 300.00, 3, "on-time");

INSERT INTO ticket VALUES("1", 300.00, "United", "102", "2024-02-12 13:25:25");
INSERT INTO ticket VALUES("2", 300.00, "United", "102", "2024-02-12 13:25:25");
INSERT INTO ticket VALUES("3", 300.00, "United", "102", "2024-02-12 13:25:25");
INSERT INTO ticket VALUES("4", 300.00, "United", "104", "2024-03-04 13:25:25");
INSERT INTO ticket VALUES("5", 300.00, "United", "104", "2024-03-04 13:25:25");
INSERT INTO ticket VALUES("6", 350.00, "United", "106", "2024-01-04 13:25:25");
INSERT INTO ticket VALUES("7", 350.00, "United", "106", "2024-01-04 13:25:25");
INSERT INTO ticket VALUES("8", 300.00, "United", "839", "2023-05-26 13:25:25");
INSERT INTO ticket VALUES("9", 300.00, "United", "102", "2024-02-12 13:25:25");
INSERT INTO ticket VALUES("11", 300.00, "United", "134", "2024-12-12 13:25:25");
INSERT INTO ticket VALUES("12", 500.00, "United", "715", "2024-02-28 10:25:25");
INSERT INTO ticket VALUES("14", 400.00, "United", "206", "2024-07-04 13:25:25");
INSERT INTO ticket VALUES("15", 400.00, "United", "206", "2024-07-04 13:25:25");
INSERT INTO ticket VALUES("16", 400.00, "United", "206", "2024-07-04 13:25:25");
INSERT INTO ticket VALUES("17", 300.00, "United", "207", "2024-08-04 13:25:25");
INSERT INTO ticket VALUES("18", 300.00, "United", "207", "2024-08-04 13:25:25");
INSERT INTO ticket VALUES("19", 3000.00, "United", "296", "2024-05-30 13:25:25");
INSERT INTO ticket VALUES("20", 3000.00, "United", "296", "2024-05-30 13:25:25");

-- INSERT INTO review VALUES('testcustomer@nyu.edu', 'United', '102', '2024-02-12 13:25:25', '4', 'Very Comfortable');
-- INSERT INTO review VALUES('user1@nyu.edu', 'United', '102', '2024-02-12 13:25:25', '5', 'Relaxing, check-in and onboarding very professional');
-- INSERT INTO review VALUES('user2@nyu.edu', 'United', '102', '2024-02-12 13:25:25', '3', 'Satisfied and will use the same flight again');
-- INSERT INTO review VALUES('testcustomer@nyu.edu', 'United', '104', '2024-03-04 13:25:25', '1', 'Customer Care services are not good');
-- INSERT INTO review VALUES('user1@nyu.edu', 'United', '104', '2024-03-04 13:25:25', '5', 'Comfortable journey and Professional');




