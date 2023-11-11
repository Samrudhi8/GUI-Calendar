#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install tkinter


# In[4]:


from tkinter import *
import calendar


# In[5]:


def showCalender():
    gui = Tk()
    gui.config(background='black')
    gui.title("GUI Calendar")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Montsserat 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()


# In[9]:


if __name__=='__main__':
    new = Tk()
    new.config(background='black')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calender",bg='black',font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',fg='Black',bg='Blue',command=showCalender)


# In[10]:


cal.grid(row=1, column=1)
year.grid(row=2, column=1)
year_field.grid(row=3, column=1)
button.grid(row=4, column=1)
new.mainloop()


# In[ ]:




