-- create a table in the database
-- database name will be passed as argument
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table(
    id,
    name,
    score)
VALUES(1, 'John', 10)
      (2, 'Alex', 3)
      (3, 'Bob', 14)
      (3, 'George', 8);