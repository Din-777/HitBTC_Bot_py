
class EMA:
	Period = 0
	LastAverage = 0
	Alpha = 0

	def __init__(self, period):
		Period = period
		Alpha = 2.0 / (period + 1.0)

	def NextAverage(self, value):
		self.LastAverage = value if self.LastAverage == 0 else (value - self.LastAverage) * self.Alpha + self.LastAverage
		return self.LastAverage

	def Average(self, value):
		_average = value if self.LastAverage == 0  else (value - self.LastAverage) * Alpha + self.LastAverage
		return _average

	def IsPrimed(self):
		if self.LastAverage == 0: return False
		elif self.LastAverage != 0: return True
		else: return False

	def Clear():
		self.LastAverage = 0
