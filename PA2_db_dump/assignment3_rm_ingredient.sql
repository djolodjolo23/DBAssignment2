-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: assignment3
-- ------------------------------------------------------
-- Server version	5.7.24

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
-- Table structure for table `rm_ingredient`
--

DROP TABLE IF EXISTS `rm_ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rm_ingredient` (
  `INGREDIENT_ID` int(11) NOT NULL,
  `NAME` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`INGREDIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rm_ingredient`
--

LOCK TABLES `rm_ingredient` WRITE;
/*!40000 ALTER TABLE `rm_ingredient` DISABLE KEYS */;
INSERT INTO `rm_ingredient` VALUES (1,'Cheese'),(2,'Bacon'),(3,'Pasta'),(4,'Olive oil'),(5,'Garlic'),(6,'Eggs'),(7,'Buns'),(8,'Meat'),(9,'Tomato'),(10,'Cabbage'),(11,'Ketchup'),(12,'Onion'),(13,'Carrot'),(14,'Broccoli'),(15,'Thai sauce'),(16,'Vegetable oil'),(17,'Sesame oil'),(18,'Balsamic Vinegar'),(19,'Cider Vinegar'),(20,'Flour'),(21,'Sugar'),(22,'Yeast'),(23,'Vanilla'),(24,'Chocolate'),(25,'Baking Powder'),(26,'Salt'),(27,'Pepper'),(28,'Honey'),(29,'Canned Tomatoes'),(30,'Tomato paste'),(31,'Anchovies'),(32,'Pumpkin'),(33,'Beans'),(34,'Rice'),(35,'Potatoes'),(36,'Basil'),(37,'Pine nuts'),(38,'Marinara sauce'),(39,'Chicken Stock'),(40,'Polenta'),(41,'Oregano'),(42,'Thyme'),(43,'Garlic powder'),(44,'White wine'),(45,'Lemon zest'),(46,'Lemon Juice'),(47,'Brown sugar'),(48,'Lemon'),(49,'Ground Beef'),(50,'Burger buns'),(51,'Mustard'),(52,'Dill pickles'),(53,'Chicken'),(54,'Ears Corn'),(55,'Chipotle mayo'),(56,'Fresh cilantro'),(57,'Chili powder'),(58,'Lime'),(59,'Frozen potatoes'),(60,'Sour cream'),(61,'Garlic salt'),(62,'Leeks'),(63,'Smoked mackerel'),(64,'Creamed horseradish'),(65,'Butter'),(66,'Bolognese sauce'),(67,'Water'),(68,'Roll dough'),(69,'Taco seasoning'),(70,'Salsa'),(71,'Jalapeno');
/*!40000 ALTER TABLE `rm_ingredient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-12  9:22:35
