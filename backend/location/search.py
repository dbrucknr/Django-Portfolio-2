from uszipcode import SearchEngine
import json
import csv

def search(data):
    # set simple_zipcode=False to use rich info database
    search = SearchEngine(simple_zipcode=False)
    zipcode = search.by_zipcode(data)

    dictData = zipcode.to_json()
    print(dictData)
    # print(dictData)
    # with open('datajson', 'w') as f:
    #     json.dump(dictData, f)
    return 'done'

search('48116')

# with open('/zipdatajson') as f:
#     o = jsonload(f)
#     print(o['zipcode_type'])

# The SQLite3 database contains Null/BLOB values that don't seem readable
# import sqlite3
# conn = sqlite3connect('/dbsqlite')

# c = conncursor()

# cexecute('SELECT zipcode FROM zipcode')
# test=cfetchall()
# with open('zipcodetxt','w') as codes:
#     for zipcode in test:
#         codeswrite(zipcode[0]+'\n')
# with open('zipcodecsv','w') as codes:
#     writer = csvwriter(codes, delimiter=' ')
#     for zipcode in test:
#         print(zipcode[0])
#         writerwriterow(zipcode[0])
#         break
# print(test)
# print(test[0])
# print(test[1])
# print(test[2])
# print(test[3])
# print(test[4][0)

# test2 = cfetchall()
# print(type(test2))
# print(type(test2[0]))
# print(test2[0])
# print(len(test2), 'tuples')
# search = SearchEngine(simple_zipcode=False)

# with open('zipcode.txt', 'r') as codes:
#     load = codes.read()
#     data = load.split('\n')

# for code in data:
#     zipcode = search.by_zipcode(code)
#     location = zipcode.to_dict()
#     # print(location['state'])
#     # print(locationkeys())
#     print(location['zipcode_type'])
#     print(location['major_city'])
#     print(location['post_office_city'])
#     print(location['common_city_list'])
#     print(location['county'])
#     print(location['state'])
#     print(location['lat'])
#     print(location['lng'])
#     print(location['timezone'])
#     print(location['radius_in_miles'])
#     print(location['area_code_list'])
#     print(location['population'])
#     print(location['population_density'])
#     print(location['land_area_in_sqmi'])
#     print(location['water_area_in_sqmi'])
#     print(location['housing_units'])
#     print(location['occupied_housing_units'])
#     print(location['median_home_value'])
#     print(location['median_household_income'])
#     print(location['bounds_west'])
#     print(location['bounds_east'])
#     print(location['bounds_north'])
#     print(location['bounds_south'])
#     print(location['zipcode'])
#     print(location['polygon'])
#     print(location['population_by_year'])
#     print(location['population_by_age'])
#     print(location['population_by_gender'])
#     print(location['population_by_race'])
#     print(location['head_of_household_by_age'])
#     print(location['families_vs_singles'])
#     print(location['households_with_kids'])
#     print(location['children_by_age'])
#     print(location['housing_type'])
#     print(location['year_housing_was_built'])
#     print(location['housing_occupancy'])
#     print(location['vancancy_reason'])
#     print(location['owner_occupied_home_values'])
#     print(location['rental_properties_by_number_of_rooms'])
#     print(location['monthly_rent_including_utilities_studio_apt'])
#     print(location['monthly_rent_including_utilities_1_b'])
#     print(location['monthly_rent_including_utilities_2_b'])
#     print(location['monthly_rent_including_utilities_3plus_b'])
#     print(location['employment_status'])
#     print(location['average_household_income_over_time'])
#     print(location['household_income'])
#     print(location['annual_individual_earning'])
#     print(location['sources_of_household_income____percent_of_households_receiving_income'])
#     print(location['sources_of_household_income____average_income_per_household_by_income_source'])
#     print(location['household_investment_income____percent_of_households_receiving_investment_income'])
#     print(location['household_investment_income____average_income_per_household_by_income_source'])
#     print(location['household_retirement_income____percent_of_households_receiving_retirement_incom'])
#     print(location['household_retirement_income____average_income_per_household_by_income_source'])
#     print(location['source_of_earnings'])
#     print(location['means_of_transportation_to_work_for_workers_16_and_over'])
#     print(location['travel_time_to_work_in_minutes'])
#     print(location['educational_attainment_for_population_25_and_over'])
#     print(location['school_enrollment_age_3_to_17'])
#     break

# zipcode_type
# major_city 
# post_office_city 
# common_city_list 
# county 
# state 
# lat 
# lng 
# timezone 
# radius_in_miles 
# area_code_list 
# population 
# population_density 
# land_area_in_sqmi 
# water_area_in_sqmi 
# housing_units 
# occupied_housing_units 
# median_home_value 
# median_household_income 
# bounds_west 
# bounds_east 
# bounds_north 
# bounds_south 
# zipcode 
# polygon 
# population_by_year 
# population_by_age 
# population_by_gender 
# population_by_race 
# head_of_household_by_age 
# families_vs_singles 
# households_with_kids 
# children_by_age 
# housing_type 
# year_housing_was_built 
# housing_occupancy 
# vancancy_reason 
# owner_occupied_home_values 
# rental_properties_by_number_of_rooms 
# monthly_rent_including_utilities_studio_apt 
# monthly_rent_including_utilities_1_b 
# monthly_rent_including_utilities_2_b 
# monthly_rent_including_utilities_3plus_b 
# employment_status 
# average_household_income_over_time 
# household_income 
# annual_individual_earnings sources_of_household_income____percent_of_households_receiving_income 
# sources_of_household_income____average_income_per_household_by_income_source 
# household_investment_income____percent_of_households_receiving_investment_income 
# household_investment_income____average_income_per_household_by_income_source 
# household_retirement_income____percent_of_households_receiving_retirement_incom 
# household_retirement_income____average_income_per_household_by_income_source 
# source_of_earnings 
# means_of_transportation_to_work_for_workers_16_and_over 
# travel_time_to_work_in_minutes 
# educational_attainment_for_population_25_and_over 
# school_enrollment_age_3_to_17