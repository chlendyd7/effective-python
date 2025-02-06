car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
# print(oldest, second_oldest, others)

oldest, second_oldest, *others = car_ages_descending
# print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
# print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_descending
# print(youngest, second_youngest, others)

car_inventory = {
    '시내': ('그랜저', '아반테', '티코'),
    '공항': ('제네시스 쿠페', '소나타', 'K5', '악센트'),
}

((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()
print(f'{loc1} 최고는 {best1}, 나머지는 {len(rest1)} 종')
print(f'{loc2} 최고는 {best2}, 나머지는 {len(rest2)} 종')

short_list = [1,2]
first, second, *rest = short_list
print(first, second, rest)

def generate_csv():
    yield ('날짜', '제조사' , '모델', '연식', '가격')
    for i in range(100):
        yield ('2019-03-25', '현대', '소나타', '2010', '2400만원')
        yield ('2019-03-26', '기아', '프라이드', '2008', '1400만원')

all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV 헤더:', header)
print('행 수: ', len(rows))

it = generate_csv()
header, *rows = it
print('CSV 헤더:', header)
print('행 수: ', len(rows))