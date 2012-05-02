-- phpMyAdmin SQL Dump
-- version 2.11.11.3
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 02, 2012 at 04:34 PM
-- Server version: 5.1.61
-- PHP Version: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `SinFrog`
--

-- --------------------------------------------------------

--
-- Table structure for table `ping`
--

DROP TABLE IF EXISTS `ping`;
CREATE TABLE IF NOT EXISTS `ping` (
  `userID` varchar(255) NOT NULL,
  `pingTime` float NOT NULL DEFAULT '0',
  `server` varchar(255) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `userID` (`userID`),
  KEY `server` (`server`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='Ping table';

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
CREATE TABLE IF NOT EXISTS `rate` (
  `userID` varchar(255) NOT NULL,
  `target` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `rate` float NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `userID` (`userID`),
  KEY `target` (`target`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='Download rate';

-- --------------------------------------------------------

--
-- Table structure for table `userID`
--

DROP TABLE IF EXISTS `userID`;
CREATE TABLE IF NOT EXISTS `userID` (
  `userID` varchar(255) NOT NULL,
  `District` varchar(500) NOT NULL,
  `ISP` varchar(500) NOT NULL,
  `Plan` varchar(500) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY `userID` (`userID`),
  KEY `Plan` (`Plan`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='User ID';
