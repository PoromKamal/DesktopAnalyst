from tkinter import * 
from tkinter import Entry, Text
from analyze import *
from deep_analysis import *
import tkinter as tk


def setOutput(txt):
    """
    Sets the output box text, by enabling the textbox,
    entering the text, and disabling.
    """
    output_text.configure(state = 'normal')
    output_text.insert(END, txt)
    output_text.configure(state = 'disabled')
def clearOutput():
    """
    Deletes all the text in the output box
    """
    output_text.configure(state = 'normal')
    output_text.delete('1.0', END)
    output_text.configure(state = 'disabled')
def startAnalysis():
    """
    Starts simple analysis, and outputs data to the output box.
    """

    #Clear the text in the output box first.
    clearOutput()
    tick = yf.Ticker(input_box.get())

    #Get the ticker info
    info = tick.info
    setOutput('BASIC INFO:\n')

    #output basic info, basic info documentation can be found in analyze.py
    setOutput(basicInfo(info))
    setOutput('\n-----------------------------------\n')
    setOutput('RATIO ANALYSIS:\n')
    
    #output ratio info, ratioInfo documentation can be found in analyze.py
    setOutput(ratioInfo(info))
    setOutput('\n-----------------------------------\n')
    overall_summary = summary(info)
    setOutput('Summary:\n')

    #Output the summary, summaryInfo can be found in analyze.py
    setOutput(overall_summary[0])

    #Output an overall recommendation based on the financial statistics:
    setOutput('-----------SCROLL FOR TLDR RECOMENDATION-----------\n')
    #Check overall score for the stock
    if overall_summary[1] == 8:
        setOutput(f"At this moment {info['shortName']} has average financial statistics.")
    elif overall_summary[1] < 8:
        setOutput(f"At this moment {info['shortName']} has below average financial statistics,\nin comparison to its competitors.")
    else:
        setOutput(f"At this moment {info['shortName']} has great financial statistics,\nin the {info['sector']} sector.")

def report_container():
    """
    Container for the event of outputting a deep analysis report.
    """
    tick = yf.Ticker(input_box.get())
    #report() documentation can be found in the deep_analysis.py file.
    report(tick)
    
    

#Initialize the window, and title
root = Tk()
root.geometry("700x800")
root.title("Desktop Analyst")
root.resizable(False, False)
root.configure(bg = 'deep sky blue')
#Set the banner,
bannerImage = PhotoImage(file = 'banner3.gif')
banner = Label(root, image=bannerImage, height = 100, width= 700, borderwidth= 3, relief= 'solid' )
banner.pack(side= "top")
#Set instructional labels
inst_label= Label(root, text= "Enter a valid Ticker symbol below")
inst_label.pack(side = 'top')

#Set text for Desktop Analyst
app_title = Label(root, text= 'Desktop Analyst', font=('Terminal', 23), bg = 'deep sky blue', borderwidth= 2, relief= SOLID)
app_title.pack()
app_title.place(relx = 0.25, rely = 0.05)

#Set the textboxs
input_box = Entry(root, width = 30)
input_box.pack(pady = 5)


#Set analyze button button
buttonFrame = Frame(root)
buttonFrame.pack(side = "top")
analyzeButton =  Button(buttonFrame, text = "Analyze!", fg = 'Blue', command= lambda:startAnalysis(), width= 16)
analyzeButton.pack()

#Set deep analysis button
deep_analyzeButton = Button(buttonFrame, text = "Detailed Report (.txt)", fg = 'purple', command= lambda: report_container())
deep_analyzeButton.pack()
#Create output box:
output_text = Text(root, width = 80, height = 36, bg= 'black', fg = 'white')
output_text.configure(state = 'disabled')
output_text.pack(side = 'top')
root.mainloop()