import tkinter as tk
from tkinter.ttk import *

import tkinter.messagebox as msgbox

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label1 = None
        self.quit = None
        self.button = None
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        game = tk.IntVar()

        conditions_djmax = ['조건1', '조건2', '조건3', '조건4', '조건5',
                            '조건6', '조건7', '조건8', '조건9', '조건10',
                            '조건11', '조건12', '조건13', '조건14', '조건15']
        conditions_ez2on = ['조건1', '조건2', '조건3', '조건4', '조건5',
                            '조건6', '조건7', '조건8', '조건9', '조건10',
                            '조건11', '조건12', '조건13', '조건14', '조건15']

        def game_rad():
            if game.get() == 0:
                self.djmaxJudge01Entry.config(state="normal")
                self.djmaxJudge02Entry.config(state="normal")
                self.djmaxJudge03Entry.config(state="normal")
                self.djmaxJudge04Entry.config(state="normal")
                self.djmaxJudge05Entry.config(state="normal")
                self.djmaxJudge06Entry.config(state="normal")
                self.djmaxJudge07Entry.config(state="normal")
                self.djmaxJudge08Entry.config(state="normal")
                self.djmaxJudge09Entry.config(state="normal")
                self.djmaxJudge10Entry.config(state="normal")
                self.djmaxJudge11Entry.config(state="normal")
                self.djmaxJudge12Entry.config(state="normal")
                self.djmaxScoreEntry.config(state="normal")
                self.djmaxRateEntry01.config(state="normal")
                self.djmaxRateEntry02.config(state="normal")
                self.djmaxBestComboEntry.config(state="normal")
                self.djmaxComboBox.config(state="normal")
                self.djmaxCalculate.config(state="normal")
                self.ez2onJudge01Entry.config(state="disabled")
                self.ez2onJudge02Entry.config(state="disabled")
                self.ez2onJudge03Entry.config(state="disabled")
                self.ez2onJudge04Entry.config(state="disabled")
                self.ez2onJudge05Entry.config(state="disabled")
                self.ez2onScoreEntry.config(state="disabled")
                self.ez2onRateEntry01.config(state="disabled")
                self.ez2onRateEntry02.config(state="disabled")
                self.ez2onMaxComboEntry.config(state="disabled")
                self.ez2onComboBox.config(state="disabled")
                self.ez2onCalculate.config(state="disabled")
                self.ez2onResult.config(text="결과 표시")
            elif game.get() == 1:
                self.djmaxJudge01Entry.config(state="disabled")
                self.djmaxJudge02Entry.config(state="disabled")
                self.djmaxJudge03Entry.config(state="disabled")
                self.djmaxJudge04Entry.config(state="disabled")
                self.djmaxJudge05Entry.config(state="disabled")
                self.djmaxJudge06Entry.config(state="disabled")
                self.djmaxJudge07Entry.config(state="disabled")
                self.djmaxJudge08Entry.config(state="disabled")
                self.djmaxJudge09Entry.config(state="disabled")
                self.djmaxJudge10Entry.config(state="disabled")
                self.djmaxJudge11Entry.config(state="disabled")
                self.djmaxJudge12Entry.config(state="disabled")
                self.djmaxScoreEntry.config(state="disabled")
                self.djmaxRateEntry01.config(state="disabled")
                self.djmaxRateEntry02.config(state="disabled")
                self.djmaxBestComboEntry.config(state="disabled")
                self.djmaxComboBox.config(state="disabled")
                self.djmaxCalculate.config(state="disabled")
                self.ez2onJudge01Entry.config(state="normal")
                self.ez2onJudge02Entry.config(state="normal")
                self.ez2onJudge03Entry.config(state="normal")
                self.ez2onJudge04Entry.config(state="normal")
                self.ez2onJudge05Entry.config(state="normal")
                self.ez2onScoreEntry.config(state="normal")
                self.ez2onRateEntry01.config(state="normal")
                self.ez2onRateEntry02.config(state="normal")
                self.ez2onMaxComboEntry.config(state="normal")
                self.ez2onComboBox.config(state="normal")
                self.ez2onCalculate.config(state="normal")
                self.djmaxResult.config(text="결과 표시")

        self.radiobutton1 = tk.Radiobutton(self, text="DJMAX", variable=game, value=0, command=game_rad)
        self.radiobutton2 = tk.Radiobutton(self, text="EZ2ON", variable=game, value=1, command=game_rad)

        def djmax_calculation():
            number_max100 = int(self.djmaxJudge01Entry.get())
            number_max90 = int(self.djmaxJudge02Entry.get())
            number_max80 = int(self.djmaxJudge03Entry.get())
            number_max70 = int(self.djmaxJudge04Entry.get())
            number_max60 = int(self.djmaxJudge05Entry.get())
            number_max50 = int(self.djmaxJudge06Entry.get())
            number_max40 = int(self.djmaxJudge07Entry.get())
            number_max30 = int(self.djmaxJudge08Entry.get())
            number_max20 = int(self.djmaxJudge09Entry.get())
            number_max10 = int(self.djmaxJudge10Entry.get())
            number_max1 = int(self.djmaxJudge11Entry.get())
            number_break = int(self.djmaxJudge12Entry.get())
            total_notes = (number_max100 + number_max90 + number_max80 + number_max70 + number_max60 + number_max50
                           + number_max40 + number_max30 + number_max20 + number_max10 + number_max1 + number_break)
            self.djmaxJudge01Entry.delete(0, "end")
            self.djmaxJudge02Entry.delete(0, "end")
            self.djmaxJudge03Entry.delete(0, "end")
            self.djmaxJudge04Entry.delete(0, "end")
            self.djmaxJudge05Entry.delete(0, "end")
            self.djmaxJudge06Entry.delete(0, "end")
            self.djmaxJudge07Entry.delete(0, "end")
            self.djmaxJudge08Entry.delete(0, "end")
            self.djmaxJudge09Entry.delete(0, "end")
            self.djmaxJudge10Entry.delete(0, "end")
            self.djmaxJudge11Entry.delete(0, "end")
            self.djmaxJudge12Entry.delete(0, "end")
            self.djmaxResult.config(text=total_notes)

        self.djmaxJudge01 = tk.Label(self, text="MAX 100%")
        self.djmaxJudge02 = tk.Label(self, text="MAX 90%")
        self.djmaxJudge03 = tk.Label(self, text="MAX 80%")
        self.djmaxJudge04 = tk.Label(self, text="MAX 70%")
        self.djmaxJudge05 = tk.Label(self, text="MAX 60%")
        self.djmaxJudge06 = tk.Label(self, text="MAX 50%")
        self.djmaxJudge07 = tk.Label(self, text="MAX 40%")
        self.djmaxJudge08 = tk.Label(self, text="MAX 30%")
        self.djmaxJudge09 = tk.Label(self, text="MAX 20%")
        self.djmaxJudge10 = tk.Label(self, text="MAX 10%")
        self.djmaxJudge11 = tk.Label(self, text="MAX 1%")
        self.djmaxJudge12 = tk.Label(self, text="BREAK")
        self.djmaxScore = tk.Label(self, text="SCORE")
        self.djmaxRate = tk.Label(self, text="RATE(00.00)")
        self.djmaxBestCombo = tk.Label(self, text="BESTCOMBO")
        self.djmaxCondition = tk.Label(self, text="조건")
        self.djmaxJudge01Entry = tk.Entry(self, justify="center")
        self.djmaxJudge02Entry = tk.Entry(self, justify="center")
        self.djmaxJudge03Entry = tk.Entry(self, justify="center")
        self.djmaxJudge04Entry = tk.Entry(self, justify="center")
        self.djmaxJudge05Entry = tk.Entry(self, justify="center")
        self.djmaxJudge06Entry = tk.Entry(self, justify="center")
        self.djmaxJudge07Entry = tk.Entry(self, justify="center")
        self.djmaxJudge08Entry = tk.Entry(self, justify="center")
        self.djmaxJudge09Entry = tk.Entry(self, justify="center")
        self.djmaxJudge10Entry = tk.Entry(self, justify="center")
        self.djmaxJudge11Entry = tk.Entry(self, justify="center")
        self.djmaxJudge12Entry = tk.Entry(self, justify="center")
        self.djmaxScoreEntry = tk.Entry(self, justify="center")
        self.djmaxRateEntry01 = tk.Entry(self, justify="center", width=10)
        self.djmaxRateDot = tk.Label(self, text=".")
        self.djmaxRateEntry02 = tk.Entry(self, justify="center", width=10)
        self.djmaxBestComboEntry = tk.Entry(self, justify="center")
        self.djmaxComboBox = Combobox(self, values=conditions_djmax, state="readonly")
        self.djmaxCalculate = tk.Button(self, text="계산", fg="black", command=djmax_calculation)
        self.djmaxResult = tk.Label(self, text="결과 표시")

        def ez2on_calculation():
            if self.ez2onJudge01Entry.get().__eq__('') or self.ez2onJudge02Entry.get().__eq__('') or self.ez2onJudge03Entry.get().__eq__('') or self.ez2onJudge04Entry.get().__eq__('') or self.ez2onJudge05Entry.get().__eq__(''):
                msgbox.showerror("오류","입력하지 않은 값이 있습니다.")
            elif not self.ez2onJudge01Entry.get().isdigit() or not self.ez2onJudge02Entry.get().isdigit() or not self.ez2onJudge03Entry.get().isdigit() or not self.ez2onJudge04Entry.get().isdigit() or not self.ez2onJudge05Entry.get().isdigit():
                msgbox.showerror("오류", "모든 값은 양의 정수로 입력해야 합니다.")
            else:
                number_kool = int(self.ez2onJudge01Entry.get())
                number_cool = int(self.ez2onJudge02Entry.get())
                number_good = int(self.ez2onJudge03Entry.get())
                number_miss = int(self.ez2onJudge04Entry.get())
                number_fail = int(self.ez2onJudge05Entry.get())
                number_score = int(self.ez2onScoreEntry.get())
                number_rate01 = int(self.ez2onRateEntry01.get())
                number_rate02 = int(self.ez2onRateEntry02.get())
                number_maxcombo = int(self.ez2onMaxComboEntry.get())
                total_notes = number_kool + number_cool + number_good + number_miss + number_fail
                total_rate = number_rate01 + (number_rate02/100)
                self.ez2onJudge01Entry.delete(0, "end")
                self.ez2onJudge02Entry.delete(0, "end")
                self.ez2onJudge03Entry.delete(0, "end")
                self.ez2onJudge04Entry.delete(0, "end")
                self.ez2onJudge05Entry.delete(0, "end")
                self.ez2onScoreEntry.delete(0, "end")
                self.ez2onRateEntry01.delete(0, "end")
                self.ez2onRateEntry02.delete(0, "end")
                self.ez2onMaxComboEntry.delete(0, "end")
                self.ez2onResult.config(text=total_rate)

        self.ez2onJudge01 = tk.Label(self, text="KOOL")
        self.ez2onJudge02 = tk.Label(self, text="COOL")
        self.ez2onJudge03 = tk.Label(self, text="GOOD")
        self.ez2onJudge04 = tk.Label(self, text="MISS")
        self.ez2onJudge05 = tk.Label(self, text="FAIL")
        self.ez2onScore = tk.Label(self, text="SCORE")
        self.ez2onRate = tk.Label(self, text="RATE(00.00)")
        self.ez2onMaxCombo = tk.Label(self, text="MAXCOMBO")
        self.ez2onCondition = tk.Label(self, text="조건")
        self.ez2onJudge01Entry = tk.Entry(self, justify="center")
        self.ez2onJudge02Entry = tk.Entry(self, justify="center")
        self.ez2onJudge03Entry = tk.Entry(self, justify="center")
        self.ez2onJudge04Entry = tk.Entry(self, justify="center")
        self.ez2onJudge05Entry = tk.Entry(self, justify="center")
        self.ez2onScoreEntry = tk.Entry(self, justify="center")
        self.ez2onRateEntry01 = tk.Entry(self, justify="center", width=10)
        self.ez2onRateDot = tk.Label(self, text=".")
        self.ez2onRateEntry02 = tk.Entry(self, justify="center", width=10)
        self.ez2onMaxComboEntry = tk.Entry(self, justify="center")
        self.ez2onComboBox = Combobox(self, values=conditions_ez2on, state="readonly")
        self.ez2onCalculate = tk.Button(self, text="계산", fg="black", command=ez2on_calculation)
        self.ez2onResult = tk.Label(self, text="결과 표시")

        self.quit = tk.Button(self, text="종료", fg="red",
                              command=self.master.destroy)

        self.radiobutton1.grid(row=0, column=4)
        self.radiobutton2.grid(row=0, column=5)

        self.djmaxJudge01.grid(row=1, column=0)
        self.djmaxJudge02.grid(row=1, column=1)
        self.djmaxJudge03.grid(row=1, column=2)
        self.djmaxJudge04.grid(row=1, column=3)
        self.djmaxJudge05.grid(row=1, column=4)
        self.djmaxJudge06.grid(row=1, column=5)
        self.djmaxJudge01Entry.grid(row=2, column=0, padx=15)
        self.djmaxJudge02Entry.grid(row=2, column=1, padx=15)
        self.djmaxJudge03Entry.grid(row=2, column=2, padx=15)
        self.djmaxJudge04Entry.grid(row=2, column=3, padx=15)
        self.djmaxJudge05Entry.grid(row=2, column=4, padx=15)
        self.djmaxJudge06Entry.grid(row=2, column=5, padx=15)
        self.djmaxJudge07.grid(row=3, column=0)
        self.djmaxJudge08.grid(row=3, column=1)
        self.djmaxJudge09.grid(row=3, column=2)
        self.djmaxJudge10.grid(row=3, column=3)
        self.djmaxJudge11.grid(row=3, column=4)
        self.djmaxJudge12.grid(row=3, column=5)
        self.djmaxJudge07Entry.grid(row=4, column=0, padx=15)
        self.djmaxJudge08Entry.grid(row=4, column=1, padx=15)
        self.djmaxJudge09Entry.grid(row=4, column=2, padx=15)
        self.djmaxJudge10Entry.grid(row=4, column=3, padx=15)
        self.djmaxJudge11Entry.grid(row=4, column=4, padx=15)
        self.djmaxJudge12Entry.grid(row=4, column=5, padx=15)
        self.djmaxScore.grid(row=5, column=0)
        self.djmaxRate.grid(row=5, column=1)
        self.djmaxBestCombo.grid(row=5, column=2)
        self.djmaxCondition.grid(row=5, column=4)
        self.djmaxScoreEntry.grid(row=6, column=0)
        self.djmaxRateEntry01.grid(row=6, column=1, sticky='w', padx=5)
        self.djmaxRateDot.grid(row=6, column=1)
        self.djmaxRateEntry02.grid(row=6, column=1, sticky='e', padx=5)
        self.djmaxBestComboEntry.grid(row=6, column=2)
        self.djmaxComboBox.grid(row=6, column=3, columnspan=3, ipadx=130)
        self.djmaxCalculate.grid(row=7, column=2, pady=10, ipadx=30)
        self.djmaxResult.grid(row=7, column=3, pady=10)

        self.ez2onJudge01.grid(row=8, column=0, columnspan=2)
        self.ez2onJudge02.grid(row=8, column=1, columnspan=2)
        self.ez2onJudge03.grid(row=8, column=2, columnspan=2)
        self.ez2onJudge04.grid(row=8, column=3, columnspan=2)
        self.ez2onJudge05.grid(row=8, column=4, columnspan=2)
        self.ez2onJudge01Entry.grid(row=9, column=0, columnspan=2, padx=15)
        self.ez2onJudge02Entry.grid(row=9, column=1, columnspan=2, padx=15)
        self.ez2onJudge03Entry.grid(row=9, column=2, columnspan=2, padx=15)
        self.ez2onJudge04Entry.grid(row=9, column=3, columnspan=2, padx=15)
        self.ez2onJudge05Entry.grid(row=9, column=4, columnspan=2, padx=15)
        self.ez2onScore.grid(row=10, column=0)
        self.ez2onRate.grid(row=10, column=1)
        self.ez2onMaxCombo.grid(row=10, column=2)
        self.ez2onCondition.grid(row=10, column=4)
        self.ez2onScoreEntry.grid(row=11, column=0, padx=15)
        self.ez2onRateEntry01.grid(row=11, column=1, sticky='w', padx=5)
        self.ez2onRateDot.grid(row=11, column=1)
        self.ez2onRateEntry02.grid(row=11, column=1, sticky='e', padx=5)
        self.ez2onMaxComboEntry.grid(row=11, column=2, padx=15)
        self.ez2onComboBox.grid(row=11, column=3, columnspan=3, ipadx=130)
        self.ez2onCalculate.grid(row=12, column=2, pady=10, ipadx=30)
        self.ez2onResult.grid(row=12, column=3, pady=10)

        game.set(0)
        game_rad()
        self.radiobutton1.select()


root = tk.Tk()
root.title('SCF2024 - AyruyA의 리듬공방 현장이벤트 전용 프로그램')
root.resizable(width=False, height=False)
app = App(master=root)
app.mainloop()