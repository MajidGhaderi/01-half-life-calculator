# Pharmacokinetics Calculator

A simple Python-based pharmacokinetics calculator for first-order drug elimination.

This project calculates drug half-life, elimination rate constant, and drug concentration over time. It also generates a concentration-time profile.

## Live Demo

Try the interactive web application:

[Pharmacokinetics Calculator Web App](https://01-half-life-calculator-icjb2b5e2vfnzz3k3ktoce.streamlit.app/)

## Features

* Calculate drug half-life from the elimination rate constant.
* Calculate the elimination rate constant from drug half-life.
* Calculate drug concentration at a specific time using first-order elimination.
* Calculate drug concentration at multiple time points.
* Plot a concentration-time profile.
* Plot a semi-log concentration-time profile.
* Validate inputs and handle invalid values using clear error messages.

## Pharmacokinetic Equations

The calculator uses first-order elimination equations to calculate pharmacokinetic parameters and drug concentration over time.

### Half-life

The elimination half-life is calculated from the elimination rate constant using the natural logarithm of 2:

$$
t_{1/2} = \frac{\ln(2)}{k}
$$

where:

* $t_{1/2}$ = elimination half-life (hours)
* $k$ = elimination rate constant (hour$^{-1}$)

### Elimination Rate Constant

The elimination rate constant can also be calculated from the half-life:

$$
k = \frac{\ln(2)}{t_{1/2}}
$$

### Drug Concentration

For first-order elimination, drug concentration at a specific time is calculated as:

$$
C(t) = C_0 e^{-kt}
$$

where:

* $C(t)$ = drug concentration at time $t$
* $C_0$ = initial drug concentration
* $k$ = elimination rate constant
* $t$ = time (hours)

### Semi-log Concentration-Time Profile

The calculator also provides a semi-log concentration-time plot with a linear time axis and a logarithmic concentration axis. This type of plot is useful for visualizing first-order drug elimination.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MajidGhaderi/01-half-life-calculator.git
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```
## Usage

Run the calculator with:

```bash
python calculator.py
```
To run the web application locally:

```bash
streamlit run app.py
```

The application provides the following options:

1. Calculate Half-life
2. Calculate Elimination Rate Constant
3. Calculate Drug Concentration
4. Plot Concentration-Time Profile
5. Plot Semi-log Concentration-Time Profile
6. Exit

Enter the required pharmacokinetic parameters when prompted by the program.

## Web Application

A Streamlit-based interactive interface is available for this calculator.

The web application allows users to:

* Calculate drug half-life.
* Calculate elimination rate constant.
* Calculate drug concentration at a specific time.
* Generate concentration-time profiles.
* Generate semi-log concentration-time profiles.

The web interface uses the same validated pharmacokinetic functions implemented in `calculator.py`.

## Running Tests

Run the test suite with:

```bash
python test_calculator.py
```

The test suite covers:

* Half-life calculations
* Elimination rate constant calculations
* Drug concentration calculations
* Concentration calculations at multiple time points
* Invalid input handling

## Project Structure

01-half-life-calculator/

│

├── calculator.py              # Pharmacokinetic calculations and CLI application

├── app.py                     # Streamlit web interface

├── test_calculator.py         # Unit tests

├── requirements.txt           # Project dependencies

├── README.md                  # Project documentation

└── .gitignore                 # Git ignore rules

## Technologies

* Python
* NumPy
* Matplotlib
* Streamlit
* unittest
* Git
* GitHub
