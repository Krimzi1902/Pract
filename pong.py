
canv_wd = 800          
canv_ht = 350

rack_wd = 10            
rack_ht = 60
right_pos = canv_wd - rack_wd 
rack_sp = 5             
leftrack_speed = 0     
rightrack_speed = 0

ball_rd = 30            
ball_spx = 5            
ball_spy = 5            
ballspeed_x = 3        
ballspeed_y = 5

center_x = canv_wd /2 - ball_rd / 2  
center_y = canv_ht /2 - ball_rd / 2

moveball_flag = 0       

from Tkinter import *
from random import randint
root = Tk()
canv = Canvas(root, height = canv_ht, width = canv_wd, bg='#006600')
canv.pack()


left_rack = canv.create_rectangle(0,0, rack_wd, rack_ht,fil = 'white')
right_rack = canv.create_rectangle(right_pos,0, canv_wd, rack_ht,fil = 'white')
canv.create_line(canv_wd/2,0, canv_wd/2, canv_ht,fil = 'white')
ball = canv.create_oval(center_x,center_y,center_x + ball_rd/2,center_y + ball_rd/2,fil = 'yellow')


left_count = 0
left_score = canv.create_text(canv_wd/2-40, 15, text=str(left_count), font="Arial 20", fill="white")
right_count = 0
right_score = canv.create_text(canv_wd/2+40, 15, text=str(right_count), font="Arial 20", fill="white")
 

def move_leftrack():
    if leftrack_speed > 0 and canv.coords(left_rack)[3] < canv_ht:
        canv.move( left_rack, 0, leftrack_speed)
    elif leftrack_speed < 0 and canv.coords(left_rack)[1] > 5:
        canv.move( left_rack, 0, leftrack_speed)

def move_rightrack():
    #print rightrack_speed
    if rightrack_speed > 0 and canv.coords(right_rack)[3] < canv_ht:
        canv.move( right_rack, 0, rightrack_speed)
    elif rightrack_speed < 0 and canv.coords(right_rack)[1] > 5:
        canv.move( right_rack, 0, rightrack_speed)


def move_ball():
    global ballspeed_x, ballspeed_y, moveball_flag, left_count, right_count 
    if moveball_flag > 0:
        if ballspeed_y > 0:
            
            y = canv.coords(ball)[3] + ballspeed_y
            if y > canv_ht:
                y = 2*canv_ht - y
                ballspeed_y = -ballspeed_y
            canv.move( ball, 0, y -canv.coords(ball)[3])    
        elif ballspeed_y < 0:
            
            y = canv.coords(ball)[1] + ballspeed_y
            if y < 0:
                y = - y
                ballspeed_y = -ballspeed_y
            canv.move( ball, 0, y - canv.coords(ball)[1])

        if ballspeed_x > 0:
            
            x = canv.coords(ball)[2] + ballspeed_x
            if x > right_pos:
                y_mid = (canv.coords(ball)[1] + canv.coords(ball)[3])/2
                if y_mid >= canv.coords(right_rack)[1] and y_mid <= canv.coords(right_rack)[3]:
                    
                    x = 2*right_pos - x
                    ballspeed_x = -ballspeed_x
                    canv.move( ball, x -canv.coords(ball)[2],0)
                else:
                    
                    left_count += 1
                    canv.itemconfig(left_score, text=str(left_count) )
                    canv.coords(ball, center_x, center_y,center_x + ball_rd/2,center_y + ball_rd/2)
                    ballspeed_x = randint(2,ball_spx)
                    moveball_flag = 0
            else:
                
                canv.move( ball, x -canv.coords(ball)[2],0)    
        elif ballspeed_x < 0:
            
            x = canv.coords(ball)[0] + ballspeed_x
            if x < rack_wd:
                
                y_mid = (canv.coords(ball)[1] + canv.coords(ball)[3])/2
                if y_mid >= canv.coords(left_rack)[1] and y_mid <= canv.coords(left_rack)[3]:
                   
                    x = 2*rack_wd - x
                    ballspeed_x = -ballspeed_x
                    canv.move( ball, x -canv.coords(ball)[2],0)
                else:
                    
                    right_count += 1
                    canv.itemconfig(right_score, text=str(right_count) )
                    canv.coords(ball,center_x,center_y,center_x + ball_rd/2,center_y + ball_rd/2)
                    ballspeed_x = -randint(2,ball_spx)
                    moveball_flag = 0
            else:
                
                canv.move( ball, x -canv.coords(ball)[0], 0)

def key_handl(event):
 
    global leftrack_speed, rightrack_speed, left_count, right_count, moveball_flag
  
    if  event.keysym == "space":   
        moveball_flag = 1
    elif event.keysym == "8":       
        rightrack_speed = -rack_sp
    elif event.keysym == "5":
        rightrack_speed = 0       
    elif event.keysym == "2":
        rightrack_speed = rack_sp
    elif event.keysym == "q":       
        leftrack_speed = -rack_sp   
    elif event.keysym == "a":
        leftrack_speed = 0       
    elif event.keysym == "z":
        leftrack_speed = rack_sp      
    elif event.keysym == "Return":  
        right_count = 0
        canv.itemconfig(right_score, text=str(right_count) )
        left_count  = 0
        canv.itemconfig(left_score, text=str(left_count) )
        canv.coords(ball,center_x,center_y,center_x + ball_rd/2,center_y + ball_rd/2)
        ballspeed_x = randint(3,6)
        ballspeed_y = randint(3,6)
        moveball_flag = 0
        main()

canv.bind("<KeyPress>", key_handl)
canv.focus_set()


def main():
    move_ball()
    move_leftrack()
    move_rightrack()
    root.after(30, main)
    
main()

root.mainloop()
