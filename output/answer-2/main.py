import pandas as pd
from pathlib import Path

# Defining path
path_to_data = Path(__file__).parent.parent.parent.joinpath('input/question-2/main.csv')
path_to_output = Path(__file__).parent.parent.parent.joinpath('output/answer-2/main.csv')

# Reading data
df = pd.read_csv(path_to_data)

# Grouping
df_grouped = df.groupby('occupation')

# New dataframe
df_output = pd.DataFrame(columns=[
        'Occupation',
        'Min',
        'Max'
])

# Finding sum
for item in df_grouped:
    max_age = item[1].max().age
    min_age = item[1].min().age
    new_row = {
        'Occupation': item[0],
        'Min': min_age,
        'Max': max_age
    }
    df_output = df_output.append(new_row, ignore_index=True)

# Save to csv
df_output.to_csv(path_to_output, index=False)
