def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if how_long(s) and first_two(s) and check_middle_num(s) and check_punctuartion(s):
        return True
    else:
        return False

def how_long(plate):
    answer=len(plate)
    if 2<=answer<=6:
        return True
    else:
        return False

def first_two(plate):
    if plate[0].isalpha() and plate[1].isalpha():
        return True
    else:
        return False
    
def check_punctuartion(plate):
    import string
    for char in plate:
        if char in string.punctuation or char in plate==" ":
            return False
    return True
        
def check_middle_num(plate):
    found_digit = False
    for i in range(len(plate)):
        if plate[i].isdigit():
            if not found_digit:
                # First digit found — check if it's '0'
                if plate[i] == '0':
                    return False
                found_digit = True
        elif found_digit:
            # If a letter comes after digits have started
            return False
    return True
            
    
    
 
    
    
main()