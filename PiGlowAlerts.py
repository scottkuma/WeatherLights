import PyGlow as PG
from time import sleep


class PiGlowAlerts:

    def __init__(self, brightness = 1):
		# Brightness = 0 < x < 1
        self.mode = 'noaction'
        self.brightness = brightness
        self.pg = PG.PyGlow()

    def clear(self):
        # print "Turning all off...."
        self.pg.all(0)

    def initialize(self):
        print "Initializing PyGlow..."
        self.clear()
        self.pg.all(brightness=255, speed=2000, pulse=True, pulse_dir=0)
        self.error()
        sleep(2)
        self.win(1)
        sleep(0.5)
        self.sew(1)
        sleep(0.5)
        self.tow(1)
        sleep(0.5)
        self.wrn(1)
        sleep(0.5)
        self.towwrn(1)
        sleep(0.5)
        self.tor(3)

    def noaction(self):
        self.clear()
        self.pg.color("green", int(100 * self.brightness))

    def spe(self):
		self.clear()
		self.pg.color("yellow", int(100* self.brightness))

    def wat(self, x):
		self.clear()
		pulsespeed=10000
		pulsedir = 0
		for i in range(x):
			self.pg.set_leds(["blue1"], brightness=int(100* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir )
			self.pg.update_leds()
			self.pg.set_leds(["blue2"], brightness=int(100* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir )
			self.pg.update_leds()
			self.pg.set_leds(["blue3"], brightness=int(100* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir )
			self.pg.update_leds()

    def error(self):
        self.clear()
        self.pg.color("yellow", int(100* self.brightness))
        self.pg.color("red", int(100* self.brightness))


    def tor(self, x):
        self.clear()
        for i in range(x):
            pulsespeed = 500 # 1/2 second per pulse, 2 second for entire
            pulsedir = -1
            self.pg.color("red", brightness=255, speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("white", brightness=255, speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("blue", brightness=255, speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("white", brightness=255, speed=pulsespeed, pulse=True, pulse_dir=pulsedir)

    def tow(self, x):
        self.clear()
        for i in range(x):
            pulsespeed = 5000 # 5 seconds per pulse
            pulsedir = 0
            self.pg.color("red", brightness=int(255 * self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)

    def towwrn(self, x):
        self.clear()
        for i in range(x):
            pulsespeed = 2000 # 1 1/2 second per pulse, 6 second for entire
            pulsedir = 0
            self.pg.color("red", brightness=int(255* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("yellow", brightness=int(255* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("red", brightness=int(255* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("yellow", brightness=int(255* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)

    def wrn(self, x):
        self.clear()
        for i in range(x):
            pulsespeed = 1500  # 1.5 seconds per pulse, 6s for entire 
            pulsedir = 0
            self.pg.color("yellow", brightness=int(255* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("white", brightness=int(200* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("yellow", brightness=int(255* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
            self.pg.color("white", brightness=int(200* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)


    def sew(self, x):
        self.clear()
        for i in range(x):
            pulsespeed = 5000  # 5 seconds per pulse
            pulsedir = 0
            self.pg.color("yellow", brightness=int(255* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)


    def win(self, x):
        self.clear()
        for i in range(x):
            pulsespeed = 5000  # 5 seconds per pulse
            pulsedir = 0
            self.pg.color("blue", brightness=int(100* self.brightness), speed=pulsespeed, pulse=True, pulse_dir=pulsedir)
    
    def frz(self):
		self.wat(self)

    def fog(self):
       self.clear()
       self.pg.color("white" , 25)
