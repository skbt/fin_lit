CREATE TABLE `users` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`school_id` VARCHAR(255) NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	`password` VARCHAR(255) NOT NULL,
	`role_id` INT NOT NULL,
	`dp` VARCHAR(255) NOT NULL,
	`major` VARCHAR(255) NOT NULL,
	`phone` VARCHAR(10) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `modules` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`desc` varchar(500) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `roles` (
	`role_id` INT NOT NULL AUTO_INCREMENT,
	`role_name` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`role_id`)
);

CREATE TABLE `module_completion` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`module_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	`completion` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `points` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`points` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `module_scores` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`module_id` INT NOT NULL,
	`module_comp_id` INT NOT NULL,
	`score` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `media` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`type` VARCHAR(255) NOT NULL,
	`path` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `module_media` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`sub_module_id` INT NOT NULL,
	`media_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `module_data` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`sub_module_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `course_completion` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`count` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `submodules` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`desc` VARCHAR(255) NOT NULL,
	`module_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `submodule_completion` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`submodule_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	`completion` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `module_quiz` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`module_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `users` ADD CONSTRAINT `users_fk0` FOREIGN KEY (`role_id`) REFERENCES `roles`(`role_id`);

ALTER TABLE `module_completion` ADD CONSTRAINT `module_completion_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules`(`id`);

ALTER TABLE `module_completion` ADD CONSTRAINT `module_completion_fk1` FOREIGN KEY (`user_id`) REFERENCES `users`(`id`);

ALTER TABLE `points` ADD CONSTRAINT `points_fk0` FOREIGN KEY (`user_id`) REFERENCES `users`(`id`);

ALTER TABLE `module_scores` ADD CONSTRAINT `module_scores_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules`(`id`);

ALTER TABLE `module_scores` ADD CONSTRAINT `module_scores_fk1` FOREIGN KEY (`module_comp_id`) REFERENCES `module_completion`(`id`);

ALTER TABLE `module_media` ADD CONSTRAINT `module_media_fk0` FOREIGN KEY (`sub_module_id`) REFERENCES `submodules`(`id`);

ALTER TABLE `module_media` ADD CONSTRAINT `module_media_fk1` FOREIGN KEY (`media_id`) REFERENCES `media`(`id`);

ALTER TABLE `module_data` ADD CONSTRAINT `module_data_fk0` FOREIGN KEY (`sub_module_id`) REFERENCES `submodules`(`id`);

ALTER TABLE `course_completion` ADD CONSTRAINT `course_completion_fk0` FOREIGN KEY (`user_id`) REFERENCES `users`(`id`);

ALTER TABLE `submodules` ADD CONSTRAINT `submodules_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules`(`id`);

ALTER TABLE `submodule_completion` ADD CONSTRAINT `submodule_completion_fk0` FOREIGN KEY (`submodule_id`) REFERENCES `submodules`(`id`);

ALTER TABLE `submodule_completion` ADD CONSTRAINT `submodule_completion_fk1` FOREIGN KEY (`user_id`) REFERENCES `users`(`id`);

ALTER TABLE `module_quiz` ADD CONSTRAINT `module_quiz_fk0` FOREIGN KEY (`module_id`) REFERENCES `modules`(`id`);