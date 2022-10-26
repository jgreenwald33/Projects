#This will determine if a series is geometric or arithmetic

print("Enter first 5 terms of series:")

terms = []

for i in range(5):
    temp_term = input()
    temp_term = int(temp_term)
    terms.append(temp_term)

print ("\nFirst 5 terms:", end=" ")
for i in range(5):
    print(int(terms[i]), end=" ")

# finds the difference and ratio between the first two terms in the series
init_diff = terms[1] - terms[0]

init_ratio = -1

if terms[0] != 0:
    init_ratio = terms[1] / terms[0]

# returns true if there is a consistent difference between first 10 terms
def is_series_arithmetic(diff_first):
    actual_diff = 0 
    for x in range(4):
        term_1 = terms[x+1]
        term_2 = terms[x]
        actual_diff = actual_diff + (term_1 - term_2)

    expected_diff = diff_first * 4

    is_arithmetic = False

    if expected_diff == actual_diff:
        is_arithmetic = True
    
    return is_arithmetic

# returns true if there is a consistent ratio between first 10 terms
def is_series_geometric(ratio_first):
    actual_ratio = 0 
    for x in range(4):
        term_1 = terms[x+1]
        term_2 = terms[x]

        if term_2 == 0:
            actual_ratio = -9999999
            break

        actual_ratio = actual_ratio + (term_1/term_2)

    expected_ratio = ratio_first * 4

    is_geometric = False

    if expected_ratio == actual_ratio:
        is_geometric = True
    
    return is_geometric


is_arithmetic = is_series_arithmetic(init_diff)
is_geometric = is_series_geometric(init_ratio)
print()

if is_arithmetic:
    print("The series is arithmetic!")
    print("Difference: " + str(init_diff))

    a_term_100 = int((terms[0]+(100-1)*init_diff))
    print("100th term of series: " + str(a_term_100))

elif is_geometric:
    print("The series is geometric!")
    print("Ratio: " + str(terms[1]/terms[0]))
    
    g_term_100 = (terms[0] * (init_ratio**(100 - 1)))
else:
    print("The series is neither arithmetic or geometric")