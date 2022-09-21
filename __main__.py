import datetime as dt
import sys
sys.path.insert(0, r'C:\OPTECH TEAM COMPLETE JOBS\Assessment-Index-Modelling-master\index_model')
from index import IndexModel


if __name__ == "__main__":
    backtest_start = dt.date(year=2020, month=1, day=1)
    backtest_end = dt.date(year=2020, month=12, day=31)
    index = IndexModel()

    index.calc_index_level(start_date=backtest_start, end_date=backtest_end)
    index.export_values("export.csv")
