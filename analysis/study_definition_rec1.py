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
    )
)
