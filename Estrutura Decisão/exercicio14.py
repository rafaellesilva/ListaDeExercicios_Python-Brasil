note_one,note_two = map(int,input('Enter value of two notes: ').split())
average = (note_one + note_two) / 2

if average >= 9 and average <= 10:
    concept = 'A'
    status = 'Aproved'
elif average >= 7.5 and average < 9:
    concept = 'B'
    status = 'Aproved'
elif average >= 6 and average < 7.5:
    concept = 'C'
    status = 'Aproved'
elif average >= 4 and average < 6:
    concept = 'D'
    status = 'Reproved'
else:
    concept = 'E'
    status = 'Reproved'

print(f'Notes{note_one, note_two}\nAverage: {average:.2f}\nConcept: {concept}\nStatus: {status}')





