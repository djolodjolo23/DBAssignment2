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
-- Table structure for table `recipe_ingredient`
--

DROP TABLE IF EXISTS `recipe_ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe_ingredient` (
  `INGREDIENT_ID` int(11) DEFAULT NULL,
  `AMOUNT` int(11) DEFAULT NULL,
  `INGREDIENT_DESC` varchar(500) DEFAULT NULL,
  `RECIPE_INGREDIENT_ID` int(11) NOT NULL,
  `RECIPE_ID` int(11) NOT NULL,
  PRIMARY KEY (`RECIPE_INGREDIENT_ID`,`RECIPE_ID`),
  KEY `RECIPE_ID_idx` (`RECIPE_ID`),
  KEY `INGREDIENT_ID_idx` (`INGREDIENT_ID`),
  CONSTRAINT `INGREDIENT_ID` FOREIGN KEY (`INGREDIENT_ID`) REFERENCES `rm_ingredient` (`INGREDIENT_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `RECIPE_ID` FOREIGN KEY (`RECIPE_ID`) REFERENCES `rm_recipe` (`RECIPE_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_ingredient`
--

LOCK TABLES `recipe_ingredient` WRITE;
/*!40000 ALTER TABLE `recipe_ingredient` DISABLE KEYS */;
INSERT INTO `recipe_ingredient` VALUES (1,30,'Parmesan cheese, 30 grams',1,1),(2,150,'Sliced Bacon, 150 grams',2,1),(6,2,'Two eggs',3,1),(3,250,'Spagetti',4,1),(4,10,'Olive oil, 10 milliliters',5,1),(5,3,'Garlic, 3 cloves',6,2),(10,100,'Cabbage, 100 grams',7,2),(12,1,'Onion, 1 piece',8,2),(13,1,'Carrot, 1 piece',9,2),(14,250,'Broccoli, 250 grams',10,2),(15,2,'Thai sauce, 2 tablespoons',11,2),(53,200,'Chicken meat, 200 grams',12,2),(1,1,'American cheese, 1 slice',13,3),(2,1,'Bacon, 1 slice',14,3),(7,2,'Buns, top and bottom piece',15,3),(8,150,'Burger patty, 150 grams ',16,3),(9,2,'Tomato, 2 slices',17,3),(10,10,'Cabbage, 10 grams',18,3),(11,1,'Ketchup, 1 teaspoon',19,3),(12,2,'Onion, 2 slices',20,3),(53,1000,'Chicken meat, 1000 grams',21,4),(38,400,'Marinara sauce, 400 mililiters',22,4),(39,700,'Chicken stock, 700 mililiters',23,4),(40,150,'Polenta, 150 grams',24,4),(26,2,'Salt, 2 teaspoons',25,4),(36,1,'Basil, 1 teaspoon',26,5),(37,30,'Pine nuts, 30 grams',27,5),(3,400,'Pasta of your choice, 400 grams',28,5),(14,400,'Broccoli, 400 grams, sliced',29,5),(5,2,'Garlic, 2 cloves',30,5),(4,150,'Extra virgin olive oil, 150 mililiters',31,5),(26,1,'Salt, 1 teaspoon',32,5),(1,140,'Parmiggiano Regiano, 140 grams',33,5),(41,2,'Oregano, 2 teaspoons',34,6),(42,2,'Thyme, 2 teaspoons',35,6),(43,2,'Garlic powder, 2 teaspoons',36,6),(44,100,'White wine, 100 mililiters',37,6),(45,1,'Lemon zest, 1 tablespoon',38,6),(46,2,'Lemon juice, 2 tablespoons',39,6),(47,1,'Brown sugar, 1 tablespoon',40,6),(48,1,'Lemon, 1 piece, cut into 6 slices',41,6),(53,1000,'Chicken meat, 1000 grams',42,6),(4,40,'Olive oil, 50 mililiters',43,6),(26,2,'Salt, 2 teaspoons',44,6),(27,1,'Pepper, 1 teaspoon',45,6),(5,4,'Garlic, 4 cloves',46,6),(54,4,'Ears corn, 4 pieces',47,7),(55,50,'Chipotle mayo, 50 grams',48,7),(56,30,'Fresh cilantro, 30 grams',49,7),(57,30,'Chipotle chili powder, 30 grams',50,7),(58,1,'Lime, 1 piece',51,7),(1,30,'Cotija cheese, 30 grams',52,7),(59,900,'Frozen diced potatoes, 900 grams',53,9),(60,200,'Sour cream, 200 ml',54,9),(39,200,'Chicken stock, 200 ml',55,9),(61,1,'Garlic salt, 1 teaspoon',56,9),(1,250,'Cheddar jack cheese, 250 grams',57,9),(35,250,'Fresh potatoes, 250 grams',58,8),(16,2,'Oil, 2 tablespoons',59,8),(62,2,'Large leeks, 2 pieces, thinkly sliced',60,8),(63,100,'Smoked mackerel, 100 grams, skin removed',61,8),(6,4,'Eggs, 4 pieces',62,8),(64,2,'Creamed horseradish, 2 tablespoons',63,8),(3,350,'Pasta for lasagna, 350 grams',64,10),(65,100,'Butter, 100 grams',65,10),(49,200,'Ground beef, 200 grams',66,10),(66,150,'Bolognese sauce, 150 ml',67,10),(1,150,'Cheddar chese, 150 grams',68,10),(67,150,'Water, 150 mililiters',69,11),(20,450,'All purpose flour, 450 grams',70,11),(25,40,'Baking powder, 40 grams',71,11),(26,1,'Salt, 1 teaspoon',72,11),(16,6,'Vegetable oil, 6 tablespoons',73,11),(68,400,'Pillsbury crescent roll dough, 400 grams',74,12),(49,350,'Ground beef, 350 grams',75,12),(69,1,'Taco seasoning, 1 small pack',76,12),(1,150,'Grated cheddar cheese, 150 grams',77,12),(70,100,'Salsa, 100 mililiters',78,12),(71,2,'Sliced jalapeno, 2 pieces',79,12);
/*!40000 ALTER TABLE `recipe_ingredient` ENABLE KEYS */;
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
