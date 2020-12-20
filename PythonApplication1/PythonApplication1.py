con=True
StudentsInfo={}
CourseInfo={}
while con :
    StuId=input("Enter student id:")
    NumCourRegi=int(input("Enter number of courses registered:"))
    for i in range(0,NumCourRegi):
        Coursename, ECTS, Grade= input("Enter course name, ECTS, grade:").split()
        CourseInfo={Coursename:(ECTS,Grade)}
        StudentsInfo.setdefault(StuId,{})[Coursename] = (ECTS,Grade)
    answer=input("Do you want to continue Y/N?")
    if answer == 'n'or answer == 'N':
        con= False
grade=0;
for id,course in StudentsInfo.items():
    for courseName,Courseinfo in course.items():
        if Courseinfo[1] == 'AA' or Courseinfo[1] == 'aa':
            count = int(Courseinfo[0])*4;
        if Courseinfo[1] == 'BA' or Courseinfo[1] == 'ba':
            count = int(Courseinfo[0])*3.5;
        if Courseinfo[1] == 'BB' or Courseinfo[1] == 'bb':
            count = int(Courseinfo[0])*3;
        if Courseinfo[1] == 'CB' or Courseinfo[1] == 'cb':
            count = int(Courseinfo[0])*2.5;
        if Courseinfo[1] == 'CC' or Courseinfo[1] == 'cc':
            count = int(Courseinfo[0])*2;
        if Courseinfo[1] == 'DC' or Courseinfo[1] == 'Dc':
            count = int(Courseinfo[0])*1.5;
        if Courseinfo[1] == 'DD' or Courseinfo[1] == 'DD':
            count = int(Courseinfo[0])*1;
        if Courseinfo[1] == 'FD' or Courseinfo[1] == 'FD':
            count = int(Courseinfo[0])*0.5;
        if Courseinfo[1] == 'FF' or Courseinfo[1] == 'ff':
            count = int(Courseinfo[0])*0;
        grade= grade + count
    print("Student id:",id,"    Grade: ", grade)
