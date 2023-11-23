import csv
from random import randint as r


class dataGeneration:
    def __init__(self):
        self.l1 = ['Calories', 'EX_Id', "Recipe"]
        self.l2 = ["Ex_routine_Id", 'Duration', "Calories", "Ex_id"]
        self.l3 = ['Loyalty_Id', "Duration", "Calories_burnt", "Calories_consumed", "Feedback", "Ex_routine_Id"]
        self.l4 = ["Recipe"]
        self.l5 = ["Id", "Ex_routine_Id"]
        self.l6 = ["Ex_id", "Description", "Type"]
        self.l7 = ["Streaks", "Level", "Loyalty_Id"]
        self.l8 = ["Id", "Gender", "Height", "Weight", "Fname", "Mname", "Lname"]
        self.l9 = ["Type_id", "Duration", "Amount", "Id", "Trainer_Id"]
        self.l10 = ["Email", "Id"]
        self.l11 = ["Trainer_Id", "Phoneno", "amount", "Name"]

    def diet_plan(self, count, ex_routine_min, ex_routine_max, cal_min, cal_max, recipe_min, recipe_max):
        # f1
        result = []
        for i in range(count):
            result.append([r(cal_min, cal_max), 'EX_routine' + str(r(ex_routine_min, ex_routine_max)),
                           "Recipe" + str(r(recipe_min, recipe_max))])
        return result

    def exercise_routine(self, count, duration_min, duration_max, cal_min, cal_max, ex_id_min, ex_id_max):
        # f2
        result = []
        for i in range(count):
            result.append(['EX_routine' + str(i), r(duration_min, duration_max), r(cal_min, cal_max),
                           "EX_ID" + str(r(ex_id_min, ex_id_max))])
        return result

    def daily_log(self, count, duration_min, duration_max, cal_min, cal_max, cal_consume_min, cal_consume_max,
                  feedback_min, feedback_max, ex_routine_min, ex_routine_max):
        # f3
        result = []
        for i in range(count):
            result.append(["LYL" + str(i), r(duration_min, duration_max), r(cal_min, cal_max),
                           r(cal_consume_min, cal_consume_max), "Feedback" + str(r(feedback_min, feedback_max), ),
                           'EX_routine' + str(r(ex_routine_min, ex_routine_max))])
        return result

    def diet_plan_recipe(self, count):
        # f4
        result = []
        for i in range(count):
            result.append(["Recipe" + str(i)])
        return result

    def does(self, count, user_id_min, user_id_max, ex_routine_min, ex_routine_max):
        # f5
        result = []
        check = []
        for i in range(count):
            id = "USR" + str(r(user_id_min, user_id_max))
            ex_r_id = 'EX_routine' + str(r(ex_routine_min, ex_routine_max))
            if (id, ex_r_id) in check:
                pass
            else:
                result.append([id, ex_r_id])
                check.append((id, ex_r_id))
        return result

    def exercise_list(self, count, description_min, description_max, type_min, type_max):
        # f6
        result = []
        for i in range(count):
            result.append(["EX_ID" + str(i), "Description" + str(r(description_min, description_max)),
                           "Type" + str(r(type_min, type_max))])
        return result

    def loyalty_pts(self, count, streaks_min, streaks_max, Level_min, Level_max, loyalty_min, loyalty_max):
        # f7
        result = []
        for i in range(count):
            result.append(
                [r(streaks_min, streaks_max), r(Level_min, Level_max), "LYL" + str(r(loyalty_min, loyalty_max))])
        return result

    def user_info(self, count, height_min, height_max, weight_min, weight_max, Fname_min, Fname_max, Mname_min,
                  Mname_max, Lname_min, Lname_max):
        # f8
        gender_min = 0
        gender_max = 2
        result = []
        for i in range(count):
            result.append(
                ["USR" + str(i), r(gender_min, gender_max), r(height_min, height_max), r(weight_min, weight_max),
                 "Fname" + str(r(Fname_min, Fname_max)), "Mname" + str(r(Mname_min, Mname_max)),
                 "Lname" + str(r(Lname_min, Lname_max))])
        return result

    def membership_type(self, count, period_min, period_max, amount_min, amount_max, user_id_min, user_id_max,
                        trainer_id_min, trainer_id_max):
        # f9
        result = []
        for i in range(count):
            result.append(["MEM" + str(i), r(period_min, period_max), r(amount_min, amount_max),
                           "USR" + str(r(user_id_min, user_id_max)),
                           "TRAINER" + str(r(trainer_id_min, trainer_id_max))])
        return result

    def user_info_email(self, count, email_min, email_max, user_id_min, user_id_max):
        # f10
        result = []
        check = list()
        for i in range(count):
            email = "email.id." + str(r(email_min, email_max)) + "@email.com"
            id = "USR" + str(r(user_id_min, user_id_max))
            if (email, id) in check:
                pass
            else:
                result.append([email, id])
                check.append((email, id))
        return result

    def trainer(self, count, fee_min, fee_max, name_min, name_max, ph_min=1000000000, ph_max=9999999999):
        # f11
        result = []
        for i in range(count):
            result.append(["TRAINER" + str(i), r(ph_min, ph_max), r(fee_min, fee_max),
                           "TrainerName" + str(r(name_min, name_max))])
        return result


if __name__ == '__main__':
    dataGen = dataGeneration()

    filename = "diet_plan.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l1)
        csvwriter.writerows(
            dataGen.diet_plan(count=100, ex_routine_min=20, ex_routine_max=60, cal_min=100, cal_max=350, recipe_min=5,
                              recipe_max=25))

    filename = "exercise_routine.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l2)
        csvwriter.writerows(
            dataGen.exercise_routine(count=200, duration_min=30, duration_max=120, cal_min=50, cal_max=400, ex_id_min=0,
                                     ex_id_max=120))

    filename = "daily_log.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l3)
        csvwriter.writerows(dataGen.daily_log(count=400, duration_min=40, duration_max=90, cal_min=90, cal_max=320,
                                              cal_consume_min=1000, cal_consume_max=2500, feedback_min=0,
                                              feedback_max=100, ex_routine_min=20, ex_routine_max=80))

    filename = "diet_plan_recipe.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l4)
        csvwriter.writerows(dataGen.diet_plan_recipe(count=80))

    filename = "does.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l5)
        csvwriter.writerows(
            dataGen.does(count=70, user_id_min=15, user_id_max=100, ex_routine_min=11, ex_routine_max=95))

    filename = "exercise_list.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l6)
        csvwriter.writerows(
            dataGen.exercise_list(count=150, description_min=20, description_max=300, type_min=5, type_max=300))

    filename = "loyalty_pts.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l7)
        csvwriter.writerows(
            dataGen.loyalty_pts(count=50, streaks_min=0, streaks_max=20, Level_min=1, Level_max=5, loyalty_min=30,
                                loyalty_max=300))

    filename = "user_info.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l8)
        csvwriter.writerows(
            dataGen.user_info(count=90, height_min=150, height_max=195, weight_min=45, weight_max=95, Fname_min=1,
                              Fname_max=200, Mname_min=5, Mname_max=250, Lname_min=5, Lname_max=250))

    filename = "membership_type.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l9)
        csvwriter.writerows(
            dataGen.membership_type(count=5, period_min=2, period_max=12, amount_min=1000, amount_max=10000,
                                    user_id_min=1, user_id_max=75, trainer_id_min=1, trainer_id_max=20))

    filename = "user_info_email.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(dataGen.user_info_email(count=60, email_min=1, email_max=50, user_id_min=1, user_id_max=50))
        csvwriter.writerow(dataGen.l10)


    filename = "trainer.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataGen.l11)
        csvwriter.writerows(
            dataGen.trainer(count=30, fee_min=1000, fee_max=10000, name_min=1, name_max=50, ph_min=1000000000,
                            ph_max=9999999999))
