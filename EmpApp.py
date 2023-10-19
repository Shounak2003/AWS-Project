
-- This SQL script defines tables for employee data storage.

-- Employee ID Table: Stores unique employee identifiers.
CREATE TABLE empid (
    emp_id INT PRIMARY KEY,
    -- Primary key for employee identification.
    -- Example: 1001, 1002, ...

    -- Add more columns if needed, such as date of joining, etc.
);

-- First Name Table: Records employees' first names.
CREATE TABLE fname (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    -- Primary key referencing empid.
    -- Example: John, Mary, ...

    -- Add more columns for additional information.
);

-- Last Name Table: Stores employees' last names.
CREATE TABLE lname (
    emp_id INT PRIMARY KEY,
    last_name VARCHAR(50),
    -- Primary key referencing empid.
    -- Example: Smith, Johnson, ...

    -- Additional columns can be added as required.
);

-- Primary Skills Table: Manages employees' primary skills.
CREATE TABLE priskill (
    emp_id INT PRIMARY KEY,
    primary_skills VARCHAR(100),
    -- Primary key referencing empid.
    -- Example: Programming, Sales, ...

    -- Additional columns for skill levels, certifications, etc.
);

-- Location Table: Tracks employees' work locations.
CREATE TABLE location (
    emp_id INT PRIMARY KEY,
    work_location VARCHAR(100),
    -- Primary key referencing empid.
    -- Example: New York, London, ...

    -- Extra columns for location details if necessary.
);

-- The code defines five tables, each dedicated to specific employee data, enabling structured data storage and retrieval.

