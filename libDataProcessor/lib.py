import polars as pl


df: pl.DataFrame = pl.DataFrame()
lf: pl.LazyFrame = pl.LazyFrame()
df_ready: bool = False
lf_ready: bool = False


""" Eager Loader"""
def read_parquet(path: str):
    global df, df_ready
    df = pl.read_parquet(path)
    df_ready = True

def read_csv(path: str):
    global df, df_ready
    df = pl.read_csv(path)
    df_ready = True

def read_json(path: str):
    global df, df_ready
    df = pl.read_json(path)
    df_ready = True

def read_ndjson(path: str):
    global df, df_ready
    df = pl.scan_ndjson(path)
    df_ready = True


""" Lazy Loader """
def scan_parquet(path: str):
    global lf, lf_ready
    lf = pl.scan_parquet(path)
    lf_ready = True

def scan_csv(path: str):
    global lf, lf_ready
    lf = pl.scan_csv(path)
    lf_ready = True

def scan_json(path: str):
    global lf, lf_ready
    lf = pl.scan_json(path)
    lf_ready = True

def scan_ndjson(path: str):
    global lf, lf_ready
    lf = pl.scan_ndjson(path)
    lf_ready = True
