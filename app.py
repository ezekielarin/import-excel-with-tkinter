import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import numpy as np
import math
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename, asksaveasfilename
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

 
window = tk.Tk()
window.title("Well Testt")
window.geometry("1900x800")
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Draw Down')
tabControl.add(tab2, text ='Build UP')
tabControl.add(tab3, text ='DST')
tabControl.add(tab4, text ='Injectory')
tabControl.pack(expand = 1, fill ="both")

 

drawdown_count = 0
buildup_count = 0




#ttk.Label(tab2, text =" ").grid(column = 0, row = 0,padx = 30, pady = 30)

############ Frames for tab 1

top_frame = Frame(tab1, bg='cyan', width=450, height=50, pady=3)

center_l1 = Frame(tab1, bg='grey', width=20, height=25, padx=3, pady=3)
center = Frame(tab1, bg='grey', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(tab1, bg='white', width=450, height=45, pady=3)
 


# layout all of the main containers
tab1.grid_rowconfigure(1, weight=1)
tab1.grid_columnconfigure(0, weight=2)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")



############ Frames for tab 2
top_frame2 = Frame(tab2, bg='cyan', width=450, height=50, pady=3)
center2 = Frame(tab2, bg='grey', width=50, height=40, padx=3, pady=3)
btm_frame2= Frame(tab2, bg='white', width=450, height=45, pady=3)
btm_frame22 = Frame(tab2, bg='lavender', width=450, height=60, pady=3)

#ttk.Label(top_frame2, text ="Draw Down").grid(column = 0, row = 0,padx = 30, pady = 30)


# layout all of the main containers
tab2.grid_rowconfigure(1, weight=1)
tab2.grid_columnconfigure(0, weight=2)

top_frame2.grid(row=0, sticky="ew")
center2.grid(row=1, sticky="nsew")
#btm_frame2.grid(row=3, sticky="ew")
btm_frame22.grid(row=4, sticky="ew")


############ Frames for tab 3
top_frame3 = Frame(tab3, bg='cyan', width=450, height=50, pady=3)
center3 = Frame(tab3, bg='grey', width=50, height=40, padx=3, pady=3)
btm_frame3= Frame(tab3, bg='white', width=450, height=45, pady=3)
btm_frame23 = Frame(tab3, bg='lavender', width=450, height=60, pady=3)

ttk.Label(top_frame3,text ="Drop Down").grid(column = 0,row = 0, padx = 30, pady = 30)

# layout all of the main containers
tab3.grid_rowconfigure(1, weight=1)
tab3.grid_columnconfigure(0, weight=2)

top_frame3.grid(row=0, sticky="ew")
center3.grid(row=1, sticky="nsew")
#btm_frame3.grid(row=3, sticky="ew")
btm_frame23.grid(row=4, sticky="ew")


############ Frames for tab 4
top_frame4 = Frame(tab4, bg='cyan', width=450, height=50, pady=3)
cent1 = Frame(tab4, bg='blue', width=20, height=40, padx=3, pady=3)
cent2 = Frame(tab4, bg='grey', width=20, height=40, padx=3, pady=3)
cent3 = Frame(tab4, bg='white', width=20, height=40, padx=3, pady=3)
cent4 = Frame(tab4, bg='grey', width=20, height=40, padx=3, pady=3)

btm_frame4= Frame(tab4, bg='white', width=450, height=45, pady=3)
btm_frame24 = Frame(tab4, bg='lavender', width=450, height=60, pady=3)

ttk.Label(top_frame4,
		text ="Draw Down").grid(column = 0,
							row = 0,
							padx = 30,
							pady = 30)

# layout all of the main containers
tab4.grid_rowconfigure(1, weight=1)
tab4.grid_columnconfigure(0, weight=2)

top_frame4.grid(row=0, sticky="ew")
cent1.grid(row=1, sticky="nsew")
cent2.grid(row=2, sticky="ns")
cent3.grid(row=1, sticky="ew")
cent4.grid(row=2, sticky="nsew")
btm_frame4.grid(row=3, sticky="ew")
btm_frame24.grid(row=4, sticky="ew")



############ Tab 1

new_button = ttk.Button(top_frame, text='Import Data', command  = lambda: select_file('drawdown'))
#new_button.pack()
new_button.grid(column=0, row=1, sticky=tk.W, padx=5, pady=0)

new_button = ttk.Button(top_frame, text='plot Log', command  = lambda: drawdown_popwin())
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

new_button = ttk.Button(top_frame, text='clear', command  = lambda: clear_canvas())
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)


##########  tab 2

new_button = ttk.Button(top_frame2, text='Import Data', command  = lambda: select_file('buildup'))
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

new_button = ttk.Button(top_frame2, text='new', command  = lambda: create_input_frame(window))
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

new_button = ttk.Button(top_frame2, text='new', command  = lambda: create_input_frame(window))
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)



############## tab3


new_button = ttk.Button(tab3, text='new', command  = lambda: create_input_frame(window))
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

new_button = ttk.Button(tab3, text='new', command  = lambda: create_input_frame(window))
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

new_button = ttk.Button(tab3, text='new', command  = lambda: create_input_frame(window))
#new_button.pack(ipadx=0,ipady=5,expand=True)
new_button.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)



def popwin():
    top = Toplevel(window)
    top.geometry("350x300")
    top.title("Collect Data")

    label = Label(top, text='Enter your Data')
    label.pack(ipadx=10, ipady=10)


    adfd_label = ttk.Label(top, text="sigma value:")
    adfd_label.pack()

    adfd = Entry(top)
    adfd.pack()

    open_button = ttk.Button(top,text='Select a File', command=select_file)
    open_button.pack(expand=True)

   # submit = ttk.Button(top, text='Submit', command=lambda: popwin())
   # submit.grid(column=0, row=0, sticky=tk.W)
    submit.pack()

    pass


def drawdown_popwin(data):
    top = Toplevel(window)
    top.geometry("800x500")
    top.title("Draw Down Graph")
    
   # body = Frame(top, bg='grey', width=50, height=40, padx=3, pady=3)
   # btm_body = Frame(top, bg='white', width=450, height=45, pady=3)
    #body.grid(row=1, sticky="nsew")
   # btm_body.grid(row=3, sticky="ew")
     


     
    pi = data['pi'].values[0]

    data['log_time'] = np.log(data.time);
    data['dp'] = data.pressure - pi;
    
    if 'dt' not in data:
        data['dt'] = data.time
    
    fig = Figure(figsize = (200, 200), dpi = 80);
    t = data.loc[:,"time"]; 
    log_t = data.loc[:,"log_time"]; 
    dp = data.loc[:,"dp"]
    p = data.loc[:,"pressure"]; 
    

    plot1 = fig.add_subplot(221); 
    plot1.title.set_text('Semi Log Plot');
    plot1.grid(True, which="both")
    plot1.semilogx(t,p)
    plot1.scatter(t,p)
    #semilog slope
    slope, intercept = np.polyfit(t, dp, 1)
    
    plot2 = fig.add_subplot(222);
   # plot2.plot(log_t, p); 
    plot2.scatter(t, p)
    plot2.grid(True, which="both")
    plot2.title.set_text('Cartesian Plot')
    #cartesian slope
    slope, intercept = np.polyfit(t, dp, 1)
     
    plot3 = fig.add_subplot(223)
    plot3.loglog();
    plot3.scatter(t,dp);
    plot3.grid(True, which="both")
    plot3.title.set_text('MDH Log log'); 
    #log log slope
    slope, intercept = np.polyfit(t, dp, 1)
   

    
    
    print(slope)
    print(intercept)
    
    
    canvas = FigureCanvasTkAgg(fig, master = top);
    canvas.draw()
    
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, top)
    toolbar.update()
    canvas.get_tk_widget().pack()
    

    pass


def buildup_popwin(data):
    top = Toplevel(window)
    top.geometry("800x500")
    top.title("Buildup Graph")
    
   # body = Frame(top, bg='grey', width=50, height=40, padx=3, pady=3)
   # btm_body = Frame(top, bg='white', width=450, height=45, pady=3)
    #body.grid(row=1, sticky="nsew")
   # btm_body.grid(row=3, sticky="ew")
     
    Qo = 1
    Uo = 1
    ct = 1
    rw = 1
    h = 1;
    np=1
   

    pi = data['pi'].values[0]
    psi = data['psi'].values[0]
    Ti = data['time'].values[0]
   
   
   
    data['dp'] = data.pressure - psi;
  

    t = data.loc[:,"time"];
    data['log_time'] = t;
   
    dp = data.loc[:,"dp"]; 
  
    p = data.loc[:,"pressure"]; 
   
    if 'tp' not in data:
       data['tp'] = t;
       
    if 'np' not in data:
       data['dt'] = data.loc[:,"time"];
       
    tp = data.loc[:,"tp"]; 
    data['dt'] = tp-Ti 
    dt = data.loc[:,"dt"];

    tpdt = (tp+dt)/dt;
  


    fig = Figure(figsize = (200, 200), dpi = 80); 
   # print(dd_data)
    semi_log = fig.add_subplot(221); 
   
    semi_log.title.set_text('Horners plot - Semi Log Plot');
  # semi_log.semilogx(t, p); 
    semi_log.scatter(tpdt,p);  
    semi_log.grid(True, which="both")
   
    plot2 = fig.add_subplot(222);
    plot2.loglog(); 
    plot2.scatter(t,dp); 
    plot2.title.set_text('Log-log Plot'); 
    plot2.grid(True, which="both")
   
   #plot3 = fig.add_subplot(223)
  # plot3.semilogy(t,p);
  # plot3.grid(True, which="both")
  # plot3.title.set_text('semi log'); #

    
    
    
    canvas = FigureCanvasTkAgg(fig, master = top);
    canvas.draw()
    
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, top)
    toolbar.update()
    canvas.get_tk_widget().pack()
    

    pass

def select_file(graph):
    filetypes = (
        ('csv', '*.csv'),
        ('excel', '*.xlsx'),
       
    )
    global dd_data
   
    
    
    filename = fd.askopenfilename(
        title='Open a file', initialdir='/documents', filetypes=filetypes)
    #df = pd.read_csv(filename)
  #  headers = ['time', 'pressure']
    
    df = pd.read_excel(filename)
    dd_data = df
   
    global drawdown_count
    global buildup_count
    print(drawdown_count)

    if(graph=="drawdown"):
        
        if(drawdown_count==0):
            draw_down_plot(df)
           
            drawdown_count = 1
            
        else:
            drawdown_popwin(df)
           
        
    if(graph=="buildup"):
        
        if(buildup_count==0):
            buildup_plot(df)
           
            buildup_count = 1
            
        else:
           buildup_popwin(df)
        
        
   # file_dir+filename


def draw_down_plot(data):

    
    pi = data['pi'].values[0]

    data['log_time'] = np.log(data.time);
    data['dp'] = data.pressure - pi;
    
    if 'dt' not in data:
        data['dt'] = data.time
    
    fig = Figure(figsize = (200, 200), dpi = 80);
    t = data.loc[:,"time"]; 
    log_t = data.loc[:,"log_time"]; 
    dp = data.loc[:,"dp"]
    p = data.loc[:,"pressure"]; 
    

    plot1 = fig.add_subplot(221); 
    plot1.title.set_text('Semi Log Plot');
    plot1.grid(True, which="both")
    plot1.semilogx(t,p)
    plot1.scatter(t,p)
    
    plot2 = fig.add_subplot(222);
   # plot2.plot(log_t, p); 
    plot2.scatter(t, p)
    plot2.grid(True, which="both")
    plot2.title.set_text('Cartesian Plot'); 
     
    plot3 = fig.add_subplot(223)
    plot3.loglog();
    plot3.scatter(t,dp,);
    plot3.grid(True, which="both")
    plot3.title.set_text('MDH Log log'); #
    
   # np.polyfit(t,p, '--')
    slope, intercept = np.polyfit(t, dp, 1)
    print(slope)
    
    
    canvas = FigureCanvasTkAgg(fig, master = center);
    canvas.draw()
    
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, center)
    toolbar.update()
    canvas.get_tk_widget().pack()
	

######## log log plot
def buildup_plot(data):
    
  
   Qo = 1
   Uo = 1
   ct = 1
   rw = 1
   h = 1;
   np=1
   

   pi = data['pi'].values[0]
   psi = data['psi'].values[0]
   Ti = data['time'].values[0]
   
   
   
   data['dp'] = data.pressure - psi;
  

   t = data.loc[:,"time"];
   data['log_time'] = t;
   
   dp = data.loc[:,"dp"]; 
  
   p = data.loc[:,"pressure"]; 
   
   if 'tp' not in data:
       data['tp'] = t;
       
   if 'np' not in data:
       data['dt'] = data.loc[:,"time"];
       
   tp = data.loc[:,"tp"]; 
   data['dt'] = tp-Ti 
   dt = data.loc[:,"dt"];

   tpdt = (tp+dt)/dt;
  


   fig = Figure(figsize = (200, 200), dpi = 80); 
   print(dd_data)
   semi_log = fig.add_subplot(221); 
   
   semi_log.title.set_text('Horners plot - Semi Log Plot');
  # semi_log.semilogx(t, p); 
   semi_log.scatter(tpdt,p);  
   semi_log.grid(True, which="both")
   
   plot2 = fig.add_subplot(222);
   plot2.loglog(); 
   plot2.scatter(t,dp); 
   plot2.title.set_text('Log-log Plot'); 
   plot2.grid(True, which="both")
   
   #plot3 = fig.add_subplot(223)
  # plot3.semilogy(t,p);
  # plot3.grid(True, which="both")
  # plot3.title.set_text('semi log'); #
   
  
   
   canvas = FigureCanvasTkAgg(fig, master = center2);
   canvas.draw()
   
   canvas.get_tk_widget().pack()
   toolbar = NavigationToolbar2Tk(canvas, center2)
   toolbar.update()
   canvas.get_tk_widget().pack()
 
    
def clear_canvas():
    center.pack_forget()
    
    pass
        

def calculate_pressure():

    k = 2  #permeability
    t = 2  #time, hour
    s = 3  #skin factor
    
    Qo = 1
    Uo = 1
    ct = 1
    rw = 1
    h = 1;
    pi = 2
    Pwf = pi - ((162.6*Qo*Bo*Uo)/k*h)(log(k*t/O*U*ct*rwˆ2)-3.23+0.87*s)
    return Pwf

#plot graph with this function
def abline(slope, intercept, graph):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

window.mainloop()
