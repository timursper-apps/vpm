from tkinter import *
from tkinter import ttk
from tkinter import simpledialog

root = Tk()
root.title("VisualProgrammMaker")
root.resizable(False, False)
root.geometry("300x300")

ru = {
    "Var settings":"Настройка переменной",
    "Enter your var name":"Введите имя вашей переменной",
    "Enter var value (for text use: \"\")":"Введите значение переменной (для текста используйте кавычки)",
    "Output settings":"Настройки вывода",
    "What do you want to output? (For text use \"\", for variables you don't need for \"\")":"Что вы хотите вывести? (Для текста используйте кавычки, для вывода переменной они не нужны)",
    "Input settings":"Настройки ввода",
    "What variable name do you want to store the input value?":"Какое название для переменной вы хотите, где будет храниться данные ввода?",
    "Function settings":"Настройки функции",
    "Enter a function name":"Введите название функции",
    "Enter a function args":"Введите передаваемые аргументы функции (поставьте пробел, если нет)",
    "Add var":"Добавить переменную",
    "Add output":"Добавить вывод",
    "Add input":"Добавить ввод",
    "Add function":"Добавить функцию",
    "Call function":"Вызвать функцию",
    "Add \"if\"":"Добавить \"if\"",
    "Add else":"Добавить else",
    "Add elif":"Добавить elif"
}

en = {
    "Настройка переменной":"Var settings",
    "Введите имя вашей переменной":"Enter your var name",
    "Введите значение переменной (для текста используйте кавычки)":"Enter var value (for text use: \"\")",
    "Настройки вывода":"Output settings",
    "Что вы хотите вывести? (Для текста используйте кавычки, для вывода переменной они не нужны)":"What do you want to output? (For text use \"\", for variables you don't need for \"\")",
    "Настройки ввода":"Input settings",
    "Какое название для переменной вы хотите, где будет храниться данные ввода?":"What variable name do you want to store the input value?",
    "Настройки функции":"Function settings",
    "Введите название функции":"Enter a function name",
    "Введите передаваемые аргументы функции (поставьте пробел, если нет)":"Enter a function args",
    "Добавить переменную":"Add var",
    "Добавить вывод":"Add output",
    "Добавить ввод":"Add input",
    "Добавить функцию":"Add function",
    "Вызвать функцию":"Call function",
    "Добавить \"if\"":"Add \"if\"",
    "Добавить else":"Add else",
    "Добавить elif":"Add elif"
}

def selected(x = 0):
    select = commands_cb.get()

    if select == "Add var" or select == ru.get("Add var"):
        if lang == 'ru':
            var_title = ru.get('Var settings')
            var_name_string = ru.get('Enter your var name')
            var_value_string = ru.get('Enter var value (for text use: \"\")')
        else:
            var_title = en.get('Настройка переменной')
            var_name_string = en.get('Введите имя вашей переменной')
            var_value_string = en.get('Введите значение переменной (для текста используйте кавычки)')
        
        var_name = simpledialog.askstring(var_title, var_name_string)
        var_value = simpledialog.askstring(var_title, var_value_string)
        
        code.insert(END, f"{var_name} = {var_value}\n")
    elif select == "Add output" or select == ru.get("Add output"):
        if lang == 'ru':
            output_title = ru.get("Output settings")
            output_value = ru.get("What do you want to output? (For text use \"\", for variables you don't need for \"\")")
        elif lang == 'en':
            output_title = en.get("Настройки вывода")
            output_value = en.get("Что вы хотите вывести? (Для текста используйте кавычки, для вывода переменной они не нужны)")
        output_text = simpledialog.askstring(output_title, output_value)
        
        code.insert(END, f"print({output_text})\n")
    elif select == "Add input" or select == ru.get("Add input"):
        if lang == 'ru':
            input_title = ru.get("Input settings")
            input_ask_string = ru.get("What do you want to ask? (you don't need to type \"\")")
            input_var_string = ru.get("What variable name do you want to store the input value?")
        elif lang == 'en':
            input_title = en.get("Настройки ввода")
            input_ask_string = "What do you want to ask? (you don't need to type \"\")"
            input_var_string = en.get("Какое название для переменной вы хотите, где будет храниться данные ввода?")

        input_ask = simpledialog.askstring(input_title, input_ask_string)
        input_var = simpledialog.askstring(input_title, input_var_string)
        code.insert(END, f"{input_var} = input({input_ask})\n")
    elif select == "Add function" or select == ru.get("Add function"):
        if lang == 'ru':
            func_name = ru.get("Enter a function name")
            func_args = ru.get("Enter a function args")
        elif lang == 'en':
            func_name = en.get("Введите название функции")
            func_args = en.get("Введите передаваемые аргументы функции (поставьте пробел, если нет)")

        function_name = simpledialog.askstring("Function settings", func_name)
        function_args = simpledialog.askstring("Function settings", func_args)

        code.insert(END, f"def {function_name}({function_args}):\n  ")
    elif select == "Call function" or select == ru.get("Call function"):
        if lang == 'ru':
            func_name = ru.get("Enter a function name")
            func_args = ru.get("Enter a function args")
        elif lang == 'en':
            func_name = en.get("Введите название функции")
            func_args = en.get("Введите передаваемые аргументы функции (поставьте пробел, если нет)")

        function_name = simpledialog.askstring("Function settings", func_name)
        function_args = simpledialog.askstring("Function settings", func_args)
        code.insert(END, f"{function_name}({function_args})")
    elif select == "Add \"if\"" or select == ru.get("Add \"if\""):
        if lang == 'ru':
            if_ = "Напишите условие"
        elif lang == 'en':
            if_ = "Write a condition"
        
        condintion = simpledialog.askstring("If settings", if_)

        code.insert(END, f"if {condintion}:\n  ")
    elif select == "Add else" or select == "Добавить else":
        code.insert(END, f"else:\n  ")
    elif select == "Add elif" or select == "Добавить elif":
        if lang == 'ru':
            elif_ = "Напишите условие"
        elif lang == 'en':
            elif_ = "Write a condition"
        
        condintion = simpledialog.askstring("If settings", elif_)
        code.insert(END, f"elif {condintion}:\n  ")


def lang_selected(x = 1):
    global lang

    select = langs.get()

    if select == 'ru':
        lang = 'ru'
        if lang == 'ru':
            for i in range(len(cmds_show)):
                for_trnslt = ru.get(cmds_show[i])

                cmds_show[i] = for_trnslt
                commands_cb.configure(values=cmds_show)
    elif select == 'en':
        lang = 'en'
        for i in range(len(cmds_show)):
            for_trnslt = en.get(cmds_show[i])

            cmds_show[i] = for_trnslt
            commands_cb.configure(values=cmds_show)

        root.update()

cmds = ["Add var", "Add output", "Add input", "Add function", "Call function", "Add \"if\"", "Add else", "Add elif"]
cmds_show = ["Add var", "Add output", "Add input", "Add function", "Call function", "Add \"if\"", "Add else", "Add elif"]

langs_list = ['Choose language / Выберите язык', 'ru', 'en']
lang = 'en'

commands_cb = ttk.Combobox(root, values=cmds_show)
commands_cb.place(x=0, y=0, width=300)

code = Text(root)
code.place(x=0, y=20, width=300, height=280)

langs = ttk.Combobox(root, values=langs_list)
langs.place(x=0, y=280, width=300)
langs.current(0)

commands_cb.bind("<<ComboboxSelected>>", selected)
langs.bind("<<ComboboxSelected>>", lang_selected)

root.mainloop()
