from easygui import *

TITLE = "Calculate Your FUTAGPA"


image = "python_and_check_logo.gif"
welcome = msgbox(
    '''Hello There. Welcome to the FUTAGPA calculator.
    You can calculate your CGPA and also find out what
    your grade is, per level, semester or even test.
    All you need is to input your scores for the subjects
    you offer. You can add a new subject with the
    number of units allocated to it.
    
            Press "OK" to continue.
          ''', TITLE, image=image)

grading = msgbox('''
      
                          FUTA's Grading System
|--------------------------------------------------------------------------
|        Mark/Score         |    Letter Grade    |   Grade Point (GP)     |
|--------------------------------------------------------------------------
|     70% and Above         |          A         |         5.00           |
|--------------------------------------------------------------------------
|        60  -  69          |          B         |         4.00           |
|--------------------------------------------------------------------------
|        50  -  59          |          C         |         3.00           |
|--------------------------------------------------------------------------
|        45  -  49          |          D         |         2.00           |
|--------------------------------------------------------------------------
|        40  -  44          |          E         |         1.00           |
|--------------------------------------------------------------------------
|         0  -  39          |          F         |         0.00           |
|--------------------------------------------------------------------------

    
         Initial idea by Owonipa Babajide
         Some references by Adegoke Obasa
         Coded by Serene_X_Sparkles.
''', TITLE)

 
# Function to convert grade to credit point STARTS
def crpoint(grade):
    if grade == "A" or grade == "a":
        return 5
    elif grade == "B" or grade == "b":
        return 4
    elif grade == "C" or grade == "c":
        return 3
    elif grade == "D" or grade == "d":
        return 2
    elif grade == "E" or grade == "e":
        return 1
    elif grade == "F" or grade == "f":
        return 0
    else:
        print("")
        print("Not Valid. Please input appropriate values") #function to convert grade to credit point ENDS


#function that calculate the gpa  using while loop
def gpa(course_no):
    k = 0
    tlu = 0
    t = 0

    while k != course_no:
        k = k+1
        unit = integerbox("Input Course unit", TITLE)  #this line gets the unit for the course
        grade = enterbox("Input Course Letter Grade: ", TITLE) #this line gets the grade for the course


        tlu = unit * crpoint(grade) + tlu
        t = t + unit

    gpa = round(tlu/t,2) #this line computes the gpa

    msgbox("You are in " + str(sem) +" Semester and your GPA is " +  str(gpa)) #this line outputs the gpa and the semester
    
    #This series of if statements print out the Class of degree
    if 4.50 <= gpa <= 5.00:
        msgbox(
            '''Congratulations,
                    --------- First Class ----------
            ''')
        print("--------- First Class ----------")
    elif 3.50 <= gpa <= 4.49:
        msgbox(
            '''Congratulations,
                    --------- 2nd (Second) Class Upper Division ----------
            ''')
        print("--------- 2nd (Second) Class Upper Division ----------")
    elif 2.40 <= gpa <= 3.49:
        msgbox(
            '''Congratulations,
                    --------- 2nd (Second) Class Lower Division ----------
            ''')
        print("--------- 2nd (Second) Class Lower Division ----------")
    elif 1.50 <= gpa <= 2.39:
        msgbox(
            '''Congratulations,
                    --------- 3rd (Third) Class ----------
            ''')
        print("--------- 3rd (Third) Class ----------")
    elif 1.00 <= gpa <= 1.49:
        msgbox(
            '''Congratulations,
                    --------- Pass ----------
            ''')
        print("--------- Pass ----------")
    elif 0.00 <= gpa <= 0.99:
        msgbox(
            '''Congratulations,
                    --------- Carry Over ----------
            ''')
        print("--------- Carry Over ----------")
    else:
        pass
#function ends here

#this line tells the user the limitations of the program
msgbox("The maximum amount of courses that this program can accept is 15 and the minimum is 2", TITLE)
#this line prompts the user for the semester
sem = enterbox("What Semester? ", TITLE)
#this line prompts the user for the number of courses offered that semester
course_no = integerbox("Number of courses offered: ", TITLE)

if  2 <= course_no <= 15:
    gpa(course_no)
else:
    msgbox("The maximum amount of courses that this program can accept is 15 and the minimum is 2", TITLE)

