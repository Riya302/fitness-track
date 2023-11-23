DELIMITER $$
CREATE TRIGGER total_no_of_user_per_trainer_exceed_check  
BEFORE INSERT 
ON membership_type FOR EACH ROW  
BEGIN  
    DECLARE user_count INT;
    SET user_count = (SELECT COUNT(*) FROM membership_type WHERE trainer_id = NEW.trainer_id);

    IF user_count > 4 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Total number of users per trainer exceeds more than 4';
    END IF;
END $$
DELIMITER ;



-- try
INSERT INTO `membership_type` (`type_id`, `duration`, `amount`, `id`, `trainer_id`) VALUES
('MEM12', 11, 3567, 'USR71', 'TRAINER20'),
('MEM13', 11, 9752, 'USR54', 'TRAINER20'),
('MEM14', 8, 2500, 'USR28', 'TRAINER20'),
('MEM15', 12, 4800, 'USR63', 'TRAINER20'),
('MEM16', 6, 1800, 'USR42', 'TRAINER20');