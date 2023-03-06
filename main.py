def validation():
    is_valid_input = False

    while not is_valid_input:
        try:
            user_date = input('Enter date in format dd.mm.yyyy: ')
            string_list = user_date.split('.')
            result = list(map(int, string_list))
            max_month = (result[0] in day_set or result[0] == 29 or result[0] == 30 or result[0] == 31) \
                        and result[1] in max_month_set
            min_month = (result[0] in day_set or result[0] == 29 or result[0] == 30) and result[1] != 2 \
                        and result[1] not in max_month_set
            feb_leap = result[0] in day_set or result[0] == 29 \
                       and (result[2] % 100 != 0 and result[2] % 4 == 0 or result[2] % 400 == 0)
            feb_not_leap = result[0] in day_set \
                           and (result[2] % 100 == 0 and result[2] % 4 != 0 or result[2] % 400 != 0)
            if len(result) == 3 and result[1] > 0 and result[1] < 13 and result[2] >= 1970:
                if max_month or min_month or feb_leap or feb_not_leap:
                    result.append(user_date)
                    is_valid_input = True
                else:
                    print('You entered wrong date')
            else:
                print('You entered wrong date')
        except ValueError:
            print('You entered wrong date')
    return result


def get_leap_year(year, date):
    leap_or_not = ''
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        leap_or_not = date + ' is leap year'
    else:
        leap_or_not = date + ' is not leap year'
    print(leap_or_not)


def get_chinese_year(year):
    string_year = str(year)
    result_chinese_year = string_year + ' is year of the ' + chinese_calendar[year % 12]
    print(result_chinese_year)


def get_month(month):
    string_month = months[month]
    print(string_month)


def get_quarter(month):
    quarter = ''
    if month >= 1 and month <= 3:
        quarter = '1st'
    elif month > 3 and month <= 6:
        quarter = '2nd'
    elif month > 6 and month <= 9:
        quarter = '3rd'
    else:
        quarter = '4th'
    print(quarter + ' quarter')


def get_number_day(day, month):
    day_number = day + month * 31
    print(day_number)


def get_week_day(year, month, day):
    year_last_num = year % 100
    first_part_year_ind = year_last_num // 12
    second_part_year_ind = year_last_num % 12
    third_part_year_ind = second_part_year_ind // 4
    year_index = first_part_year_ind + second_part_year_ind + third_part_year_ind
    month_index = month_index_dict[month]
    if year // 100 == 19:
        century_index = 1
    else:
        century_index = 0
    if year_last_num % 4 == 0 and (month == 1 or month == 2):
        leap_year_index = 1
    else:
        leap_year_index = 0
    week_num = (year_index + month_index + day + century_index - leap_year_index) % 7
    week_day = week_days[week_num]
    print(week_day)


chinese_calendar = {0: 'monkey', 1: 'rooster', 2: 'dog', 3: 'pig', 4: 'rat', 5: 'bull', 6: 'tiger', 7: 'rabbit',
                    8: 'dragon', 9: 'snake', 10: 'horse', 11: 'sheep'}

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}

max_month_set = {1, 3, 5, 7, 8, 10, 12}

day_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
           27, 28}

month_index_dict = {1: 6, 2: 2, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}

week_days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


###


date_list = validation()
day = date_list[0]
month = date_list[1]
year = date_list[2]
date = date_list[3]
get_leap_year(year, date)
get_chinese_year(year)
get_quarter(month)
get_month(month)
print(day)
get_number_day(day, month)
get_week_day(year, month, day)





