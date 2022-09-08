from random import randint
import time
import pygame
pygame.init()
mainboard=[[0 for x in range(102)] for y in range(102)]
reflex=[[0 for x in range(102)] for y in range(102)]
safhe=pygame.display.set_mode((600,600))
run=True
fps=5
alowed="10"
black=(0,0,0)
white=(255,255,255)
pygame.display.set_caption("Conway game of life")
fpsClock=pygame.time.Clock()
fpsClock.tick(fps)

for i in range(1,101):
	for j in range(1,101):
		mainboard[i][j]=randint(0, 1)


def neighbour_count(x,y):
	tmp=0
	if mainboard[x+1][y+1] == 1:
		tmp=tmp+1
	if mainboard[x+1][y] == 1:
		tmp=tmp+1
	if mainboard[x+1][y-1] == 1:
		tmp=tmp+1
	if mainboard[x][y+1] == 1:
		tmp=tmp+1
	if mainboard[x][y-1] == 1:
		tmp=tmp+1
	if mainboard[x-1][y+1] == 1:
		tmp=tmp+1
	if mainboard[x-1][y] == 1:
		tmp=tmp+1
	if mainboard[x-1][y-1] == 1:
		tmp=tmp+1
	return tmp


def cell_change(x,y):
	neighbour=neighbour_count(x,y)
	if mainboard[x][y]==0:
		if neighbour ==3:
			reflex[x][y]=1
		else:
			reflex[x][y]=0
	else:
		if neighbour>1 and neighbour<4:
			reflex[x][y]=1
		else:
			reflex[x][y]=0


def next_gen():
	for i in range(1,101):
		for j in range(1,101):
			cell_change(i,j)
	x=randint(1,100)
	y=randint(1,100)
	time.sleep(0.04)
	reflex[x][y]=1
	for i in range(1,101):
		for j in range(1,101):
			mainboard[i][j]=reflex[i][j]


def main():
	for i in range(1,101):
		for j in range(1,101):
			if mainboard[i][j]==1:
				 pygame.draw.rect(safhe,black,((i-1)*6,(j-1)*6,6,6))
			else:
				pygame.draw.rect(safhe,white,((i-1)*6,(j-1)*6,6,6))
	pygame.display.update()
	next_gen()


while True:
	for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
	if __name__=="__main__":
		main()


