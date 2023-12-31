-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: 45.154.99.10    Database: tasko
-- ------------------------------------------------------
-- Server version	5.5.5-10.11.3-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `tasko`48wGK#t0:ZOx9c
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tasko` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `tasko`;

--
-- Table structure for table `FLAG`
--

DROP TABLE IF EXISTS `FLAG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FLAG` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `color` varchar(7) DEFAULT '#FFFFFF',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table des flags';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FLAG`
--

LOCK TABLES `FLAG` WRITE;
/*!40000 ALTER TABLE `FLAG` DISABLE KEYS */;
INSERT INTO `FLAG` (`id`, `name`, `color`) VALUES (1,'testflag','#FFFFFF'),(3,'testviapython','#000000'),(4,'New Flag Updated','#BBBBBB'),(5,'New Flag','#AAAAAA'),(6,'New Flag','#AAAAAA'),(7,'New Flag','#AAAAAA'),(8,'New Flag','#AAAAAA'),(9,'New Flag','#AAAAAA');
/*!40000 ALTER TABLE `FLAG` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRIORITY`
--

DROP TABLE IF EXISTS `PRIORITY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PRIORITY` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table des priorités';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRIORITY`
--

LOCK TABLES `PRIORITY` WRITE;
/*!40000 ALTER TABLE `PRIORITY` DISABLE KEYS */;
INSERT INTO `PRIORITY` (`id`, `name`) VALUES (1,'P1'),(2,'P2'),(3,'P3'),(4,'P4'),(5,'New Priority'),(6,'New Priority Updated'),(7,'New Priority'),(8,'New Priority'),(9,'New Priority'),(10,'New Priority');
/*!40000 ALTER TABLE `PRIORITY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROJECT`
--

DROP TABLE IF EXISTS `PROJECT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROJECT` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROJECT`
--

LOCK TABLES `PROJECT` WRITE;
/*!40000 ALTER TABLE `PROJECT` DISABLE KEYS */;
INSERT INTO `PROJECT` (`id`, `name`, `description`, `user_id`) VALUES (1,'project','projectdescription',1);
/*!40000 ALTER TABLE `PROJECT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROJECT_TASK`
--

DROP TABLE IF EXISTS `PROJECT_TASK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROJECT_TASK` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `task_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `PROJECT_TASK_FK` (`task_id`),
  KEY `PROJECT_TASK_FK_1` (`project_id`),
  CONSTRAINT `PROJECT_TASK_FK` FOREIGN KEY (`task_id`) REFERENCES `TASK` (`id`),
  CONSTRAINT `PROJECT_TASK_FK_1` FOREIGN KEY (`project_id`) REFERENCES `PROJECT` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROJECT_TASK`
--

LOCK TABLES `PROJECT_TASK` WRITE;
/*!40000 ALTER TABLE `PROJECT_TASK` DISABLE KEYS */;
INSERT INTO `PROJECT_TASK` (`id`, `project_id`, `task_id`) VALUES (1,1,1),(2,1,66),(3,1,67),(4,1,68),(5,1,69),(6,1,70),(7,1,71),(8,1,72),(9,1,73),(10,1,74);
/*!40000 ALTER TABLE `PROJECT_TASK` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROJECT_USER`
--

DROP TABLE IF EXISTS `PROJECT_USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROJECT_USER` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_d` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `PROJECT_USER_FK` (`project_d`),
  KEY `PROJECT_USER_FK_1` (`user_id`),
  CONSTRAINT `PROJECT_USER_FK` FOREIGN KEY (`project_d`) REFERENCES `PROJECT` (`id`),
  CONSTRAINT `PROJECT_USER_FK_1` FOREIGN KEY (`user_id`) REFERENCES `USER` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROJECT_USER`
--

LOCK TABLES `PROJECT_USER` WRITE;
/*!40000 ALTER TABLE `PROJECT_USER` DISABLE KEYS */;
INSERT INTO `PROJECT_USER` (`id`, `project_d`, `user_id`) VALUES (1,1,1);
/*!40000 ALTER TABLE `PROJECT_USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RIGHTS`
--

DROP TABLE IF EXISTS `RIGHTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RIGHTS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `read` tinyint(1) NOT NULL DEFAULT 0,
  `write` tinyint(1) NOT NULL DEFAULT 0,
  `description` mediumtext DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table des droits';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RIGHTS`
--

LOCK TABLES `RIGHTS` WRITE;
/*!40000 ALTER TABLE `RIGHTS` DISABLE KEYS */;
INSERT INTO `RIGHTS` (`id`, `read`, `write`, `description`) VALUES (1,1,1,'ALL RIGHTS'),(2,1,0,'READ ONLY');
/*!40000 ALTER TABLE `RIGHTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STATE`
--

DROP TABLE IF EXISTS `STATE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `STATE` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table des états de tâches';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STATE`
--

LOCK TABLES `STATE` WRITE;
/*!40000 ALTER TABLE `STATE` DISABLE KEYS */;
INSERT INTO `STATE` (`id`, `name`) VALUES (1,'TO START'),(2,'IN PROGRESS'),(3,'FINISHED'),(4,'New State'),(5,'New State');
/*!40000 ALTER TABLE `STATE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUBTASK`
--

DROP TABLE IF EXISTS `SUBTASK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUBTASK` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL,
  `flag_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `priority_id` int(11) DEFAULT NULL,
  `task_id` int(11) DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `SUBTASK_FK` (`state_id`),
  KEY `SUBTASK_FK_1` (`flag_id`),
  KEY `SUBTASK_FK_2` (`priority_id`),
  CONSTRAINT `SUBTASK_FK` FOREIGN KEY (`state_id`) REFERENCES `STATE` (`id`),
  CONSTRAINT `SUBTASK_FK_1` FOREIGN KEY (`flag_id`) REFERENCES `FLAG` (`id`),
  CONSTRAINT `SUBTASK_FK_2` FOREIGN KEY (`priority_id`) REFERENCES `PRIORITY` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table de sous-tâche';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUBTASK`
--

LOCK TABLES `SUBTASK` WRITE;
/*!40000 ALTER TABLE `SUBTASK` DISABLE KEYS */;
INSERT INTO `SUBTASK` (`id`, `name`, `description`, `state_id`, `flag_id`, `user_id`, `priority_id`, `task_id`, `due_date`) VALUES (1,'subtasktest','subtasktestdescription',2,1,1,1,0,NULL),(2,'New Subtask','Description of the subtask',1,1,1,1,0,NULL),(7,'New Subtask Updated','Description of the subtask Updated',1,1,1,1,0,NULL),(8,'New Subtask','Description of the subtask',1,1,1,1,0,NULL),(14,'New Subtask','Description of the subtask',1,1,1,1,0,NULL),(15,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(16,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(17,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(18,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(19,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(20,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(21,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(22,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(23,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(24,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(25,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(26,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(27,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(28,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL),(29,'New Subtask','Description of the subtask',1,1,1,1,NULL,NULL);
/*!40000 ALTER TABLE `SUBTASK` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUBTASK_USER`
--

DROP TABLE IF EXISTS `SUBTASK_USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUBTASK_USER` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `subtask_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `SUBTASK_USER_FK` (`subtask_id`),
  KEY `SUBTASK_USER_FK_1` (`user_id`),
  CONSTRAINT `SUBTASK_USER_FK` FOREIGN KEY (`subtask_id`) REFERENCES `SUBTASK` (`id`),
  CONSTRAINT `SUBTASK_USER_FK_1` FOREIGN KEY (`user_id`) REFERENCES `USER` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table qui lie les sous-tâches et les utilisateurs';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUBTASK_USER`
--

LOCK TABLES `SUBTASK_USER` WRITE;
/*!40000 ALTER TABLE `SUBTASK_USER` DISABLE KEYS */;
INSERT INTO `SUBTASK_USER` (`id`, `user_id`, `subtask_id`) VALUES (1,7,1),(2,7,1),(3,7,1),(4,7,1),(5,7,1);
/*!40000 ALTER TABLE `SUBTASK_USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TASK`
--

DROP TABLE IF EXISTS `TASK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TASK` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext NOT NULL,
  `description` longtext DEFAULT NULL,
  `priority_id` int(11) DEFAULT NULL,
  `flag_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL,
  `subtask_id` int(11) DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TASK_FK` (`priority_id`),
  KEY `TASK_FK_1` (`flag_id`),
  KEY `TASK_FK_3` (`state_id`),
  KEY `TASK_FK_4` (`subtask_id`),
  KEY `TASK_FK_2` (`user_id`),
  CONSTRAINT `TASK_FK` FOREIGN KEY (`priority_id`) REFERENCES `PRIORITY` (`id`),
  CONSTRAINT `TASK_FK_1` FOREIGN KEY (`flag_id`) REFERENCES `FLAG` (`id`),
  CONSTRAINT `TASK_FK_2` FOREIGN KEY (`user_id`) REFERENCES `TASK_USER` (`id`),
  CONSTRAINT `TASK_FK_3` FOREIGN KEY (`state_id`) REFERENCES `STATE` (`id`),
  CONSTRAINT `TASK_FK_4` FOREIGN KEY (`subtask_id`) REFERENCES `SUBTASK` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table des tâches';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TASK`
--

LOCK TABLES `TASK` WRITE;
/*!40000 ALTER TABLE `TASK` DISABLE KEYS */;
INSERT INTO `TASK` (`id`, `name`, `description`, `priority_id`, `flag_id`, `user_id`, `state_id`, `subtask_id`, `due_date`, `project_id`) VALUES (1,'testtask','testtaskdescription',1,1,1,1,1,NULL,NULL),(2,'testviapython','descriptionviapython',1,1,1,1,1,NULL,NULL),(3,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,NULL,NULL),(4,'New Task PyTest Updated','Description of the task PyTest Updated',1,1,1,1,1,NULL,NULL),(5,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,NULL,NULL),(6,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,NULL,NULL),(9,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(10,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(11,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(12,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(13,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(14,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(15,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(16,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(17,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(18,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(19,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(20,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(21,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(22,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(23,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(24,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(25,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(26,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(27,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(28,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(29,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(30,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(31,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(32,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(33,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(34,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(35,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(36,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(37,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(38,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(39,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(40,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(41,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(43,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(44,'test','',1,1,1,1,1,'2023-12-31',NULL),(45,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(46,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(47,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(48,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(49,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(50,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(51,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(52,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(53,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(54,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(55,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(56,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(57,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(58,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(59,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(60,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(61,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(62,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(63,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(64,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(65,'New Task PyTest','Description of the task PyTest',1,1,1,1,1,'2021-01-01',NULL),(66,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(67,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(68,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(69,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(70,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(71,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(72,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(73,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL),(74,'New Task','Description of the task',1,1,1,1,NULL,NULL,NULL);
/*!40000 ALTER TABLE `TASK` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TASK_SUBTASK`
--

DROP TABLE IF EXISTS `TASK_SUBTASK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TASK_SUBTASK` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) DEFAULT NULL,
  `subtask_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TASK_SUBTASK_FK` (`task_id`),
  KEY `TASK_SUBTASK_FK_1` (`subtask_id`),
  CONSTRAINT `TASK_SUBTASK_FK` FOREIGN KEY (`task_id`) REFERENCES `TASK` (`id`),
  CONSTRAINT `TASK_SUBTASK_FK_1` FOREIGN KEY (`subtask_id`) REFERENCES `SUBTASK` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table qui lie les tâches et les sous- tâches';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TASK_SUBTASK`
--

LOCK TABLES `TASK_SUBTASK` WRITE;
/*!40000 ALTER TABLE `TASK_SUBTASK` DISABLE KEYS */;
INSERT INTO `TASK_SUBTASK` (`id`, `task_id`, `subtask_id`) VALUES (1,1,1),(2,1,NULL),(3,1,NULL),(4,1,NULL),(5,1,NULL),(6,1,16),(7,1,17),(8,1,18),(9,1,19),(10,1,20),(11,1,21),(12,1,22),(13,1,23),(14,1,1),(15,1,24),(16,1,1),(17,1,25),(18,1,26),(19,1,27),(20,1,28),(21,1,1),(22,1,29),(23,1,1);
/*!40000 ALTER TABLE `TASK_SUBTASK` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TASK_USER`
--

DROP TABLE IF EXISTS `TASK_USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TASK_USER` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TASK_USER_FK` (`task_id`),
  KEY `TASK_USER_FK_1` (`user_id`),
  CONSTRAINT `TASK_USER_FK` FOREIGN KEY (`task_id`) REFERENCES `TASK` (`id`),
  CONSTRAINT `TASK_USER_FK_1` FOREIGN KEY (`user_id`) REFERENCES `USER` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table qui lie les utilisateurs et les tâches';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TASK_USER`
--

LOCK TABLES `TASK_USER` WRITE;
/*!40000 ALTER TABLE `TASK_USER` DISABLE KEYS */;
INSERT INTO `TASK_USER` (`id`, `task_id`, `user_id`) VALUES (1,1,7),(4,1,7),(5,1,7),(6,1,7),(7,1,7),(8,1,7);
/*!40000 ALTER TABLE `TASK_USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USER` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mail` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `rights_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `USER_FK` (`rights_id`),
  CONSTRAINT `USER_FK` FOREIGN KEY (`rights_id`) REFERENCES `RIGHTS` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table des utilisateurs';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER`
--

LOCK TABLES `USER` WRITE;
/*!40000 ALTER TABLE `USER` DISABLE KEYS */;
INSERT INTO `USER` (`id`, `mail`, `password`, `name`, `rights_id`) VALUES (1,'testpytest@totor.com','passwordupdated','totorupdated',1),(7,'test@test.com','testpassword','testname',2),(15,'louis@test.com','test','louis',1),(16,'john@pytest.com','password','John',1),(17,'john@pytest.com','password','John',1),(18,'john@pytest.com','password','John',1),(19,'john@pytest.com','password','John',1),(20,'martin.baumgaertner@uha.fr','martin','martin',1),(21,'martin.martin@gmail.com','martin','martin',1),(22,'john@pytest.com','password','John',1),(23,'john@pytest.com','password','John',1);
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-12 10:00:14