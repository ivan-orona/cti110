#Miguel Orona
#CTI-110 M6HW1 - Test Average and Grade
#November 22, 2017
#The program will accept 5 test scores and print the average

#The function for calculating the average score
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

#The number score will be established with the corresponding letter grade
def determine_grade (totalscore):
    if(totalscore < 60):
        return "F"
    elif(totalscore < 70):
        return "D"
    elif(totalscore < 80):
        return "C"
    elif(totalscore < 90):
        return "B"
    elif(totalscore < 101):
        return "A"

#The user will be prompted to enter the scores
def askforScore():
    score1 = float(input("Please enter score 1: "))
    score2 = float(input("Please enter score 2: "))
    score3 = float(input("Please enter score 3: "))
    score4 = float(input("please enter score 4: "))
    score5 = float(input("please enter score 5: "))

    return score1, score2, score3, score4, score5

#The main function and grade will be printed
def main():
    score1, score2, score3, score4, score5 = askforScore()
   
    average_score = calc_average(score1, score2, score3, score4, score5)
    print("Your average score is: ", average_score)
    print("Your final grade is: ", determine_grade(average_score))

main()
#End program
