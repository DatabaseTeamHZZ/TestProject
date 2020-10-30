/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : b1

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-10-29 20:17:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for buyer
-- ----------------------------
DROP TABLE IF EXISTS `buyer`;
CREATE TABLE `buyer` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `b_id` (`id`),
  CONSTRAINT `b_id` FOREIGN KEY (`id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of buyer
-- ----------------------------
INSERT INTO `buyer` VALUES ('1003', null, null);

-- ----------------------------
-- Table structure for cashier
-- ----------------------------
DROP TABLE IF EXISTS `cashier`;
CREATE TABLE `cashier` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cs_id` (`id`),
  CONSTRAINT `cs_id` FOREIGN KEY (`id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of cashier
-- ----------------------------
INSERT INTO `cashier` VALUES ('1002', null, null);

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `point` decimal(10,2) NOT NULL DEFAULT '0.00',
  `vip` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `cstm_id` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES ('1', '初始顾客', '12345', '1000.00', '1');

-- ----------------------------
-- Table structure for customer_point
-- ----------------------------
DROP TABLE IF EXISTS `customer_point`;
CREATE TABLE `customer_point` (
  `order` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `get_point` decimal(10,2) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `way` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`order`),
  KEY `cstm_id` (`customer_id`),
  CONSTRAINT `cstm_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of customer_point
-- ----------------------------
INSERT INTO `customer_point` VALUES ('1', '1', '50.00', '2020-10-29 20:03:13', '1');
INSERT INTO `customer_point` VALUES ('2', '1', '950.00', '2020-10-29 20:11:17', '2');

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `goods_id` int NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(20) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `cost` decimal(10,2) NOT NULL,
  `quantity` int unsigned NOT NULL DEFAULT '0',
  `goods_type` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`goods_id`),
  UNIQUE KEY `gds_id` (`goods_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('1', '初始商品', '10.00', '5.00', '5', '0');

-- ----------------------------
-- Table structure for goods_type_name
-- ----------------------------
DROP TABLE IF EXISTS `goods_type_name`;
CREATE TABLE `goods_type_name` (
  `goods_type` int NOT NULL,
  `type_name` varchar(20) NOT NULL,
  PRIMARY KEY (`goods_type`,`type_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of goods_type_name
-- ----------------------------
INSERT INTO `goods_type_name` VALUES ('0', '未定义类');
INSERT INTO `goods_type_name` VALUES ('1', '生活类');
INSERT INTO `goods_type_name` VALUES ('2', '办公类');
INSERT INTO `goods_type_name` VALUES ('3', '书籍类');
INSERT INTO `goods_type_name` VALUES ('4', '电器类');
INSERT INTO `goods_type_name` VALUES ('5', '饮食类');

-- ----------------------------
-- Table structure for purchase
-- ----------------------------
DROP TABLE IF EXISTS `purchase`;
CREATE TABLE `purchase` (
  `customer_id` int NOT NULL,
  `goods_id` int NOT NULL,
  `quantity` int NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `payment` decimal(10,2) NOT NULL DEFAULT '0.00',
  `profit` decimal(10,2) NOT NULL DEFAULT '0.00',
  `order` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`order`),
  KEY `cst_id` (`customer_id`),
  KEY `gds_id` (`goods_id`),
  CONSTRAINT `cst_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `gds_id` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`goods_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of purchase
-- ----------------------------
INSERT INTO `purchase` VALUES ('1', '1', '5', '2020-10-29 20:03:13', '50.00', '25.00', '4');

-- ----------------------------
-- Table structure for stock
-- ----------------------------
DROP TABLE IF EXISTS `stock`;
CREATE TABLE `stock` (
  `order` int NOT NULL AUTO_INCREMENT,
  `goods_id` int NOT NULL,
  `id` int NOT NULL,
  `quantity` int NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order`),
  KEY `g_id` (`goods_id`),
  KEY `buyer_id` (`id`),
  CONSTRAINT `buyer_id` FOREIGN KEY (`id`) REFERENCES `buyer` (`id`),
  CONSTRAINT `g_id` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`goods_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of stock
-- ----------------------------
INSERT INTO `stock` VALUES ('1', '1', '1003', '10', '2020-10-29 20:02:00');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(10) NOT NULL,
  `user_type` int NOT NULL,
  `if_logout` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_id` (`id`) USING BTREE,
  KEY `u_type` (`user_type`)
) ENGINE=InnoDB AUTO_INCREMENT=1004 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1000', '123', '1', '0');
INSERT INTO `user` VALUES ('1001', '123', '1', '0');
INSERT INTO `user` VALUES ('1002', '123', '2', '0');
INSERT INTO `user` VALUES ('1003', '123', '3', '0');

-- ----------------------------
-- Table structure for vip_discount
-- ----------------------------
DROP TABLE IF EXISTS `vip_discount`;
CREATE TABLE `vip_discount` (
  `vip` int NOT NULL,
  `discount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`vip`),
  UNIQUE KEY `vip-level` (`vip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of vip_discount
-- ----------------------------
INSERT INTO `vip_discount` VALUES ('0', '1.00');
INSERT INTO `vip_discount` VALUES ('1', '0.98');
INSERT INTO `vip_discount` VALUES ('2', '0.96');
INSERT INTO `vip_discount` VALUES ('3', '0.94');
INSERT INTO `vip_discount` VALUES ('4', '0.92');
INSERT INTO `vip_discount` VALUES ('5', '0.90');
DROP TRIGGER IF EXISTS `after_get_point`;
DELIMITER ;;
CREATE TRIGGER `after_get_point` AFTER INSERT ON `customer_point` FOR EACH ROW begin
    declare origin_point decimal(10,2);
    declare new_point decimal(10,2);
    declare new_vip int;
    set origin_point=(select point from customer where customer_id=new.customer_id);
    set new_point=(origin_point+new.get_point);
    update customer set point=new_point where customer_id=new.customer_id;
    set new_vip=0;
    if(new_point>=1000 and new_point<3000) then set new_vip=1;end if;
    if(new_point>=3000 and new_point<5000) then set new_vip=2;end if;
    if(new_point>=5000 and new_point<10000) then set new_vip=3;end if;
    if(new_point>=10000 and new_point<20000) then set new_vip=4;end if;
    if(new_point>=20000) then set new_vip=5;end if;
    update customer set vip=new_vip where customer_id=new.customer_id;
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `after_purchase`;
DELIMITER ;;
CREATE TRIGGER `after_purchase` AFTER INSERT ON `purchase` FOR EACH ROW begin
    declare original_quantity int;
    declare remain_quantity int;
    declare point decimal(10,2);
    set original_quantity=(select quantity from goods where goods_id=new.goods_id);
    set remain_quantity=(original_quantity-new.quantity);
    update goods set quantity=remain_quantity where goods_id=new.goods_id;
    set point=new.payment;
    insert into customer_point(customer_id,get_point,way) values (new.customer_id,point,1);
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `after_stock`;
DELIMITER ;;
CREATE TRIGGER `after_stock` AFTER INSERT ON `stock` FOR EACH ROW begin
    declare origin_quantity int;
    declare new_quantity int;
    set origin_quantity=(select quantity from goods where goods_id=new.goods_id);
    set new_quantity=origin_quantity+new.quantity;
    update goods set quantity=new_quantity where goods_id=new.goods_id;
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `insert_staff`;
DELIMITER ;;
CREATE TRIGGER `insert_staff` AFTER INSERT ON `user` FOR EACH ROW begin
    if(new.user_type=2) then insert into cashier(id) values(new.id);
    end if;
    if(new.user_type=3) then insert into buyer(id) values(new.id);
    end if;
end
;;
DELIMITER ;
