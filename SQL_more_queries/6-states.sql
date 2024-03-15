-- Ensure the database hbtn_0d_usa exists, like marking the territory for our garden
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Create the states table, akin to preparing the soil with just the right nutrients
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT, -- Think of each id as a unique tag on every tree in our garden
    name VARCHAR(256) NOT NULL, -- And the name is the label, like "Apple Tree," that cannot be left blank
    PRIMARY KEY (id) -- The id tag is the primary way we identify each tree
);
