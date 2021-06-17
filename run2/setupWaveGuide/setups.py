def setupB(fdtd, delta=0):
	delta = int(delta)
	for i in range(1,14+delta):
		fdtd.setnamed("circle_8_"+str(i), "enabled", False)
	for i in range(14+delta, 26):
		fdtd.setnamed("circle_8_"+str(i), "enabled", True)
	start = 13+delta
	for i in range(13, 24):
		fdtd.setnamed("circle_9_"+str(i), "enabled", i!=start and i-1!=start)
		fdtd.setnamed("circle_9_"+str(i+1), "enabled", i!=start)
		fdtd.setnamed("circle_10_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_11_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_12_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_13_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_14_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_15_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_16_"+str(i+5), "enabled", i!=start)

def setupA(fdtd, delta=0):
	delta = int(delta)
	for i in range(1,14+delta):
		fdtd.setnamed("circle_28_"+str(i), "enabled", False)
	for i in range(14+delta, 26):
		fdtd.setnamed("circle_28_"+str(i), "enabled", True)
	start = 13+delta
	for i in range(13, 24):
		fdtd.setnamed("circle_27_"+str(i), "enabled", i!=start and i-1!=start)
		fdtd.setnamed("circle_27_"+str(i+1), "enabled", i!=start)
		fdtd.setnamed("circle_26_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_25_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_24_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_23_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_22_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_21_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_20_"+str(i+5), "enabled", i!=start)

def setupUpperRadius(fdtd, solution):
	for i in range(17, 33):
		fdtd.setnamed('circle_19_'+str(i), 'radius', 155e-9)
	fdtd.setnamed('circle_19_'+str(int(18+solution[5])), 'radius', 1e-9*solution[0])
	fdtd.setnamed('circle_19_'+str(int(18+solution[5]+1)), 'radius', 1e-9*solution[1])
	fdtd.setnamed('circle_19_'+str(int(18+solution[5]-1)), 'radius', 1e-9*solution[2])
