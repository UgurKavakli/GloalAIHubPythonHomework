def invalid_name():
    print("Please enter a valid name")


def invalid_value():
    print("Please enter a valid value between 0 and 100")


def try_again():
    print("Please try again later.")


class Calculator:
    def __init__(self, m, f, p):
        self.m = m
        self.f = f
        self.p = p

        avrg = (m * 0.3) + (f * 0.5) + (p * 0.2)
        if avrg >= 90:
            print("\nYour grade is AA\n")
        elif 70 <= avrg < 90:
            print("\nYour grade is BB\n")
        elif 50 <= avrg < 70:
            print("\nYour grade is CC\n")
        elif 30 <= avrg < 50:
            print("\nYour grade is DD\n")
        else:
            print("Your grade is FF\n")


tries = 2
course_list = []

while True:
    student_name = input("Please enter your name: ")
    if not student_name.isalpha() and tries != 0:
        invalid_name()
        tries -= 1
        continue
    elif not student_name.isalpha() and tries == 0:
        try_again()
        break
    else:
        student_surname = input("Please enter your last name: ")
        if not student_surname.isalpha() and tries != 0:
            invalid_name()
            tries -= 1
            continue
        elif not student_surname.isalpha() and tries == 0:
            try_again()
            break
        else:
            print(f"Welcome {student_name} {student_surname} \n")
            break
print("Please enter the courses you took.")

while True:
    course = input("Course: ")
    course = course.upper()
    course_list.append(course)
    if course == "":
        course_list.remove("")
        break
    elif len(course_list) == 5:
        break

if len(course_list) < 3:
    print("You failed class.")
else:
    print("\n")

    while True:
        for i, n in enumerate(course_list, 1):
            print(f"{i}. {n}")
        answer = input("\nPlease enter the index of the course to add exam results" +
                       "or type 'X' to exit ")
        try:
            int(answer)
            if answer.isdigit() and 0 < int(answer) < len(course_list):
                while True:
                    course_ = course_list[int(answer) - 1]
                    midterm = input(f"Please enter your midterm exam result for {course_}: ")
                    try:
                        int(midterm)
                        if 100 >= int(midterm) > 0:
                            break
                        else:
                            invalid_value()
                            continue
                    except ValueError:
                        invalid_value()
                        continue
                while True:
                    final = input(f"Please enter your final exam result for {course_list[int(answer) - 1]}: ")
                    try:
                        int(final)
                        if 100 >= int(final) > 0:
                            break
                        else:
                            invalid_value()
                            continue
                    except ValueError:
                        invalid_value()
                        continue
                while True:
                    project = input(f"Please enter your project result for {course_list[int(answer) - 1]}")
                    try:
                        int(project)
                        if 100 >= int(project) > 0:
                            Calculator(int(midterm), int(final), int(project))
                            break
                        else:
                            invalid_value()
                            continue
                    except ValueError:
                        invalid_value()
                        continue
        except ValueError:
            if answer.upper() == "X":
                raise SystemExit
            else:
                invalid_value()
                continue


