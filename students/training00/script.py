print('Geben Sie das Kürzel Ihres Studiengang ein und bestätigen Sie mit [Enter]:')
major = input().lower()

if major == 'gs':
    print('Sie studieren Geodata Science!')
    print('Willkommen an der Studienfakultät MUC.DAI')
elif major == 'dc':
    print('Sie studieren Data Science & Scientific Computing!')
    print('Willkommen an der Fakultät für Informatik und Mathematik')
else:
    print(f'\"{major}\" ist mir unbekannt. Sind Sie hier richtig?')