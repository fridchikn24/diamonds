# Diamonds Analysis

This project focuses on analyzing a dataset of diamonds to understand the factors influencing their prices and to build predictive models for price estimation.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis and Modeling](#analysis-and-modeling)
- [Contributing](#contributing)

## Project Overview

Diamonds are evaluated based on various attributes such as carat, cut, color, and clarity. This project aims to:

- Perform exploratory data analysis (EDA) to uncover insights about the dataset.
- Build predictive models to estimate diamond prices based on their attributes.
- Provide visualizations to aid in understanding the relationships between different features and the price.

## Dataset

The dataset used in this project contains information about diamonds, including:

- **Carat**: The weight of the diamond.
- **Cut**: Quality of the cut (e.g., Fair, Good, Very Good, Premium, Ideal).
- **Color**: Diamond color, with categories ranging from D (best) to J (worst).
- **Clarity**: A measurement of how clear the diamond is (e.g., I1, SI1, SI2, VS1, VS2, VVS1, VVS2, IF).
- **Depth**: Total depth percentage.
- **Table**: Width of the top of the diamond relative to the widest point.
- **Price**: Price in US dollars.
- **X**: Length in mm.
- **Y**: Width in mm.
- **Z**: Depth in mm.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

         git clone https://github.com/fridchikn24/diamonds.git
   
         cd diamonds

3. **Install dependencies:**

Ensure you have Poetry installed. Then, run:

      poetry install

This command will create a virtual environment and install all required dependencies as specified in pyproject.toml

## Usage

Activate the virtual environment:

   poetry shell

Run the analysis:

Execute the main analysis script:

       python src/analyze_diamonds.py

This script will perform EDA, build predictive models, and generate visualizations. The results will be saved in the results directory.

## Analysis and Modeling

The project includes:

- Exploratory Data Analysis (EDA): Visualizations and statistical summaries to understand the distribution of features and their relationships with the price.
- Predictive Modeling: Building regression models to predict diamond prices based on their attributes. Models may include linear regression, decision trees, or more advanced algorithms.
- Evaluation: Assessing model performance using appropriate metrics and validation techniques.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request. Ensure that your contributions align with the project's coding standards and include appropriate tests.
