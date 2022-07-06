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
-- Table structure for table `defectlog`
--

DROP TABLE IF EXISTS `defectlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `defectlog` (
  `DEFECTLOG_ID` int NOT NULL AUTO_INCREMENT,
  `DEFECT_BIKE_ID` int NOT NULL,
  `DEFECT_USER_ID` int NOT NULL,
  `DEFECT_BIKEPART_ID` int NOT NULL,
  `DEFECT_STATUS` int NOT NULL,
  `DEFECT_TIMESTAMP` datetime NOT NULL,
  `DEFECT_REPAIR_TIMESTAMP` datetime DEFAULT NULL,
  `DEFECT_COMMENTS` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`DEFECTLOG_ID`),
  KEY `DEFECT_BIKE_ID_idx` (`DEFECT_BIKE_ID`),
  KEY `DEFECT_USER_ID_idx` (`DEFECT_USER_ID`),
  KEY `DEFECT_BIKEPART_ID_idx` (`DEFECT_BIKEPART_ID`),
  CONSTRAINT `DEFECT_BIKE_ID` FOREIGN KEY (`DEFECT_BIKE_ID`) REFERENCES `bike` (`BIKE_ID`),
  CONSTRAINT `DEFECT_BIKEPART_ID` FOREIGN KEY (`DEFECT_BIKEPART_ID`) REFERENCES `bikepart` (`BIKEPART_ID`),
  CONSTRAINT `DEFECT_USER_ID` FOREIGN KEY (`DEFECT_USER_ID`) REFERENCES `user` (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `defectlog`
--

LOCK TABLES `defectlog` WRITE;
/*!40000 ALTER TABLE `defectlog` DISABLE KEYS */;
INSERT INTO `defectlog` VALUES (1,1,3,4,0,'2021-11-01 13:00:11','2021-11-01 13:06:56','  broken seat                                \r\n                                '),(2,1,4,2,0,'2021-12-01 13:00:11','2021-12-01 13:10:11','headlight broken'),(3,1,2,3,0,'2021-11-01 13:00:11','2021-11-01 13:10:11','tires punctured'),(4,2,3,5,0,'2021-10-01 13:00:11','2021-10-01 13:10:11','handles broken'),(5,3,2,1,0,'2021-09-01 13:00:11','2021-09-01 13:10:11','brakes not working'),(6,4,2,4,0,'2021-12-01 13:00:11','2021-12-01 13:10:11','seats torn'),(7,4,5,2,0,'2021-11-01 13:00:11','2021-11-01 13:20:11','headlights broken'),(8,5,4,4,0,'2021-10-01 13:00:11','2021-10-01 13:40:11','broken seats'),(9,4,3,1,0,'2021-11-01 13:00:11','2021-11-01 13:20:11','brakes not working'),(10,1,3,2,0,'2021-11-01 17:10:59','2021-11-02 14:20:18','broken light           \r\n                                '),(11,1,4,1,0,'2021-11-02 19:05:12','2021-11-02 19:12:12','                                  \r\n                                '),(12,7,4,1,0,'2021-11-02 19:06:44','2021-11-02 19:12:14','                                  \r\n                                '),(13,16,3,4,0,'2021-11-02 19:11:27','2021-11-02 19:12:16','bad seat                         \r\n                                ');
/*!40000 ALTER TABLE `defectlog` ENABLE KEYS */;
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
