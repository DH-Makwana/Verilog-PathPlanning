import numpy as np
import pygame
pygame.init()

n = 12
res = [600, 600]
start = [0, 0]
end = [n-1, n-1]
started = False
ended = False

win = pygame.display.set_mode(res)
pygame.display.set_caption("Dijkstra's Algo")

def addText(str, size, pos, textColor, bgColor):
    global win
    font = pygame.font.Font("freesansbold.ttf", size)
    text = font.render(str, True, textColor, bgColor)
    textRect = text.get_rect()
    textRect.center = pos
    win.blit(text, textRect)

class block(object):
    def __init__(self, pos, x, y, color):
        self.pos = pos
        self.x = x + res[0]/(n*20)
        self.y = y + res[0]/(n*20)
        self.w = (res[0]/n) - res[0]/(n*10)
        self.h = (res[1]/n) - res[0]/(n*10)
        self.val = 255
        self.selected = False
        self.color = color
        self.path = False

    def disp(self, key):
        global started, start
        global ended, end
        global win, n
        msPos = pygame.mouse.get_pos()
        if self.x < msPos[0] < self.x + self.w and self.y < msPos[1] < self.y + self.h:
            clr = []
            for i in range(3):
                if self.color[i]+50 > 255:
                    c = 255
                else:
                    c = self.color[i]+50
                clr.append(c)
            color = (clr[0], clr[1], clr[2])
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    self.color = (255, 200, 0)
                    self.val = -1
                if key[pygame.K_e] and event.type == pygame.KEYUP and not ended:
                    self.color = (0, 0, 200)
                    end = self.pos
                    self.val = -2
                    ended = True
                if key[pygame.K_s] and event.type == pygame.KEYUP and not started:
                    self.color = (0, 200, 0)
                    start = self.pos
                    self.val = 0
                    started = True
        else:
            if 0 < self.val < 255 and not self.path:
                color = (0, 200, 200)
            else:
                color = self.color
	        
        pygame.draw.rect(win, color, (self.x, self.y, self.w, self.h))
        addText(str(self.val), 16, (self.x+self.w/2, self.y+self.h/2), (255, 255, 255), color)
        #pygame.display.update()

    def getval(self):
        return self.val
    def setval(self, val):
        self.val = val


class node(object):
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.prv = self
        self.checked = False


blocks = []

for i in range(n):
    b = []
    for j in range(n):
        b.append(0)
    blocks.append(b)

for i in range(n):
    for j in range(n):
        blk = block([i, j], i*res[0]/n, j*res[1]/n, (200, 200, 200))
        blocks[i][j] = blk



def findPath(arr, st):
    q = []
    path = []
    #print()
    #print([st.i, st.j])
    i = st.i
    j = st.j
    
    if st.j-1 >= 0 and not arr[i][j-1].checked:
        #arr[i][j-1].checked = True
        q. append(arr[i][j-1])
    if st.i+1 <= n-1 and not arr[i+1][j].checked:
        #arr[i+1][j].checked = True
        q. append(arr[i+1][j])
    if st.j+1 <= n-1 and not arr[i][j+1].checked:
        #arr[i][j+1].checked = True
        q. append(arr[i][j+1])
    if st.i-1 >= 0 and not arr[i-1][j].checked:
        #arr[i-1][j].checked = True
        q. append(arr[i-1][j])

    if q == []:
        return np.ndarray([n*n])
    else:
        paths = []
        for p in q:
            if p.val == -2:
                return [st]
            else:
                if st.val+1 < p.val:
                    arr[p.i][p.j].prv = st
                    arr[p.i][p.j].val = st.val + 1
                    path = findPath(arr, p)
                    if len(path) < n*n:
                        path = path + [st]
                    else:
                        path = np.ndarray([n*n])
                else:
                    path = np.ndarray([n*n])
            paths.append(path)
        
        L = []
        for i in paths:
            L.append(len(i))
        for i in range(len(L)):
            if len(paths[i]) == min(L):
                l = i
        
        return paths[l]
            

found = False
arr = []
for i in range(n):
            a = []
            for j in range(n):
                a.append(node(i, j, 255))
            arr.append(a)

while True:
    #win.fill((0, 0, 0))
    error = False
    key = pygame.key.get_pressed()
    for i in range(n):
        for j in range(n):
            arr[i][j].val = blocks[i][j].getval()
            blocks[i][j].disp(key)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if (key[pygame.K_SPACE] and event.type == pygame.KEYUP) and started and ended and not found:
            path = findPath(arr, arr[start[0]][start[1]])
            try:
                found = True
                #print(start, end)
                print(len(path))
                for pth in path[:-1]:
                    blocks[pth.i][pth.j].color = (200, 0, 0)
                    blocks[pth.i][pth.j].path = True
            except:
                print("Path not found!!")
                exit()

            for i in range(n):
                for j in range(n):
                    blocks[i][j].setval(int(arr[i][j].val))


    # for i in range(n):
    #     for j in range(n):
    #         pass
            

    pygame.display.update()