# #   koshish karo

# # value error 
# a = int(input("enter the number: "))
# if a>6:
#     print("the number is greater then 6")
# # --> in this we have givven command that the  input will we a number when we write any alphabet in place of the number
# # yeh hota hai value error (means hume ek input me number dalna th ahume hag diya)

# --> lets perform the task
while(True):
    print("enter q to quit..")
    a = input("enter the number: ")
    if a == 'q' :
        break 
    try:
        print("triying....")
        a =int(a)
        if a > 6: 
            print("The number is greater then 6")
        else:
            print("number is less then 6")
        
    except Exception as  e:
        print(f"the erroe is {e}")

print("thanks for playing th egame")

        
        
    