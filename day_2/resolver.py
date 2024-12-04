accepted = 0

with open("input", "r") as code_input:
    text = code_input.readlines()

    for number_set in text:
        difference_list = []
        signed_difference_list = []
        accept_set = True

        number_set = number_set.split()
        signed_difference_list.append(int(number_set[0]) - int(number_set[1]))
        difference_list.append(abs(int(number_set[0]) - int(number_set[1])))


        for i in range(1,len(number_set) - 1):
            difference_list.append(abs(int(number_set[i]) - int(number_set[i + 1])))
            signed_difference_list.append(int(number_set[i]) - int(number_set[i + 1]))

            if signed_difference_list[i - 1] * signed_difference_list[i] < 0:
                accept_set = False
                break

    

        if max(difference_list) < 4 and accept_set == True and difference_list.count(0) < 1:
            accepted += 1

print(accepted)

        

            


