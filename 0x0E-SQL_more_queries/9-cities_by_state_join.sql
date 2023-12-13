-- Select cities with corresponding state names using a JOIN
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON states.id = city.states_id
ORDER BY cities.id;
