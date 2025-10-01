# PyQt5 Digital Clock

A tiny desktop digital clock built with **PyQt5**. Displays the current time in 12‑hour format with seconds and AM/PM, neon‑green digits on a black background, and updates every second.

## Features
- ⏰ 12‑hour time with seconds and AM/PM (`hh:mm:ss AP`)
- 🔄 Updates every 1000 ms via `QTimer`
- 🎨 Custom seven‑segment style font (**DS‑DIGIT.TTF**) with green digits on black background
- 🧰 Simple, single‑file script (`pyqt5_digital_clock.py`)

## Requirements
- Python 3.8+
- PyQt5

Install:
```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate       # Windows PowerShell
pip install PyQt5
```

## Project structure
```
.
├── pyqt5_digital_clock.py
└── DS-DIGIT.TTF           # optional custom font used by the app
```

## Screenshots
(digital_clock_ss.png)
* Screenshot of the output for the digital clock.

## Running
```bash
python pyqt5_digital_clock.py
```

## Font notes (DS-DIGIT.TTF)
The app loads a custom font with:
```python
font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
```

If your working directory is not the same as the script’s folder, the font may not load. Two reliable options:

**A) Load the font relative to the script (recommended)**
```python
from pathlib import Path
font_path = Path(__file__).resolve().with_name("DS-DIGIT.TTF")
font_id = QFontDatabase.addApplicationFont(str(font_path))
```

**B) Use an absolute path (works, but not portable)**
```python
font_id = QFontDatabase.addApplicationFont("/absolute/path/to/DS-DIGIT.TTF")
```

**C) Install the font system‑wide** (macOS Font Book / Windows Fonts) and use:
```python
self.time_label.setFont(QFont("DS-Digital", 150))
```

If the font fails to load, `applicationFontFamilies(font_id)` can be empty; pick a fallback like `Menlo` or `Monaco`.

## Customize
- **Color**: change the label stylesheet color (e.g., `#26ff00`).
- **Size**: set the size in `QFont(…, <size>)` or in the stylesheet (pick one to avoid conflicts).
- **Format**: switch to 24‑hour time with `QTime.currentTime().toString("HH:mm:ss")`.

## Troubleshooting
- **IndexError: list index out of range** at `applicationFontFamilies(...)[0]` → the font didn’t load.
  - Check the path / filename (case‑sensitive on macOS).
  - Ensure the file is readable; on macOS you can remove the quarantine flag:
    ```bash
    xattr -d com.apple.quarantine DS-DIGIT.TTF
    ```
- **PyQt5 not found** → `pip install PyQt5` in your active virtualenv.

---

Happy timing! ⏱️
