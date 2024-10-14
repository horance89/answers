-- Create the events table for eProcessor
CREATE TABLE IF NOT EXISTS events (
    hash VARCHAR(255) PRIMARY KEY,
    status VARCHAR(50),
    type INT
);

-- Additional tables for other services can be added here as needed
