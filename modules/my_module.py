# Zawartość pliku my_module.py

import pandas as pd
import pandas_gbq
from datetime import datetime
import random
import string

def append_random_record_to_bq(table_id: str, project_id: str):
    """
    Generuje losowy ciąg znaków, tworzy z niego DataFrame z aktualnym czasem
    i dołącza go do wskazanej tabeli w BigQuery.
    
    Args:
        table_id (str): Pełny identyfikator tabeli w formacie 'dataset.table_name'.
        project_id (str): Identyfikator projektu GCP.

    Returns:
        pd.DataFrame: DataFrame, który został dołączony do tabeli.
    """
    # Generowanie losowego ciągu znaków
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    
    # Tworzenie DataFrame z nowymi danymi
    df_new = pd.DataFrame([{'time': datetime.now(), 'output': random_string}])
    
    # Dołączanie DataFrame do tabeli BigQuery
    pandas_gbq.to_gbq(
        df_new, 
        table_id,
        project_id=project_id, 
        if_exists='append'
    )
    
    print(f"Pomyślnie dodano rekord do tabeli: {table_id}")
    return df_new