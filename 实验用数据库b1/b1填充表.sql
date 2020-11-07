/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : b1

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-11-05 21:56:36
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
INSERT INTO `buyer` VALUES ('1006', '韩', '12345');
INSERT INTO `buyer` VALUES ('1007', '赵', '12345');
INSERT INTO `buyer` VALUES ('1008', '朱', '12345');
INSERT INTO `buyer` VALUES ('1009', null, null);
INSERT INTO `buyer` VALUES ('1010', null, null);

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
INSERT INTO `cashier` VALUES ('1001', '韩', '12345');
INSERT INTO `cashier` VALUES ('1002', '赵', '12345');
INSERT INTO `cashier` VALUES ('1003', '朱', '12345');
INSERT INTO `cashier` VALUES ('1004', null, null);
INSERT INTO `cashier` VALUES ('1005', null, null);

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
  UNIQUE KEY `cstm_id` (`customer_id`),
  KEY `vip_level` (`vip`),
  CONSTRAINT `vip_level` FOREIGN KEY (`vip`) REFERENCES `vip_discount` (`vip`)
) ENGINE=InnoDB AUTO_INCREMENT=2009 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES ('2001', '赵', '12345', '9786.66', '3');
INSERT INTO `customer` VALUES ('2002', '钱', '12345', '17311.12', '4');
INSERT INTO `customer` VALUES ('2003', '孙', '12345', '86552.50', '5');
INSERT INTO `customer` VALUES ('2004', '李', '12345', '7535.34', '3');
INSERT INTO `customer` VALUES ('2005', '周', '54321', '6100.12', '3');
INSERT INTO `customer` VALUES ('2006', '吴', '54321', '8415.40', '3');
INSERT INTO `customer` VALUES ('2007', '郑', '54321', '369.40', '0');
INSERT INTO `customer` VALUES ('2008', '王', '54321', '75.00', '0');

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
  KEY `way_name` (`way`),
  CONSTRAINT `cstm_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `way_name` FOREIGN KEY (`way`) REFERENCES `get_point_way` (`way`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of customer_point
-- ----------------------------
INSERT INTO `customer_point` VALUES ('1', '2001', '4950.00', '2020-08-01 20:30:31', '1');
INSERT INTO `customer_point` VALUES ('2', '2002', '7900.00', '2020-08-01 20:31:18', '1');
INSERT INTO `customer_point` VALUES ('3', '2003', '3150.00', '2020-08-01 20:31:36', '1');
INSERT INTO `customer_point` VALUES ('4', '2004', '1336.00', '2020-08-01 20:32:13', '1');
INSERT INTO `customer_point` VALUES ('5', '2001', '4800.00', '2020-08-05 10:15:30', '1');
INSERT INTO `customer_point` VALUES ('6', '2005', '40.00', '2020-08-06 09:25:00', '1');
INSERT INTO `customer_point` VALUES ('7', '2007', '45.00', '2020-08-10 14:30:18', '1');
INSERT INTO `customer_point` VALUES ('8', '2003', '9600.00', '2020-08-13 20:36:24', '1');
INSERT INTO `customer_point` VALUES ('9', '2006', '16.00', '2020-08-13 17:37:49', '1');
INSERT INTO `customer_point` VALUES ('10', '2004', '1000.00', '2020-08-14 12:18:04', '2');
INSERT INTO `customer_point` VALUES ('11', '2005', '15.00', '2020-08-16 13:43:07', '1');
INSERT INTO `customer_point` VALUES ('12', '2002', '3.76', '2020-08-16 14:16:47', '1');
INSERT INTO `customer_point` VALUES ('13', '2003', '73600.00', '2020-08-25 09:40:02', '1');
INSERT INTO `customer_point` VALUES ('14', '2007', '60.00', '2020-08-26 19:47:52', '1');
INSERT INTO `customer_point` VALUES ('15', '2004', '39.20', '2020-08-29 07:25:07', '1');
INSERT INTO `customer_point` VALUES ('16', '2002', '9400.00', '2020-08-31 08:48:23', '1');
INSERT INTO `customer_point` VALUES ('17', '2001', '4.70', '2020-09-02 10:38:38', '1');
INSERT INTO `customer_point` VALUES ('18', '2005', '6000.00', '2020-09-02 11:50:00', '1');
INSERT INTO `customer_point` VALUES ('19', '2006', '20.00', '2020-09-03 15:47:45', '1');
INSERT INTO `customer_point` VALUES ('20', '2003', '7.20', '2020-09-05 13:50:57', '1');
INSERT INTO `customer_point` VALUES ('21', '2006', '99.00', '2020-09-06 14:11:13', '1');
INSERT INTO `customer_point` VALUES ('22', '2006', '15.00', '2020-09-10 10:51:59', '1');
INSERT INTO `customer_point` VALUES ('23', '2006', '1000.00', '2020-09-10 14:39:15', '2');
INSERT INTO `customer_point` VALUES ('24', '2007', '15.00', '2020-09-11 20:54:46', '1');
INSERT INTO `customer_point` VALUES ('25', '2007', '18.00', '2020-09-14 10:33:53', '1');
INSERT INTO `customer_point` VALUES ('26', '2001', '28.20', '2020-09-15 11:25:25', '1');
INSERT INTO `customer_point` VALUES ('27', '2002', '7.36', '2020-09-17 17:12:39', '1');
INSERT INTO `customer_point` VALUES ('28', '2004', '77.42', '2020-09-17 20:15:49', '1');
INSERT INTO `customer_point` VALUES ('29', '2007', '99.00', '2020-09-20 13:20:57', '1');
INSERT INTO `customer_point` VALUES ('30', '2005', '28.20', '2020-09-21 10:16:14', '1');
INSERT INTO `customer_point` VALUES ('31', '2004', '3000.00', '2020-09-22 15:00:24', '2');
INSERT INTO `customer_point` VALUES ('32', '2006', '1000.00', '2020-09-22 15:01:39', '2');
INSERT INTO `customer_point` VALUES ('33', '2004', '18.80', '2020-09-23 16:11:58', '1');
INSERT INTO `customer_point` VALUES ('34', '2004', '2000.00', '2020-09-26 10:58:20', '2');
INSERT INTO `customer_point` VALUES ('35', '2005', '2.82', '2020-09-27 12:00:16', '1');
INSERT INTO `customer_point` VALUES ('36', '2003', '2.70', '2020-09-28 13:30:24', '1');
INSERT INTO `customer_point` VALUES ('37', '2003', '72.00', '2020-09-29 11:05:35', '1');
INSERT INTO `customer_point` VALUES ('38', '2003', '63.00', '2020-09-29 19:44:51', '1');
INSERT INTO `customer_point` VALUES ('39', '2006', '5880.00', '2020-10-01 08:01:11', '1');
INSERT INTO `customer_point` VALUES ('40', '2007', '33.40', '2020-10-01 09:11:28', '1');
INSERT INTO `customer_point` VALUES ('41', '2003', '3.60', '2020-10-01 11:09:40', '1');
INSERT INTO `customer_point` VALUES ('42', '2004', '42.30', '2020-10-03 18:06:52', '1');
INSERT INTO `customer_point` VALUES ('43', '2007', '30.00', '2020-10-04 13:02:52', '1');
INSERT INTO `customer_point` VALUES ('44', '2003', '54.00', '2020-10-05 15:43:03', '1');
INSERT INTO `customer_point` VALUES ('45', '2004', '7.52', '2020-10-08 11:56:08', '1');
INSERT INTO `customer_point` VALUES ('46', '2006', '371.30', '2020-10-09 12:04:19', '1');
INSERT INTO `customer_point` VALUES ('47', '2008', '75.00', '2020-10-11 09:30:32', '1');
INSERT INTO `customer_point` VALUES ('48', '2007', '3.00', '2020-10-12 15:01:49', '1');
INSERT INTO `customer_point` VALUES ('49', '2005', '14.10', '2020-10-15 14:25:08', '1');
INSERT INTO `customer_point` VALUES ('50', '2001', '3.76', '2020-10-18 07:35:17', '1');
INSERT INTO `customer_point` VALUES ('51', '2007', '18.00', '2020-10-19 11:17:49', '1');
INSERT INTO `customer_point` VALUES ('52', '2007', '40.00', '2020-10-20 15:12:56', '1');
INSERT INTO `customer_point` VALUES ('53', '2006', '14.10', '2020-10-21 17:06:06', '1');
INSERT INTO `customer_point` VALUES ('54', '2004', '14.10', '2020-10-22 10:33:15', '1');
INSERT INTO `customer_point` VALUES ('55', '2007', '8.00', '2020-10-22 18:17:17', '1');

-- ----------------------------
-- Table structure for get_point_way
-- ----------------------------
DROP TABLE IF EXISTS `get_point_way`;
CREATE TABLE `get_point_way` (
  `way` int NOT NULL,
  `way_name` varchar(20) NOT NULL,
  PRIMARY KEY (`way`,`way_name`),
  KEY `way` (`way`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of get_point_way
-- ----------------------------
INSERT INTO `get_point_way` VALUES ('1', '购买商品获得');
INSERT INTO `get_point_way` VALUES ('2', '直接充值获得');

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
  UNIQUE KEY `gds_id` (`goods_id`),
  KEY `gds_type` (`goods_type`),
  CONSTRAINT `gds_type` FOREIGN KEY (`goods_type`) REFERENCES `goods_type_name` (`goods_type`)
) ENGINE=InnoDB AUTO_INCREMENT=3021 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('3001', '数据库系统概念', '99.00', '20.00', '248', '3');
INSERT INTO `goods` VALUES ('3002', '数据结构算法与应用', '79.00', '15.00', '394', '3');
INSERT INTO `goods` VALUES ('3003', '计算机组成原理', '45.00', '10.00', '330', '3');
INSERT INTO `goods` VALUES ('3004', '概率论与数理统计', '33.40', '10.00', '359', '3');
INSERT INTO `goods` VALUES ('3005', 'I牌手机', '8000.00', '6000.00', '20', '4');
INSERT INTO `goods` VALUES ('3006', 'H牌手机', '5000.00', '3000.00', '59', '4');
INSERT INTO `goods` VALUES ('3007', 'L牌电脑', '6000.00', '3500.00', '28', '4');
INSERT INTO `goods` VALUES ('3008', 'G牌冰箱', '10000.00', '6000.00', '8', '4');
INSERT INTO `goods` VALUES ('3009', 'M牌牛奶', '70.00', '30.00', '49', '5');
INSERT INTO `goods` VALUES ('3010', 'Q牌咖啡', '20.00', '8.00', '29', '5');
INSERT INTO `goods` VALUES ('3011', 'T牌面包', '8.00', '2.50', '14', '5');
INSERT INTO `goods` VALUES ('3012', 'K牌方便面', '4.00', '0.80', '42', '5');
INSERT INTO `goods` VALUES ('3013', '茶杯', '15.00', '5.00', '12', '1');
INSERT INTO `goods` VALUES ('3014', '灯管', '30.00', '20.00', '7', '1');
INSERT INTO `goods` VALUES ('3015', '牙膏', '15.00', '5.00', '9', '1');
INSERT INTO `goods` VALUES ('3016', '拖把', '18.00', '6.50', '13', '1');
INSERT INTO `goods` VALUES ('3017', '钢笔', '40.00', '35.00', '25', '2');
INSERT INTO `goods` VALUES ('3018', '复印纸', '15.00', '10.00', '63', '2');
INSERT INTO `goods` VALUES ('3019', '圆珠笔', '3.00', '1.20', '77', '2');
INSERT INTO `goods` VALUES ('3020', '订书器', '5.00', '1.00', '29', '2');

-- ----------------------------
-- Table structure for goods_type_name
-- ----------------------------
DROP TABLE IF EXISTS `goods_type_name`;
CREATE TABLE `goods_type_name` (
  `goods_type` int NOT NULL,
  `type_name` varchar(20) NOT NULL,
  PRIMARY KEY (`goods_type`,`type_name`),
  KEY `goods_type` (`goods_type`)
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
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of purchase
-- ----------------------------
INSERT INTO `purchase` VALUES ('2001', '3001', '50', '2020-08-01 20:30:31', '4950.00', '3950.00', '1');
INSERT INTO `purchase` VALUES ('2002', '3002', '100', '2020-08-01 20:31:18', '7900.00', '6400.00', '2');
INSERT INTO `purchase` VALUES ('2003', '3003', '70', '2020-08-01 20:31:36', '3150.00', '2450.00', '3');
INSERT INTO `purchase` VALUES ('2004', '3004', '40', '2020-08-01 20:32:13', '1336.00', '936.00', '4');
INSERT INTO `purchase` VALUES ('2001', '3006', '1', '2020-08-05 10:15:30', '4800.00', '1800.00', '5');
INSERT INTO `purchase` VALUES ('2005', '3017', '1', '2020-08-06 09:25:00', '40.00', '5.00', '6');
INSERT INTO `purchase` VALUES ('2007', '3015', '3', '2020-08-10 14:30:18', '45.00', '30.00', '7');
INSERT INTO `purchase` VALUES ('2003', '3008', '1', '2020-08-13 20:36:24', '9600.00', '3600.00', '8');
INSERT INTO `purchase` VALUES ('2006', '3011', '2', '2020-08-13 17:37:49', '16.00', '11.00', '9');
INSERT INTO `purchase` VALUES ('2005', '3018', '1', '2020-08-16 13:43:07', '15.00', '5.00', '10');
INSERT INTO `purchase` VALUES ('2002', '3012', '1', '2020-08-16 14:16:47', '3.76', '2.96', '11');
INSERT INTO `purchase` VALUES ('2003', '3005', '10', '2020-08-25 09:40:02', '73600.00', '13600.00', '12');
INSERT INTO `purchase` VALUES ('2007', '3019', '20', '2020-08-26 19:47:52', '60.00', '36.00', '13');
INSERT INTO `purchase` VALUES ('2004', '3017', '1', '2020-08-29 07:25:07', '39.20', '4.20', '14');
INSERT INTO `purchase` VALUES ('2002', '3008', '1', '2020-08-31 08:48:23', '9400.00', '3400.00', '15');
INSERT INTO `purchase` VALUES ('2001', '3020', '1', '2020-09-02 10:38:38', '4.70', '3.70', '16');
INSERT INTO `purchase` VALUES ('2005', '3007', '1', '2020-09-02 11:50:00', '6000.00', '2500.00', '17');
INSERT INTO `purchase` VALUES ('2006', '3012', '5', '2020-09-03 15:47:45', '20.00', '16.00', '18');
INSERT INTO `purchase` VALUES ('2003', '3011', '1', '2020-09-05 13:50:57', '7.20', '4.70', '19');
INSERT INTO `purchase` VALUES ('2006', '3001', '1', '2020-09-06 14:11:13', '99.00', '79.00', '20');
INSERT INTO `purchase` VALUES ('2006', '3018', '1', '2020-09-10 10:51:59', '15.00', '5.00', '21');
INSERT INTO `purchase` VALUES ('2007', '3015', '1', '2020-09-11 20:54:46', '15.00', '10.00', '22');
INSERT INTO `purchase` VALUES ('2007', '3016', '1', '2020-09-14 10:33:53', '18.00', '11.50', '23');
INSERT INTO `purchase` VALUES ('2001', '3014', '1', '2020-09-15 11:25:25', '28.20', '8.20', '24');
INSERT INTO `purchase` VALUES ('2002', '3011', '1', '2020-09-17 17:12:39', '7.36', '4.86', '25');
INSERT INTO `purchase` VALUES ('2004', '3002', '1', '2020-09-17 20:15:49', '77.42', '62.42', '26');
INSERT INTO `purchase` VALUES ('2007', '3001', '1', '2020-09-20 13:20:57', '99.00', '79.00', '27');
INSERT INTO `purchase` VALUES ('2005', '3015', '2', '2020-09-21 10:16:14', '28.20', '18.20', '28');
INSERT INTO `purchase` VALUES ('2004', '3010', '1', '2020-09-23 16:11:58', '18.80', '10.80', '29');
INSERT INTO `purchase` VALUES ('2005', '3019', '1', '2020-09-27 12:00:16', '2.82', '1.62', '30');
INSERT INTO `purchase` VALUES ('2003', '3019', '1', '2020-09-28 13:30:24', '2.70', '1.50', '31');
INSERT INTO `purchase` VALUES ('2003', '3017', '2', '2020-09-29 11:05:35', '72.00', '2.00', '32');
INSERT INTO `purchase` VALUES ('2003', '3009', '1', '2020-09-29 19:44:51', '63.00', '33.00', '33');
INSERT INTO `purchase` VALUES ('2006', '3007', '1', '2020-10-01 08:01:11', '5880.00', '2380.00', '34');
INSERT INTO `purchase` VALUES ('2007', '3004', '1', '2020-10-01 09:11:28', '33.40', '23.40', '35');
INSERT INTO `purchase` VALUES ('2003', '3012', '1', '2020-10-01 11:09:40', '3.60', '2.80', '36');
INSERT INTO `purchase` VALUES ('2004', '3015', '3', '2020-10-03 18:06:52', '42.30', '27.30', '37');
INSERT INTO `purchase` VALUES ('2007', '3013', '2', '2020-10-04 13:02:52', '30.00', '20.00', '38');
INSERT INTO `purchase` VALUES ('2003', '3014', '2', '2020-10-05 15:43:03', '54.00', '14.00', '39');
INSERT INTO `purchase` VALUES ('2004', '3011', '1', '2020-10-08 11:56:08', '7.52', '5.02', '40');
INSERT INTO `purchase` VALUES ('2006', '3002', '5', '2020-10-09 12:04:19', '371.30', '296.30', '41');
INSERT INTO `purchase` VALUES ('2008', '3013', '5', '2020-10-11 09:30:32', '75.00', '50.00', '42');
INSERT INTO `purchase` VALUES ('2007', '3019', '1', '2020-10-12 15:01:49', '3.00', '1.80', '43');
INSERT INTO `purchase` VALUES ('2005', '3013', '1', '2020-10-15 14:25:08', '14.10', '9.10', '44');
INSERT INTO `purchase` VALUES ('2001', '3012', '1', '2020-10-18 07:35:17', '3.76', '2.96', '45');
INSERT INTO `purchase` VALUES ('2007', '3016', '1', '2020-10-19 11:17:49', '18.00', '11.50', '46');
INSERT INTO `purchase` VALUES ('2007', '3017', '1', '2020-10-20 15:12:56', '40.00', '5.00', '47');
INSERT INTO `purchase` VALUES ('2006', '3015', '1', '2020-10-21 17:06:06', '14.10', '9.10', '48');
INSERT INTO `purchase` VALUES ('2004', '3015', '1', '2020-10-22 10:33:15', '14.10', '9.10', '49');
INSERT INTO `purchase` VALUES ('2007', '3011', '1', '2020-10-22 18:17:17', '8.00', '5.50', '50');

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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of stock
-- ----------------------------
INSERT INTO `stock` VALUES ('1', '3001', '1006', '300', '2020-01-01 06:00:00');
INSERT INTO `stock` VALUES ('2', '3002', '1007', '500', '2020-01-02 06:00:00');
INSERT INTO `stock` VALUES ('3', '3003', '1008', '400', '2020-01-03 07:00:00');
INSERT INTO `stock` VALUES ('4', '3004', '1006', '400', '2020-03-01 06:00:00');
INSERT INTO `stock` VALUES ('5', '3005', '1006', '30', '2020-03-01 07:00:00');
INSERT INTO `stock` VALUES ('6', '3006', '1007', '20', '2020-05-04 07:00:00');
INSERT INTO `stock` VALUES ('7', '3007', '1008', '30', '2020-05-05 07:00:00');
INSERT INTO `stock` VALUES ('8', '3008', '1008', '10', '2020-05-06 08:00:00');
INSERT INTO `stock` VALUES ('9', '3006', '1006', '40', '2020-07-01 07:00:00');
INSERT INTO `stock` VALUES ('10', '3009', '1006', '50', '2020-07-01 07:00:00');
INSERT INTO `stock` VALUES ('11', '3010', '1007', '30', '2020-07-02 09:00:00');
INSERT INTO `stock` VALUES ('12', '3011', '1007', '20', '2020-07-03 10:00:00');
INSERT INTO `stock` VALUES ('13', '3012', '1008', '50', '2020-07-07 09:00:00');
INSERT INTO `stock` VALUES ('14', '3013', '1007', '10', '2020-07-08 09:00:00');
INSERT INTO `stock` VALUES ('15', '3014', '1006', '10', '2020-07-14 09:30:00');
INSERT INTO `stock` VALUES ('16', '3015', '1007', '20', '2020-07-15 07:00:00');
INSERT INTO `stock` VALUES ('17', '3016', '1008', '10', '2020-07-16 07:40:00');
INSERT INTO `stock` VALUES ('18', '3017', '1007', '10', '2020-07-16 08:00:00');
INSERT INTO `stock` VALUES ('19', '3018', '1006', '15', '2020-07-17 08:30:00');
INSERT INTO `stock` VALUES ('20', '3018', '1008', '50', '2020-07-21 09:00:00');
INSERT INTO `stock` VALUES ('21', '3019', '1007', '100', '2020-07-22 10:00:00');
INSERT INTO `stock` VALUES ('22', '3020', '1006', '30', '2020-07-23 10:00:00');
INSERT INTO `stock` VALUES ('23', '3017', '1006', '20', '2020-07-23 11:00:00');
INSERT INTO `stock` VALUES ('24', '3013', '1006', '10', '2020-07-24 07:00:00');
INSERT INTO `stock` VALUES ('25', '3016', '1007', '5', '2020-07-27 08:00:00');

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
  KEY `u_type` (`user_type`),
  CONSTRAINT `type_name` FOREIGN KEY (`user_type`) REFERENCES `user_type_name` (`user_type`)
) ENGINE=InnoDB AUTO_INCREMENT=1011 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1000', '123', '1', '0');
INSERT INTO `user` VALUES ('1001', '123', '2', '0');
INSERT INTO `user` VALUES ('1002', '123', '2', '0');
INSERT INTO `user` VALUES ('1003', '123', '2', '0');
INSERT INTO `user` VALUES ('1004', '123', '2', '0');
INSERT INTO `user` VALUES ('1005', '123', '2', '0');
INSERT INTO `user` VALUES ('1006', '123', '3', '0');
INSERT INTO `user` VALUES ('1007', '123', '3', '0');
INSERT INTO `user` VALUES ('1008', '123', '3', '0');
INSERT INTO `user` VALUES ('1009', '123', '3', '0');
INSERT INTO `user` VALUES ('1010', '123', '3', '0');

-- ----------------------------
-- Table structure for user_type_name
-- ----------------------------
DROP TABLE IF EXISTS `user_type_name`;
CREATE TABLE `user_type_name` (
  `user_type` int NOT NULL,
  `user_type_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user_type`,`user_type_name`),
  KEY `user_type` (`user_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user_type_name
-- ----------------------------
INSERT INTO `user_type_name` VALUES ('1', '管理员');
INSERT INTO `user_type_name` VALUES ('2', '收银员');
INSERT INTO `user_type_name` VALUES ('3', '进货员');

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
