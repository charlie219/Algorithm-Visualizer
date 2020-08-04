import pygame
import random
import time
import math
from ExtraElements import *
from test import *
from threading import *
from tkinter import *
import StartProcess

RunClock=True

class Sorting:
    def __init__(self, NoOfElements, Speed, AlgorithmName):
        self.NoOfElements = NoOfElements
        self.Speed = Speed
        self.AlgorithmName = AlgorithmName
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.blue = (0,0,255)
        self.running = True
        self.Sorting = True
        self.array = []
        self.colours=[]
        self.Operations=0

        for i in range(self.NoOfElements):
            self.colours.append(self.white)
        self.WaitForEndProcess = True

        self.HeightDiff = 400/self.NoOfElements

        self.gap = 2

        for i in range(1, self.NoOfElements + 1):
            self.array.append(self.HeightDiff * i)

        self.SortedArray = sorted(self.array)
        self.thickness = math.ceil((800 - self.gap * (self.NoOfElements + 1)) / self.NoOfElements)
        self.initial = (self.gap + self.thickness) / 2
        self.difference = self.thickness + self.gap

        self.resize_x = int(self.initial + (self.NoOfElements-1)*self.difference)

        self.screen = pygame.display.set_mode((self.resize_x+(math.ceil(self.thickness/2)+self.gap), 600))

        pygame.display.set_caption(self.AlgorithmName)

        random.shuffle(self.array)

        self.StartVisualisation()

    def StartVisualisation(self):
        try:
            AddClock = Clock(self.screen, self.resize_x + (math.ceil(self.thickness / 2) + self.gap) - 75,
                             550, 25)
            AddClock.start()
            AddMainMenuButton=MainMenuButton(self.screen,(self.resize_x + (math.ceil(self.thickness / 2) + self.gap)) / 3,550)
            AddMainMenuButton.start()
            AddExitText= ExitText(self.screen,((self.resize_x + (math.ceil(self.thickness / 2) + self.gap)) / 3) +25 ,500)
            AddExitText.start()

        except:
            pass

        if self.AlgorithmName == 'Bubble Sort':
            DrawElements = Thread(target=self.DrawBubbleSort)
            DrawElements.start()

        elif self.AlgorithmName == "Insertion Sort":
            DrawElements = Thread(target=self.DrawInsertionSort)
            DrawElements.start()

        elif self.AlgorithmName == "Selection Sort":
            DrawElements = Thread(target=self.DrawSelectionSort)
            DrawElements.start()
            
        elif self.AlgorithmName == "Heap Sort":
            DrawElements = Thread(target=self.DrawHeapSort)
            DrawElements.start()
            
        elif self.AlgorithmName == "Merge Sort":
            DrawElements = Thread(target=self.DrawMergeSort)
            DrawElements.start()


        self.CheckActions()


    def CheckActions(self):
        self.X = (self.resize_x+(math.ceil(self.thickness/2)+self.gap))/3
        self.Y = 550
        while (self.running):
            try:
                self.pos = pygame.mouse.get_pos()
            except:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()

                if self.pos[0] > self.X and self.pos[0] < self.X + 240 and self.pos[1] > self.Y and self.pos[
                    1] < self.Y + 35:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        try:
                            self.running=False
                            self.Sorting=False
                            Process = StartProcess.START()
                            Process.start()

                            while(self.WaitForEndProcess):
                                pass

                            pygame.quit()
                            SortingAlgorithm.RunClock=True
                        except:
                            pass


    def draw(self):
        self.last = self.initial
        for i in range(len(self.array)):
            pygame.draw.line(self.screen, self.colours[i], (self.last, 0), (self.last, self.array[i]),self.thickness)
            self.last += self.difference

        if self.array == self.SortedArray:
            self.Sorting=False
            self.last = self.initial
            for i in range(len(self.array)):
                pygame.draw.line(self.screen, self.green, (self.last, 0), (self.last, self.array[i]),self.thickness)
                self.last += self.difference

            OperationsDone(self.Operations, self.screen,
                           (self.resize_x + (math.ceil(self.thickness / 2) + self.gap)) / 6 - 125, 450)
            SortingAlgorithm.RunClock=False


    def DrawBubbleSort(self):
        self.CurrentPosition=0
        while(self.Sorting):
            if self.CurrentPosition == self.NoOfElements -1:
                self.CurrentPosition=0
            self.Operations+=1
            if self.array[self.CurrentPosition] > self.array[self.CurrentPosition+1]:
                self.Operations+=1
                self.colours[self.CurrentPosition]=self.green
                self.colours[self.CurrentPosition+1]=self.red
                self.draw()
                if not self.running:
                    break
                time.sleep(1/self.Speed)

                self.colours[self.CurrentPosition] = self.black
                self.draw()
                self.array[self.CurrentPosition],self.array[self.CurrentPosition+1]=self.array[self.CurrentPosition+1],self.array[self.CurrentPosition]
                self.colours[self.CurrentPosition]=self.red
                self.colours[self.CurrentPosition+1] = self.green
                self.draw()
                if not self.running:
                    break
                time.sleep(1/self.Speed)

                self.colours[self.CurrentPosition] = self.white
                self.colours[self.CurrentPosition + 1] = self.white

            else:
                self.colours[self.CurrentPosition]=self.green
                self.colours[self.CurrentPosition+1]=self.green
                self.draw()
                if not self.running:
                    break
                time.sleep(1/self.Speed)

                self.colours[self.CurrentPosition] = self.white
                self.colours[self.CurrentPosition+1] = self.white
            self.CurrentPosition+=1
        self.WaitForEndProcess=False


    def DrawSelectionSort(self):
        self.CurrentPosition=0
        while(self.Sorting):
            self.min=min(self.array[self.CurrentPosition:])
            self.minPosition=0
            for i in range(self.CurrentPosition,self.NoOfElements):
                self.Operations+=1
                if self.array[i]==self.min:
                    self.minPosition=i
                self.colours[i] = self.blue
                self.draw()
                if not self.running:
                    break
                time.sleep(1/self.Speed)
                self.colours[i] = self.white
            self.Operations+=1
            if not self.running:
                break
            if self.CurrentPosition==self.minPosition:
                self.colours[self.minPosition]=self.green
                self.draw()
                time.sleep(1/self.Speed)
                self.colours[self.minPosition]=self.white
            else:
                self.colours[self.CurrentPosition]=self.red
                self.colours[self.minPosition]=self.green
                self.draw()
                time.sleep(1/self.Speed)
                self.colours[self.CurrentPosition] = self.black
                self.colours[self.minPosition] = self.white
                self.draw()
                self.array[self.CurrentPosition],self.array[self.minPosition]=self.array[self.minPosition],self.array[self.CurrentPosition]

                self.colours[self.CurrentPosition] = self.green
                self.colours[self.minPosition] = self.red
                self.draw()
                if not self.running:
                    break
                time.sleep(1/self.Speed)
                self.colours[self.CurrentPosition] = self.white
                self.colours[self.minPosition] = self.white

            self.CurrentPosition+=1
        self.WaitForEndProcess=False


    def DrawInsertionSort(self):
        self.CurrentPosition = 0
        while(self.Sorting):
            self.colours[self.CurrentPosition]=self.blue
            self.draw()
            time.sleep(1/self.Speed)
            self.colours[self.CurrentPosition]=self.white
            self.temp=self.array[self.CurrentPosition]
            i=self.CurrentPosition-1
            while(i>=0 and self.array[i]>self.temp):
                self.Operations+=1
                self.colours[i]=self.red
                self.draw()
                time.sleep(1/self.Speed)
                if not self.running:
                    break
                self.colours[i + 1] = self.black
                self.colours[i] = self.black
                self.draw()
                self.array[i+1]=self.array[i]
                self.colours[i]=self.red
                self.colours[i+1]=self.green
                self.draw()
                time.sleep(1/self.Speed)
                self.colours[i+1]=self.white
                self.colours[i]=self.white
                i-=1
            self.Operations+=1
            self.colours[i + 1] = self.black
            self.colours[i]  = self.black
            self.draw()
            self.colours[i + 1] = self.white
            self.colours[i] = self.white
            self.array[i+1] = self.temp
            if not self.running:
                break
            self.colours[i+1]=self.blue
            self.draw()
            time.sleep(1/self.Speed)
            self.colours[i+1]=self.white
            self.CurrentPosition+=1

        self.WaitForEndProcess=False


    def Heapify(self):
        for i in range(self.NoOfElements-1,-1,-1):
            while (2 * i + 1 < self.NoOfElements and (self.array[2 * i + 1] > self.array[i] or (2 * i + 2 < self.NoOfElements and self.array[2 * i + 2] > self.array[i]))):
                self.Operations+=1
                if 2 * i + 2 < self.NoOfElements:
                    if self.array[2 * i + 1] == max(self.array[2 * i + 1], self.array[2 * i + 2]):
                        self.colours[i]=self.red
                        self.colours[2*i+1]=self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1/self.Speed)
                        self.colours[2 * i + 1] = self.black
                        self.draw()
                        self.array[i], self.array[2 * i + 1] = self.array[2 * i + 1], self.array[i]
                        self.colours[2 * i + 1] = self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1/self.Speed)
                        self.colours[i] = self.white
                        self.colours[2 * i + 1] = self.white
                        self.draw()
                        i = 2 * i + 1

                    else:
                        self.colours[i] = self.red
                        self.colours[2 * i + 2] = self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1/self.Speed)
                        self.colours[2 * i + 2] = self.black
                        self.draw()
                        self.array[i], self.array[2 * i + 2] = self.array[2 * i + 2], self.array[i]
                        self.colours[2*i+2]=self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1/self.Speed)
                        self.colours[i] = self.white
                        self.colours[2 * i + 2] = self.white
                        self.draw()
                        i = 2 * i + 2
                else:
                    self.colours[i] = self.red
                    self.colours[2 * i + 1] = self.red
                    self.draw()
                    if not self.Sorting:
                        break
                    time.sleep(1 / self.Speed)
                    self.colours[2 * i + 1] = self.black
                    self.draw()
                    self.array[i], self.array[2 * i + 1] = self.array[2 * i + 1], self.array[i]
                    self.colours[2 * i + 1] = self.red
                    self.draw()
                    if not self.Sorting:
                        break
                    time.sleep(1 / self.Speed)
                    self.colours[i] = self.white
                    self.colours[2 * i + 1] = self.white
                    self.draw()
                    i = 2 * i + 1
            if not self.Sorting:
                break
        if not self.Sorting:
            self.WaitForEndProcess=False




    def DrawHeapSort(self):
        self.Heapify()
        j=self.NoOfElements
        while(self.Sorting):
            j-=1
            self.colours[0]=self.green
            self.colours[j]=self.red
            self.draw()
            if not self.Sorting:
                break
            time.sleep(1/self.Speed)
            self.colours[0]=self.black
            self.draw()
            self.Operations+=1
            self.array[j], self.array[0] = self.array[0], self.array[j]
            self.colours[j]=self.green
            self.colours[0]=self.red
            self.draw()
            self.colours[j] = self.white
            self.colours[0] = self.white
            if not self.Sorting:
                break
            time.sleep(1/self.Speed)
            i = 0
            while (2 * i + 1 < j and (self.array[2 * i + 1] > self.array[i] or (2 * i + 2 < j and self.array[2 * i + 2] > self.array[i]))):
                self.Operations+=1
                if 2 * i + 2 < j:
                    if self.array[2 * i + 1] == max(self.array[2 * i + 1], self.array[2 * i + 2]):
                        self.colours[i] = self.red
                        self.colours[2 * i + 1] = self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1 / self.Speed)
                        self.colours[2 * i + 1] = self.black
                        self.draw()
                        self.array[i], self.array[2 * i + 1] = self.array[2 * i + 1], self.array[i]
                        self.colours[2 * i + 1] = self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1 / self.Speed)
                        self.colours[i] = self.white
                        self.colours[2 * i + 1] = self.white
                        self.draw()
                        i = 2 * i + 1
                    else:
                        self.colours[i] = self.red
                        self.colours[2 * i + 2] = self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1 / self.Speed)
                        self.colours[2 * i + 2] = self.black
                        self.draw()
                        self.array[i], self.array[2 * i + 2] = self.array[2 * i + 2], self.array[i]
                        self.colours[2 * i + 2] = self.red
                        self.draw()
                        if not self.Sorting:
                            break
                        time.sleep(1 / self.Speed)
                        self.colours[i] = self.white
                        self.colours[2 * i + 2] = self.white
                        self.draw()
                        i = 2 * i + 2
                else:
                    self.colours[i] = self.red
                    self.colours[2 * i + 1] = self.red
                    self.draw()
                    if not self.Sorting:
                        break
                    time.sleep(1 / self.Speed)
                    self.colours[2 * i + 1] = self.black
                    self.draw()
                    self.array[i], self.array[2 * i + 1] = self.array[2 * i + 1], self.array[i]
                    self.colours[2 * i + 1] = self.red
                    self.draw()
                    if not self.Sorting:
                        break
                    time.sleep(1 / self.Speed)
                    self.colours[i] = self.white
                    self.colours[2 * i + 1] = self.white
                    self.draw()
                    i = 2 * i + 1
            if not self.Sorting:
                break
        self.WaitForEndProcess=False

    def merge(self,L,M,R):
        left_index=L
        right_index=M+1
        current=L
        if(not self.Sorting):
            return
        
        while(left_index<right_index and right_index<=R):
            self.Operations+=1
            if(not self.Sorting):
                return

            self.colours[left_index]=self.blue
            self.colours[right_index]=self.blue
            self.draw()
            time.sleep(1/self.Speed)
            
            if(self.array[left_index]<self.array[right_index]):
                if(not self.Sorting):
                    return

                self.colours[left_index]=self.white
                self.colours[right_index]=self.white
                self.draw()
                left_index+=1
            else:
                if(not self.Sorting):
                    return

                temp=right_index
                self.colours[left_index]=self.green
                self.colours[right_index]=self.red
                self.draw()
                
                time.sleep(1/self.Speed)
                
                self.colours[left_index]=self.white
                self.colours[right_index]=self.white
                self.draw()
                
                while(temp!=left_index):
                    if(not self.Sorting):
                        return
                    
                    self.colours[temp]=self.green
                    self.colours[temp-1]=self.red
                    self.draw()
                    time.sleep((1/self.Speed)/10)
                    
                    self.colours[temp]=self.black
                    self.colours[temp-1]=self.black
                    self.draw()
                    self.array[temp],self.array[temp-1]=self.array[temp-1],self.array[temp]
                    self.colours[temp]=self.white
                    self.colours[temp-1]=self.white
                    self.draw()
                    temp-=1
                    
                self.colours[left_index]=self.green
                self.colours[right_index]=self.red
                self.draw()
                time.sleep(1/self.Speed)
                
                self.colours[left_index]=self.white
                self.colours[right_index]=self.white
                self.draw()
                
                left_index+=1
                right_index+=1
            if(not self.Sorting):
                return
                    
    def MergeSort(self,left_ind,right_ind):
        
        if(not self.Sorting):
            return 

        if(right_ind!=left_ind):
            mid=(left_ind+right_ind)//2
            self.MergeSort(left_ind,mid)

            if(not self.Sorting):
                return
            self.MergeSort(mid+1,right_ind)

            if(not self.Sorting):
                return
            self.merge(left_ind,mid,right_ind)
            
    def DrawMergeSort(self):
        self.Speed*=3
        self.draw()
        self.MergeSort(0,len(self.array)-1)
        self.draw()
        self.WaitForEndProcess=False
