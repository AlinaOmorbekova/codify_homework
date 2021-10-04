
--1. Напишите запрос, чтобы получить название продукта и количество/единицу. 
select product_name, quantity_per_unit from products;
--2. Напишите запрос для получения текущего списка продуктов (ID и название продукта). 
select product_id, product_name from products;
--3. Напишите запрос для получения списка продуктов, со скидкой (ID и название продукта). 
select product_id, product_name from products where discontinued = 1;
--4. Напишите запрос, чтобы получить список самых дорогих и самых дешевых 
--продуктов (название и цена за единицу). 
select product_name, unit_price from products where unit_price = (select MAX(unit_price) from products);
select product_name, unit_price from products where unit_price = (select MIN(unit_price) from products);
--5. Напишите запрос, чтобы получить список продуктов (идентификатор, название, цена за единицу), 
--в котором текущие продукты стоят менее $20. 
select product_id, product_name, unit_price from products where unit_price < 20;
--6. Выведите всех сотрудников которые старше 55 лет.
SELECT employee_id, last_name, first_name from employees where date_part('year', age(birth_date)) :: int > 55; 
--7. Выведите всех сотрудников которые младше 55 лет.
SELECT employee_id, last_name, first_name from employees where date_part('year', age(birth_date)) :: int < 55;
--8. Выведите всех сотрудников, возраст которых между 55 и 60 годами.
SELECT employee_id, last_name, first_name from employees where date_part('year', age(birth_date)) :: int > 55 and date_part('year', age(birth_date)) :: int < 60;  
