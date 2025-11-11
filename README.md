# Python Practice Projects

A collection of Python scripts and projects demonstrating various programming concepts, from basic OOP principles to API integrations and data visualization.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [AI & Chatbots](#ai--chatbots)
  - [Banking & Finance](#banking--finance)
  - [Calculators](#calculators)
  - [Data Visualization](#data-visualization)
  - [Entertainment & Media](#entertainment--media)
  - [Utilities](#utilities)
  - [Student Management](#student-management)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## 🎯 Overview

This repository contains various Python practice projects covering different domains including:
- Object-Oriented Programming (OOP)
- API Integration
- Data Visualization with Matplotlib
- Desktop Notifications
- Text Processing
- AI/Chatbot Development

## 📁 Projects

### 🤖 AI & Chatbots

#### Gemini AI (`Gemini_AI.py`)
An interactive chatbot powered by Google's Gemini API.
- **Features:**
  - Real-time conversation with Google's Gemini 2.5 Flash model
  - Environment variable support for API key management
  - Continuous chat until user says "goodbye"
- **Dependencies:** `google-genai`, `python-dotenv`
- **Setup:** Create a `.env` file with your `GEMINI_API_KEY`

#### Basic Bot (`basic_bot.py`)
A simple rule-based chatbot demonstrating basic conditional logic.
- **Features:**
  - Responds to greetings (hello, hi)
  - Simple conversation flow
  - Exit command with "bye"

### 💰 Banking & Finance

#### Bank Account System (`bank.py`)
Basic implementation of a bank account class with essential operations.
- **Features:**
  - Account creation with account number and initial balance
  - Debit operation with insufficient funds check
  - Credit operation
  - Balance inquiry
- **OOP Concepts:** Classes, methods, attributes

#### Advanced Bank Account (`bank2.py`)
Enhanced version with additional features.
- **Features:**
  - All features from `bank.py`
  - Fund transfer between accounts
  - Account information retrieval
  - Type hints for better code clarity
- **OOP Concepts:** Classes, methods, string formatting

#### Currency Converter (`currency2converter.py`)
Real-time currency conversion tool.
- **Features:**
  - Convert between multiple currencies
  - User-friendly input interface
  - Live exchange rates
- **Dependencies:** `currency-converter`

### 🧮 Calculators

#### Simple Calculator (`calc.py`)
One-line calculator using Python's `eval()` function.
- **Features:** Execute mathematical expressions directly
- **Note:** For educational purposes only; `eval()` can be unsafe with untrusted input

#### OOP Calculator (`calculator(with_oop).py`)
Feature-rich calculator built with Object-Oriented Programming.
- **Features:**
  - Addition, subtraction, multiplication, division
  - Division by zero error handling
  - Interactive menu system
  - Continuous operation mode
- **OOP Concepts:** Classes, methods, exception handling

### 📊 Data Visualization

All visualization scripts use `matplotlib` and accept user input for custom charts.

#### Bar Chart (`graph_chart/bar_chart.py`)
- Create custom bar charts
- Dynamic data input
- Customizable titles and labels

#### Line Chart (`graph_chart/line.py`)
- Plot line graphs with multiple data points
- Custom axis labels
- Interactive data entry

#### Pie Chart (`graph_chart/pie.py`)
- Generate pie charts with percentage display
- Support for multiple segments
- Automatic percentage calculation

### 🎬 Entertainment & Media

#### Anime Cast Finder (`anime_cast.py`)
Retrieve cast information for anime titles using IMDb.
- **Features:**
  - Search anime by name
  - Display top 10 cast members with voice actors
  - Character to actor mapping
  - Anime genre verification
- **Dependencies:** `IMDbPY`

#### Valentine's Day Greeting (`valentines_day.py`)
Display a colorful ASCII art message.
- **Features:**
  - Large ASCII text using figlet
  - Colored terminal output
- **Dependencies:** `pyfiglet`, `termcolor`

### 🛠️ Utilities

#### Desktop Notification (`desktop_notification.py`)
Automated reminder system with periodic notifications.
- **Features:**
  - Break reminder every 15 minutes
  - Cross-platform desktop notifications
  - Customizable messages
- **Dependencies:** `plyer`

#### URL Opener (`url_using_python.py`)
Simple utility to open URLs in the default browser.
- **Features:** Open any URL from command line input

#### Text Translator (`translate.py`)
Translate text between different languages.
- **Features:**
  - Support for multiple languages
  - Google Translate integration
- **Dependencies:** `translators`
- **Example:** Translates Bengali to English

#### String Manipulation (`remove_n_character_string.py`)
Remove first N characters from a string.
- **Educational:** Demonstrates string slicing in Python

#### File Operations (`practice.py`)
Basic file reading operations.
- **Concepts:** File I/O, reading text files

### 🎓 Student Management

#### Student Record with Grading (`student_grade.py`)
Complete student record management with grade calculation.
- **Features:**
  - Store student name and marks
  - Calculate average marks
  - Automatic grade assignment (A-F)
  - Static method for grade conversion
- **OOP Concepts:** Classes, static methods, decorators
- **Grade Scale:**
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: Below 60

#### Basic Student Class (`student.py`)
Simple student class for average calculation.
- **Features:**
  - Store student information
  - Calculate average of three marks
  - Display formatted results

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shaikat020/Python_practice.git
   cd Python_practice
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **For Gemini AI, create a `.env` file:**
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## 💻 Usage

Run any script using Python:

```bash
python script_name.py
```

### Examples:

```bash
# Run the OOP calculator
python calculator(with_oop).py

# Search for anime cast
python anime_cast.py

# Start desktop notifications
python desktop_notification.py

# Chat with Gemini AI
python Gemini_AI.py

# Create a bar chart
python graph_chart/bar_chart.py
```

## 📦 Dependencies

Main dependencies include:

- **AI & APIs:**
  - `google-genai` - Google Gemini API
  - `IMDbPY` (cinemagoer) - IMDb data access
  - `translators` - Translation services

- **Data Visualization:**
  - `matplotlib` - Plotting and charts
  - `pillow` - Image processing

- **Utilities:**
  - `plyer` - Desktop notifications
  - `pyfiglet` - ASCII art text
  - `termcolor` - Colored terminal output
  - `currency-converter` - Currency conversion
  - `python-dotenv` - Environment variable management

- **Web:**
  - `requests` - HTTP requests
  - `beautifulsoup4` - Web scraping
  - `Flask` - Web framework

See `requirements.txt` for the complete list of dependencies.

## 🎯 Learning Objectives

This repository demonstrates:

- ✅ Object-Oriented Programming principles
- ✅ API integration and external library usage
- ✅ File I/O operations
- ✅ Data visualization techniques
- ✅ User input handling and validation
- ✅ Error handling and exception management
- ✅ Working with third-party APIs
- ✅ Cross-platform desktop application features

## 📝 Notes

- Some scripts require API keys (Gemini AI)
- The `calc.py` script uses `eval()` - use with caution
- Desktop notifications require platform-specific permissions
- Currency conversion requires internet connection

## 🤝 Contributing

Feel free to fork this repository and submit pull requests with improvements or additional practice projects!

## 📄 License

This project is for educational purposes.

---

**Happy Coding! 🎉**
