# Text Analyzer

A Python terminal-based text analyzer that counts characters, vowels, consonants, digits, spaces, and special characters, displaying statistics with stylish tables and progress bars using the [Rich](https://github.com/Textualize/rich) library.

---

## Features

* ✅ Counts vowels, consonants, digits, spaces, and special characters
* ✅ Calculates the density (%) of each category
* ✅ Displays results in a **colorful Rich table**
* ✅ Includes a **progress bar** animation during analysis
* ✅ Safe handling of empty input
* ✅ Loop to analyze multiple texts without restarting the program

---

## Demo

```
┌────────────────────────────────────────┐
│             Text Analyzer              │
└────────────────────────────────────────┘

Enter your text:
> Hello, World! 123

Analyzing...
Done!
Total characters = 16

+------------------+-------+---------+
| Character        | Count | Density |
+------------------+-------+---------+
| Vowels           | 3     | 18.8%   |
| Consonants       | 7     | 43.8%   |
| Digits           | 3     | 18.8%   |
| Spaces           | 2     | 12.5%   |
| Special Characters | 1   | 6.3%    |
+------------------+-------+---------+

Do you want to analyze another text? (y/n):
```

---

## Installation

1. Clone the repository:

```bash
cd text-analyzer
```

2. Install dependencies:

```bash
pip install rich
```

3. Run the program:

```bash
python analyzer.py
```

---

## Usage

* Simply run the script in your terminal.
* Enter any text to analyze.
* View colorful statistics and densities.
* Choose to analyze another text or exit.

---

## Requirements

* Python 3.8 or higher
* [Rich](https://pypi.org/project/rich/)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Future Improvements

* Add word and sentence count
* Add visual density bars for each category
* Export results to a `.txt` or `.csv` file
* Convert into a GUI app with Tkinter or PyQt

---

Made with ❤️ using Python and Rich
