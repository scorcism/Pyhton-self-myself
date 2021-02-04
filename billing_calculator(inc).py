
#lets make a billing calculator from scratch as im also noob
sum = 0
while True:
    input_amount = input("Enter the amount or press q to exit : ")
    print(f"you have choosen this much amount {input_amount}")

    if input_amount!="q":
        list1=[sum + int(input_amount)]#becz input alwasy take str

    else:
        print(f"your total bill is ===={list1}")
        break

    with open("billing.txt", "w") as f:
        list2=f.write(list1)
        # print(list2)
    # print(f"{i}{sum}")





