import pandas as pd

def lambda_handler(events, context):
    data = {'col1':[1, 2], 'col2':[3, 4] }
    df = pd.DataFrame(data=data)
    print(df)
    