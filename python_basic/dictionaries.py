#Dictionaries Example
#Helps map certain other values to another value
#Keys are the names of the people
#The keys are mapped to values which are the ages

ages = {"alice": 22, "bob": 27}

#adding another key "charlie" and its mapped value 30
ages["charlie"] = 30

#editing the value of one the variables later on
ages["alice"] += 1

def main():

    print(ages)

if __name__ == "__main__":
    main()