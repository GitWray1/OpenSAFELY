# Import all of the packages we will require
from cohortextractor import (
    StudyDefinition,
    codelist,
    codelist_from_csv,
    combine_codelists,
    filter_codes_by_category,
    patients,
)

# Import our predefined codelists
from codelists import *

# Define the pandemic start date
pandemic_start_date = "2020-02-01"

# Define the study definition
study = StudyDefinition(

    # Define the dummy data behaviour
    default_expectations={
        "date": {"earliest": pandemic_start_date, "latest": "today"},
        "rate": "uniform",
        "incidence": 0.8,
    },

    # Define the study population
    population=patients.with_these_clinical_events(
        susp_or_confirmed_covid_codes,
        on_or_after=pandemic_start_date
    ),

    # Select the date column for people with suspected or confirmed COVID (Used to get advice given after diagnosis)
    susp_or_confirmed_covid_date=patients.with_these_clinical_events(
        susp_or_confirmed_covid_codes,
        find_first_match_in_period=True,
        returning='date',
        date_format='YYYY-MM-DD',
        return_expectations={"date": {"earliest": pandemic_start_date, "latest": "2021-10-04"},
                             "rate": "uniform"},
    ),

    # Define the variables we are interested in
    advice_provided=patients.with_these_clinical_events(
        covid_advice_provided_codes, 
        on_or_after="susp_or_confirmed_covid_date",
        find_first_match_in_period=True,
        returning='date',
        date_format='YYYY-MM-DD',
        return_expectations={"date": {"earliest": pandemic_start_date, "latest": "2021-10-04"},
                             "rate": "uniform"},
    ),

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
            }
    ),

    region=patients.registered_practice_as_of(
        pandemic_start_date,
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.2,
                    "South East": 0.2,
                },
            },
        },
    )
)

imd=
ethnicity=
age_group=