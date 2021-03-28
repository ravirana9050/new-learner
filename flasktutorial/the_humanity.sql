-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 28, 2021 at 09:12 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `the humanity`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `mes` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone_num`, `mes`, `date`) VALUES
(1, 'first post', 'firstpost@gmail.com', '1234567890', 'first post', '2021-03-03 11:39:39'),
(2, 'ravi rana', 'ravirana7085@gmail.com', '9050857085', 'hi this is my app', NULL),
(4, 'ravi rana', 'ravirana7085@gmail.com', '9050857085', 'hi', '2021-03-03 12:25:59'),
(5, 'sangram singh', 'ravi1234@gmail.com', '1234567891', 'by by', '2021-03-09 11:45:14'),
(6, 'hjgukfuk', 'hvfk@vfk', '1564654646', 'hguykfuykfufukyyuugki', '2021-03-09 12:39:21'),
(7, 'ufyuu', 'bkkk@hjgj', 'jhvsfch', 'jbskjf', '2021-03-09 12:44:27'),
(8, 'ufyuu', 'bkkk@hjgj', 'jhvsfch', 'jbskjf', '2021-03-09 12:45:30'),
(9, 'gigiuhill', 'hvfk@vfk', '1564654646', 'iugiugiu', '2021-03-09 12:54:07'),
(10, 'hjgukfuk', 'hvfk@vfk', '1564654646', 'hi msg aaya', '2021-03-09 13:02:17'),
(11, 'Ravi Pratap Singh', 'ravipartapynr@gmail.com', '8168926325', 'hii', '2021-03-09 13:13:59'),
(12, 'Ravi Pratap Singh', 'ravipartapynr@gmail.com', '8168926325', 'hii', '2021-03-09 13:30:57'),
(13, 'Ravi Pratap Singh', 'ravipartapynr@gmail.com', '9050857085', 'this is my website', '2021-03-09 13:32:52'),
(14, 'Ravi Pratap Singh', 'ravipartapynr@gmail.com', '8168926325', 'where r u going', '2021-03-09 13:34:23'),
(15, 'Ravi Pratap Singh', 'ravipartapynr@gmail.com', '8168926325', 'who', '0000-00-00 00:00:00'),
(16, 'Ravi Pratap Singh', 'ravipartapynr@gmail.com', '8168926325', 'koni tunda hain', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` varchar(50) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'what are gamers', 'my 1st post', 'first-post', 'A gamer is a person ravi who plays interactive games, especially video games, tabletop role-playing games, and skill-based card games, and who plays for usually long periods of time. Some gamers are competitive, meaning that they compete in some games for money. In some countries such as the UK and Australia, the term \"gaming\" can refer to legalized gambling, which can take both traditional and digital forms, through online gambling. There are many different gamer communities around the world. Since the advent of the Internet, many communities take the form of Internet forums or YouTube or Twitch virtual communities, as well as in-person social clubs.', 'home-bg.jpg', '2021-03-18 12:51:32'),
(2, 'This is second post', 'my 2nd post', 'second-post', 'Image result for types of pc games\r\nHere is some information that will help you to better understand the various computer game genres.\r\nMassively Multiplayer Online (MMO) These games are played over a LAN (local area network) or via the Internet. ...\r\nSimulations. ...\r\nAdventure. ...\r\nReal-Time Strategy (RTS) ...\r\nPuzzle. ...\r\nAction. ...\r\nStealth Shooter. ...\r\nCombat.', 'post-bg.jpg', '2021-03-11 11:20:25'),
(4, '1. Action Games', 'Action', 'fourth-post', 'Action games are just that—games where the player is in control of and at the center of the action, which is mainly comprised of physical challenges players must overcome. Most early video games like Donkey Kong and Galaga fall into the action category.\r\n\r\nBecause action games are usually easy to get into and start playing, they still, by most accounts, make up the most popular video games.', 'post-bg.jpg', '2021-03-11 11:47:45'),
(5, 'Fighting\r\n', 'Fight ', 'fifth-post', 'Fighting games like Mortal Kombat and Street Fighter II focus the action on combat, and in most cases, hand-to-hand combat. Most fighting games feature a stable of playable characters, each one specializing in their own unique abilities or fighting style. In most traditional fighting games, players fight their way to the top, taking on more and more difficult opponents as they progress.', 'post-bg.jpg', '2021-03-11 11:51:33'),
(6, 'Action-Adventure Games', 'Adventure', 'sixth-post', 'Action-adventure games most frequently incorporate two game mechanics—game-long quests or obstacles that must be conquered using a tool or item collected, as well as an action element where the item(s) are used.\r\n\r\nFor example, in The Legend of Zelda, Link must find his way through eight dungeons to gather the scattered pieces of the Triforce of Wisdom. Once he’s collected all eight pieces and assembled the artifact, Link can enter the ninth and final dungeon to rescue Princess Zelda. Link uses a boomerang to collect distant items and attack enemies.', 'post-bg.jpg', '2021-03-11 11:51:33'),
(10, 'website', 'movie website', '7th post', 'movies website to download movie', 'post-bg.jpg', '2021-03-21 11:09:34'),
(11, 'call of duty 15', 'army games', '8th', 'army shooting game', 'post-bg.jpg', '2021-03-21 11:52:31');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
