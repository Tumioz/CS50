def Calculator(calculations):
    calculations= calculations.split()
    numA=float(calculations[0])
    numB=float(calculations[2])
    if calculations[1]=="+":
        answer=numA+numB
    elif calculations[1]=="-":
        answer=numA-numB
    elif calculations[1]=="/":
        answer=numA/numB
    else:
        answer=numA*numB
    return round(answer,1)
        

expression= input()
print(Calculator(expression))

        