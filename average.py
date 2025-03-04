grades_input = input()
grades = list(map(float, grades_input.split()))

weights = [2, 3, 4, 1]

def calculate_weighted_average(grades, weights):
    weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight

def exame(final_nota):
    try:
        nota = float(input())
    except EOFError:
        nota = 0.0

    print(f"Nota do exame: {nota:.1f}")
    final_average = (nota + final_nota) / 2
    return final_average

def main(grades):
    final_media = calculate_weighted_average(grades, weights)
    print(f"Media: {final_media:.1f}")

    if final_media >= 7.0:
        print("Aluno aprovado.")
    elif final_media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        final_average = exame(final_media)
        if final_average >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {final_average:.1f}")

# Run the main function
main(grades)