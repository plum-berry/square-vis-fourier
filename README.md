# Square Wave Visualization in python with Fourier Series

A simple Square Wave Visualization which demonstrates the use of Fourier Series

## Description

This project is a demonstration of the use of Fourier Series to generate a square wave. 
We implement this by using the Fourier Series of a square wave.

$$
f(t) = \frac{4}{\pi} \sum_{n=1,3,5,\dots}^{\infty} \frac{1}{n} \sin(nt)
$$

## Requirements

- Python 3.8 or higher
- pip for package installation
- pygame

## Installation

Step-by-step instructions to set up the project.

1. Clone the repository:
```terminal
git clone https://github.com/plum-berry/square-vis-fourier.git
```
2. Navigate to the project directory:
```
cd square-vis-fourier
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage
To run the script you need to provide a argument `n` which is the number of sine waves that our square wave generate should use.
```cmd
python main.py 5
```
This should generate a approximation of a square wave using sum of 5 sine waves. The 5 circles on the left represent each of those sine waves.




