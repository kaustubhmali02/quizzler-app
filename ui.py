from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
APP_NAME = "Quizzler"
WINDOW_PADDING = 20
CANVAS_TEXT_FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title(APP_NAME)
        self.window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=CANVAS_TEXT_FONT)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=CANVAS_TEXT_FONT,
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        false_button_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.true_button_click)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_button_click)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the questions")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_click(self):
        self.give_feedback(self.quiz.check_answer("TRUE"))

    def false_button_click(self):
        self.give_feedback(self.quiz.check_answer("FALSE"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.quiz.score += 1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


