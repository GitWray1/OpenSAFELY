import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

rec1_df = pd.read_csv(
    'output/input_rec1.csv',
    parse_dates = True,
    names = ['covid_date','advice_date','ID'],
    header=0
    )

rec1_df.to_csv('output/output_table.csv', index=False)