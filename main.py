import time

class Clock():
	def __init__(self, hours, minutes, seconds):
		self.seconds = seconds
		self.minutes = minutes
		self.hours = hours

	def start(self):
		while self.seconds >= 0 :
			print('Hours:', self.hours, '|| Minutes:', self.minutes, '|| Seconds:', self.seconds)
			if self.seconds == 0 and self.minutes == 0 and self.hours > 0:
				self.seconds = 60
				self.minutes = 59
				self.hours -= 1

			elif self.seconds == 0 and self.minutes > 0:
				self.seconds = 60
				self.minutes -= 1

			elif self.seconds == 0: 
				return False
			self.seconds -= 1

			time.sleep(1)

intro = '''
|||==================================================|||
||||    WELCOME TO THE BEST TIMER IN THE WORLD!!!   ||||
|||==================================================|||
'''

outro = '''
|||==================================================|||
||||                     OVER!!!                    ||||
|||==================================================|||
'''

print(intro)
try:

	hours = int(input('Hours?'))
	minutes = int(input('Minutes?'))
	seconds = int(input('Seconds?'))
	print(f'SET TIMER => {hours} hours, {minutes} minutes, {seconds} seconds')

except Exception as e:
	print(e)

clock = Clock(hours, minutes, seconds)

state = clock.start()
if state == False:
	print(outro)