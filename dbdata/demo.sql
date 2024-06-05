INSERT INTO airline VALUES("United");

INSERT INTO airplane VALUES("United", 1, 4, "Boeing", "B-101", "2013-05-02");
INSERT INTO airplane VALUES("United", 2, 4, "Airbus", "A-101", "2011-05-02");
INSERT INTO airplane VALUES("United", 3, 50, "Boeing", "B-101", "2015-05-02");

INSERT INTO maintenance VALUES("2024-06-27 13:25:25", "2024-06-29 07:25:25", "United", 1 );
INSERT INTO maintenance VALUES("2024-01-27 13:25:25", "2024-01-29 07:25:25", "United", 2 );

INSERT INTO airport VALUES("JFK", "John F. Kennedy International Airport", "NYC", "USA", 4, "Both");
INSERT INTO airport VALUES("BOS", "Logan International Airport", "Boston", "USA", 2, "Both");
INSERT INTO airport VALUES("PVG", "Shanghai Pudong International Airport", "Shanghai", "China", 2, "Both");
INSERT INTO airport VALUES("BEI", "Beijing Capital International Airport", "Beijing", "China", 2, "Both");
INSERT INTO airport VALUES("SFO", "San Francisco International Airport", "San Francisco", "USA", 4, "Both");
INSERT INTO airport VALUES("LAX", "Los Angeles International Airport", "Los Angeles", "USA", 2, "Both");
INSERT INTO airport VALUES("HKA", "Hong Kong International Airport", "Hong Kong", "China", 2, "Both");
INSERT INTO airport VALUES("SHEN", "Shenzhen Bao'an International Airport", "Shenzhen", "China", 2, "Both");

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
INSERT INTO ticket VALUES("21", 300.00, "United", "102", "2024-02-12 13:25:25");
INSERT INTO ticket VALUES("22", 400.00, "United", "206", "2024-07-04 13:25:25");
INSERT INTO ticket VALUES("23", 400.00, "United", "206", "2024-07-04 13:25:25");





