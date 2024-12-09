-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        8.0.40 - MySQL Community Server - GPL
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 导出 dropindb 的数据库结构
DROP DATABASE IF EXISTS `dropindb`;
CREATE DATABASE IF NOT EXISTS `dropindb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dropindb`;

-- 导出  表 dropindb.cards 结构
DROP TABLE IF EXISTS `cards`;
CREATE TABLE IF NOT EXISTS `cards` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL COMMENT 'only english, for others, use dict<id, lang>',
  `url` varchar(128) NOT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sort` int DEFAULT NULL COMMENT 'show order by',
  `type` varchar(16) NOT NULL COMMENT 'G1, G2, D40',
  `img` varchar(16) NOT NULL COMMENT '图片文件名称，不带状态',
  `is_published` int DEFAULT NULL,
  `coming_img` varchar(16) DEFAULT NULL COMMENT '未发布时的图片，为空则是默认值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 数据导出被取消选择。

-- 导出  表 dropindb.games 结构
DROP TABLE IF EXISTS `games`;
CREATE TABLE IF NOT EXISTS `games` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uid` varchar(32) NOT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `ip` varchar(48) NOT NULL COMMENT 'ipv4, ipv6',
  `passed` tinyint NOT NULL DEFAULT '0',
  `score` int NOT NULL DEFAULT '0',
  `gold` int NOT NULL DEFAULT '0',
  `steps` json DEFAULT NULL COMMENT 'layout, steps, null first.',
  `award_ext` json DEFAULT NULL COMMENT 'custom json data, eg: reward 2 cards one game.',
  PRIMARY KEY (`id`),
  KEY `FK_games_users` (`uid`) USING BTREE,
  CONSTRAINT `FK_games_users` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='game''s record';

-- 数据导出被取消选择。

-- 导出  表 dropindb.internal_configs 结构
DROP TABLE IF EXISTS `internal_configs`;
CREATE TABLE IF NOT EXISTS `internal_configs` (
  `key` varchar(32) NOT NULL,
  `value` json NOT NULL,
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='内部配置表';

-- 数据导出被取消选择。

-- 导出  表 dropindb.internal_tasks 结构
DROP TABLE IF EXISTS `internal_tasks`;
CREATE TABLE IF NOT EXISTS `internal_tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(64) NOT NULL,
  `type` varchar(32) NOT NULL COMMENT 'page use',
  `title` varchar(128) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `image` varchar(64) NOT NULL COMMENT 'icon name or image url',
  `score` int NOT NULL DEFAULT '0',
  `gold` int NOT NULL DEFAULT '0',
  `card` int unsigned DEFAULT NULL COMMENT 'award_card_id, no use now',
  `ext` json DEFAULT NULL COMMENT 'extend',
  `order` int DEFAULT NULL COMMENT 'show order by',
  PRIMARY KEY (`id`),
  KEY `FK_internal_tasks_cards` (`card`),
  CONSTRAINT `FK_internal_tasks_cards` FOREIGN KEY (`card`) REFERENCES `cards` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='admin config tasks. NOTE: no sign in tasks.';

-- 数据导出被取消选择。

-- 导出  表 dropindb.users 结构
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `tid` bigint NOT NULL COMMENT 'telegram WebAppUser.id',
  `uid` char(32) NOT NULL COMMENT 'uuid 36',
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) DEFAULT NULL,
  `username` varchar(64) DEFAULT NULL,
  `language_code` varchar(64) DEFAULT NULL COMMENT 'zh, en, ru',
  `is_premium` tinyint DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `inviter` bigint DEFAULT NULL COMMENT 'inviter tid',
  `score` int NOT NULL DEFAULT '0',
  `gold` int NOT NULL DEFAULT '0',
  `done_count` int NOT NULL DEFAULT '0' COMMENT 'finish''s count',
  `x` bigint DEFAULT NULL COMMENT 'twitter account',
  `x_followed` tinyint NOT NULL DEFAULT '0' COMMENT 'is follow x''s account',
  `invite_type` varchar(32) DEFAULT NULL COMMENT 'my invite type: common, pro, ...',
  `wallet` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`uid`) USING BTREE,
  UNIQUE KEY `tid` (`tid`),
  UNIQUE KEY `wallet` (`wallet`),
  KEY `FK_users_users` (`inviter`),
  CONSTRAINT `FK_users_users` FOREIGN KEY (`inviter`) REFERENCES `users` (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='users table';

-- 数据导出被取消选择。

-- 导出  表 dropindb.users_cards 结构
DROP TABLE IF EXISTS `users_cards`;
CREATE TABLE IF NOT EXISTS `users_cards` (
  `uid` char(32) NOT NULL,
  `card_id` int unsigned NOT NULL,
  `by_type` varchar(32) NOT NULL COMMENT 'G1, G2, invite, signIn40',
  `game_id` bigint unsigned DEFAULT NULL,
  `invite_uid` char(32) DEFAULT NULL,
  `task_id` bigint unsigned DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `FK_users_cards_users` (`uid`),
  KEY `FK_users_cards_games` (`game_id`),
  KEY `FK_users_cards_users_2` (`invite_uid`),
  KEY `FK_users_cards_users_tasks` (`task_id`),
  CONSTRAINT `FK_users_cards_games` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`),
  CONSTRAINT `FK_users_cards_users` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`),
  CONSTRAINT `FK_users_cards_users_2` FOREIGN KEY (`invite_uid`) REFERENCES `users` (`uid`),
  CONSTRAINT `FK_users_cards_users_tasks` FOREIGN KEY (`task_id`) REFERENCES `users_tasks` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='user''s cards';

-- 数据导出被取消选择。

-- 导出  表 dropindb.users_golds 结构
DROP TABLE IF EXISTS `users_golds`;
CREATE TABLE IF NOT EXISTS `users_golds` (
  `uid` char(32) NOT NULL,
  `gold` int NOT NULL COMMENT 'get/consume gold',
  `by_type` varchar(32) NOT NULL COMMENT 'firstDone, invite, signIn40',
  `game_id` bigint unsigned DEFAULT NULL,
  `invite_uid` char(32) DEFAULT NULL,
  `task_id` bigint unsigned DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `FK_users_golds_users` (`uid`) USING BTREE,
  KEY `FK_users_golds_games` (`game_id`) USING BTREE,
  KEY `FK_users_golds_users_2` (`invite_uid`) USING BTREE,
  KEY `FK_users_golds_users_tasks` (`task_id`) USING BTREE,
  CONSTRAINT `FK_users_golds_games` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`),
  CONSTRAINT `FK_users_golds_users` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`),
  CONSTRAINT `FK_users_golds_users_2` FOREIGN KEY (`invite_uid`) REFERENCES `users` (`uid`),
  CONSTRAINT `FK_users_golds_users_tasks` FOREIGN KEY (`task_id`) REFERENCES `users_tasks` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 数据导出被取消选择。

-- 导出  表 dropindb.users_scores 结构
DROP TABLE IF EXISTS `users_scores`;
CREATE TABLE IF NOT EXISTS `users_scores` (
  `uid` char(32) NOT NULL,
  `score` int NOT NULL COMMENT 'get/consume score',
  `by_type` varchar(32) NOT NULL COMMENT 'gameDone, invite, signIn40',
  `game_id` bigint unsigned DEFAULT NULL,
  `invite_uid` char(32) DEFAULT NULL,
  `task_id` bigint unsigned DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `FK_users_scores_users` (`uid`),
  KEY `FK_users_scores_games` (`game_id`),
  KEY `FK_users_scores_users_2` (`invite_uid`),
  KEY `FK_users_scores_users_tasks` (`task_id`),
  CONSTRAINT `FK_users_scores_games` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`),
  CONSTRAINT `FK_users_scores_users` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`),
  CONSTRAINT `FK_users_scores_users_2` FOREIGN KEY (`invite_uid`) REFERENCES `users` (`uid`),
  CONSTRAINT `FK_users_scores_users_tasks` FOREIGN KEY (`task_id`) REFERENCES `users_tasks` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 数据导出被取消选择。

-- 导出  表 dropindb.users_tasks 结构
DROP TABLE IF EXISTS `users_tasks`;
CREATE TABLE IF NOT EXISTS `users_tasks` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uid` char(32) NOT NULL,
  `type` varchar(16) NOT NULL COMMENT 'task type: signIn, bindX, followX',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `score` int NOT NULL DEFAULT '0',
  `gold` int NOT NULL DEFAULT '0',
  `card` int unsigned DEFAULT NULL,
  `signin_date` date DEFAULT NULL COMMENT 'only for signIn',
  `award_ext` varchar(64) DEFAULT NULL COMMENT 'json: custom award, eg: 2 cards one game.\r\ndescription for this task and award, eg: signIn40',
  `wait` json DEFAULT NULL COMMENT 'wait tasks',
  `complete` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `FK_users_tasks_users` (`uid`),
  KEY `FK_users_tasks_cards` (`card`) USING BTREE,
  CONSTRAINT `FK_users_tasks_cards` FOREIGN KEY (`card`) REFERENCES `cards` (`id`),
  CONSTRAINT `FK_users_tasks_users` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 数据导出被取消选择。

-- 导出  表 dropindb.user_logins 结构
DROP TABLE IF EXISTS `user_logins`;
CREATE TABLE IF NOT EXISTS `user_logins` (
  `uid` char(32) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ip` varchar(48) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='login records.';

-- 数据导出被取消选择。

-- 导出  表 dropindb.user_wallets 结构
DROP TABLE IF EXISTS `user_wallets`;
CREATE TABLE IF NOT EXISTS `user_wallets` (
  `uid` char(32) NOT NULL,
  `address` varchar(128) NOT NULL,
  `create_time` datetime NOT NULL,
  `account` json NOT NULL,
  `update_time` datetime DEFAULT NULL,
  KEY `FK_user_wallets_users` (`uid`),
  CONSTRAINT `FK_user_wallets_users` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 数据导出被取消选择。

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
