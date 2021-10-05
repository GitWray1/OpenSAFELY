from cohortextractor import codelist, codelist_from_csv, combine_codelists

susp_or_confirmed_covid_codes = codelist_from_csv(
    "codelists/opensafely-covid-identification-in-primary-care-suspected-covid-suspected-codes.csv",
    system="ctv3",
    column="CTV3ID"
)

covid_advice_provided_codes = codelist_from_csv(
    "codelists/opensafely-covid-identification-in-primary-care-suspected-covid-advice.csv",
    system="ctv3",
    column="CTV3ID"
    )
