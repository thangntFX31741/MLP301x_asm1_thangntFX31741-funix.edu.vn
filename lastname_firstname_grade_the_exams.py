import numpy as np

# Task 1

inputname = input("Enter a class to grade (i.e. class1 for class1.txt): ")
# Handle file name: add txt format
filename = inputname + ".txt"

try:
    f = open(filename)
except:
    print("File cannot be found.")
else:
    print("Successfully opened " + filename)
    lines = f.readlines()
    f.close()


# Task 2

    valid_data = []
    invalid_line = 0
    
    print("**** ANALYZING ****")
    for line in lines:
        line = list(line.strip().split(","))
    
        # Check student ID
        student_id = line[0]
        cut_id = student_id[1:]
        check = True
        try:
            type(int(cut_id))
        except:
            check = False
        if len(cut_id) != 8:
            check = False

        # Check whether each line is valid
        if len(line) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
        if not(check):
            print("Invalid line of data: N# is invalid")
        if len(line) != 26 or not(check):
            print(','.join(line)) # Convert list to str
            invalid_line += 1
        else:
            valid_data.append(line)
                  
    if invalid_line == 0:
        print("No errors found!")
    print("**** REPORT ****")
    print("Total valid lines of data: {}".format(len(valid_data)))
    print("Total invalid lines of data: {}".format(invalid_line))
        

# Task 3

    score_table = []
    student_record = []

    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = list(answer_key.split(","))

    # Calculate score for each student in valid data
    for record in valid_data:
        score_personal = 0
        
        for i in range(1,len(record)): # record[0]: student_id
            if record[i] == answer_key[i-1]:
                score_personal += 4
            elif record[i] == '':
                score_personal += 0
            else:
                score_personal -= 1
                
        score_table.append(score_personal)
        student_record.append([record[0],str(score_personal)])
    
    score_table = np.array(score_table)

    print("Mean (average) score: {}".format(np.mean(score_table)))
    print("Highest score: {}".format(np.max(score_table)))
    print("Lowest score: {}".format(np.min(score_table)))
    print("Range of score: {}".format(np.max(score_table) - np.min(score_table)))
    print("Median score: {}".format(np.median(score_table)))
 

 #Task 4   

    #Save result to file
    save_file = inputname + "_grades.txt"
    with open(save_file, 'w') as f:
        for line in student_record:
            f.write(','.join(line)+'\n')