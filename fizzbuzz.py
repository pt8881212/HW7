#Pratiksha Aga
# fizzbuzz
# homework 7

# function for fizzbuzz
def fbfunc(n):
    result = []
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            result.append("fizz buzz")
        elif x % 3 == 0:
            result.append('fizz')
        elif x % 5 == 0:
            result.append('buzz')
        else:
            result.append(str(x))
    return result

def main():
    print('\n'.join(fbfunc(100)))

main()
        