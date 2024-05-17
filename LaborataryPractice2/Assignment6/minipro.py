# Employee performance evaluation expert system
import csv

class Expert:
    def __init__(self, name, oname):
        self.ifilename = name
        self.ofilename = oname

    def add_Employee(self):
        with open(self.ifilename,'a', newline='') as file1:
            w = csv.writer(file1, quoting=csv.QUOTE_NONE)
            ask = input("Enter Employee ID : ")
            ask1 = input("Enter Employee Name : ")
            ask2 = int(input("Entr score of Employee for Deadline Handling : "))
            ask3 = int(input("Entr score of Employee for Knowledge about job : "))
            ask4 = int(input("Entr score of Employee for Communication and interaction : "))
            ask5 = int(input("Entr score of Employee for Educational and professional Qualification : "))
            ask6 = int(input("Entr score of Employee for Punctuality : "))
            ask7 = int(input("Entr score of Employee for Adaptibility : "))
            print()
            w.writerow([ask,ask1,ask2,ask3,ask4,ask5,ask6,ask7])
            print("Employee Data of " + ask1 + " Added to database successfully")
        
    def evaluate(self):
        result = []
        with open(self.ifilename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[2].isdigit()):
                    # calculate result
                    data = [int(row[2]),int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7])]
                    resulte = self.Calculate(data)

                    #check for increment
                    choice = "Employee has cosistent performance, continue with same salary"
                    if (resulte >= 90):
                        choice = "Employee has shown very good performance!! Give an increment in salary by " + str(resulte-89) + "%"
                    elif (resulte <= 20):
                        choice = "Employee is showing poor performance!! Give a decrement in salary by " + str(21 - resulte) + "%"

                    #give comments
                    suggestion = []
                    crit = ['Deadline Handling','Knowledge about job','Communication and interaction','Educational and professional Qualification','Punctuality','Adaptibility']
                    for i in range(len(data)):
                        if(data[i] < 3):
                            suggestion.append(["Your performance is seen low in " + crit[i] + " area, please pay more attention and work on it."])
                            if(i == 3):
                                suggestion[-1][0] += " Start by choosing relevant courses and training programs."
                            elif(i == 2):
                                suggestion[-1][0] += " You can start by trying to communicate with your colleagues and take opportunities to speak up or present ideas during meetings"
                            elif(i == 1):
                                suggestion[-1][0] += " Start by managing your daily schedule and keep note of all deadlines on calendar and sticky notes"
    
                        elif(data[i] <=6):
                            suggestion.append(["Your performance in marginal in " + crit[i] + " field, you may put some efforts on this field to have significant impact in your performance evaluation."])
                            if(i == 3):
                                suggestion[-1][0] += " You may try choosing relevant courses and training programs."
                            elif(i == 2):
                                suggestion[-1][0] += " You can start by trying to communicate with your colleagues and take opportunities to speak up or present ideas during meetings"
                            elif(i == 1):
                                suggestion[-1][0] += " Focus on your daily schedule and keep note of all deadlines on calendar and sticky notes"
                    if(len(suggestion) == 0):
                        suggestion.append(["You are working very hard!! Congratulations on a good evaluation score!!! Keep up your good work!!"])
                    elif(len(suggestion) == 6):
                        suggestion.append(["You are not being attentive and not taking your job seriously!! Please pay more attention and work harder!! You can do it too!!"])
                    result.append([row[0],row[1],resulte, choice, suggestion])
            with open(self.ofilename,'w', newline='') as ofile:
                writer = csv.writer(ofile)
                writer.writerow(['Emp_No','Emp_Name','Evaluation_Score', 'Salary_status', 'suggestions'])
                writer.writerows(result)
                print()
            print("Evaluation completed")
    

    def display(self, empName):
        flag = False
        print()
        with open(self.ifilename,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[1] == empName):
                    flag = True
                    #detail matched, print all info
                    print("Employee ID : ",row[0])
                    print("Employee name : ",row[1])
                    print("Employee Score in Deadline Handling : ", row[2])
                    print("Employee Score in Knowledge about job : ", row[3])
                    print("Employee Score in Communication and interaction : ", row[4])
                    print("Employee Score in Educational and professional Qualification : ", row[5])
                    print("Employee Score in Punctuality : ", row[6])
                    print("Employee Score in Adaptibility : ", row[7])
                    print()
                    print("Evaluated score of employee : ", self.Calculate([int(row[2]),int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7])]) ,"%")
            
                    break
            if(flag == False):
                print("Employee name doesnot match.. please try again later")
            print()

    def display_Evaluation(self,check, empName):
        flag = False
        print()
        with open(self.ofilename,'r') as oread:
            reader = csv.reader(oread)
            if(check == False):
                print("First perform evaluation to get results")
                return
            for row in reader:
                if(row[1] == empName):
                    flag = True
                    #detail matched, print all info
                    print("Employee ID : ",row[0])
                    print("Employee name : ",row[1])
                    print("Evaluated score of employee : ", row[2] ,"%")
                    print("Remark on Employee's Salary : ", row[3])
                    print("Suggestions to Employee to improve their performance", row[1], " : ")
                    
                    s = row[4][2:-3].split("], [")
                    for i in range(len(s)):
                        print(str(i+1) + ". " + s[i][1:-1])
                    break
            if(flag == False):
                print("Employee name doesnot match.. please try again later")
            print()

    def Calculate(self, data):
        performance = (sum(data)/60)*100
        return performance

def main():
    
    flag = False
    to_con = "y"
    while(to_con == "y"):
        print()
        print("Hello!!! Welcome to Employee performance Evaluation")
        print("1. Press 1 to perform performance evaluation")
        print("2. Press 2 to display the details of particular employee")
        print("3. Press 3 to enter employee data")
        print("4. Press 4 to display the Evaluation report of particular employee")
        ask = int(input("\nEnter your choice : "))
        exp = Expert('people.csv', 'output.csv')
        if(ask == 1):
            print("Please wait a second.. we are evaluating the data")
            exp.evaluate()
            flag = True
            to_con = input("Do you want to continue(y/n) : ")
        elif(ask == 2):
            s = input("Enter employee Name : ")
            exp.display(s)
            to_con = input("Do you want to continue(y/n) : ")
        elif(ask == 3):
            exp.add_Employee()
            to_con = input("Do you want to continue(y/n) : ")
        elif(ask == 4):
            s = input("Enter employee Name : ")
            exp.display_Evaluation(flag,s)
            to_con = input("Do you want to continue(y/n) : ")
        else:
            print("Wrong input.. try again")
    
              

if __name__=="__main__": 
    main()



