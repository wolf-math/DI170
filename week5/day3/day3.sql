-- New table

CREATE TABLE countries (
  country_id   SERIAL PRIMARY KEY,
  country_name VARCHAR(100) NOT NULL
);

-- Insert values

INSERT INTO countries (country_name) VALUES
  ('USA'),
  ('UK'),
  ('France'),
  ('Atlantis');

-- New actors

INSERT INTO actor (first_name, last_name, dob, number_oscars) VALUES
  ('Ada', 'Stone', '1980-02-01', 1),
  ('Ben', 'Lake',  '1975-05-20', 0),
  ('Cia', 'Reed',  '1990-11-11', 2);


-- Inner join

SELECT
  actor.actor_id, actor.first_name, actor.last_name,
  country.country_id, country.country_name
FROM actor
INNER JOIN countries
  ON actor.actor_id = country.country_id;

-- Left outer join

SELECT
  actor.actor_id,
  actor.first_name,
  actor.last_name,
  countries.country_name
FROM actor
LEFT JOIN countries
  ON actor.actor_id = countries.country_id;



-- Right outer join

SELECT
  actor.actor_id, actor.first_name, actor.last_name,
  country.country_id, country.country_name
FROM actor
RIGHT JOIN countries
  ON actor.actor_id = country.country_id;


-- Full outer join

SELECT
  actoractor_id, actorfirst_name, actorlast_name,
  country.country_id, country.country_name
FROM actor 
FULL OUTER JOIN countries
  ON actoractor_id = country.country_id;
