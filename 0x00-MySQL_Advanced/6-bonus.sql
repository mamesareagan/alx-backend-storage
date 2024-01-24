-- SQL script that creates a stored procedure
-- that adds a bonus to a user for a project
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
    DECLARE project_id INT DEFAULT 0;
    DECLARE project_count INT DEFAULT 0;

    SELECT COUNT(*) 
        INTO project_count
        FROM projects
        WHERE name = project_name;
    
    IF project_count = 0 THEN
        INSERT INTO projects (name)
        VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    ELSE
        SELECT id
            INTO project_id
            FROM projects
            WHERE name = project_name;
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, project_id, score);
END$$
DELIMITER ;
