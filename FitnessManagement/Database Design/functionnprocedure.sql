-- Correcting Gender
DELIMITER $$ 
CREATE FUNCTION correcting_gender(GENDER1 INT)
RETURNS INT
DETERMINISTIC 
BEGIN
   DECLARE gender INT;
   SET gender = GENDER1 ;
   IF gender > 0 THEN 
   SET gender = 1;
   ELSE 
   SET gender = 0;
   END IF;
	RETURN gender;
	
END $$
DELIMITER ;


DELIMITER $$
CREATE procedure gender_updation()
BEGIN
UPDATE user_info
SET gender = correcting_gender(gender);
END;$$
DELIMITER ;


-- BMI calculation function
DELIMITER $$
CREATE FUNCTION bmi_cal(height INT, weight INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE BMI FLOAT;
    SET BMI = weight / POWER((height / 100), 2);
    RETURN BMI;
END $$
DELIMITER ;

-- BMI calculation procedure
DELIMITER $$
CREATE PROCEDURE bmi_updation()
BEGIN
    UPDATE user_info
    SET bmi = bmi_cal(user_info.height, user_info.weight);
END $$
DELIMITER ;


call gender_updation();
call bmi_updation();

-- SELECT
    -- routine_name
-- FROM
   -- information_schema.routines
-- WHERE
    -- routine_type = 'procedures'

