CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    model VARCHAR(50),
    year INT,
    price FLOAT
);


INSERT INTO cars (name, model, year, price) VALUES
('Toyota', 'Camry', 2018, 24000),
('Honda', 'Civic', 2020, 20000),
('Ford', 'Mustang', 2019, 35000),
('Chevrolet', 'Malibu', 2017, 22000),
('Nissan', 'Altima', 2018, 23000),
('Hyundai', 'Elantra', 2019, 19000),
('BMW', '3 Series', 2020, 42000),
('Audi', 'A4', 2019, 41000),
('Mercedes-Benz', 'C-Class', 2021, 50000),
('Volkswagen', 'Jetta', 2018, 21000),
('Subaru', 'Impreza', 2020, 22000),
('Mazda', 'Mazda3', 2019, 21000),
('Kia', 'Optima', 2018, 20000),
('Tesla', 'Model 3', 2021, 55000),
('Lexus', 'IS', 2020, 45000),
('Acura', 'TLX', 2019, 37000),
('Infiniti', 'Q50', 2018, 38000),
('Volvo', 'S60', 2020, 43000),
('Jaguar', 'XE', 2021, 47000),
('Genesis', 'G70', 2019, 39000);



-- 1. Retrieve All Cars:
SELECT * FROM cars;

-- 2. Search by Year:
SELECT * FROM cars WHERE year = 2018;

-- 3. Find Expensive Cars:
SELECT * FROM cars WHERE price > 20000;

-- 4. Count Cars by Name:
SELECT name, COUNT() AS count FROM cars GROUP BY name;

-- 5. Average Price by Year:
SELECT year, AVG(price) AS average_price FROM cars GROUP BY year;

-- 6. Find the Most Expensive Car:
SELECT * FROM cars ORDER BY price DESC LIMIT 1;

-- 7. Cars within Price Range:
SELECT * FROM cars WHERE price BETWEEN 15000 AND 30000;

-- 8. Update Car Price:
UPDATE cars SET price = price * 1.10 WHERE year < 2015;

-- 9. Delete Old Cars:
DELETE FROM cars 
WHERE year < (strftime('%Y', 'now') - 10);

-- 10. Complex Query:
SELECT name, model, MAX(price) AS max_price
FROM cars
GROUP BY year, name, model;

-- 11. Complex Query 2:
SELECT name, AVG(price) AS average_price
FROM cars
GROUP BY name
HAVING COUNT() > 3;