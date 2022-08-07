-- --------------------------------------------------------
-- Host:                         cxmgkzhk95kfgbq4.cbetxkdyhwsb.us-east-1.rds.amazonaws.com
-- Server version:               10.4.24-MariaDB-log - Source distribution
-- Server OS:                    Linux
-- HeidiSQL Version:             11.3.0.6449
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for fin_lit
CREATE DATABASE IF NOT EXISTS `fin_lit` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `fin_lit`;

-- Dumping structure for table fin_lit.course_completion
CREATE TABLE IF NOT EXISTS `course_completion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `course_completion_fk0` (`user_id`),
  CONSTRAINT `course_completion_fk0` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.course_completion: ~0 rows (approximately)

-- Dumping structure for table fin_lit.media
CREATE TABLE IF NOT EXISTS `media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `path` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.media: ~0 rows (approximately)

-- Dumping structure for table fin_lit.modules
CREATE TABLE IF NOT EXISTS `modules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `desc` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.modules: ~3 rows (approximately)
INSERT INTO `modules` (`id`, `name`, `desc`, `image`) VALUES
	(1, 'Credit Cards', 'This module will go through credit cards and its usage', 'credit_card.svg'),
	(2, 'Major Expenditure', 'This module dives deep into all the expenses that are major', 'major.svg'),
	(3, 'Rule of 72', 'This module talks about Rule of 72', '72.svg');

-- Dumping structure for table fin_lit.module_completion
CREATE TABLE IF NOT EXISTS `module_completion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_id` int(11) NOT NULL,
  `user_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `completion` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `module_completion_fk0` (`module_id`),
  KEY `module_completion_fk1` (`user_id`),
  CONSTRAINT `module_completion_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules` (`id`),
  CONSTRAINT `module_completion_fk1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.module_completion: ~0 rows (approximately)

-- Dumping structure for table fin_lit.module_data
CREATE TABLE IF NOT EXISTS `module_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_module_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `module_data_fk0` (`sub_module_id`),
  CONSTRAINT `module_data_fk0` FOREIGN KEY (`sub_module_id`) REFERENCES `submodules` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.module_data: ~0 rows (approximately)

-- Dumping structure for table fin_lit.module_media
CREATE TABLE IF NOT EXISTS `module_media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_module_id` int(11) NOT NULL,
  `media_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `module_media_fk0` (`sub_module_id`),
  KEY `module_media_fk1` (`media_id`),
  CONSTRAINT `module_media_fk0` FOREIGN KEY (`sub_module_id`) REFERENCES `submodules` (`id`),
  CONSTRAINT `module_media_fk1` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.module_media: ~0 rows (approximately)

-- Dumping structure for table fin_lit.module_quiz
CREATE TABLE IF NOT EXISTS `module_quiz` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `file_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` enum('quiz','workbook') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'quiz',
  PRIMARY KEY (`id`),
  KEY `module_quiz_fk0` (`module_id`),
  CONSTRAINT `module_quiz_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.module_quiz: ~3 rows (approximately)
INSERT INTO `module_quiz` (`id`, `module_id`, `name`, `file_name`, `type`) VALUES
	(1, 1, 'Introductory Quiz', 'quiz_1', 'quiz'),
	(2, 1, 'Advance Quiz', 'quiz_2', 'quiz'),
	(3, 1, 'Workbook', 'workbook_1', 'workbook');

-- Dumping structure for table fin_lit.module_scores
CREATE TABLE IF NOT EXISTS `module_scores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_id` int(11) NOT NULL,
  `module_comp_id` int(11) NOT NULL,
  `score` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `module_scores_fk0` (`module_id`),
  KEY `module_scores_fk1` (`module_comp_id`),
  CONSTRAINT `module_scores_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules` (`id`),
  CONSTRAINT `module_scores_fk1` FOREIGN KEY (`module_comp_id`) REFERENCES `module_completion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.module_scores: ~0 rows (approximately)

-- Dumping structure for table fin_lit.points
CREATE TABLE IF NOT EXISTS `points` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `points` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `points_fk0` (`user_id`),
  CONSTRAINT `points_fk0` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.points: ~0 rows (approximately)

-- Dumping structure for table fin_lit.roles
CREATE TABLE IF NOT EXISTS `roles` (
  `role_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.roles: ~0 rows (approximately)
INSERT INTO `roles` (`role_id`, `role_name`) VALUES
	(1, 'user'),
	(2, 'admin');

-- Dumping structure for table fin_lit.submodules
CREATE TABLE IF NOT EXISTS `submodules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `desc` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `module_id` int(11) NOT NULL,
  `type` enum('PPT','PDF','IMG','VID') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'PPT',
  `data` text COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `submodules_fk0` (`module_id`),
  CONSTRAINT `submodules_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.submodules: ~0 rows (approximately)
INSERT INTO `submodules` (`id`, `name`, `desc`, `module_id`, `type`, `data`) VALUES
	(1, 'Introduction', 'This is the introduction', 1, 'PPT', 'https://docs.google.com/presentation/d/e/2PACX-1vRhMeFi6XXwhYt013imfabcuxSocJPzSuVxYGUBQNFNU0RdPX9XoYxyD33MxnWzQ0wrcq0TXiP-Lb88/embed?start=false&loop=false&delayms=5000'),
	(2, 'Introduction Info Sheet', 'This is the info sheet', 1, 'PDF', 'assets/modules/1/intro.pdf'),
	(3, 'Advanced Credit Card', 'These are some advanced topics', 1, 'PPT', 'https://docs.google.com/presentation/d/e/2PACX-1vRq0im-jbjM5UaUOvl1eF4TZqNivzNd5XZk1OvzY1hUbyVGbaXP_ZS6L2gx3pKW0mTzntdcmqiDVzIk/embed?start=false&loop=false&delayms=5000'),
	(4, 'Understanding Credit Cards', 'Understand them', 1, 'PDF', 'assets/modules/1/understand.pdf');

-- Dumping structure for table fin_lit.submodule_completion
CREATE TABLE IF NOT EXISTS `submodule_completion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `submodule_id` int(11) NOT NULL,
  `user_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `completion` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `submodule_completion_fk0` (`submodule_id`),
  KEY `submodule_completion_fk1` (`user_id`),
  CONSTRAINT `submodule_completion_fk0` FOREIGN KEY (`submodule_id`) REFERENCES `submodules` (`id`),
  CONSTRAINT `submodule_completion_fk1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.submodule_completion: ~0 rows (approximately)

-- Dumping structure for table fin_lit.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `school` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role_id` int(11) NOT NULL,
  `dp` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `major` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_fk0` (`role_id`),
  CONSTRAINT `users_fk0` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.users: ~0 rows (approximately)
INSERT INTO `users` (`id`, `name`, `school`, `email`, `password`, `role_id`, `dp`, `major`, `phone`) VALUES
	('1001', 'Aman', 'UTA', '', '$pbkdf2-sha256$29000$ao2RMqYUIsSYM2YMAaB0bg$fOMLttz5/VBTS7n.al2.9gT3mQA3M/WHHuhfTlVd.70', 1, 'https://res.cloudinary.com/dtvhyzofv/image/upload/v1647144583/banter/dp/user_awjxuf.png', '', ''),
	('1001750503', 'Aneesh Melkot', 'UTA', '', '$pbkdf2-sha256$29000$AiDE.L/Xeu8dI2TMube2Ng$f7PgXZ2/whPxPLDc9jaQhBrXREBRalFfh3aAaTMTONU', 1, 'https://res.cloudinary.com/dtvhyzofv/image/upload/v1647144583/banter/dp/user_awjxuf.png', '', ''),
	('1001773798', 'Nabeel Eusufzai', 'University of Texas at Arlington', '', '$pbkdf2-sha256$29000$vPee837v/X9vzZmT8l5r7Q$RmFVFRtDBoR6nwkh/HAzoENzpj8AgWCJkRqh50of/JA', 1, 'https://res.cloudinary.com/dtvhyzofv/image/upload/v1647144583/banter/dp/user_awjxuf.png', '', ''),
	('1001860116', 'Tabitha Griffin', 'University of Texas at Arlington ', '', '$pbkdf2-sha256$29000$XisFYKxVCuFci/Fea40RAg$Y6BwRZBqjGwhsT0vTlvHzGzqGfGiGHAH0KR5Yg2wDVc', 1, 'https://res.cloudinary.com/dtvhyzofv/image/upload/v1647144583/banter/dp/user_awjxuf.png', '', ''),
	('100188', 'Lavin', 'University of Texas at Arlington ', '', '$pbkdf2-sha256$29000$ovQ.R4iRMmYsZcxZ6z1HaA$qm38AGregCny.04IJcjqO70mSog1YnAq/9QXJGmVMhk', 1, 'https://res.cloudinary.com/dtvhyzofv/image/upload/v1647144583/banter/dp/user_awjxuf.png', '', '');

-- Dumping structure for table fin_lit.videos
CREATE TABLE IF NOT EXISTS `videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `file_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cover` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table fin_lit.videos: ~7 rows (approximately)
INSERT INTO `videos` (`id`, `title`, `description`, `file_name`, `cover`) VALUES
	(1, 'Introduction Video', 'Introduction Video', 'intro.mov', 'intro.png'),
	(2, 'UTA Off Campus Apartment Options', 'UTA Off Campus Apartment Options', 'offcampus_apts.mp4', 'offcampus_apts.png'),
	(3, 'Rent a car', 'Rent a car', 'rideshare.mov', 'rideshare.png'),
	(4, 'Arlington VIA service', 'Arlington VIA service', 'via.mp4', 'via.png'),
	(5, 'Budget Friendly Gyms for UTA Students', 'Budget Friendly Gyms for UTA Students', 'gym.mov', 'gym.png'),
	(6, 'Apple Education Pricing', 'Apple Education Pricing', 'apple.mp4', 'apple.png'),
	(7, 'Comparing Textbook Prices', 'Comparing Textbook Prices', 'textbook.mp4', 'textbook.png'),
	(8, 'Free Resume Help for UTA Students', 'Free Resume Help for UTA Students', 'resume.mp4', 'resume.png');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
