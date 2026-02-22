def process_scores(students):
    avgDic = dict()
    for key, value in students.items():
        total =0
        totalVal = len(value)
        for i in value:
            total = i+total
        avg = round(total/totalVal,2)

        avgDic[key] = avg

    return avgDic


def classify_grades(averages):
    for name,val in averages.items():
        if val >= 90:
            grade = "A"
        elif val >=75 and val <= 89:
            grade ="B"
        elif val >=60 and val <=74:
            grade = "C"
        else :
            grade = "F"
        
        averages [name] = (val,grade)
    return averages


def generate_report(classified, passing_avg=70):
    print ("===== Student Grade Report =====")
    passed =0
    total = len(classified)
    for k, v in classified.items():
        status = v[1]
        if v[0] >=70:
            passed +=1 
        print (f"{k:<10}| Avg: {v[0]:<6}| Grade: {status:<3}| Status: {'PASS' if v[0] >=70 else 'FAIL'}")

    print("=================================")

    print (f"Total Students : {total}")
    print (f"Passed         : {passed}")
    print (f"Failed         : {total - passed}")



students = {
    "Indhu": [80,89,95],
    "Sharmi" :[60,85,97,66],
    "John": [90,94,7],
    "Max": [40, 22,10]
}

result = process_scores(students)
scores = classify_grades(result)
generate_report(scores)

