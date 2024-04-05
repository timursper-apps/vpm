from tkinter import *
from tkinter import ttk
from tkinter import simpledialog

root = Tk()
root.title("VisualProgrammMaker")
root.resizable(False, False)
root.geometry("300x300")

def selected(x = 0):
    select = commands_cb.get()

    if select == "Add var":
        var_name = simpledialog.askstring("Var settings", "Enter your var name")
        var_value = simpledialog.askstring("Var settings", "Enter var value (for text use: \"\")")
        code.insert(END, f"{var_name} = {var_value}\n")
    elif select == "Add output":
        output_text = simpledialog.askstring("Output settings", "What do you want to output? (For text use \"\", for variables you don't need for \"\")")
        code.insert(END, f"print({output_text})\n")
    elif select == "Add input":
        input_ask = simpledialog.askstring("Input settings", "What do you want to ask? (you don't need to type \"\")")
        input_var = simpledialog.askstring("Input settings", "What variable name do you want to store the input value?")
        code.insert(END, f"{input_var} = input({input_ask})\n")
    elif select == "Add function":
        function_name = simpledialog.askstring("Function settings", "Enter a function name")
        function_args = simpledialog.askstring("Function settings", "Enter a function args")

        code.insert(END, f"def {function_name}({function_args}):\n  ")
    elif select == "Call function":
        function_name = simpledialog.askstring("Function settings", "Enter a function name")
        function_args = simpledialog.askstring("Function settings", "Enter a function args")

        code.insert(END, f"{function_name}({function_args})")


cmds = ["Add var", "Add output", "Add input", "Add function", "Call function"]

commands_cb = ttk.Combobox(root, values=cmds)
commands_cb.place(x=0, y=0, width=300)

code = Text(root)
code.place(x=0, y=20, width=300, height=280)

commands_cb.bind("<<ComboboxSelected>>", selected)

root.mainloop()
