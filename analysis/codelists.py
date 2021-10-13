from cohortextractor import codelist, codelist_from_csv, combine_codelists

susp_or_confirmed_covid_codes = codelist_from_csv(
    "user-JWray-nice-acute-covid.csv",
    system="snomed",
    column="code"
)

covid_advice_provided_codes = codelist_from_csv(
    "user-JWray-nice-covid-advice-provided.csv",
    system="snomed",
    column="code"
    )

ethnicity_codes = codelist_from_csv(
    "opensafely-ethnicity-snomed.csv",
    system="snomed",
    column="code"
    )