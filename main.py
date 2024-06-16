from tkinter import *    #imports
from tkinter import filedialog
import tkinter as tk
from tkinter import scrolledtext
from tkinter import colorchooser
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo
import webbrowser
import os

#main window
root = Tk()
root.title("WSengine 2.0")
root.geometry("1000x800")
toolbar = Menu(root)


def exit():#exit function
    root.destroy()

def clear_all():#clear all text content function
    mainhtmlCodeInputField.delete("1.0", tk.END)

def paste():#paste text function
     content = root.clipboard_get()
     mainhtmlCodeInputField.insert(tk.END, content)

def pasteOnMousebtn(event):#paste text on mouse button
    text = root.clipboard_get()
    cursor_position = mainhtmlCodeInputField.index(tk.INSERT)
    mainhtmlCodeInputField.insert(cursor_position, text)

def copy():
    root.clipboard_append(mainhtmlCodeInputField.get('1.0', tk.END).rstrip())

def save():# save mainn window function
    saving_content = mainhtmlCodeInputField.get("1.0", "end")
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(saving_content)

def simpleSave():
    code = mainhtmlCodeInputField.get("1.0", "end")
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)    

def openTextFile():#open txt file main window function
    file_path = filedialog.askopenfilename(filetypes=[("TEXT files", "*.txt")])
    with open(file_path, "r", encoding="utf-8") as file:
        text_content = file.read()
        mainhtmlCodeInputField.insert(tk.END, text_content)

def openHtmlFile():#open html file main window function
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        mainhtmlCodeInputField.insert(tk.END, html_content)

def viewprojectinBrowser():
    content = mainhtmlCodeInputField.get("1.0", tk.END)
    with open(f"output.html", "w") as file:
        file.write(content)
    webbrowser.open("output.html")

def delete():
    os.remove("output.html")

def colorPicker():#colorpicker widget window 
    colorroot = Tk()
    colorroot.geometry("300x300")
    colorroot.title("WSengine colorpicker")
    colorroot.resizable(0,0)
    def colorIndikatorFunction():
        color = colorchooser.askcolor(title="choose color")
        color_code = color[1]
        colorIndikator.config(bg=color_code)
        colorcode.insert(0, color_code)
    colorIndikator = Label(colorroot, width=20, height=10, bg="gray")
    colorIndikator.pack()
    Label(colorroot, text="color code:", font="Verdana").pack()
    colorcode = Listbox(colorroot, width=20, height=1)
    colorcode.pack()
    btnChoosecolor = Button(colorroot, text="select color", font="Bold", command=colorIndikatorFunction)
    btnChoosecolor.pack()
    btnCopycolorcode = Button(colorroot, text="copy color code", font="Bold")
    btnCopycolorcode.pack()
    colorroot.mainloop()

def createJs():# js file script window
    jsroot = Tk()
    jsroot.geometry("1000x800")
    jsroot.title("WSengine create js script file")

    def exit():
        jsroot.destroy()

    def openJsFile():
        file_path = filedialog.askopenfilename(filetypes=[("JS files", "*.js")])
        with open(file_path, "r", encoding="utf-8") as file:
            js_content = file.read()
            jsScriptInputField.insert(tk.END, js_content)

    def saveJs():# save js window function
        saving_content = jsScriptInputField.get("1.0", "end")
        file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("JS files", "*.js")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(saving_content)

    jsScriptInputField = scrolledtext.ScrolledText(jsroot, width=500, height=500)
    jsScriptInputField.pack()
    jstoolbar = Menu(jsroot)
    jsfile = Menu(jsroot, tearoff=0)
    jstoolbar.add_cascade(label="File", menu=jsfile)
    jsfile.add_command(label="save as", command=saveJs)
    jsfile.add_command(label="import txt", command=openTextFile)
    jsfile.add_command(label="import js", command=openJsFile)
    jsfile.add_command(label="exit", command=exit)
    jsedit = Menu(root, tearoff=0)
    jstoolbar.add_cascade(label="Edit", menu=jsedit)
    jsedit.add_command(label="clear all", command=clear_all)
    jsedit.add_command(label="paste", command=paste)
    jsedit.add_command(label="copy", command=copy)
    jsroot.config(menu=jstoolbar)
    jsroot.mainloop()
    
def createCss():
    cssroot = Tk()
    cssroot.geometry("1000x800")
    cssroot.title("WSengine create css styles file")

    def saveCss():
        saving_content = cssInputField.get("1.0", "end")
        file_path = filedialog.asksaveasfilename(defaultextension=".css", filetypes=[("CSS files", "*.css")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(saving_content)

    def openCssFile():
        file_path = filedialog.askopenfilename(filetypes=[("CSS files", "*.css")])
        with open(file_path, "r", encoding="utf-8") as file:
            css_content = file.read()
            cssInputField.insert(tk.END, css_content)

    cssInputField = scrolledtext.ScrolledText(cssroot, width=500, height=500)
    cssInputField.pack()
    csstoolbar = Menu(cssroot)
    cssfile = Menu(cssroot, tearoff=0)
    csstoolbar.add_cascade(label="File", menu=cssfile)
    cssfile.add_command(label="save as", command=saveCss)
    cssfile.add_command(label="import txt", command=openTextFile)
    cssfile.add_command(label="import css", command=openCssFile)
    cssfile.add_command(label="exit", command=exit)
    cssedit = Menu(root, tearoff=0)
    csstoolbar.add_cascade(label="Edit", menu=cssedit)
    cssedit.add_command(label="clear all", command=clear_all)
    cssedit.add_command(label="paste", command=paste)
    cssedit.add_command(label="copy", command=copy)
    cssroot.config(menu=csstoolbar)
    cssroot.mainloop()


#main window input code field
mainhtmlCodeInputField = scrolledtext.ScrolledText(root, width=500, height=500)
mainhtmlCodeInputField.pack()
mainhtmlCodeInputField.bind("<Button-3>", pasteOnMousebtn)

#main window toolbar
file = Menu(root, tearoff=0)
toolbar.add_cascade(label="File", menu=file)
file.add_command(label="save", command=simpleSave)
file.add_command(label="save as", command=save)
file.add_command(label="import txt", command=openTextFile)
file.add_command(label="import html", command=openHtmlFile)
file.add_command(label="exit", command=exit)
edit = Menu(root, tearoff=0)
toolbar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="clear all", command=clear_all)
edit.add_command(label="paste", command=paste)
edit.add_command(label="copy", command=copy)
actions = Menu(root, tearoff=0)
toolbar.add_cascade(label="Actions", menu=actions)
actions.add_command(label="create css file", command=createCss)
actions.add_command(label="create js file", command=createJs)
actions.add_command(label="открыть colorpicker", command=colorPicker)
functions = Menu(root, tearoff=0)
toolbar.add_radiobutton(label="launch in webbrowser", command=viewprojectinBrowser)
toolbar.add_radiobutton(label="remove output.html")


root.config(menu=toolbar)
root.mainloop()
