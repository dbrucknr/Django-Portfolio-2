# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Zipcode(models.Model):
    zipcode = models.CharField(max_length=200)
    zipcode_type = models.CharField(blank=True, null=True, max_length=200)
    major_city = models.CharField(blank=True, null=True, max_length=200)
    post_office_city = models.CharField(blank=True, null=True, max_length=200)
    common_city_list = models.TextField(blank=True, null=True)
    county = models.CharField(blank=True, null=True, max_length=200)
    state = models.CharField(blank=True, null=True, max_length=200)
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    lng = models.TextField(blank=True, null=True)  # This field type is a guess.
    timezone = models.CharField(blank=True, null=True, max_length=200)
    radius_in_miles = models.TextField(blank=True, null=True)  # This field type is a guess.
    area_code_list = models.TextField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    population_density = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_wage = models.IntegerField(blank=True, null=True)
    land_area_in_sqmi = models.TextField(blank=True, null=True)  # This field type is a guess.
    water_area_in_sqmi = models.TextField(blank=True, null=True)  # This field type is a guess.
    housing_units = models.IntegerField(blank=True, null=True)
    occupied_housing_units = models.IntegerField(blank=True, null=True)
    median_home_value = models.IntegerField(blank=True, null=True)
    median_household_income = models.IntegerField(blank=True, null=True)
    bounds_west = models.TextField(blank=True, null=True)  # This field type is a guess.
    bounds_east = models.TextField(blank=True, null=True)  # This field type is a guess.
    bounds_north = models.TextField(blank=True, null=True)  # This field type is a guess.
    bounds_south = models.TextField(blank=True, null=True)  # This field type is a guess.
    polygon = models.TextField(blank=True, null=True)
    population_by_year = models.TextField(blank=True, null=True)
    population_by_age = models.TextField(blank=True, null=True)
    population_by_gender = models.TextField(blank=True, null=True)
    population_by_race = models.TextField(blank=True, null=True)
    head_of_household_by_age = models.TextField(blank=True, null=True)
    families_vs_singles = models.TextField(blank=True, null=True)
    households_with_kids = models.TextField(blank=True, null=True)
    children_by_age = models.TextField(blank=True, null=True)
    housing_type = models.TextField(blank=True, null=True)
    year_housing_was_built = models.TextField(blank=True, null=True)
    housing_occupancy = models.TextField(blank=True, null=True)
    vancancy_reason = models.TextField(blank=True, null=True)
    owner_occupied_home_values = models.TextField(blank=True, null=True)
    rental_properties_by_number_of_rooms = models.TextField(blank=True, null=True)
    monthly_rent_including_utilities_studio_apt = models.TextField(blank=True, null=True)
    monthly_rent_including_utilities_1_b = models.TextField(blank=True, null=True)
    monthly_rent_including_utilities_2_b = models.TextField(blank=True, null=True)
    monthly_rent_including_utilities_3plus_b = models.TextField(blank=True, null=True)
    employment_status = models.TextField(blank=True, null=True)
    average_household_income_over_time = models.TextField(blank=True, null=True)
    household_income = models.TextField(blank=True, null=True)
    annual_individual_earnings = models.TextField(blank=True, null=True)
    sources_of_household_income_percent_of_households_receiving_income = models.TextField(db_column='sources_of_household_income____percent_of_households_receiving_income', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    sources_of_household_income_average_income_per_household_by_income_source = models.TextField(db_column='sources_of_household_income____average_income_per_household_by_income_source', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    household_investment_income_percent_of_households_receiving_investment_income = models.TextField(db_column='household_investment_income____percent_of_households_receiving_investment_income', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    household_investment_income_average_income_per_household_by_income_source = models.TextField(db_column='household_investment_income____average_income_per_household_by_income_source', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    household_retirement_income_percent_of_households_receiving_retirement_incom = models.TextField(db_column='household_retirement_income____percent_of_households_receiving_retirement_incom', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    household_retirement_income_average_income_per_household_by_income_source = models.TextField(db_column='household_retirement_income____average_income_per_household_by_income_source', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    source_of_earnings = models.TextField(blank=True, null=True)
    means_of_transportation_to_work_for_workers_16_and_over = models.TextField(blank=True, null=True)
    travel_time_to_work_in_minutes = models.TextField(blank=True, null=True)
    educational_attainment_for_population_25_and_over = models.TextField(blank=True, null=True)
    school_enrollment_age_3_to_17 = models.TextField(blank=True, null=True)
