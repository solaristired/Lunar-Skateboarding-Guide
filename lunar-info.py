#First solo project that is unrelated to skateboarding. This should be talking about around skateboarding injuries to some basic stuff.



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def main_menu_window():
    main_menu_window = tk.Tk()
    title_label = tk.Label(main_menu_window, text= "Welcome to your main guide for skateboarding information", font=('Arial', 20))
    title_label.pack(pady = 20)
    main_menu_window.geometry('700x700')
    main_menu_window.title("Main Menu")

#Different button to bring the users in different sections
    mainbutton1 = tk.Button(main_menu_window, text = 'Types of Injuries', command = typesofinjury_window)
    mainbutton1.pack(expand = True)

    mainbutton2 = tk.Button(main_menu_window, text = 'Recovery', command = healing_window)
    mainbutton2.pack(expand = True)

    mainbutton3 = tk.Button(main_menu_window, text = 'Fun facts', command = funfacts_window)
    mainbutton3.pack(expand = True)

    main_menu_window.mainloop()

#The injury section to show three topics: Rolled Ankles, Sprained Wrists and Broken Bones
#There are also buttons to go into these sections and back buttons to go into the main menu
def typesofinjury_window():
    injury_window = tk.Toplevel()
    injury_window.geometry('700x700')
    injury_window.title("Types of injuries")
    
    injury_info= tk.Label(injury_window, text="The most common injuries are:",foreground="white", font =("Helvetica",22))
    injury_info.pack(pady = 20)
    
    injury_list = tk.Label(injury_window,
                           text="1. Rolled Ankles",
                           foreground="white",
                           font = ("Helvetica",22),
                           justify = 'left'
    )
    
    injury_list.pack(anchor = 'w',padx = 20, pady = 10)
    
    injury_list2 = tk.Label(injury_window,
                           text="2. Sprained Wrists",
                           foreground="white",
                           font = ("Helvetica",22),
                           justify = 'left'
    )
    
    injury_list2.pack(anchor = 'w',padx = 20, pady = 10)
    
    injury_list3 = tk.Label(injury_window,
                           text="3. Broken Bones",
                           foreground="white",
                           font = ("Helvetica",22),
                           justify = 'left'
    )
    

    injury_list3.pack(anchor = 'w',padx = 20, pady = 10)
    
    
    #Buttons here
    theanklesbutton = tk.Button(injury_window,text = "1. Ankle", command = Rolled_Ankle_window)
    theanklesbutton.pack(expand = True)
    
    wristbutton = tk.Button(injury_window, text ='2. Sprained Wrist', command = Sprained_Wrists_window)
    wristbutton.pack(expand = True)
    
    bonebutton = tk.Button(injury_window, text = '3. Bones', command = Broken_Bones)
    bonebutton.pack(expand = True)
    
    injurybackbutton = tk.Button(injury_window, text = 'Back', command = injury_window.destroy)
    injurybackbutton.pack(expand = True)
    
    
    injury_window.mainloop()

#The Ankle section which talks about how to deal with ankle injuries
def Rolled_Ankle_window():
    ankle_window = tk.Toplevel()
    ankle_window.geometry('700x700')
    ankle_window.title("Rolled Ankles")
        
    ankle_info= tk.Label(ankle_window, text="Ankle Injuries",foreground="white", font =("Helvetica",22))
    ankle_info.pack(pady = 20)
        
    anklepoint1 = tk.Label(ankle_window,
                        text ="- Ankle injuries are the worse. They can be something minor to deal with to something that may required doctor visits. However, they are super simple to treat with.",
                        foreground ="white",
                        font = ("Helvetica",16),
                        justify = 'left'
                          )
    
    anklepoint2 = tk.Label(ankle_window,
                        text ="- One step you can do is ice and rest. Most skaters understand to use ice on their ankle but some people still don't know. \nDepending on the injury or how bad you rolled it, you can notice your ankle swollen up. When this occurs it is crucial to put a ice pack on it so the swollen can go down.",
                        font = ("Helvetica",16),
                        justify = 'left'
                          )
    
    anklepoint3 = tk.Label(ankle_window,
                        text ="- For anything worse, it is recommdended to see medical help so you can get the proper care and recover. I hope to whoever is reading this has a speedy recovery.\nEven if you don't skate, I hope the best for you :).",
                        foreground ="white",
                        font = ("Helvetica",16),
                        justify = 'left'
                          )
    
    anklepoint1.pack(anchor = 'w',padx = 4, pady = 4)
    anklepoint2.pack(anchor = 'w',padx = 4, pady = 4)
    anklepoint3.pack(anchor = 'w',padx = 4, pady = 4)
    
    anklegobackbutton = tk.Button(ankle_window,text = "Back", command= ankle_window.destroy)
    anklegobackbutton.pack(expand = True)
        
    ankle_window.mainloop()

#Sprained Wrist section to talk about how to deal with wrist pains and everything.
def Sprained_Wrists_window():
    wrist_window = tk.Toplevel()
    wrist_window.geometry('700x700')
    wrist_window.title("Sprained Wrists")
    
    wrist_info= tk.Label(wrist_window, text="Wrist Injuries",foreground="white", font =("Helvetica",22))
    wrist_info.pack(pady = 20)
    
    wriststuff1 = tk.Label(wrist_window,
                        text ="- Wrist injuries  are a little bit easier to deal with in my opinion. The treatments are similar like a ankle injury (the ice pack is your best friend).",
                        foreground ="white",
                        font = ("Helvetica",16),
                        justify = 'left'
                          )
    
    wriststuff2 = tk.Label(wrist_window,
                        text ="- Some other ways to deal with this would be to invest into a brace. This was not mentioned in the Ankle injury section but a brace does help as your wrist is healing.\nDepending how bad your wrist is after the fall, you can be wearing a brace for a week to maybe a month(it also depends on your doctor too).",
                        foreground ="white",
                        font = ("Helvetica",16),
                        justify = 'left'
                          )
    

    wriststuff1.pack(anchor = 'w',padx = 4, pady = 4)
    wriststuff2.pack(anchor = 'w',padx = 4, pady = 4)
    
    
    wristgobackbutton = tk.Button(wrist_window, text = "Back", command= wrist_window.destroy)
    wristgobackbutton.pack(expand = True)
    
    wrist_window.mainloop()

#This section talks about bones and only has one bullet point
def Broken_Bones():
    bones_window = tk.Toplevel()
    bones_window.geometry('700x700')
    bones_window.title("Recovery")
    
    bones_dot = tk.Label(bones_window, text = "The most scariest injury.... A BROKEN BONE!",foreground = "white", font =("Helvetica", 22))
    bones_dot.pack(pady = 20)
    
    bones_dot= tk.Label(bones_window,
                         text = "- Broken bones are very serious. Accidents do happen to all of us in skateboarding or not. Go to the doctor and get some help on how to deal with it and some xrays.\n Take the time to rest up and make sure you're fully healed and get the thumbs up from your doctor to go back into skateboarding.",
                         font = ("Helvetica",16),
                         justify = 'left'
    )
    bones_dot.pack(anchor = 'w',padx = 4, pady = 4)
    
    bonesbackbutton = tk.Button(bones_window, text = "Back", command = bones_window.destroy)
    bonesbackbutton.pack(expand = True)
    
    bones_window.mainloop()
    
#Random space to give room between each sections

                         
#This is the healing section. These sections are Stretching, Ice and and Taking Breaks. In this section, there is also back buttons to go back to the main menu section
def healing_window():
    heal_window = tk.Toplevel()
    heal_window.geometry('700x700')
    heal_window.title("Recovery")
    
    heal_info= tk.Label(heal_window, text="Some ways to recover",foreground="white", font = ("Helvetica",22))
    heal_info.pack(pady = 20)
    
    heal_info1 = tk.Label(heal_window, 
                          text="1. Stretching/Yoga",
                          foreground="white",
                          font = ("Helvetica",22),
                          justify='left'
                          )

    heal_info1.pack(anchor = 'w',padx = 20, pady = 10)
    
    heal_info2 = tk.Label(heal_window, 
                          text="2. Ice",
                          foreground="white",
                          font = ("Helvetica",22),
                          justify='left'
                          )

    heal_info2.pack(anchor = 'w',padx = 20, pady = 10)
    
    heal_info3 = tk.Label(heal_window, 
                          text="3. Taking Breaks",
                          foreground="white",
                          font = ("Helvetica",22),
                          justify='left'
                          )

    heal_info3.pack(anchor = 'w',padx = 20, pady = 10)
    
    #Buttons here
    
    stretchbutton = tk.Button(heal_window, text = "1. Stretching", command = yoga_stretch)
    stretchbutton.pack(expand = True)
    
    icebutton = tk.Button(heal_window, text ='2. Ice', command = cool_ice)
    icebutton.pack(expand = True)
    
    breaktimebutton = tk.Button(heal_window, text = '3. Taking Breaks', command = break_time)
    breaktimebutton.pack(expand = True)
    
    recoverybackbutton = tk.Button(heal_window, text = 'Back', command = heal_window.destroy)
    recoverybackbutton.pack(expand = True)
    
    heal_window.mainloop()
    
    #The yoga/stretching section here talking about how to deal with stretching before a skate sesh
def yoga_stretch():
    yoga_window = tk.Toplevel()
    yoga_window.geometry('700x700')
    yoga_window.title("Stretches and Yoga")
        
    yoga_info = tk.Label(yoga_window, text = "Stretches", foreground = "white", font =("Helvetica", 22))
    yoga_info.pack(pady = 20)
    
    stretchpose = tk.Label(yoga_window,
                           text="- Not a lot skaters do stretches or yoga but it's quite useful.The reason I mention yoga is because a lot of skaters in recent times are starting to do it. Yoga in my opinion is extremely underrated in the skate world.",
                           foreground = "white",
                           font = ("Helvetica", 16),
                           justify='left'
    )
    stretchpose2 = tk.Label(yoga_window,
                            text = "- Some stretches that you can do before your skate sesh would be some leg and hip stretches.\n - Legs stretching will help your body feel quite more flexible instead of being stiff. \n - When it comes to hip stretches, a few tricks in skateboarding requires you turn with your body and you turn with using your arms and hips.",
                            foreground ="white",
                            font = ("Helvetica",16),
                            justify='left'
    )
    stretchpose3 = tk.Label(yoga_window,
                            text = "- There are also arms stretches some skaters can do. You can do the windmill arm rotations or cross arm stretches. \n My personal favorite is the cross arm stretches because you can do them at anytime throughout the day.",
                            foreground ="white",
                            font = ("Helvetica",16),
                            justify='left'
    )
    
    stretchpose.pack(anchor = 'w',padx = 4, pady = 4)
    stretchpose2.pack(anchor = 'w',padx = 4, pady = 4)
    stretchpose3.pack(anchor = 'w',padx = 4, pady = 4)
    
    stretchbackbutton = tk.Button(yoga_window, text = "Back", command = yoga_window.destroy)
    stretchbackbutton.pack(expand = True)
    
   
    yoga_window.mainloop()
    
    #Ice pack section. That's basically it. Nothing much to explain in this section
    
def cool_ice():
    ice_window = tk.Toplevel()
    ice_window.geometry('700x700')
    ice_window.title("Ice")
        
    ice_info = tk.Label(ice_window, text = "Ice", foreground = "white", font =("Helvetica", 22))
    ice_info.pack(pady = 20)
        
    icefunfact = tk.Label(ice_window,
                              text = "- This topic is very simple. As previously mentioned in the injury section, ice is your best friend. You don't need to get a massive ice pack but a small one that you can. \n You can put ice on anything that is swollen to sore. You don't have to fully keep the ice pack on for a long time but a few minutes will do the job.",
                              foreground ="white",
                              font =("Helvetica",16),
                              justify = 'left'
        )
        
    icefunfact.pack(anchor = 'w', padx = 20, pady = 10)
        
    icebackbutton = tk.Button(ice_window, text = "Back", command = ice_window.destroy)
    icebackbutton.pack(expand = True)
        
    ice_window.mainloop()
        
    
        
        
#This is a break information section. Enjoy your break in skating or just life
def break_time():
        break_window = tk.Toplevel()
        break_window.geometry('700x700')
        break_window.title("Rest")
        
        breakinformation = tk.Label(break_window, text = "Taking Breaks", foreground = "white",font = ("Helvetica", 22))
        breakinformation.pack(pady = 20)
        
        breakinfo1 = tk.Label(break_window,
                              text = "- This is going be super simple. REMEMBER TO TAKE BREAKS. PHYSICAL OR MENTAL BREAKS. \n Your body and mind matters. Take time to rest up.",
                              foreground ="white",
                              font =("Helvetica",16),
                              justify = 'left'
        )
        breakinfo1.pack(anchor ='w', padx = 20, pady = 10)
        
        breakbutton = tk.Button(break_window, text = "Back", command = break_window.destroy)
        breakbutton.pack(expand = True)
        
# A random fun fact window section
def funfacts_window():
        fun_window = tk.Toplevel()
        fun_window.geometry('700x700')
        fun_window.title("Fun facts")
    
        fun_info = tk.Label(fun_window,text ="Random Fun Facts", foreground = "white", font = ("Helvetica", 22))
        fun_info.pack(pady = 20)
    
        funfacts_dot = tk.Label(fun_window,
                           text="- A lot of colleges in recent times are starting to create skateboarding clubs for the community. Montclair State University and NJIT one.",
                           foreground="white",
                           font = ("Helvetica",16),
                           justify = 'left'
                           )
        funfacts2_dot = tk.Label(fun_window,
                           text="- Skateboarding takes a lot of patience and time. Learning tricks are going take time to do and master. Remember to have fun in skateboarding and don't rush progress.",
                           foreground="white",
                           font = ("Helvetica",16),
                           justify = 'left'
                           )
        
        funfacts_dot.pack(anchor = 'w', padx = 4, pady = 4)
        funfacts2_dot.pack(anchor = 'w', padx = 4, pady = 4)
        
        funbutton= tk.Button(fun_window, text = 'Back', command = fun_window.destroy)
        funbutton.pack(expand = True)
    
        fun_window.mainloop()  
    

if __name__ == "__main__":
    main_menu_window()

#Most of the code is repetitive but is super easy to read and understand it.