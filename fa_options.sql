/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50744
 Source Host           : localhost:3306
 Source Schema         : fastadmin

 Target Server Type    : MySQL
 Target Server Version : 50744
 File Encoding         : 65001

 Date: 24/06/2024 18:00:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for fa_options
-- ----------------------------
DROP TABLE IF EXISTS `fa_options`;
CREATE TABLE `fa_options`  (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `ques_id` int(20) NULL DEFAULT NULL,
  `type` int(20) NULL DEFAULT NULL COMMENT '选项类型：1->‘select’,2->\'radio\'',
  `opa` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `opb` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `opc` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `opd` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `ope` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `opf` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `opg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `oph` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `opi` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fa_options
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
