import tkinter as tk

WINDOW_SIZE = "250x150"


def check(bmi):
    if bmi < 18.5:
        result = "低体重"
    elif bmi < 25.0:
        result = "普通体重"
    elif bmi < 30.0:
        result = "肥満度１"
    elif bmi < 35.0:
        result = "肥満度２"
    elif bmi < 40.0:
        result = "肥満度３"
    else:
        result = "肥満度４"
    return result


def judgement(weight, height):
    weight_value = weight.get()
    height_value = height.get()

    if weight_value == "" or height_value == "":
        return "体重と身長を入力してください"

    weight_value = float(weight_value)
    height_value = float(height_value) / 100

    calc = weight_value / (height_value ** 2)
    result = "肥満度：" + check(calc)

    return result


def main():
    root = tk.Tk()
    root.title("肥満度チェック")
    root.geometry(WINDOW_SIZE)

    label_1 = tk.Label(root, text="体重")
    label_2 = tk.Label(root, text="kg")
    label_3 = tk.Label(root, text="身長")
    label_4 = tk.Label(root, text="cm")
    label_5 = tk.Label(root, text="体重と身長を入力してください")

    weight = tk.Entry(width=5)
    height = tk.Entry(width=5)

    button = tk.Button(root, text="BMI判定", command=lambda: label_5.config(text=judgement(weight, height)))

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    label_1.grid(column=0, row=0, sticky=tk.E)
    weight.grid(column=1, row=0)
    label_2.grid(column=2, row=0, sticky=tk.W)
    label_3.grid(column=0, row=1, sticky=tk.E)
    height.grid(column=1, row=1)
    label_4.grid(column=2, row=1, sticky=tk.W)
    button.grid(column=0, row=2, columnspan=3)
    label_5.grid(column=0, row=3, columnspan=3)

    root.mainloop()


if __name__ == '__main__':
    main()
