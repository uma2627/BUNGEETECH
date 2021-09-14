import pandas as pd
from pathlib import Path

# Defining path
path_to_data = Path(__file__).parent.parent.parent.joinpath('input/question-1/main.csv')
path_to_output = Path(__file__).parent.parent.parent.joinpath('output/answer-1/main.csv')

# Reading data
df = pd.read_csv(path_to_data)

# Grouping
df_grouped = df.groupby((df.Year//10)*10)

# New dataframe
df_output = df[0:0]

# Finding sum
for item in df_grouped:
    population = str(item[1].iloc[[-1]].Population).split()[1]
    new_row_df = item[1].sum()
    new_row = {
        'Year': item[0],
        'Population': population,
        'Total': new_row_df.Total,
        'Violent': new_row_df.Violent,
        'Property': new_row_df.Property,
        'Murder': new_row_df.Murder,
        'Forcible_Rape': new_row_df.Forcible_Rape,
        'Robbery': new_row_df.Robbery,
        'Aggravated_assault': new_row_df.Aggravated_assault,
        'Burglary': new_row_df.Burglary,
        'Larceny_Theft': new_row_df.Larceny_Theft,
        'Vehicle_Theft': new_row_df.Vehicle_Theft
    }
    df_output = df_output.append(new_row, ignore_index=True)

# Save to csv
df_output.to_csv(path_to_output, index=False)
