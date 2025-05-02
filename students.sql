-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2025 at 09:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `students`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `Name` varchar(50) NOT NULL,
  `Age` int(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Marks` int(50) NOT NULL,
  `Percentage` double NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Grade` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`Name`, `Age`, `Email`, `Marks`, `Percentage`, `Department`, `Grade`) VALUES
('Abirami', 25, 'abi@gmail.com', 88, 65, 'Computer science', 'A+'),
('Anu', 25, 'anu@gmail.com', 85, 60, 'Zoology', 'A'),
('sathya', 28, 'sathya@gmail.com', 95, 78, 'Economics', 'B'),
('Kavitha', 27, 'kavi@gmail.com', 75, 69, 'computer science', 'A+'),
('karthika', 27, 'karthika@gmail.com', 62, 65, 'Zoology', 'A'),
('Ram', 27, 'ram@gmail.com', 55, 59, 'physics', 'B'),
('Rathika', 26, 'rathika@gmail.com', 88, 60.5, 'Bilogy', 'A+'),
('Ramya', 18, 'ramya@gmail.com', 89, 61.5, 'chemistry', 'B+'),
('Geetha', 19, 'geethaa@gmail.com', 87, 63.5, 'Bilogy', 'B+'),
('Geetha', 19, 'geetha@gmail.com', 87, 63.45, 'Bilogy', 'B+'),
('meena', 18, 'meena@gmail.com', 89, 59.3, 'computer science', 'A+'),
('dhanam', 29, 'dhanam@gmail.com', 92, 88.3, 'Biology', 'B'),
('aarthi', 18, 'aarthi@gmail.com', 76, 61.3, 'Economics', 'B'),
('aakash', 20, 'aakash@gmail.com', 77, 61.3, 'Economics', 'B');

-- --------------------------------------------------------

--
-- Table structure for table `signin`
--

CREATE TABLE `signin` (
  `username` varchar(50) NOT NULL,
  `password` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `signin`
--

INSERT INTO `signin` (`username`, `password`) VALUES
('Ananthi', 3216),
('saranya', 6547);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(50) NOT NULL,
  `password` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`) VALUES
('meena@gmail.com', 1234),
('Anu@gmail.com', 5678),
('meena@gmail.com', 1234),
('meena@gmail.com', 1234),
('meena@gmail.com', 1234),
('meena@gmail.com', 1234),
('divya@gmail.com', 2589);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
