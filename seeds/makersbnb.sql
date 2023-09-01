-- Drop existing tables and sequences
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

-- Recreate sequences
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;

-- Create 'users' table
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username text,
    fullname text,
    password text
);

-- Insert data into 'users' table
INSERT INTO users (username, fullname, password) VALUES ('dan123', 'Dan Gibson', '123321');
INSERT INTO users (username, fullname, password) VALUES ('khalifa123', 'Khalifa Fadel', '123321');
INSERT INTO users (username, fullname, password) VALUES ('tom123', 'Tom Whelan', '123321');
INSERT INTO users (username, fullname, password) VALUES ('lily123', 'Lily Barton', '123321');

-- Create 'spaces' table
CREATE TABLE spaces(
    id SERIAL PRIMARY KEY,
    SpaceName text,
    description text,
    Price numeric,
    usersID Int
);

-- Insert data into 'spaces' table
INSERT INTO spaces (SpaceName, description, Price, usersID) VALUES ('danHouse', 'Located on the Beach', 20, 1);
INSERT INTO spaces (SpaceName, description, Price, usersID) VALUES ('khalifaHouse', 'Central Location', 15, 2);
INSERT INTO spaces (SpaceName, description, Price, usersID) VALUES ('tomHouse', 'toursity location', 80, 3);
INSERT INTO spaces (SpaceName, description, Price, usersID) VALUES ('lilyHouse', 'located in a lovely touristy village', 90, 4);

-- Create 'bookings' table
CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    spacesID int,
    usersID int,
    dates_of_booking text
);

-- Insert data into 'bookings' table
INSERT INTO bookings (spacesID, usersID, dates_of_booking) VALUES (1, 1, '21-08-2023');
INSERT INTO bookings (spacesID, usersID, dates_of_booking) VALUES (2, 2, '22-08-2023');
INSERT INTO bookings (spacesID, usersID, dates_of_booking) VALUES (3, 3, '23-08-2023');
INSERT INTO bookings (spacesID, usersID, dates_of_booking) VALUES (4, 4, '24-08-2023');
