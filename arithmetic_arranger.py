def arithmetic_arranger(a,b=0):
    errors = []
    numbers = []
    for i in range(len(a)):
        a[i] = a[i].split(' ')
        if (a[i][1] != '+' and a[i][1] != '-'):
            errors.append('+-')
        try:
            int(a[i][0])
        except:
            errors.append('dig')
        try:
            int(a[i][2])
        except:
            errors.append('dig')

        if(len(a[i][0]) > 4 or len(a[i][2]) > 4):
            errors.append('4+')

    if len(errors) > 5:
        return "Too many errors"
    elif '+-' in errors:
        return "Error: Operator must be '+' or '-'."
    elif 'dig' in errors:
        return "Error: Numbers must only contain digits."
    elif '4+' in errors:
        return "Error: Numbers cannot be more than four digits."

    # END OF ERROR CHECK

    for i in range(len(a)):
        if (a[i][1]=='+'):
            numbers.append(str(int(a[i][0])+int(a[i][2])))
        else:
            numbers.append(str(int(a[i][0])-int(a[i][2])))

    def spacer(a, b, c):
        for k in range(a):
            b.append(c)
        return b

    res = []
    dashes = []
    for i in [0, 2]:
        rows = []
        for j in range(len(a)):
            
            ans = []
            if(i == 0):
                x = 2
                y = 2
            else:
                x = 0
                y = 1

            if(i == 2):
                ans.append(a[j][1])

            if len(a[j][i]) > len(a[j][x]):
                ans = spacer(y, ans, ' ')
                l = len(a[j][i])+2

            else:
                ans = spacer(y+len(a[j][x])-len(a[j][i]), ans, ' ')
                l = len(a[j][x])+2

            if (i == 0):
                dashes.append(l)

            ans.append(a[j][i])

            if (j == len(a)-1):
                ans.append('\n')
            else:
                ans = spacer(4, ans, ' ')

            rows+=(ans)
        res+=(rows)

    for i in range(len(dashes)):
        res = spacer(dashes[i], res, '-')
        if (i != len(dashes)-1):
            res = spacer(4, res, ' ')

    if (b):
        res.append('\n')
        for i in range(len(numbers)):
            res = spacer(dashes[i]-len(numbers[i]),res,' ')
            res.append(numbers[i])
            if (i != len(dashes)-1):
                res = spacer(4, res, ' ')

    return ''.join(res)


print(arithmetic_arranger(["32 + 638", "3801 - 2", "45 + 43", "123 + 49"]))
