import pandas as pd
import json

def read_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.json'):
        data = json.load(file)
        return pd.DataFrame(data)
    else:
        raise ValueError("صيغة غير مدعومة! يرجى استخدام CSV أو JSON.")
