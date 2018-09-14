CREATE TABLE `keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `leader` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `keyword` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `goal` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `summary` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `textbook` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `curriculum` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `keyword_c5c777d7` (`ex_type`),
  CONSTRAINT `experience_ex_type_6bb48d317f62021a_fk_experience_type_id` FOREIGN KEY (`ex_type`) REFERENCES `experience_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `EVENT` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `icon` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `c_url` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `domain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title_kor` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `title_eng` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `desc_kor` text COLLATE utf8_unicode_ci,
  `desc_eng` text COLLATE utf8_unicode_ci,
  `icon` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `experience_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `experience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start` date NOT NULL,
  `end` date DEFAULT NULL,
  `title_kor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `title_enh` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_kor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `location_eng` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `desc_kor` longtext COLLATE utf8_unicode_ci NOT NULL,
  `desc_eng` longtext COLLATE utf8_unicode_ci,
  `ex_type` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `experience_c5c777d7` (`ex_type`),
  CONSTRAINT `experience_ex_type_6bb48d317f62021a_fk_experience_type_id` FOREIGN KEY (`ex_type`) REFERENCES `experience_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title_kor` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `title_eng` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `title_img` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_start` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `desc_kor` text COLLATE utf8_unicode_ci NOT NULL,
  `desc_eng` text COLLATE utf8_unicode_ci,
  `proj_url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `publication_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_type` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `p_type` (`p_type`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `publication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_date` date NOT NULL,
  `citation_kor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `citation_eng` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc_kor` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc_eng` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `p_type` int(11) NOT NULL,
  `p_url` varchar(300) COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `publication_ee532d29` (`p_type`),
  CONSTRAINT `publication_p_type_4497eeb232344f3f_fk_publication_type_id` FOREIGN KEY (`p_type`) REFERENCES `publication_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;