import time
import pyautogui 
import cv2

#locate the center of the image on the screen
#res=pyautogui.locateCenterOnScreen("game_icon3.png")
#res = pyautogui.locateCenterOnScreen(r"C:\Users\d-mon\OneDrive\Desktop\MPQScript\game_icon.png")

#print(res)


#Bot that automatically opens the vault 

#pyautogui.moveTo(res)
#pyautogui.doubleClick(res) 
    

#time.sleep(7)
VTabx=2250
VTaby=250
RTabx=700
RTaby=100
STabx=2250
STaby=800
swipes=14

#scrollspeed= input('How fast do you want it to scrooll')

def RecruitHeroes():
    pyautogui.moveTo(RTabx,RTaby)
#time.sleep(1)
#res5=pyautogui.locateCenterOnScreen("recruit.png")
    pyautogui.click(700,100)

def GoToVaultsTab():
    pyautogui.moveTo(VTabx,VTaby)
    pyautogui.click(VTabx,VTaby)

def ScrolltoSweetVault():
   pyautogui.moveTo(STabx,STaby)
   pyautogui.scroll(-50)

def ScrolltoSweetVault2():
    # Move the mouse to the starting point
    pyautogui.moveTo(STabx, STaby)  # Replace with the coordinates of your Vaults screen
    for _ in range(swipes):
    # Move to the starting position before each drag
        pyautogui.moveTo(STabx, STaby)
    
    # Drag to simulate scrolling (e.g., scroll down)
        pyautogui.dragRel(0, -300, duration=0.5)  # Drag up to scroll down
    
    # Optional: Add a delay to avoid rapid scrolling
        time.sleep(0.5)

def GetCovers():
    pyautogui.click(cover_icon,)

RecruitHeroes()
GoToVaultsTab()
ScrolltoSweetVault2()
time.sleep(1)
cover_icon=pyautogui.locateOnScreen("get_covers2.png",confidence=0.8)
pyautogui.moveTo(cover_icon)
GetCovers()
