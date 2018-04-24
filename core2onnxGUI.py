import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename

# packages for convert models
from coremltools.models.utils import load_spec
from winmltools import convert_coreml
from winmltools.utils import save_model

import os.path

win = tk.Tk()
win.resizable(0,0)  ## fix size
win.title("CoreML to ONNX converter")

## Label for status
status_variable = tk.StringVar()
status_variable.set(">> Ready.")
status_label = tk.Label(win, textvariable=status_variable)

## label for filename
infile_label = tk.Label(win, text="Input Model (.mlmodel)")
outfile_label = tk.Label(win, text="Output Model (.onnx)")

## pathName for in and out
infile_name  = tk.StringVar()
outfile_name = tk.StringVar()
infile_entry  = tk.Entry(win, width=50, textvariable=infile_name )
outfile_entry = tk.Entry(win, width=50, textvariable=outfile_name)

### function to select input path
def selectInfile():
    _filename = askopenfilename(filetypes=[('CoreML model', '.mlmodel')])
    status_variable.set(">> Ready.")
    # check whether path is qualified
    infile_name.set(_filename)

### function to select output path
def selectOutfile():
    _filename = asksaveasfilename(filetypes=[('ONNX model', '.onnx')])
    status_variable.set(">> Ready.")
    outfile_name.set(_filename)

## button to select file and select output path
infile_button = tk.Button(win, text="Select File", command=selectInfile)
outfile_button = tk.Button(win, text="Select File", command=selectOutfile)

## convert function
def convertModel():
    coreML_name = infile_name.get()
    onnx_name   = outfile_name.get()

    if coreML_name == "":
        status_variable.set("\t (!) Input file doesn't exist.")
        return
    if onnx_name == "":
        status_variable.set("\t (!) Output file doesn't exist.")
        return

    ## check coreML_name
    if len(coreML_name) <= len(".mlmodel") or coreML_name[-len(".mlmodel"):] != ".mlmodel":
        status_variable.set("\t (!) File name error: \""+ coreML_name+ "\" is not a coreMLmodel. It's not ended with \".mlmodel\"")
        return

    ## check file exist
    if not os.path.isfile(coreML_name):
        status_variable.set("\t (!) File doesn't exist: \""+ coreML_name+ "\" does not exist, please provide another one.")
        return



    status_variable.set(">> load model from:" + coreML_name + "...")
    model_coreml = load_spec(coreML_name)

    status_variable.set(">> covert model...")
    model_onnx = convert_coreml(model_coreml)

    status_variable.set(">> save model to:" + onnx_name + "...")
    save_model(model_onnx, onnx_name)

    status_variable.set(">> Convert Finished! ")



## button for convert
convert_button = tk.Button(win, text="Convert", width=80, command=convertModel)

infile_label.grid(column=0, row=0, sticky="W")
outfile_label.grid(column=0, row=1, sticky="W")
infile_entry.grid(column=1, row=0)
outfile_entry.grid(column=1, row=1)
infile_button.grid(column=2, row=0)
outfile_button.grid(column=2, row=1)
convert_button.grid(column=0, row=2, columnspan=3, sticky="W", padx=5)
status_label.grid(column=0, row=3, columnspan=3, sticky="W")
win.grid_rowconfigure(2, pad=10)
win.grid_columnconfigure(2, pad=10)
win.mainloop()
