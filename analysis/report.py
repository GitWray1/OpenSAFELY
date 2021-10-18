#Import relevant packages
import pandas as pd

# Read in the results dataframe produced from the study definition
df = pd.read_csv(
    'output/input.csv',
    parse_dates=True,
    names=['covid_date', 'advice_date', 'sex', 'region', 'IMD_category', 'age_group', 'ethnicity', 'ID'],
    header=0,
    na_values=['', 'NA', 0]
    )

# Create a list to keep all the information about the recs - will use to build the final dataframe
rec_list = []

# Extract all of the information for Recommendation 1.1
Rec1_1_num = df[df.advice_date >= df.covid_date].advice_date.count()
Rec1_1_num_missing = df['advice_date'].isna().sum() / len(df['advice_date'])
Rec1_1_denom = df.dropna(subset=['covid_date', 'advice_date']).covid_date.count()
Rec1_1_denom_missing = df['covid_date'].isna().sum() / len(df['covid_date'])
Rec1_1_ratio = Rec1_1_num / Rec1_1_denom
Rec1_1 = ['1.1', 'Advice given', Rec1_1_num, Rec1_1_num_missing, Rec1_1_denom, Rec1_1_denom_missing, Rec1_1_ratio]
rec_list.append(Rec1_1)

# Create a dataframe to summarize the results
results_df = pd.DataFrame(rec_list, columns=['Rec number', 'Description', 'Numerator', '%Num_missing', 'Denominator', '%Denom_Missing', 'Num/Denom'])

results_df.to_csv('output/results_table.csv', index=False)
