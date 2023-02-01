-- --------------------------------------------------------
-- Database: `mydb`
-- --------------------------------------------------------

CREATE DATABASE IF NOT EXISTS `mydb`;
USE `mydb`;

-- --------------------------------------------------------
-- Table structure
-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS `Emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  AUTO_INCREMENT=10001 ;


CREATE TABLE IF NOT EXISTS `Scores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `score` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  AUTO_INCREMENT=10001 ;

