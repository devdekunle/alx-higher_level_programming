-- creates a table second_table in the database hbtn_0c_0 in your MySQL server
-- add multiples rows.
CREATE TABLE IF NOT EXISTS
    `second_table` (
     `id` INT(11),
     `name` VARCHAR(256),
     `score` INT(11)
     ) ENGINE=InnoDB AUTO_INCREMENT=5;
INSERT INTO `second_table` VALUES(1, "John", 10);
INSERT INTO `second_table` VALUES(2, "Alex", 3);
INSERT INTO `second_table` VALUES(3, "BOB", 14);
INSERT INTO `second_table` VALUES(4, "George", 8);
