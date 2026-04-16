-- Run these queries in MySQL to set up the database

-- 1. Create database
CREATE DATABASE IF NOT EXISTS college_notice_board;
USE college_notice_board;

-- 2. Users table (students and admins)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- stored as plain text for simplicity
    role ENUM('student', 'admin') NOT NULL DEFAULT 'student'
);

-- 3. Notices table
CREATE TABLE IF NOT EXISTS notices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    date_added DATE NOT NULL,
    last_date DATE NOT NULL
);

-- 4. Insert sample users (password is plain text for demo)
INSERT INTO users (name, email, password, role) VALUES
('Admin User', 'admin@college.edu', 'admin123', 'admin'),
('Student One', 'student@college.edu', 'student123', 'student');

-- 5. Insert sample notices
INSERT INTO notices (title, description, category, date_added, last_date) VALUES
('Mid-Semester Exam Schedule', 'Mid-semester exams will begin from 20th April. Check the timetable on the college website.', 'Exam', '2026-04-10', '2026-04-20'),
('Library Book Return', 'All students must return borrowed books before 25th April to avoid fines.', 'Library', '2026-04-08', '2026-04-25'),
('Sports Day Registration', 'Register for the Annual Sports Day by visiting the sports department. Open to all students.', 'Event', '2026-04-12', '2026-04-18');
