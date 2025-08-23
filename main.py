from scraper.crawler import crawl_xoso_miennam
import pandas as pd
df_kq = crawl_xoso_miennam(1)
df_kq = df_kq.explode('lottery_number')
df_kq.to_csv("ket_qua_xoso.csv", index=False)
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:12345678@localhost:5432/postgres")
# Ghi vào bảng ket_qua_xo_so, nếu bảng chưa tồn tại thì sẽ tự tạo
df_kq.to_sql("res_lottery", engine, if_exists="append", index=False)
