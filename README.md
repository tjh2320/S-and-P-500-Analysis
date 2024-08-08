# Clone the repository
git clone https://github.com/tjh2320/S-and-P-500-Analysis.git
cd S-and-P-500-Analysis

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Create a requirements.txt file with necessary packages
echo "
pandas
matplotlib
numpy
" > requirements.txt

# Install the required packages
pip install -r requirements.txt

# Create the README.md file
echo "
# S&P 500 Stock Analysis

## Project Description

This project analyzes the performance of the top 10, middle 10, and bottom 10 S&P 500 stocks over the past 10 years. It includes a simulation of an investment strategy where a fixed amount is invested in these stocks each year, and visualizes the investment performance over time.

## Features

1. **Data Loading:**
   - Reads multiple CSV files containing stock data and company information.

2. **Data Cleaning and Merging:**
   - Cleans the data and merges the datasets.
   - Calculates new values such as annual returns for each stock.

3. **Data Visualization:**
   - Generates line plots to visualize the performance of top 10, middle 10, and bottom 10 stocks over time using Matplotlib.

## Installation

### Setting up a virtual environment

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/tjh2320/S-and-P-500-Analysis.git
   cd S-and-P-500-Analysis
   \`\`\`

2. **Create and activate a virtual environment:**
   - On Windows:
     \`\`\`bash
     python -m venv venv
     venv\Scripts\activate
     \`\`\`
   - On MacOS and Linux:
     \`\`\`bash
     python3 -m venv venv
     source venv/bin/activate
     \`\`\`

3. **Install the required packages:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Running the Project

1. **Activate the virtual environment (if not already activated):**
   - On Windows:
     \`\`\`bash
     venv\Scripts\activate
     \`\`\`
   - On MacOS and Linux:
     \`\`\`bash
     source venv/bin/activate
     \`\`\`

2. **Run the data processing script:**
   \`\`\`bash
   python DataProcessing.py
   \`\`\`

3. **Run the investment simulation and visualization script:**
   \`\`\`bash
   python StockRankingandInvestmentSimulation.py
   \`\`\`

## Project Structure

- \`DataProcessing.py\`: Script for data cleaning and merging.
- \`StockRankingandInvestmentSimulation.py\`: Script for calculating and visualizing stock performance.
- \`requirements.txt\`: List of required Python packages.
- \`README.md\`: Project documentation.

## Data Dictionary

| Column Name         | Description                                      |
|---------------------|--------------------------------------------------|
| Date                | Trading date                                     |
| Symbol              | Stock symbol                                     |
| Adj Close           | Adjusted closing price of the stock              |
| Fulltimeemployees   | Number of full-time employees in the company     |
| Longbusinesssummary | Summary of the business                          |
| Weight              | Weight of the stock in the S&P 500 index         |
| Annual_Return       | Annual return of the stock                       |
| Log_Return          | Logarithmic return of the stock                  |

## Unit Tests

(To be added if applicable)

## Special Instructions

- Ensure you have an internet connection to install the required packages.
- Follow the instructions step by step to set up the virtual environment and run the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to Kaggle for the S&P 500 dataset.
