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
-- Table structure for table `rm_recipe`
--

DROP TABLE IF EXISTS `rm_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rm_recipe` (
  `RECIPE_ID` int(11) NOT NULL,
  `COOKING_TIME` int(11) DEFAULT NULL,
  `DESCRIPTION` varchar(4000) DEFAULT NULL,
  `TITLE` varchar(4000) DEFAULT NULL,
  `USERACC_ID` int(11) NOT NULL,
  PRIMARY KEY (`RECIPE_ID`),
  KEY `USERACC_ID_idx` (`USERACC_ID`),
  CONSTRAINT `USERACC_ID` FOREIGN KEY (`USERACC_ID`) REFERENCES `rm_useracc` (`USERACC_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rm_recipe`
--

LOCK TABLES `rm_recipe` WRITE;
/*!40000 ALTER TABLE `rm_recipe` DISABLE KEYS */;
INSERT INTO `rm_recipe` VALUES (1,20,'Cook pasta in a pot, meanwhile fry bacon with garlic in a pan. Add pasta, eggs and parmesan. Enjoy','Carbonara',1),(2,30,'Cut all the vegetables, fry them for 5 minutes in a wok pan. Add garlic, fry for another minute. Add cooked noodles with sauce and mix all together.','Simple Wok ',2),(3,40,'Place the burger patty covered in melted cheese on top of the brioche bun. Sprinkle the chopped brown onion over the top, followed by a layer of sliced pickles. Add ketchup and mustard and place the bun over the top.','Cheeseburger',3),(4,30,'Sprinkle the chicken thighs with 1 teaspoon salt and add them along with the tomato sauce to your pressure cooker, giving it a quick stir to combine.','Instant Pot Chicken Marinara With Polenta',4),(5,20,'n a large pot bring water ** to a rapid boil. Add the broccoli, bring the water back up to a boil for two minutes. Do not drain the water! Immediately transfer broccoli (with a slotted spoon) to a colander place under cold running water to stop further cooking. Bring the water ** back to a boil and add your favorite pasta and cook according to the package (reserve 1 cup of pasta cooking water before draining). In a large blender or food processor, blend together broccoli, basil, garlic, pine nuts, olive oil, salt and Parmigiano-Reggiano until smooth. Slowly pour in 1 cup of reserved pasta water until a nice sauce is formed. If sauce is too thick, add more pasta water one tablespoon at a time. Toss hot pasta with sauce until completely coated. Top with extra Parmesan, pine nuts and chili flakes if desired. Enjoy!','Broccoli Pesto Pasta',1),(6,30,'Heat the oven to 400 degrees F. Pat the chicken breast dry and place them in a 9 x 13 baking dish. In a small bowl, mix the olive oil, oregano, thyme, garlic powder, 1 teaspoon salt and pepper to create a thick marinade/paste. Coat the chicken breast with seasoning paste. Using the same bowl mix together the white wine, garlic, lemon zest, lemon juice, brown sugar and remaining 1 teaspoon salt. Pour over chicken breast. If using, nestle the lemon slices between the chicken bake for 15 minutes, baste the chicken with the pan juice, bake for another 15 minutes or until the internal temperature of the chicken reads 165 F. ','Lemon Chicken',5),(7,30,'Preheat grill to medium high. Prepare corn by removing husk and silk. Set corn directly on hot grill and allow to cook, rotating often, until slightly charred on all sides. While still warm use the back of a spoon or a pastry brush to spread the chipotle mayo all over each corn. Sprinkle with cotija cheese, fresh cilantro and chipotle powder. Serve with a lime wedge. Enjoy!','Elote (Mexican Street Corn)',2),(8,20,'Put the potatoes in a microwaveable bowl with a splash of water, cover, then cook on high for 5 mins until tender (or steam or simmer them). Meanwhile, heat the oil in a frying pan over a medium heat, add the leeks with a pinch of salt and cook for 10 mins, stirring so they don’t stick, until softened. Tip in the potatoes, turn up the heat and fry for a couple of mins to crisp them up a bit. Flake through the mackerel. Make four indents in the leek mixture in the pan, crack an egg into each, season, then cover the pan and cook for 6-8 mins until the whites have set and the yolks are runny. Serve the horseradish on the side, with the pan in the middle of the table.','Smoked mackerel & leek hash with horseradish',1),(9,240,'Spray slow cooker with cooking spray (this is optional, but I like to do it). Put frozen potatoes in a slow cooker. In a bowl combine sour cream, cream of chicken soup and garlic salt and stir to combine. Pour mixture on top of the potatoes. Add cheese to the slow cooker and stir everything together. Turn slow cooker on high and cook for 4 hours, then serve and enjoy.  ','Slow Cooker Cheesy Potatoes',3),(10,40,'Preheat oven to 350 F. Brown ground beef, drain, and set aside. Layer lasagna dish with 1/4th of pasta sauce, 1/3rd of the ground beef, and 1/3rd of the cheese. Place a layer of noodles over top of the cheese, and dab with 3 TBS of butter. Repeat the above step to make a total of three layers. When the last layer of pasta noodles are placed add the last of the butter, sauce, and cheese.Bake for 40 minutes. Enjoy! ','Lasagna',4),(11,15,'Preheat the oven to 450 degrees F. Combine all the ingredients together in a large bowl. Knead the dough on a floured surface for about 30 seconds. Roll to 1/2 inch thick. Use a circle cutter (or an upturned drinking glass) to cut the biscuits. Place the biscuits on ungreased cookie sheet. Brush the tops with melted butter to help them brown. Bake at 450 degrees F for about 15 minutes.','No Milk Biscuit Recipe',5),(12,20,'Preheat oven to 350 degrees F. Spray a 9 x 13-inch baking dish with cooking spray. Unroll crescent roll dough and gently press into the bottom of the prepared dish to form a crust. Set aside. Cook ground beef in a large skillet over medium-high heat until meat is no longer pink. Drain and return to skillet. Stir in taco seasoning mix and ⅔ cup water. Bring to a boil, reduce heat to low, and simmer uncovered for 3-4 minutes (stirring often), until thickened. Stir in salsa. Spoon beef mixture over the crescent roll dough. Sprinkle with grated cheese. Bake for 20 minutes, or until crust is golden brown. Cut into squares, garnish with optional toppings, and serve. ','Taco Casserole',2);
/*!40000 ALTER TABLE `rm_recipe` ENABLE KEYS */;
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
