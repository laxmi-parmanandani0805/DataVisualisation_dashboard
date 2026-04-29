# 🌍 Global Intelligence Dashboard

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.x-orange.svg)
![Seaborn](https://img.shields.io/badge/seaborn-0.11%2B-green.svg)

An interactive, hybrid data visualization dashboard built with Python. This project utilizes `matplotlib` and `seaborn` to generate a 2x2 grid of insightful visualizations, comparing custom user-inputted country metrics against a robust set of programmatically generated global data.

---

## ✨ Features

* **Hybrid Data Visualization:** Seamlessly blends static random data generation with dynamic CLI user inputs.
* **Interactive Element:** Prompts the user in the terminal to input specific GDP and Life Expectancy metrics to plot their own custom data point.
* **Multi-Plot Dashboard:** Renders four distinct visualizations in a single, cohesive view:
  1. **Wealth vs. Health (Scatter Plot):** Highlights the user's custom data point against a backdrop of global statistics, utilizing a logarithmic scale for GDP.
  2. **Healthcare Index (Boxplot):** Displays the distribution of healthcare quality across different continents.
  3. **Regional Averages (Heatmap):** Provides a clear, color-coded matrix of mean GDP and Healthcare metrics by region.
  4. **Health Density (KDE Plot):** Visualizes the probability distribution of life expectancy grouped by continent.
* **Error Handling:** Gracefully handles invalid console inputs by falling back to default visualization parameters.

---

## 🛠️ Tech Stack & Requirements

To run this script, you need Python installed on your machine along with the following libraries:

* **[Python 3.8+](https://www.python.org/downloads/)**
* **Pandas:** For data manipulation and structuring.
* **NumPy:** For generating the simulated background dataset.
* **Matplotlib:** For the core dashboard figure and axis management.
* **Seaborn:** For high-level, aesthetically pleasing statistical graphics.

---

## ⚙️ Installation & Setup

1. **Clone the repository** (or download the script):
   ```bash
   git clone [https://github.com/your-username/global-intelligence-dashboard.git](https://github.com/your-username/global-intelligence-dashboard.git)
   cd global-intelligence-dashboard
   ```
2. **Install the required dependencies:**
It is recommended to use a virtual environment.

```bash
pip install pandas numpy matplotlib seaborn
```
3. **Save the script:** Ensure the python code is saved in a file named dashboard.py.

---

## 🚀 Usage
**Run the script from your terminal:**
```bash
python dashboard.py
```
**Follow the interactive prompts:**
The terminal will pause and ask for three inputs to generate your custom data point on the first plot:
- Enter GDP per Capita (e.g., 45000): -> Enter a numeric value.
- Enter Life Expectancy (e.g., 82): -> Enter a numeric value.
- Enter a name for your data point: -> Enter a string (e.g., "India", "My Country").

Once the data is entered, the fully styled Matplotlib dashboard window will open!

---

## 👩‍💻 Author
**Laxmi Parmanandani** 
- LinkedIn: https://www.linkedin.com/in/laxmi-parmanandani-63733a386/
  
