/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50627
Source Host           : localhost:3306
Source Database       : message_core

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2018-12-09 20:58:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add cust message', '7', 'add_custmessage');
INSERT INTO `auth_permission` VALUES ('26', 'Can change cust message', '7', 'change_custmessage');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete cust message', '7', 'delete_custmessage');
INSERT INTO `auth_permission` VALUES ('28', 'Can view cust message', '7', 'view_custmessage');
INSERT INTO `auth_permission` VALUES ('29', 'Can add user profile', '8', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('30', 'Can change user profile', '8', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete user profile', '8', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('32', 'Can view user profile', '8', 'view_userprofile');
INSERT INTO `auth_permission` VALUES ('33', 'Can add auto message', '9', 'add_automessage');
INSERT INTO `auth_permission` VALUES ('34', 'Can change auto message', '9', 'change_automessage');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete auto message', '9', 'delete_automessage');
INSERT INTO `auth_permission` VALUES ('36', 'Can view auto message', '9', 'view_automessage');
INSERT INTO `auth_permission` VALUES ('37', 'Can add tag mapping', '10', 'add_tagmapping');
INSERT INTO `auth_permission` VALUES ('38', 'Can change tag mapping', '10', 'change_tagmapping');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete tag mapping', '10', 'delete_tagmapping');
INSERT INTO `auth_permission` VALUES ('40', 'Can view tag mapping', '10', 'view_tagmapping');
INSERT INTO `auth_permission` VALUES ('41', 'Can add msg template', '11', 'add_msgtemplate');
INSERT INTO `auth_permission` VALUES ('42', 'Can change msg template', '11', 'change_msgtemplate');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete msg template', '11', 'delete_msgtemplate');
INSERT INTO `auth_permission` VALUES ('44', 'Can view msg template', '11', 'view_msgtemplate');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$120000$2qrSanDgDyUI$9QjO/7DiVXCOOBS8y1KzRSW2ZuiCC+GeoSLQbXYMzQQ=', '2018-12-09 18:09:20.256000', '1', 'admin', '', '', 'fly_wang_fei@163.com', '1', '1', '2018-09-27 15:07:19.523000');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$120000$uTtk1dIHLNWk$WyaJdgtIO0oaCU7K3dJp434KrjK3dMHcOH76b84qj/0=', '2018-12-09 20:54:30.238064', '0', '张三', '', '', '', '0', '1', '2018-09-27 15:09:55.363000');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$120000$CeYcQSaWftc9$O71LlIVaMAfy7ms5rR/273JLfOAxpCiTf0qzzxTbX+g=', '2018-11-02 10:36:43.364000', '0', '李四', '', '', '', '0', '1', '2018-09-27 15:10:30.054000');
INSERT INTO `auth_user` VALUES ('4', 'pbkdf2_sha256$120000$RGY28UtxKUrI$pNaRhOGL7GYiZV1QO1DqvoFfdw3WZIrB/UhdB6zEmKs=', null, '0', '王飞', '', '', '', '0', '1', '2018-11-18 21:54:27.997000');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-09-27 15:09:55.498000', '2', '张三', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-09-27 15:10:30.139000', '3', '李四', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-09-27 16:10:19.178000', '1', '<Profile for 张三>', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-09-27 16:10:29.830000', '2', '<Profile for 李四>', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2018-09-27 16:17:19.861000', '1', 'CustMessage object (1)', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2018-09-27 21:08:14.960000', '2', 'CustMessage object (2)', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2018-09-28 14:25:56.772000', '2', 'CustMessage object (2)', '2', '[{\"changed\": {\"fields\": [\"last_follow_user\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2018-09-28 16:18:34.036000', '3', 'CustMessage object (3)', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2018-09-28 16:19:20.324000', '4', 'CustMessage object (4)', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2018-11-18 22:32:37.218000', '4', '王飞', '2', '[{\"changed\": {\"fields\": [\"password\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2018-11-25 13:09:51.027000', '12', 'CustMessage object (12)', '2', '[{\"changed\": {\"fields\": [\"type\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2018-12-03 17:17:50.103000', '24', 'CustMessage object (24)', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2018-12-03 17:17:50.254000', '23', 'CustMessage object (23)', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2018-12-03 17:17:50.569000', '22', 'CustMessage object (22)', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2018-12-03 17:17:51.053000', '21', 'CustMessage object (21)', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2018-12-03 17:17:51.155000', '20', 'CustMessage object (20)', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2018-12-03 17:17:51.263000', '19', 'CustMessage object (19)', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2018-12-03 17:17:51.364000', '18', 'CustMessage object (18)', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2018-12-03 17:17:51.481000', '17', 'CustMessage object (17)', '3', '', '7', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'manager', 'automessage');
INSERT INTO `django_content_type` VALUES ('11', 'manager', 'msgtemplate');
INSERT INTO `django_content_type` VALUES ('10', 'manager', 'tagmapping');
INSERT INTO `django_content_type` VALUES ('7', 'message_core', 'custmessage');
INSERT INTO `django_content_type` VALUES ('8', 'message_core', 'userprofile');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-12-09 20:39:03.594015');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-12-09 20:39:03.993686');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-12-09 20:39:04.102250');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-12-09 20:39:04.120263');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2018-12-09 20:39:04.137774');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2018-12-09 20:39:04.214325');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2018-12-09 20:39:04.242750');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2018-12-09 20:39:04.283050');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2018-12-09 20:39:04.298061');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2018-12-09 20:39:04.340640');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2018-12-09 20:39:04.346142');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2018-12-09 20:39:04.360080');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2018-12-09 20:39:04.406111');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2018-12-09 20:39:04.458646');
INSERT INTO `django_migrations` VALUES ('15', 'message_core', '0001_initial', '2018-12-09 20:39:04.588618');
INSERT INTO `django_migrations` VALUES ('16', 'message_core', '0002_auto_20180927_1513', '2018-12-09 20:39:04.640309');
INSERT INTO `django_migrations` VALUES ('17', 'message_core', '0003_auto_20180927_1603', '2018-12-09 20:39:04.825053');
INSERT INTO `django_migrations` VALUES ('18', 'message_core', '0004_auto_20180927_1614', '2018-12-09 20:39:04.922497');
INSERT INTO `django_migrations` VALUES ('19', 'message_core', '0005_auto_20180927_1616', '2018-12-09 20:39:05.018135');
INSERT INTO `django_migrations` VALUES ('20', 'message_core', '0006_userprofile_user_status', '2018-12-09 20:39:05.073172');
INSERT INTO `django_migrations` VALUES ('21', 'message_core', '0007_auto_20181125_1140', '2018-12-09 20:39:05.175506');
INSERT INTO `django_migrations` VALUES ('22', 'manager', '0001_initial', '2018-12-09 20:39:05.310019');
INSERT INTO `django_migrations` VALUES ('23', 'manager', '0002_auto_20181209_2038', '2018-12-09 20:39:05.384394');
INSERT INTO `django_migrations` VALUES ('24', 'sessions', '0001_initial', '2018-12-09 20:39:05.421953');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('7009g940v5saidy63zax0gt8wnuk817c', 'ZTI4NWFlYjNmZmFhOWU0NWNlNWIxZGMyNjRiYjI2ZGNiY2YyZmJkZDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5MTdiNTg0YjljZWNkNGI0MWY1MmFhZTkzMjFmZDQ0MzdiYWZhZGQxIn0=', '2018-11-30 11:42:08.190000');
INSERT INTO `django_session` VALUES ('84bf994g76i17m03e01qxz0ajwoef27g', 'ZTI4NWFlYjNmZmFhOWU0NWNlNWIxZGMyNjRiYjI2ZGNiY2YyZmJkZDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5MTdiNTg0YjljZWNkNGI0MWY1MmFhZTkzMjFmZDQ0MzdiYWZhZGQxIn0=', '2018-11-11 14:24:26.500000');
INSERT INTO `django_session` VALUES ('aibthmmsjcczkezine2xi5vlzkkqatof', 'YWU3YmI4YWIzNDM0OTBmZGQyNDNmNWYwYTVmMDNmN2E3NTg4YWM5NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE2ZDc2NjYyMzI0M2ZkYmQyYTQ4ZmVlNWJkODBkYzdlZGI2NWM2ZjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-12-23 20:54:30.254081');
INSERT INTO `django_session` VALUES ('au2ue1cnucgxhc8vlnrreis1347q487d', 'ZjBhNzlmYzdmMmUzMTgzMjM3NDRiNzY3ZDFlNjU5ZTc2MDFhYmVlYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2hhc2giOiI5MTdiNTg0YjljZWNkNGI0MWY1MmFhZTkzMjFmZDQ0MzdiYWZhZGQxIn0=', '2018-10-15 09:43:17.040000');
INSERT INTO `django_session` VALUES ('c30ptql9oxmrtuuq5may23s21or526td', 'MmM0YjI3YTEyNTVlYTE5OTg5NTQ5MjE0NDkwOTk5NTZlZGQwMTUyNzp7fQ==', '2018-11-30 10:19:13.769000');
INSERT INTO `django_session` VALUES ('caj4x4uyd8qfjpxtsm0cp1w04qn2zk8j', 'YzFjN2EyYjRlZGFmZTQwZDRhNTYzOTg3NDM4MzhiYmIyYzc1NTUzMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1NzBjNWY2YTE3OGRmNjgxYjhiNTc3OWZkNDEyZjU5N2I4NjJlN2E0In0=', '2018-12-05 20:53:40.057000');
INSERT INTO `django_session` VALUES ('esnfk1m4x488meqbl5oofrrd2atwudsb', 'ZmQ0ODczNTM0NGFmM2E5YWM3YzNiYjZhZDk3YjA5ZmM2YjIxZjE0ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjkxN2I1ODRiOWNlY2Q0YjQxZjUyYWFlOTMyMWZkNDQzN2JhZmFkZDEiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-12-02 10:40:36.147000');
INSERT INTO `django_session` VALUES ('iofm47wvrpskyiu9mcjkuf7bh4bpyq4p', 'NTRlYmFiYTVjZDgyNGYyOTdjYTRhNjM5MjA0NGE1ODU0MzBjYjk3ODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOTE3YjU4NGI5Y2VjZDRiNDFmNTJhYWU5MzIxZmQ0NDM3YmFmYWRkMSIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-11-10 11:34:51.863000');
INSERT INTO `django_session` VALUES ('llx3073f9cf1e55cleeklzzawqc7v2sr', 'NDNiNDg5MWU1N2VmMWZkNjNkYzczNzcyOTY2NmFjNDU5NWE4YzcyYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjkxN2I1ODRiOWNlY2Q0YjQxZjUyYWFlOTMyMWZkNDQzN2JhZmFkZDEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-11-10 22:29:48.321000');
INSERT INTO `django_session` VALUES ('nvl3tm2u7umjjixq3klspu5p8qswuj4v', 'ZTI4NWFlYjNmZmFhOWU0NWNlNWIxZGMyNjRiYjI2ZGNiY2YyZmJkZDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5MTdiNTg0YjljZWNkNGI0MWY1MmFhZTkzMjFmZDQ0MzdiYWZhZGQxIn0=', '2018-10-22 10:40:09.907000');
INSERT INTO `django_session` VALUES ('s4caqft4cc7f8vtp3lclutd5zauc04yd', 'ZTI4NWFlYjNmZmFhOWU0NWNlNWIxZGMyNjRiYjI2ZGNiY2YyZmJkZDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5MTdiNTg0YjljZWNkNGI0MWY1MmFhZTkzMjFmZDQ0MzdiYWZhZGQxIn0=', '2018-10-13 14:37:57.550000');
INSERT INTO `django_session` VALUES ('tl3yv16rncir0li8rnyayttowt0yz5sa', 'ODI5OTJkZTNkMGYzYTc4NjgzNGY5N2Y1OGI4NWRhMTdjMjdlNTQxYTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhNmQ3NjY2MjMyNDNmZGJkMmE0OGZlZTViZDgwZGM3ZWRiNjVjNmYxIn0=', '2018-12-23 18:15:57.667000');

-- ----------------------------
-- Table structure for `manager_automessage`
-- ----------------------------
DROP TABLE IF EXISTS `manager_automessage`;
CREATE TABLE `manager_automessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cur_user_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_automessage_cur_user_id_27bd06d2_fk_message_c` (`cur_user_id`),
  CONSTRAINT `manager_automessage_cur_user_id_27bd06d2_fk_message_c` FOREIGN KEY (`cur_user_id`) REFERENCES `message_core_userprofile` (`user_num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_automessage
-- ----------------------------
INSERT INTO `manager_automessage` VALUES ('1', '2');

-- ----------------------------
-- Table structure for `manager_msgtemplate`
-- ----------------------------
DROP TABLE IF EXISTS `manager_msgtemplate`;
CREATE TABLE `manager_msgtemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `template_key` varchar(30) NOT NULL,
  `has_firstline` tinyint(1) NOT NULL,
  `col_username` varchar(2) DEFAULT NULL,
  `col_mobilephone` varchar(2) NOT NULL,
  `col_address` varchar(2) DEFAULT NULL,
  `col_message` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `template_key` (`template_key`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_msgtemplate
-- ----------------------------
INSERT INTO `manager_msgtemplate` VALUES ('1', '123', '1', null, 'B', null, null);
INSERT INTO `manager_msgtemplate` VALUES ('2', '234', '0', null, 'c', null, null);
INSERT INTO `manager_msgtemplate` VALUES ('3', '213', '1', null, 'D', null, null);
INSERT INTO `manager_msgtemplate` VALUES ('4', 'myTmp', '1', 'c', 'E', 'F', 'j');
INSERT INTO `manager_msgtemplate` VALUES ('5', 'homeTest', '1', 'B', 'e', 'g', 'I');

-- ----------------------------
-- Table structure for `manager_tagmapping`
-- ----------------------------
DROP TABLE IF EXISTS `manager_tagmapping`;
CREATE TABLE `manager_tagmapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(30) NOT NULL,
  `ref_template_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_name` (`tag_name`),
  KEY `manager_tagmapping_ref_template_id_7c6e1875_fk_manager_m` (`ref_template_id`),
  CONSTRAINT `manager_tagmapping_ref_template_id_7c6e1875_fk_manager_m` FOREIGN KEY (`ref_template_id`) REFERENCES `manager_msgtemplate` (`template_key`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_tagmapping
-- ----------------------------
INSERT INTO `manager_tagmapping` VALUES ('1', '123', '123');
INSERT INTO `manager_tagmapping` VALUES ('2', 'nihao', '213');
INSERT INTO `manager_tagmapping` VALUES ('3', 'mySource', 'myTmp');
INSERT INTO `manager_tagmapping` VALUES ('4', 'homeTag', 'homeTest');

-- ----------------------------
-- Table structure for `message_core_custmessage`
-- ----------------------------
DROP TABLE IF EXISTS `message_core_custmessage`;
CREATE TABLE `message_core_custmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_name` varchar(30) DEFAULT NULL,
  `cust_mobile` varchar(30) NOT NULL,
  `cust_address` varchar(50) DEFAULT NULL,
  `message` longtext,
  `visit_record` longtext,
  `next_visit_date` date DEFAULT NULL,
  `type` int(11) NOT NULL,
  `source_tag` varchar(50) DEFAULT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `follow_user_id` varchar(20) NOT NULL,
  `last_follow_user_id` varchar(20) DEFAULT NULL,
  `last_type` int(11) NOT NULL,
  `message_status` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cust_mobile` (`cust_mobile`),
  KEY `message_core_custmes_follow_user_id_2f7647b2_fk_message_c` (`follow_user_id`),
  KEY `message_core_custmes_last_follow_user_id_2a6a8031_fk_message_c` (`last_follow_user_id`),
  CONSTRAINT `message_core_custmes_follow_user_id_2f7647b2_fk_message_c` FOREIGN KEY (`follow_user_id`) REFERENCES `message_core_userprofile` (`user_num`),
  CONSTRAINT `message_core_custmes_last_follow_user_id_2a6a8031_fk_message_c` FOREIGN KEY (`last_follow_user_id`) REFERENCES `message_core_userprofile` (`user_num`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message_core_custmessage
-- ----------------------------
INSERT INTO `message_core_custmessage` VALUES ('1', null, '15523658654', null, '', '', '2018-10-03', '1', null, '2018-09-27 16:17:19.860000', '2018-10-01 10:29:50.235000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('2', '客户一', '15523658655', '湖北武汉', '和法国恢复规划高房价 反光镜到房管局地方公交车V型内存 查地方刚恢复规划家分店将豆腐干将发达国家反光镜反光镜', '电风扇公司的风格下车V型橙V\r\n重复过交付给‘\r\n发过节费\r\n地方和地方\r\n凤凰过分的话', '2018-09-30', '1', '995', '2018-09-27 21:08:14.958000', '2018-09-28 14:25:56.771000', '1', '2', '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('3', '客户二', '15523658656', '广东深圳', '哈哈哈', '李四', '2018-09-28', '1', '999', '2018-09-28 16:18:34.034000', '2018-11-02 10:36:49.439000', '1', '2', '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('4', '客户四', '15523658657', '湖北孝感', '法国恢复规划', '打个电话', '2018-09-30', '1', '666网', '2018-09-28 16:19:20.323000', '2018-09-28 16:19:20.323000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('5', '客户四', '15523658658', '广东深圳', '随时随地', '<p><strong>地方打个电话</strong></p>\r\n\r\n<p><em>归档</em><u>电饭锅</u>电饭锅<span style=\"background-color:#27ae60\">电饭锅滴滴</span></p>', '2018-10-01', '1', null, '2018-09-30 09:51:54.526000', '2018-10-28 21:36:35.610000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('6', '客户五', '15523658659', '北京通城', '你好啊', '<p>放松放松的</p>', '2018-10-27', '1', null, '2018-09-30 09:55:35.916000', '2018-10-28 21:32:53.333000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('7', '客户刘', '15523658660', '湖北安陆', '水电费收费', '<p>是多大</p>\r\n\r\n<p>电饭锅</p>', '2018-10-05', '1', null, '2018-09-30 10:34:55.197000', '2018-10-28 21:43:07.835000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('8', '客户七', '15523658661', '广东深圳', '随碟附送2', '<p>下车V型橙V宣传V型水电费敢死队是第三个三等功三等功水电工水电工水电工水电工水电工水电工水电工水电工水电工</p>', '2018-10-01', '2', null, '2018-09-30 10:58:05.754000', '2018-10-28 21:47:29.541000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('9', null, '15523658666', null, '', '', '2018-08-01', '1', null, '2018-09-30 15:02:52.060000', '2018-12-08 23:46:35.293000', '123', '1', '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('10', '厄尔单独', '15523658667', '四川成都', '地方多个1', '<p>的法规法规</p>', '2018-09-30', '2', null, '2018-09-30 15:58:30.834000', '2018-11-02 10:38:42.479000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('11', 'nihao', '15523658675', '广东湛江', '', '', '2018-10-08', '1', null, '2018-09-30 17:10:23.785000', '2018-11-22 23:45:29.001000', '123', '2', '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('12', '你猜', '13546474627', '四川成都', '呵呵呵', '<p>的方法对方</p>', '2018-10-10', '3', null, '2018-10-01 08:50:08.819000', '2018-11-25 13:15:07.100000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('13', '客户李', '15523658688', '舒服啥地方', '地方的法规q', '<p>随碟附送的</p>', '2018-10-29', '3', '123', '2018-10-08 10:44:29.311000', '2018-11-25 13:19:30.231000', '1', null, '2', '1');
INSERT INTO `message_core_custmessage` VALUES ('14', '千万千万', '13423345678', '大幅度', '', '', null, '2', null, '2018-11-25 09:09:02.688000', '2018-11-25 13:14:53.951000', '1', null, '3', '1');
INSERT INTO `message_core_custmessage` VALUES ('15', '是否打底衫1', '12344335522', '梵蒂冈1', '12', '<p>12</p>', '2018-11-25', '2', '8891', '2018-11-25 09:18:28.242000', '2018-11-25 20:39:32.211000', '1', null, '3', '1');
INSERT INTO `message_core_custmessage` VALUES ('16', '颠三倒四', '13245678909', '法国巴黎', '吊死扶伤', '', null, '1', '998', '2018-11-25 20:33:05.016000', '2018-11-25 21:14:24.609000', '2', '123', '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('25', '玩玩', '15827340285', '留言1', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.612000', '2018-12-03 23:07:39.612000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('26', '所示', '15827340286', '留言2', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.612000', '2018-12-03 23:07:39.612000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('27', '调度', '15827340287', '留言3', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.612000', '2018-12-03 23:07:39.612000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('28', '方法', '15827340288', '留言4', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.612000', '2018-12-03 23:07:39.612000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('29', '谷歌', '15827340289', '留言5', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.612000', '2018-12-03 23:07:39.612000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('30', '哈哈', '15827340280', '留言6', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.612000', '2018-12-03 23:07:39.612000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('31', '解决', '15827340284', '留言7', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.612000', '2018-12-03 23:07:39.612000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('32', '可空', '15827340283', '留言8', null, null, null, '1', 'homeTag', '2018-12-03 23:07:39.613000', '2018-12-03 23:07:39.613000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('33', '玩玩', '15727340285', '留言1', null, null, null, '1', 'homeTag', '2018-12-04 22:41:10.942000', '2018-12-04 22:41:10.942000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('34', '所示', '15727340286', '留言2', null, null, null, '1', 'homeTag', '2018-12-04 22:41:10.943000', '2018-12-04 22:41:10.943000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('35', '调度', '15727340287', '留言3', null, null, null, '1', 'homeTag', '2018-12-04 22:41:10.943000', '2018-12-04 22:41:10.943000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('36', '方法', '15727340288', '留言4', null, null, null, '1', 'homeTag', '2018-12-04 22:41:10.943000', '2018-12-04 22:41:10.943000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('37', '哈哈', '15727340280', '留言6', null, null, null, '1', 'homeTag', '2018-12-04 22:41:10.943000', '2018-12-04 22:41:10.943000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('38', '解决', '15627340284', '留言7', null, null, null, '1', 'homeTag', '2018-12-04 22:41:10.943000', '2018-12-04 22:41:10.943000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('39', '可空', '15427340283', '留言8', null, null, null, '1', 'homeTag', '2018-12-04 22:41:10.943000', '2018-12-04 22:41:10.943000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('40', '玩玩', '15427340285', '留言1', '', null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-09 17:59:58.724000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('41', '所示', '15427340286', '留言2', null, null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-08 22:25:40.000000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('42', '调度', '15427340287', '留言3', null, null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-08 22:25:40.000000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('43', '方法', '15427340288', '留言4', null, null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-08 22:25:40.000000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('44', '谷歌', '15422334456', '留言5', null, null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-08 22:25:40.000000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('45', '哈哈', '15427340280', '留言6', null, null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-08 22:25:40.000000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('46', '解决', '15427340284', '留言7', null, null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-08 22:25:40.000000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('47', '可空', '15327340283', '留言8', null, null, null, '1', 'homeTag', '2018-12-08 22:25:40.000000', '2018-12-08 22:25:40.000000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('48', '玩玩', '13427340285', '深圳1', '留言1', null, null, '1', 'homeTag', '2018-12-08 22:46:56.774000', '2018-12-08 22:46:56.774000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('49', '所示', '13427340286', '深圳2', '留言2', null, null, '1', 'homeTag', '2018-12-08 22:46:56.774000', '2018-12-08 22:46:56.774000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('50', '调度', '13427340287', '深圳3', '留言3', null, null, '1', 'homeTag', '2018-12-08 22:46:56.774000', '2018-12-08 22:46:56.774000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('51', '玩玩', '13327340285', '深圳1', '留言1', null, null, '1', 'homeTag', '2018-12-08 23:10:13.092000', '2018-12-08 23:10:13.092000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('52', '调度', '13327340287', '深圳3', '留言3', null, null, '1', 'homeTag', '2018-12-08 23:10:13.092000', '2018-12-08 23:10:13.092000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('53', null, '13248765543', null, '', '', null, '1', null, '2018-12-08 23:24:26.061000', '2018-12-08 23:24:26.061000', '123', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('54', null, '15122345309', null, '', null, null, '1', null, '2018-12-08 23:24:45.190000', '2018-12-09 18:04:33.376000', '1', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('55', null, '15678904325', null, '', '', null, '1', null, '2018-12-08 23:24:59.551000', '2018-12-08 23:24:59.552000', '2', null, '1', '1');
INSERT INTO `message_core_custmessage` VALUES ('56', null, '17625364785', null, '', '', null, '1', null, '2018-12-08 23:28:36.534000', '2018-12-08 23:28:36.534000', '2', null, '1', '1');

-- ----------------------------
-- Table structure for `message_core_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `message_core_userprofile`;
CREATE TABLE `message_core_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_num` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_status` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_num` (`user_num`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `message_core_userprofile_user_id_c880714d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message_core_userprofile
-- ----------------------------
INSERT INTO `message_core_userprofile` VALUES ('1', '1', '2', '1');
INSERT INTO `message_core_userprofile` VALUES ('2', '2', '3', '1');
INSERT INTO `message_core_userprofile` VALUES ('3', '123', '4', '1');
