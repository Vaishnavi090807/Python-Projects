import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText


# --------------------- Small UI Helpers ---------------------
def center_window(win, w=700, h=520):
    win.update_idletasks()
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw - w) // 2
    y = (sh - h) // 2
    win.geometry(f"{w}x{h}+{x}+{y}")


def make_labeled_entry(parent, label_text, row, placeholder=""):
    lbl = ttk.Label(parent, text=label_text)
    lbl.grid(row=row, column=0, sticky="w", pady=(6, 6), padx=(0, 10))

    var = tk.StringVar()
    ent = ttk.Entry(parent, textvariable=var, width=28)
    ent.grid(row=row, column=1, sticky="ew", pady=(6, 6))

    if placeholder:
        ent.insert(0, placeholder)
        ent.configure(foreground="#666")

        def on_focus_in(_):
            if ent.get() == placeholder and ent.cget("foreground") == "#666":
                ent.delete(0, "end")
                ent.configure(foreground="#000")

        def on_focus_out(_):
            if not ent.get().strip():
                ent.insert(0, placeholder)
                ent.configure(foreground="#666")

        ent.bind("<FocusIn>", on_focus_in)
        ent.bind("<FocusOut>", on_focus_out)

    return var, ent


def clean_value(entry_widget, var, placeholder=""):
    val = var.get().strip()
    # If placeholder is still present, treat as empty
    if placeholder and val == placeholder and entry_widget.cget("foreground") == "#666":
        return ""
    return val


# --------------------- Story Windows ---------------------
def open_story1(root):
    tl = tk.Toplevel(root)
    tl.title("A Memorable Day")
    center_window(tl, 760, 560)

    container = ttk.Frame(tl, padding=18)
    container.pack(fill="both", expand=True)

    title = ttk.Label(container, text="A Memorable Day", style="Title.TLabel")
    title.pack(anchor="w")

    subtitle = ttk.Label(
        container,
        text="Fill in the blanks and click Generate to see your story!",
        style="Sub.TLabel"
    )
    subtitle.pack(anchor="w", pady=(2, 14))

    form = ttk.Frame(container)
    form.pack(fill="x")

    form.columnconfigure(1, weight=1)

    name_var, name_ent = make_labeled_entry(form, "Friend's name:", 0, "e.g., Riya")
    sport_var, sport_ent = make_labeled_entry(form, "Game/Sport:", 1, "e.g., Cricket")
    city_var, city_ent = make_labeled_entry(form, "City:", 2, "e.g., Hyderabad")
    player_var, player_ent = make_labeled_entry(form, "Favorite player:", 3, "e.g., Dhoni")
    drink_var, drink_ent = make_labeled_entry(form, "Drink:", 4, "e.g., Lemon soda")
    snack_var, snack_ent = make_labeled_entry(form, "Snack:", 5, "e.g., Popcorn")

    preview_label = ttk.Label(container, text="Story Preview", style="Header.TLabel")
    preview_label.pack(anchor="w", pady=(16, 6))

    preview = ScrolledText(container, height=10, wrap="word", font=("Segoe UI", 11))
    preview.pack(fill="both", expand=True)
    preview.insert("end", "Your story will appear here...")
    preview.configure(state="disabled")

    def generate():
        name = clean_value(name_ent, name_var, "e.g., Riya")
        sports = clean_value(sport_ent, sport_var, "e.g., Cricket")
        city = clean_value(city_ent, city_var, "e.g., Hyderabad")
        player = clean_value(player_ent, player_var, "e.g., Dhoni")
        drink = clean_value(drink_ent, drink_var, "e.g., Lemon soda")
        snack = clean_value(snack_ent, snack_var, "e.g., Popcorn")

        missing = []
        if not name: missing.append("Friend's name")
        if not sports: missing.append("Game/Sport")
        if not city: missing.append("City")
        if not player: missing.append("Favorite player")
        if not drink: missing.append("Drink")
        if not snack: missing.append("Snack")

        if missing:
            messagebox.showwarning("Missing info", "Please fill: " + ", ".join(missing))
            return

        text = (
            f"One day, me and my friend {name} decided to play a {sports} game in {city}. "
            f"But we were not able to play, so we went to watch the game and our favourite player {player}. "
            f"We drank {drink} and also ate some {snack}. "
            f"We really enjoyed it! We are looking forward to going again and enjoying it!"
        )

        preview.configure(state="normal")
        preview.delete("1.0", "end")
        preview.insert("end", text)
        preview.configure(state="disabled")

    def reset():
        for ent, var, ph in [
            (name_ent, name_var, "e.g., Riya"),
            (sport_ent, sport_var, "e.g., Cricket"),
            (city_ent, city_var, "e.g., Hyderabad"),
            (player_ent, player_var, "e.g., Dhoni"),
            (drink_ent, drink_var, "e.g., Lemon soda"),
            (snack_ent, snack_var, "e.g., Popcorn"),
        ]:
            ent.delete(0, "end")
            ent.insert(0, ph)
            ent.configure(foreground="#666")
            var.set(ph)

        preview.configure(state="normal")
        preview.delete("1.0", "end")
        preview.insert("end", "Your story will appear here...")
        preview.configure(state="disabled")

    btns = ttk.Frame(container)
    btns.pack(fill="x", pady=(12, 0))

    ttk.Button(btns, text="Generate Story", command=generate).pack(side="left")
    ttk.Button(btns, text="Reset", command=reset).pack(side="left", padx=10)
    ttk.Button(btns, text="Close", command=tl.destroy).pack(side="right")

    tl.transient(root)
    tl.grab_set()


def open_story2(root):
    tl = tk.Toplevel(root)
    tl.title("Ambitions")
    center_window(tl, 760, 560)

    container = ttk.Frame(tl, padding=18)
    container.pack(fill="both", expand=True)

    title = ttk.Label(container, text="Ambitions", style="Title.TLabel")
    title.pack(anchor="w")

    subtitle = ttk.Label(
        container,
        text="Pick words and generate an inspiring (and funny) mini-story.",
        style="Sub.TLabel"
    )
    subtitle.pack(anchor="w", pady=(2, 14))

    form = ttk.Frame(container)
    form.pack(fill="x")
    form.columnconfigure(1, weight=1)

    prof_var, prof_ent = make_labeled_entry(form, "Profession:", 0, "e.g., Doctor")
    noun_var, noun_ent = make_labeled_entry(form, "Noun (field/interest):", 1, "e.g., Music")
    feel_var, feel_ent = make_labeled_entry(form, "Feeling:", 2, "e.g., Happy")
    emo_var, emo_ent = make_labeled_entry(form, "Emotion:", 3, "e.g., Inspired")

    # Verb: better as a dropdown (interactive)
    ttk.Label(form, text="Verb (past tense):").grid(row=4, column=0, sticky="w", pady=(6, 6), padx=(0, 10))
    verb_var = tk.StringVar(value="struggled")
    verb_box = ttk.Combobox(
        form,
        textvariable=verb_var,
        values=["struggled", "worked", "learned", "failed", "improved", "paused", "restarted"],
        state="readonly",
        width=26
    )
    verb_box.grid(row=4, column=1, sticky="ew", pady=(6, 6))

    preview_label = ttk.Label(container, text="Story Preview", style="Header.TLabel")
    preview_label.pack(anchor="w", pady=(16, 6))

    preview = ScrolledText(container, height=10, wrap="word", font=("Segoe UI", 11))
    preview.pack(fill="both", expand=True)
    preview.insert("end", "Your story will appear here...")
    preview.configure(state="disabled")

    def generate():
        profession = clean_value(prof_ent, prof_var, "e.g., Doctor")
        noun = clean_value(noun_ent, noun_var, "e.g., Music")
        feeling = clean_value(feel_ent, feel_var, "e.g., Happy")
        emotion = clean_value(emo_ent, emo_var, "e.g., Inspired")
        verb = verb_var.get().strip()

        missing = []
        if not profession: missing.append("Profession")
        if not noun: missing.append("Noun")
        if not feeling: missing.append("Feeling")
        if not emotion: missing.append("Emotion")
        if not verb: missing.append("Verb")

        if missing:
            messagebox.showwarning("Missing info", "Please fill: " + ", ".join(missing))
            return

        text = (
            f"When I was a child, I wanted to become a {profession}. "
            f"But as I grew up, I got into {noun} and decided to become an engineer. "
            f"Then I went into a job where I was not {feeling}. "
            f"After feeling {emotion}, I decided to do what I truly love. "
            f"Despite getting lower and {verb} more than I used to in my previous job, "
            f"I feel {feeling} now."
        )

        preview.configure(state="normal")
        preview.delete("1.0", "end")
        preview.insert("end", text)
        preview.configure(state="disabled")

    def reset():
        for ent, var, ph in [
            (prof_ent, prof_var, "e.g., Doctor"),
            (noun_ent, noun_var, "e.g., Music"),
            (feel_ent, feel_var, "e.g., Happy"),
            (emo_ent, emo_var, "e.g., Inspired"),
        ]:
            ent.delete(0, "end")
            ent.insert(0, ph)
            ent.configure(foreground="#666")
            var.set(ph)

        verb_var.set("struggled")

        preview.configure(state="normal")
        preview.delete("1.0", "end")
        preview.insert("end", "Your story will appear here...")
        preview.configure(state="disabled")

    btns = ttk.Frame(container)
    btns.pack(fill="x", pady=(12, 0))

    ttk.Button(btns, text="Generate Story", command=generate).pack(side="left")
    ttk.Button(btns, text="Reset", command=reset).pack(side="left", padx=10)
    ttk.Button(btns, text="Close", command=tl.destroy).pack(side="right")

    tl.transient(root)
    tl.grab_set()


# --------------------- Main App ---------------------
def main():
    root = tk.Tk()
    root.title("Mad Libs Generator")
    center_window(root, 800, 520)

    # Modern styling
    style = ttk.Style()
    style.theme_use("clam")  # looks good across Windows/Mac/Linux
    style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"))
    style.configure("Sub.TLabel", font=("Segoe UI", 11))
    style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))
    style.configure("Card.TFrame", padding=18, relief="ridge")
    style.configure("TButton", font=("Segoe UI", 11), padding=(12, 8))

    container = ttk.Frame(root, padding=20)
    container.pack(fill="both", expand=True)

    header = ttk.Label(container, text="Mad Libs Generator", style="Title.TLabel")
    header.pack(anchor="w")

    desc = ttk.Label(
        container,
        text="Choose a story, fill the blanks, and instantly preview your Mad Libs!",
        style="Sub.TLabel"
    )
    desc.pack(anchor="w", pady=(4, 18))

    cards = ttk.Frame(container)
    cards.pack(fill="both", expand=True)

    cards.columnconfigure(0, weight=1)
    cards.columnconfigure(1, weight=1)

    # Card 1
    card1 = ttk.Frame(cards, style="Card.TFrame")
    card1.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)

    ttk.Label(card1, text="A Memorable Day", style="Header.TLabel").pack(anchor="w")
    ttk.Label(
        card1,
        text="A fun story about a match day with your friend and favourite player.",
        wraplength=320
    ).pack(anchor="w", pady=(6, 14))

    ttk.Button(card1, text="Open", command=lambda: open_story1(root)).pack(anchor="w")

    # Card 2
    card2 = ttk.Frame(cards, style="Card.TFrame")
    card2.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=10)

    ttk.Label(card2, text="Ambitions", style="Header.TLabel").pack(anchor="w")
    ttk.Label(
        card2,
        text="A motivational (and slightly dramatic) story about dreams and careers.",
        wraplength=320
    ).pack(anchor="w", pady=(6, 14))

    ttk.Button(card2, text="Open", command=lambda: open_story2(root)).pack(anchor="w")

    footer = ttk.Frame(container)
    footer.pack(fill="x", pady=(10, 0))

    ttk.Label(footer, text="Tip: Press Tab to move between fields fast.").pack(side="left")
    ttk.Button(footer, text="Exit", command=root.destroy).pack(side="right")

    root.mainloop()


if __name__ == "__main__":
    main()
