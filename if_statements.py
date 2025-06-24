#if statements


opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
# print(apps_data)
opened_file.close()

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # print(rating)
    # Complete the code from here

"""
What's the average rating of non-free apps?
What's the average rating of free apps?
"""
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
print(app_data_set)
list_of_lists = row_1[4] + row_2[4] + row_3[4] + row_4[4] + row_5[4]
print(list_of_lists)
# avg_rating = list_of_lists / 5
# print(avg_rating)
