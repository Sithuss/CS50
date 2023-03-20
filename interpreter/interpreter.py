cal = input("Expression: ").strip().split()
val1 = float(cal[0])
val2 = float(cal[2])
operator = cal[1]

match operator:
    case "+":
        ans = val1 + val2
    case "-":
        ans = val1 - val2
    case "*":
        ans = val1 * val2
    case "/":
        ans = val1 / val2
    case "%":
        ans =  val2 % val2

print(ans)
