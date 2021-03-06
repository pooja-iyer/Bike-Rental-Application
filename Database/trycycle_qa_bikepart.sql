-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: trycycle_qa
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bikepart`
--

DROP TABLE IF EXISTS `bikepart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bikepart` (
  `BIKEPART_ID` int NOT NULL AUTO_INCREMENT,
  `BIKEPART_NAME` varchar(45) NOT NULL,
  PRIMARY KEY (`BIKEPART_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bikepart`
--

LOCK TABLES `bikepart` WRITE;
/*!40000 ALTER TABLE `bikepart` DISABLE KEYS */;
INSERT INTO `bikepart` VALUES (1,'brakes'),(2,'headlight'),(3,'tires'),(4,'seat'),(5,'handle');
/*!40000 ALTER TABLE `bikepart` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-03 10:37:57

-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: trycycle_qa
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `rentallog`
--

DROP TABLE IF EXISTS `rentallog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rentallog` (
  `RENTALLOG_ID` int NOT NULL AUTO_INCREMENT,
  `RENTAL_USER_ID` int NOT NULL,
  `RENTAL_BIKE_ID` int NOT NULL,
  `RENTAL_START_BSID` int NOT NULL,
  `RENTAL_END_BSID` int DEFAULT NULL,
  `RENTAL_START_TIME` datetime NOT NULL,
  `RENTAL_END_TIME` datetime DEFAULT NULL,
  `RENTAL_DURATION` int DEFAULT NULL,
  `RENTAL_PRICE` float DEFAULT NULL,
  PRIMARY KEY (`RENTALLOG_ID`),
  KEY `RENTAL_USER_ID_idx` (`RENTAL_USER_ID`),
  KEY `RENTAL_BIKE_ID_idx` (`RENTAL_BIKE_ID`),
  KEY `RENTAL_START_BSID_idx` (`RENTAL_START_BSID`),
  KEY `RENTAL_END_BS_ID_idx` (`RENTAL_END_BSID`),
  CONSTRAINT `RENTAL_BIKE_ID` FOREIGN KEY (`RENTAL_BIKE_ID`) REFERENCES `bike` (`BIKE_ID`),
  CONSTRAINT `RENTAL_END_BSID` FOREIGN KEY (`RENTAL_END_BSID`) REFERENCES `bikestation` (`BIKESTATION_ID`),
  CONSTRAINT `RENTAL_START_BSID` FOREIGN KEY (`RENTAL_START_BSID`) REFERENCES `bikestation` (`BIKESTATION_ID`),
  CONSTRAINT `RENTAL_USER_ID` FOREIGN KEY (`RENTAL_USER_ID`) REFERENCES `user` (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rentallog`
--

LOCK TABLES `rentallog` WRITE;
/*!40000 ALTER TABLE `rentallog` DISABLE KEYS */;
INSERT INTO `rentallog` VALUES (2,2,1,1,NULL,'2021-10-26 20:53:08',NULL,NULL,NULL),(3,3,4,1,2,'2021-10-26 21:07:39','2021-10-27 21:34:45',27,0),(4,3,5,1,2,'2021-10-29 10:47:24','2021-10-29 11:14:58',28,0),(5,3,2,2,3,'2021-10-29 11:26:32','2021-10-29 11:28:53',2,0),(6,4,4,1,3,'2021-10-30 22:04:05','2021-10-30 22:04:33',0,0),(7,6,2,1,3,'2021-11-01 11:11:49','2021-11-01 11:13:19',2,0),(8,3,5,1,3,'2021-11-01 17:08:33','2021-11-01 17:17:25',9,0),(9,3,2,3,1,'2021-11-01 19:08:03','2021-11-01 19:10:45',3,0.18),(10,4,2,3,2,'2021-11-02 19:04:04','2021-11-02 19:08:10',4,20.5);
/*!40000 ALTER TABLE `rentallog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-03 10:37:58
