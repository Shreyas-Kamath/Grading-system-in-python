import os

PASSING_MARKS = 32
PASSING_MARKS_X_V2 = 70
QUALIFY_X_V2 = "PASSED - QUALIFIED FOR X v2"
PASSED = "PASSED"
FAIL = "FAILED"

PASS_TEMPLATE_X_V2 = "Congratulations {}!\nYou have successfully cleared X examination.\nYour marks are as follows:\n MATHS : {}\n PHYSICS : {}\n CHEMISTRY : {}\n AVERAGE SCORE : {:.3f}\n STATUS: {}\nPlease note, you have also qualified for X v2 examination"

PASS_TEMPLATE = "Congratulations {}!\nYou have successfully cleared X examination.\nYour marks are as follows:\n MATHS : {}\n PHYSICS : {}\n CHEMISTRY : {}\n AVERAGE SCORE : {:.3f}\n STATUS: {}\n"

FAIL_TEMPLATE = "Dear {},\nYou have been unsuccessful in clearing X examination.\nYour marks are as follows:\n MATHS : {}\n PHYSICS : {}\n CHEMISTRY : {}\n AVERAGE SCORE : {:.3f}\n STATUS: {}\n"

class Student:
    def __init__(self, name: str, physics: int, chemistry: int, maths: int) -> None:
        self.__name = name
        self.__physics = physics
        self.__chemistry = chemistry
        self.__maths = maths
        self.__avg = (physics + chemistry + maths)/3
        self.__status = self.__avg >= PASSING_MARKS

    def get_name(self) -> str:
          return self.__name
    
    def get_phy(self) -> int:
          return self.__physics
    
    def get_chem(self) -> int:
          return self.__chemistry
    
    def get_maths(self) -> int:
          return self.__maths
    
    def get_avg(self) -> float:
          return self.__avg
    
    def get_status(self) -> bool:
          return self.__status

    
def read(filename: str) -> list[Student]:
      try:
            students = list()
            with open(filename, 'r') as file:
                  content = file.read().splitlines()

            for student in content:
                  _ = student.split(',')
                  students.append(Student(str(_[0]),int(_[1]),int(_[2]),int(_[3])))
      except:
            print("File not found")
      return students

def write(students: list[Student]) -> None:
      with open("RESULTS.csv", 'w') as results:
            results.write("NAME,PHYSICS,CHEMISTRY,MATHS,AVERAGE,STATUS\n")
            for student in students:
                  results.write(f"{student.get_name()},{student.get_phy()},{student.get_chem()},{student.get_maths()},{student.get_avg():.3f},{"PASSED" if student.get_status() else "FAILED"}\n")

def generate_reports(students: list[Student]) -> None:
      if not os.path.exists("INDIVIDUAL REPORTS"):
            os.mkdir("INDIVIDUAL REPORTS")
      os.chdir("INDIVIDUAL REPORTS")

      for student in students:
            status =  QUALIFY_X_V2 if student.get_avg() >= PASSING_MARKS_X_V2 else (PASSED if student.get_status() else FAIL)
            with open(student.get_name() + " - "+ status + ".txt", 'w+') as report:
                  if status == QUALIFY_X_V2:
                        report.write(PASS_TEMPLATE_X_V2.format(student.get_name(), student.get_maths(), student.get_phy(), student.get_chem(), student.get_avg(), student.get_avg()))
                  elif status == PASSED:
                        report.write(PASS_TEMPLATE.format(student.get_name(), student.get_maths(), student.get_phy(), student.get_chem(), student.get_avg(), student.get_avg()))
                  else:
                        report.write(FAIL_TEMPLATE.format(student.get_name(), student.get_maths(), student.get_phy(), student.get_chem(), student.get_avg(), student.get_avg()))      