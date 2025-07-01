# PRODIGI_SD_1
temperature  converter PRODIGY Software Deve

Here's your **project report** in a **clean, professional, and complete format**, revised to reflect that the GUI is not yet implemented:

---

# 🌡️ Temperature Converter

## 📌 Project Overview

This project is a simple and effective **Temperature Converter** created as part of the **Prodigy Infotech Data Science Internship (Task - Prodigy\_SD\_01)**.
It allows users to convert temperature values between **Celsius, Fahrenheit, and Kelvin** through a **Command-Line Interface (CLI)**.

> *Note: GUI integration (using Tkinter) is planned but not yet implemented.*

---

## ✅ Features

* Convert temperatures between:

  * Celsius ↔ Fahrenheit
  * Celsius ↔ Kelvin
  * Fahrenheit ↔ Kelvin
* Simple and user-friendly **command-line interface**.
* **Error handling** for invalid or improperly formatted inputs.

---

## 🧑‍💻 How to Run the Program

### 🔧 Prerequisites

Ensure **Python 3** is installed on your system.
You can download Python from the official website:
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 🚀 Steps to Run

1. **Clone the repository** (if not already done):

   ```bash
   git clone https://github.com/SaskankSami21/PRODIGY_SD_01.git
   cd PRODIGY_SD_01/task-01-temperature-converter
   ```

2. **Navigate to the directory** containing the Python file:

   ```bash
   cd path_to_your_script_directory
   ```

3. **Run the script**:

   ```bash
   python temperature_converter.py
   ```

---

## 🧪 Usage Instructions

1. The program will prompt:

   ```
   Enter a temperature (e.g., '25C', '77F', '298K'). Type 'exit' to quit.
   ```
2. Enter values such as `100C`, `32F`, or `273K`.
3. The converted temperatures will be shown in the appropriate units.
4. Type `exit` to quit the program.

---

## 🧠 Conversion Formulas Used

| From           | To             | Formula                 |
| -------------- | -------------- | ----------------------- |
| Celsius (C)    | Fahrenheit (F) | (C × 9/5) + 32          |
| Celsius (C)    | Kelvin (K)     | C + 273.15              |
| Fahrenheit (F) | Celsius (C)    | (F - 32) × 5/9          |
| Fahrenheit (F) | Kelvin (K)     | (F - 32) × 5/9 + 273.15 |
| Kelvin (K)     | Celsius (C)    | K - 273.15              |
| Kelvin (K)     | Fahrenheit (F) | (K - 273.15) × 9/5 + 32 |

---

## 🗂️ Project Structure

```
PRODIGY_SD_01/
└── task-01-temperature-converter/
    ├── temperature_converter.py   # Main CLI-based conversion script
    └── README.md                  # Project documentation (this file)
```

---

## 📷 Screenshots 


![Temperature Converter Screenshot](screenshots/temp_converter_gui.png)


---

## 🏫 Internship Details

* **Internship Provider:** [Prodigy Infotech](https://www.prodigyinfotech.com/)
* **Intern Name: Govind Sarki
* **Task Name:Prodigy\_SD\_01 – Build a Temperature Conversion Program
* **Internship Period: 1st July 2025

---

## 📝 License

This project is open-sourced under the **MIT License**.
Feel free to use, modify, and distribute it.

---

## 🙏 Acknowledgements

* **Prodigy Infotech** for the opportunity and guidance.
* Python community for robust documentation and support.



