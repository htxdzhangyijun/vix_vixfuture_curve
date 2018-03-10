import csv
import re
import pandas as pd

class csv_data:
	def __init__(self, csvfile1):
		self.csvfile1 = csvfile1

	def read_csvdata_ticker(self):
		fields = ['m_localSymbol']

		Symbols1 = pd.read_csv(self.csvfile1, skipinitialspace=True, usecols=fields,
								low_memory=False)
		Symbols1 = Symbols1.astype(str).values.tolist()
		Symbols = [Symbols1[i][0] for i in range(len(Symbols1))]

		return Symbols

	def read_csvdata_all(self):

		allinfo1 = pd.read_csv(self.csvfile1, skipinitialspace=True)


		return allinfo1

	def read_csvdata_date(self):
		fields = ['date']
		date1 = pd.read_csv(self.csvfile1, skipinitialspace=True, usecols=fields,
								low_memory=False)
		date1 = date1.astype(str).values.tolist()
		date = [date1[i][0] for i in range(len(date1))]

		return date

	def read_csvdata_close(self):
		fields = ['close']
		close1 = pd.read_csv(self.csvfile1, skipinitialspace=True, usecols=fields,
								low_memory=False)
		close1 = close1.astype(str).values.tolist()
		close = [close1[i][0] for i in range(len(close1))]

		return close

	def read_csvdate_expiration(self):
		expiration1 = pd.read_csv(self.csvfile1, skipinitialspace=True,
									low_memory=False, names = ["m_localSymbol", "date"])

		return expiration1





