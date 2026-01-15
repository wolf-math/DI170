-- Create another table, called countries, with two fields : country_id and coutry_name. It has no foreign key. It's a table to test the PostgreSQL Joins.

-- Use INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, and FULL OUTER JOIN to join the table countries with the table actors, depending on the comparaison of their primary key
-- Look at the results, and analyse them to understand the difference between the types of PostgreSQL Joins


-- Create country table:
-- CREATE TABLE country (
--   country_id SERIAL PRIMARY KEY,
--   country_name VARCHAR(34) NOT NULL
-- );

-- INSERT INTO country (country_name) values
-- ('Argentina'),
-- ('Wakanda'),
-- ('Somailand'),
-- ('Atlantis'),
-- ('Latveria');

SELECT actor.actor_id, actor.first_name, actor.last_name, country.country_id, country.country_name
FROM actor
FULL JOIN country
ON actor.actor_id = country.country_id
ORDER BY actor_id ASC;