#PART-1
ranges = [0, 20, 40, 60, 80, 100, 120]  #initialize credit ranges in array

progress = 0
trailer = 0
exclude = 0
retriever = 0
count = 0

progress_inputs = []
trailer_inputs = []
exclude_inputs = []
retriever_inputs = []

while True:
    while True:
        try:
            Pass = int(input("Please enter your credits at pass : "))   #getting pass credit
            if Pass not in ranges:   #check input credits are in the range
                print("Out of range\n")
            else:
                break   #break the loop & go to next step
        except ValueError:
            print("Integer required\n")   #print Integer required

    while True:
        try:
            Defer = int(input("Please enter your credit at defer : "))  #getting defer credit
            if Defer not in ranges:  #check input credits are in the range
                print("Out of range\n")
            else:
                break   #break the loop & go to next step
        except ValueError:
            print("Integer required\n")   #print Integer required

    while True:
        try:
            Fail = int(input("Please enter your credit at fail : "))    #getting fail credit
            if Fail not in ranges:   #check input credits are in the range
                print("Out of range\n")
            else:
                break   #break the loop & go to next step
        except ValueError:
            print("Integer required\n")   #print Integer required

    total = Pass+Defer+Fail
    if total == 120:
        count = count+1   #increment count
        if Pass == 120:
            print("Progress")  #print progress
            progress_inputs.append([Pass, Defer, Fail])    #append to progress array
            progress = progress+1  #increment progress
        elif Pass == 100:
            print("Progress(module trailer)")  #print progress(module trailer)
            trailer_inputs.append([Pass, Defer, Fail])     #append to trailer array
            trailer = trailer+1   #increment trailer
        elif Fail >= 80:
            print("Exclude")  #print exclude
            exclude_inputs.append([Pass, Defer, Fail])    #append to exclude array
            exclude = exclude+1   #increment exclude
        else:
            print("Do not progress – module retriever")   #print module retriever
            retriever_inputs.append([Pass, Defer, Fail])    #append to retriever array
            retriever = retriever+1   #increment retriever
        print("\nWould you like to enter another set of data?")
        n = input("Enter 'y' for yes or 'q' to quit and view results: ")  #getting input to break or continue the loop
        print("")
        if n.lower() == "q":    #quit loop
            break
        elif n.lower() == "y":  #continue loop
            continue
    else:
        print("Total incorrect\n")  #print total incorrect

print("\nHorizontal Histogram")  #print Horizontal Histogram
print("Progress ", progress, "   : ", "*"*progress)
print("Trailer ", trailer, "    : ", "*"*trailer)
print("Retriever ", retriever, "  : ", "*"*retriever)
print("Excluded ", exclude, "   : ", "*"*exclude)
print(f"\n{count} outcomes in total.")

#PART-2
print("\nProgress",progress,"  | Trailing",trailer,"  | Retriever",retriever,"  | Excluded",exclude)  #print vertical Histogram
while count > 0:
    if progress > 0:
        print(f"{'*':>5}", end="")
        progress = progress-1
        count = count-1
    else:
        print(f"{' ':>5}", end="")

    if trailer > 0:
        print(f"{'*':>15}", end="")
        trailer = trailer-1
        count = count-1
    else:
        print(f"{' ':>15}", end="")

    if retriever > 0:
        print(f"{'*':>15}", end="")
        retriever = retriever-1
        count = count-1
    else:
        print(f"{' ':>15}", end="")

    if exclude > 0:
        print(f"{'*':>15}")
        exclude = exclude-1
        count = count-1
    else:
        print(f"{' ':>15}")
print()

#PART-3
for p in progress_inputs:
    print("Progress - ", p)
for q in trailer_inputs:
    print("Progress (module trailer) - ", q)
for r in retriever_inputs:
    print("Module retriever - ", r)
for s in exclude_inputs:
    print("Exclude - ", s)


#PART-4
def out_file():
    output = open('output data.txt', 'w')
    for a in progress_inputs:
        output.write("Progress - " + str(a)+'\n')
    for b in trailer_inputs:   
        output.write("Progress (module trailer) - " + str(b)+'\n')
    for c in retriever_inputs:
        output.write("Module retriever - " + str(c)+'\n')
    for d in exclude_inputs:
        output.write("Exclude - " + str(d)+'\n')
    output.close()   #close text file

    read_file = open('output data.txt', 'r')
    print("\nstored data from output text file:")
    for line in read_file:
        print('\t'+line, end="")
    read_file.close()

out_file()
