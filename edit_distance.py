# ;=======1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**
# ;  Author information
# ;  Author name: Victor Prieto
# ;  Author email: victorprie@csu.fullerton.edu
# ;
# ;Program information
# ;  Program name: Victor Prieto
# ;  Programming languages: Python
# ;  Date of last update: 2024 April 19
# ;
# ;
# ;This file
# ;   File name: edit_distance.py
# ;   Language: Python
# ;=======1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**

# ;=======1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**
# 
# ; TO RUN: Simply type in console: python3 edit_distance.py
# 
# ;=======1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**


def print_matrix(first, second, matrix):
    m = len(first)
    n = len(second)
    
    print("The matrix:")
    
    print(" " * 5 + "-" * (4 * (n + 1) + 1))
    
    for i in range(m + 1):
        if i == 0:
            print(f"  {i} |", end='')
        else:
            print(f" {i} |", end='')
        for j in range(n + 1):
            print(f" {matrix[i][j]:2} :", end='')
        print()
        print(" " * 5 + "-" * (4 * (n + 1) + 1))

def align_strings(first, second, matrix):
    m = len(first)
    n = len(second)
    
    alignment_first = []
    alignment_second = []
    i = m
    j = n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and first[i - 1] == second[j - 1]:
            alignment_first.append(first[i - 1])
            alignment_second.append(second[j - 1])
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or matrix[i][j] == matrix[i][j - 1] + 1):
            alignment_first.append("_")
            alignment_second.append(second[j - 1])
            j -= 1
        elif i > 0 and (j == 0 or matrix[i][j] == matrix[i - 1][j] + 1):
            alignment_first.append(first[i - 1])
            alignment_second.append("_")
            i -= 1
        else:
            alignment_first.append(first[i - 1])
            alignment_second.append(second[j - 1])
            i -= 1
            j -= 1
    
    alignment_first.reverse()
    alignment_second.reverse()
    return ''.join(alignment_first), ''.join(alignment_second)

def main():
    first_word = input("Enter the first word: ")
    second_word = input("Enter the second word: ")
    
    matrix = [[0] * (len(second_word) + 1) for _ in range(len(first_word) + 1)]
    
    for i in range(len(first_word) + 1):
        matrix[i][0] = i
    
    for j in range(len(second_word) + 1):
        matrix[0][j] = j
    
    for i in range(1, len(first_word) + 1):
        for j in range(1, len(second_word) + 1):
            if first_word[i - 1] == second_word[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
    
    print_matrix(first_word, second_word, matrix)
    print()
    print("The edit distance is:", matrix[-1][-1])
    print()
    alignment_first, alignment_second = align_strings(first_word, second_word, matrix)
    print("Alignment is:")
    print(alignment_first)
    print(alignment_second)


if __name__ == "__main__":
    main()
