# PyCalc Ultra v1

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Rich](https://img.shields.io/badge/Rich-Console%20UI-purple)](https://rich.readthedocs.io/en/stable/)

**PyCalc Ultra v1** is a feature-rich command-line calculator built in Python with a sleek, colorful interface using the [Rich](https://rich.readthedocs.io/) library. It supports basic and advanced operations, history tracking, and math functions.

---

## Features

* Perform **basic arithmetic** operations: `+`, `-`, `*`, `/`, `**`

* Use **Python math functions**: `math.log10(100)`, `math.sqrt(16)`, etc.

* Supports **bitwise operations**: `&`, `|`, `^`, `~`, `<<`, `>>`

* **History tracking**: view previous calculations

* **Interactive commands**:

  * `h` → show calculation history
  * `f` → show calculator features
  * `q` → quit the calculator

* Beautiful **colored UI** with tables, progress bars, and prompts

* Easy to extend with additional math functions

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pycalc-ultra.git
cd pycalc-ultra
```

2. Install dependencies:

```bash
pip install rich
```

3. Run the calculator:

```bash
python pycalc_ultra.py
```

---

## Usage

When you run the calculator, you’ll see a colorful welcome screen:

```
┌─────────────────────────────────────┐
│          PyCalc Ultra v1            │
└─────────────────────────────────────┘

Enter h to check history • enter q to quit • enter f to check the calculator features.
Start calculating:
> 2 + 3
= 5
> math.log10(100)
= 2
> h
```

* Type any valid arithmetic or math expression.
* Use `h` to see history, `f` to see features, and `q` to quit.

---

## Example

```
> 10 / 2
= 5.0
> 2 ** 8
= 256
> math.sqrt(144)
= 12.0
> h
Expression       Result
10 / 2           5.0
2 ** 8           256
math.sqrt(144)   12.0
```

---

## Future Improvements

* Add **persistent history** stored in JSON
* Implement **last result (`ans`) support**
* Improve **input validation** and **safety** with restricted `eval`
* Add **input history navigation**

---

## License

This project is licensed under the MIT License.
