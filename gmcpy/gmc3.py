add = lambda x,y :  x+y
subtract = lambda x,y : x-y
divide = lambda x,y : x/y
multiply = lambda x,y : x*y
operations = {"+":add , "-":subtract , "/":divide , "*":multiply}
def calculator(): 
    x=int(input("write the 1st number"))
    should_continue = True
 
    while should_continue:
        s= input("write the operator : ")
        y=int(input("write the 2nd number"))
        if s in operations:
            function_calcul=operations[s]
            answer=function_calcul(x,y)
            print(f"{x} {s} {y} = {answer}")
        else:
            s= input("write the operator : ")

        ask=input("did you want to change the numbers ?: (y/n) ")

        if ask == "y":
           x =answer
        else:
            should_continue=False
            calculator()
calculator()
           
        

        

calculator() 

            