import pandas as pd
from pathlib import Path

# Defining path
path_to_data = Path(__file__).parent.parent.parent.joinpath('input/question-3/main.csv')
path_to_output = Path(__file__).parent.parent.parent.joinpath('output/answer-3/main.csv')

# Reading data
df = pd.read_csv(path_to_data)

# Sorting data
df_grouped = df.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])

# New dataframe
df_output = df_grouped[['Team', 'Yellow Cards', 'Red Cards']].copy()

# Save to csv
df_output.to_csv(path_to_output, index=False)
