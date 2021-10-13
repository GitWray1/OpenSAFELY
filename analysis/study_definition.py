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
        "pandemic_start_date",
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
    ),

    imd_category=patients.categorised_as(
        {
            "0": "DEFAULT",
            "1": """index_of_multiple_deprivation >=1 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 AND index_of_multiple_deprivation < 32844""",
        },
        index_of_multiple_deprivation=patients.address_as_of(
            "pandemic_start_date",
            returning="index_of_multiple_deprivation",
            round_to_nearest=100,
        ),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.05,
                    "1": 0.19,
                    "2": 0.19,
                    "3": 0.19,
                    "4": 0.19,
                    "5": 0.19,
                }
            },
        },
    ),
    age_group=patients.categorised_as(
        {
            "0-17": "age < 18",
            "18-24": "age >= 18 AND age < 25",
            "25-34": "age >= 25 AND age < 35",
            "35-44": "age >= 35 AND age < 45",
            "45-54": "age >= 45 AND age < 55",
            "55-69": "age >= 55 AND age < 70",
            "70-79": "age >= 70 AND age < 80",
            "80+": "age >= 80",
            "missing": "DEFAULT",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0-17": 0.1,
                    "18-24": 0.1,
                    "25-34": 0.1,
                    "35-44": 0.1,
                    "45-54": 0.2,
                    "55-69": 0.2,
                    "70-79": 0.1,
                    "80+": 0.1,
                }
            },
        },
        age=patients.age_as_of("pandemic_start_date"),
    ),

    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,
        returning="category",
        find_last_match_in_period=True,
        on_or_before="index_date",
        return_expectations={
            "category": {"ratios": {"1": 0.8, "5": 0.1, "3": 0.1}},
            "incidence": 0.75,
        },
    ),
)
