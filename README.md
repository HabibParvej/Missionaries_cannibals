
# 🧠 Missionaries and Cannibals Puzzle Game – Django Web App

A fun and interactive web-based implementation of the classic **Missionaries and Cannibals river-crossing puzzle**, built using **Django**.

![Game Screenshot](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Missionaries_and_Cannibals.svg/800px-Missionaries_and_Cannibals.svg.png)

---

## 🎯 Objective

Safely move all **3 missionaries** and **3 cannibals** from the **left bank** of a river to the **right bank** using a boat. The boat can carry **1 or 2 people** at a time.  
Beware! If cannibals outnumber missionaries on **either bank**, the missionaries will be eaten and the game ends.

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap optional)
- **State Management**: Django Sessions
- **Logic**: Python-based game state validation

---

## 🚀 Features

- Interactive move selection (via forms/buttons)
- Game state tracking (who is on which bank + boat position)
- Win and loss detection based on rules
- Move counter (optional)
- Restart option
- Clean and simple UI

---

## 📦 Project Structure

```
mc_game/
├── game/
│   ├── migrations/
│   ├── templates/
│   │   └── game/
│   │       └── index.html
│   ├── static/
│   │   └── game/
│   │       └── style.css
│   ├── views.py
│   ├── urls.py
│   └── logic.py  <-- custom game logic
├── mc_game/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── manage.py
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mc-game-django.git
cd mc-game-django
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python manage.py runserver
```

### 5. Open in Browser

Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and start playing!

---

## 🎮 Game Rules Summary

- Boat can carry **1 or 2** people.
- At least **1 person** must be in the boat to cross.
- If cannibals ever **outnumber missionaries** on either side (and missionaries are present), you **lose**.
- Move all 3 missionaries and 3 cannibals to the right side safely to **win**.

---

## ✨ Optional Enhancements

- Move counter
- Animated boat crossing (JS/CSS)
- Sound effects
- Difficulty levels (e.g., more characters, fewer moves)
- Mobile responsive design

---

## 🤝 Contributing

Pull requests are welcome. Feel free to fork the repo and submit improvements, UI upgrades, or new features.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙏 Credits

- Logic inspired by classic puzzle problem
- Built with ❤️ using Django

---

## 📷 Screenshot (example UI)

> *(Insert your own screenshot once UI is ready)*
