# Import all of the packages we will require
from cohortextractor import (
    StudyDefinition,
    codelist,
    codelist_from_csv,
    combine_codelists,
    filter_codes_by_category,
    patients,
)
from codelists import *

susp_or_confirmed_covid_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv", system="ctv3", column="CTV3ID"
)

covid_advice_provided_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv", system="ctv3", column="CTV3ID"
)


# Define the study definition
study = StudyDefinition(

    # Define the study index date
    index_date = "2020-03-21",

    # Define the dummy data behaviour
    default_expectations = {},

    # Define the study population
    population = patients.with_these_clinical_events(
        susp_or_confirmed_covid_codes, on_or_after=index_date, include_date_of_match = True
    ),

    # Define the variables we are interested in
    received_info = patients.with_these_clinical_events(
        covid_advice_provided_codes, on_or_after = 
    )
)
