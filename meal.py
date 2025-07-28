def main():
    current_time=input("What time is it? ")
    check_time=convert(current_time)
    
    if 7<=check_time<=8:
        print("breakfast time")
    elif 12<= check_time <=13:
        print("lunch time")
    elif 18<= check_time <= 19:
        print("dinner time")
    else:
        return None


def convert(time):
    sep_time=time.split(":")
    minutes=float(sep_time[1])/60
    hours=float(sep_time[0])
    total_time=hours+minutes
    return total_time
    


if __name__ == "__main__":
    main()
