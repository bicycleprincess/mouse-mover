import time
import pyautogui

def cal(a, b):
	left = 500
	right = 100
	step = 5
	r, d, l, u = [], [], [], []
	
	for x in range(right, left+1, step):
		r.append([right, x])
		d.append([x, right])
		l.append([left, x])
		u.append([x, left])


def move(a, b, step):
	la, lb = 0, 0
	left=500
	right=100
	t = 2
	while 1:
		na, nb = pyautogui.position()

		if (na, nb) != (a, b) and (na, nb) == (la, lb) or (na, nb) == (a, b):
			if a == right and b != left: b += step
			elif b == left and a!= left: a += step
			elif a == b == left: b -= step
			elif a == left and b > right: b -= step
			else: a -= step
			pyautogui.moveTo(a, b, duration=-1e4)
			time.sleep(t)
		else:
			la, lb = pyautogui.position()
			time.sleep(t*100)			

if __name__ == '__main__':
	a = b = 100
	step = 10
	pyautogui.moveTo(a, b, duration=-1e4)
	move(a, b, step)



"""
stepsize = 10
c = [(stepsize, 0), (0, stepsize), (-stepsize, 0), (0, -stepsize)]
px, py = 500, 500
for dx, dy in c:
	for i in range(4):
		px += dx
		py += dy
		pyautogui.moveTo(px, py, duration=0.5)
"""