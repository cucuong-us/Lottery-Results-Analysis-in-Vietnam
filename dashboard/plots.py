from sqlalchemy import create_engine
import pandas as pd
engine = create_engine("postgresql+psycopg2://postgres:12345678@localhost:5432/postgres")
df = pd.read_sql("SELECT * FROM res_lottery", engine)
print(df.head())  # Hiển thị 5 dòng đầu tiên của DataFrame