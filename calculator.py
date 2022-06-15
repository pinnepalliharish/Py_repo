
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
def calculator():
    num1=float(input("enter the first number :"))


    for key in operations:
        print(key)
    calculation_is_done=False
    while not calculation_is_done:
        operation_symbol=input("enter the operation symbol to calculate : ")
        num2=float(input("enter the next number :"))
        calculate=operations[operation_symbol]
        answer=calculate(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")


        option=input("type y to continue calculation with result and n to start from begining :").lower()
        if option=="y":
            num1=answer
    
        if option=="n":
            calculation_is_done=True
            calculator()
            
calculator()