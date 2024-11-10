"imports"
import time
"inputs"
input1 = input()
input12 = float(input())
input22 = float(input())
"calculate"
if input1 == "add":
    ans = input12 + input22
    print(ans)
elif input1 == "subtract":
    ans = input12 - input22
    print(ans)
elif input1 == "multiply":
    ans = input12 * input22
    print(ans)
elif input1 == "divide":
    ans = input12 / input22
    print(ans)
else:
    print("invalid operation")
time.sleep(4)
