from operator import itemgetter

candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
{"name": "Nadya",  "scores": {"math": 94, "russian_language": 30, "computer_science": 35},  "extra_scores":1}
]

def find_top_20(units):
    for row in units:
        row['sum_all_scores'] = sum(row["scores"].values()) + row["extra_scores"]
        row['sum_priority_scores'] = row["scores"]["math"] + row["scores"]["computer_science"]

    best_units = sorted(units, key=lambda d: (d['sum_all_scores'], d['sum_priority_scores']),reverse=True)
    best_units_list=[]
    for row in best_units:
        best_units_list.append(row["name"])

    print(best_units_list[0:21])


find_top_20(candidates)

names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
birthday_years = [1962,1995,2000,None,None,None,None,1998,2001]
genders = ["Male","Female","Male","Female","Male",None,None,None,None]

def get_inductees(n,b,g):
    keys = ['name', 'birt_year','gender']
    zipped = zip(n,b,g)
    dicts = [dict(zip(keys, values)) for values in zipped]
    list_no_suit = [row for row in dicts if row['gender'] is None or row['birt_year'] is None]
    new_list = [row for row in dicts if row['gender'] == "Male" and row['birt_year'] != None and row['birt_year'] > 1991]

    print(f'Призывники это {new_list}. А не-призывники это {list_no_suit}')

get_inductees(names, birthday_years, genders)

know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

def find_athlets(i, m,n):
    results = list(set(i) & set(m) & set(n))
    print(results)

find_athlets(know_english,sportsmen,more_than_20_years)


students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}

import xlsxwriter
def make_report_about_top3(d):
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    list_best = sorted_d[:3]
    book = xlsxwriter.Book('Best students.xlsx')
    sheet = book.add_sheet()
    row = 0
    column = 0
    for i in list_best:
        sheet.write(row,column,i)
        row+=1
    book.close()

make_report_about_top3(students_avg_scores)