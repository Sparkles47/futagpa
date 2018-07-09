print ('''
      
                                FUTA's Grading System
|----------------------------------------------------------------------------|
|           Mark/Score         |    Letter Grade    |   Grade Point (GP)     |
|----------------------------------------------------------------------------|
|        70% and Above         |          A         |         5.00           |
|----------------------------------------------------------------------------|
|           60  -  69          |          B         |         4.00           |
|----------------------------------------------------------------------------|
|           50  -  59          |          C         |         3.00           |
|----------------------------------------------------------------------------|
|           45  -  49          |          D         |         2.00           |
|----------------------------------------------------------------------------|
|           40  -  44          |          E         |         1.00           |
|----------------------------------------------------------------------------|
|            0  -  39          |          F         |         0.00           |
|----------------------------------------------------------------------------|

    
         Initial idea by Owonipa Babajide
         Some references by Adegoke Obasa
         Coded by Serene_X_Sparkles.
''')

 
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
        unit = int(input("Input Course unit: " ))  #this line gets the unit for the course
        grade = input("Input Course Letter Grade: ") #this line gets the grade for the course

        tlu = unit * crpoint(grade) + tlu
        t = t + unit

    gpa = round(tlu/t,2) #this line computes the gpa

    print("You are in ",sem," Semester and your GPA is " ,gpa) #this line outputs the gpa and the semester
    
    #This series of if statements print out the Class of degree
    if 4.50 <= gpa <= 5.00:
        print("--------- First Class ----------")
    elif 3.50 <= gpa <= 4.49:
        print("--------- 2nd (Second) Class Upper Division ----------")
    elif 2.40 <= gpa <= 3.49:
        print("--------- 2nd (Second) Class Lower Division ----------")
    elif 1.50 <= gpa <= 2.39:
        print("--------- 3rd (Third) Class ----------")
    elif 1.00 <= gpa <= 1.49:
        print("--------- Pass ----------")
    elif 0.00 <= gpa <= 0.99:
        print("--------- Carry Over ----------")
    else:
        pass
#function ends here

#this line tells the user the limitations of the program
print("The maximum amount of courses that this program can accept is 15 and the minimum is 2")
#this line prompts the user for the semester
sem = input("Which Semester? ")
#this line prompts the user for the number of courses offered that semester
course_no = int(input("Number of courses offered: "))

if  2 <= course_no <= 15:
    gpa(course_no)

