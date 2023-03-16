import PySimpleGUI as sg
label=sg.Text(" Enter the message")
input=sg.InputText(tooltip="Enter here")
add_button=sg.Button("submit")

window=sg.Window(" this is my Python App",layout=[[label,input],[add_button]])
window.read()
window.close()