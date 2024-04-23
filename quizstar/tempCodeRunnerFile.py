save_btn = Button(
    button_frame,
    text="Save",
    font=("Consolas", 12),
    width=10,
    command=save_answer,  # Call the 'save_answer' function when clicked
    background="#C99E73",
    fg="#623A14",
)
submit_btn = Button(
    button_frame,
    text="Submit",
    font=("Consolas", 12),
    width=10,
    command=submit,  # Call the 'submit' function when clicked
    background="#C99E73",
    fg="#623A14",
)
save_btn.grid(row=4, column=0, padx=10 , pady=50 )
submit_btn.grid(row=4, column=1, padx=10 , pady=50 )