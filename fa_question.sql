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

 Date: 24/06/2024 18:01:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for fa_question
-- ----------------------------
DROP TABLE IF EXISTS `fa_question`;
CREATE TABLE `fa_question`  (
  `ques_id` int(255) NOT NULL AUTO_INCREMENT COMMENT '试题id',
  `ques_title` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '题目',
  `ques_head` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '选项对应的列标题',
  `ques_section` int(10) NULL DEFAULT NULL COMMENT '试题所属试卷的section',
  `ques_expla` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '试题文字解析',
  `ques_count` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '统计做题次数',
  `ques_expla_voice` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '试题的语音解析',
  `ques_status` int(5) NULL DEFAULT 1 COMMENT '试题状态',
  `ques_know` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '知识点',
  `ques_tags` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '试题标签',
  `ques_ans` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '答案',
  `ques_type` int(15) NULL DEFAULT NULL COMMENT '试题分类',
  `ques_create_time` int(10) NULL DEFAULT NULL COMMENT '创建试卷',
  `ques_discri` float(20, 5) NULL DEFAULT NULL COMMENT '试题的区分度',
  `ques_diff` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '试题难度',
  `ques_guess` float(20, 5) NULL DEFAULT NULL COMMENT '试题猜测系数',
  `passage_id` int(20) NULL DEFAULT NULL COMMENT '阅读理解文章id',
  `passage` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '阅读文章',
  `print_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'og书上面对应的id',
  `ques_hash` int(20) NULL DEFAULT NULL COMMENT '试题的唯一哈希识别码',
  PRIMARY KEY (`ques_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9671 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fa_question
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
