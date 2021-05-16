import json
from datetime import datetime
from uszipcode import SearchEngine
from django.core.management import BaseCommand

from location.models import Zipcode
from pytz import UTC


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads uszipcode data into our Django database."

    def handle(self, *args, **options):
        if Zipcode.objects.exists():
            print('data already loaded...exiting.')
            return
        print("Creating data")
        search = SearchEngine(simple_zipcode=False)
        
        with open('zipcode.txt', 'r') as codes:
            load = codes.read()
            data = load.split('\n')
        
        for code in data:
            locDB = Zipcode()
            zipcode = search.by_zipcode(code)
            location = zipcode.to_dict()

            locDB.zipcode_type = location['zipcode_type']
            locDB.major_city = location['major_city']
            locDB.post_office_city = location['post_office_city']
            locDB.common_city_list = location['common_city_list']
            locDB.county = location['county']
            locDB.state = location['state']
            locDB.lat = location['lat']
            locDB.lng = location['lng']
            locDB.timezone = location['timezone']
            locDB.radius_in_miles = location['radius_in_miles']
            locDB.area_code_list = location['area_code_list']
            locDB.population = location['population']
            locDB.population_density = location['population_density']
            locDB.land_area_in_sqmi = location['land_area_in_sqmi']
            locDB.water_area_in_sqmi = location['water_area_in_sqmi']
            locDB.housing_units = location['housing_units']
            locDB.occupied_housing_units = location['occupied_housing_units']
            locDB.median_home_value = location['median_home_value']
            locDB.median_household_income = location['median_household_income']
            locDB.bounds_west = location['bounds_west']
            locDB.bounds_east = location['bounds_east']
            locDB.bounds_north = location['bounds_north']
            locDB.bounds_south = location['bounds_south']
            locDB.zipcode = location['zipcode']
            locDB.polygon = location['polygon']
            locDB.population_by_year = location['population_by_year']
            locDB.population_by_age = location['population_by_age']
            locDB.population_by_gender = location['population_by_gender']
            locDB.population_by_race = location['population_by_race']
            locDB.head_of_household_by_age = location['head_of_household_by_age']
            locDB.families_vs_singles = location['families_vs_singles']
            locDB.households_with_kids = location['households_with_kids']
            locDB.children_by_age = location['children_by_age']
            locDB.housing_type = location['housing_type']
            locDB.year_housing_was_built = location['year_housing_was_built']
            locDB.housing_occupancy = location['housing_occupancy']
            locDB.vancancy_reason = location['vancancy_reason']
            locDB.owner_occupied_home_values = location['owner_occupied_home_values']
            locDB.rental_properties_by_number_of_rooms = location['rental_properties_by_number_of_rooms']
            # print(location['monthly_rent_including_utilities_studio_apt'])
            locDB.monthly_rent_including_utilities_studio_apt = location['monthly_rent_including_utilities_studio_apt']
            # print(location['monthly_rent_including_utilities_1_b'])
            locDB.monthly_rent_including_utilities_1_b = location['monthly_rent_including_utilities_1_b']
            # print(location['monthly_rent_including_utilities_2_b'])
            locDB.monthly_rent_including_utilities_2_b = location['monthly_rent_including_utilities_2_b']
            # print(location['monthly_rent_including_utilities_3plus_b'])
            locDB.monthly_rent_including_utilities_3plus_b = location['monthly_rent_including_utilities_3plus_b']
            # print(location['employment_status'])
            locDB.employment_status = location['employment_status']
            # print(location['average_household_income_over_time'])
            locDB.average_household_income_over_time = location['average_household_income_over_time']
            # print(location['household_income'])
            locDB.household_income = location['household_income']
            # print(location['annual_individual_earning'])
            locDB.annual_individual_earnings = location['annual_individual_earnings']
            # print(location['sources_of_household_income____percent_of_households_receiving_income'])
            locDB.sources_of_household_income____percent_of_households_receiving_income = location['sources_of_household_income____percent_of_households_receiving_income']
            # print(location['sources_of_household_income____average_income_per_household_by_income_source'])
            locDB.sources_of_household_income____average_income_per_household_by_income_source = location['sources_of_household_income____average_income_per_household_by_income_source']
            # print(location['household_investment_income____percent_of_households_receiving_investment_income'])
            locDB.household_investment_income____percent_of_households_receiving_investment_income = location['household_investment_income____percent_of_households_receiving_investment_income']
            # print(location['household_investment_income____average_income_per_household_by_income_source'])
            locDB.household_investment_income____average_income_per_household_by_income_source = location['household_investment_income____average_income_per_household_by_income_source']
            # print(location['household_retirement_income____percent_of_households_receiving_retirement_incom'])
            locDB.household_retirement_income____percent_of_households_receiving_retirement_incom = location['household_retirement_income____percent_of_households_receiving_retirement_incom']
            # print(location['household_retirement_income____average_income_per_household_by_income_source'])
            locDB.household_retirement_income____average_income_per_household_by_income_source = location['household_retirement_income____average_income_per_household_by_income_source']
            # print(location['source_of_earnings'])
            locDB.source_of_earnings = location['source_of_earnings']
            # print(location['means_of_transportation_to_work_for_workers_16_and_over'])
            locDB.means_of_transportation_to_work_for_workers_16_and_over = location['means_of_transportation_to_work_for_workers_16_and_over']
            # print(location['travel_time_to_work_in_minutes'])
            locDB.travel_time_to_work_in_minutes = location['travel_time_to_work_in_minutes']
            # print(location['educational_attainment_for_population_25_and_over'])
            locDB.educational_attainment_for_population_25_and_over = location['educational_attainment_for_population_25_and_over']
            # print(location['school_enrollment_age_3_to_17'])
            locDB.school_enrollment_age_3_to_17 = location['school_enrollment_age_3_to_17']

            locDB.save()


        # with open('./zipdata.json') as f:
        #     loc = Location()
        #     o = json.load(f)
        #     loc.zipcode_type = o['zipcode_type']
        #     loc.major_city = o['major_city']
        #     loc.post_office_city = o['post_office_city']
        #     loc.common_city_list = o['common_city_list']
        #     loc.county = o['county']
        #     loc.state = o['state']
        #     loc.save()

