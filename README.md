# Homework 3 
# Wine Quality Explorer 

An interactive dashboard that lets you explore and analyze wine quality data from over 6,000 red and white wines.

## What Does This Do?
This dashboard helps you explore relationships between wine characteristics (like alcohol content, acidity, sugar) and quality ratings. In the dashboard you have the choice to:

- Filter wines by type - either red or white wine
- Adjust quality score ranges
- Set alcohol percentage ranges
- See how alcohol affects quality scores
- View quality distributions
- Download filtered data as CSV

## How to Use
- The dashboard will open automatically in your web browser

### Left Sidebar - Filters
- **Wine Type**: Choose Red or White
- **Min Quality**: Set the lowest quality score you want to see (3-9)
- **Max Quality**: Set the highest quality score you want to see (3-9)
- **Alcohol Range**: Choose the alcohol percentage range (8% - 15%)
- **Download CSV**: Export your filtered data

### Main Area - Three Tabs

**Tab 1: Scatterplot** 
- Shows how alcohol content relates to quality
- Each dot is one wine
- Hover to see exact values

**Tab 2: Bar Chart** 
- Shows how many wines have each quality score
- Easy to see which scores are most common

**Tab 3: Data Table** 
- See all the details for each wine
- Click headers to sort
- Shows chemical properties like acidity, sugar, etc.


## Data description
- **Total Wines**: 6,497 (1,599 red + 4,898 white)
- **Quality Scores**: Range from 3 (lowest) to 9 (highest)
- **Most Common Score**: 5-6 (most wines are average quality)
- **Measurements**: 12 different chemical properties per wine

### Wine Properties Measured
- Fixed acidity
- Volatile acidity  
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- **Alcohol**  - main focus for visualizations
- **Quality**  - we are analyzing

## Key Findings
- Most wines score 5 or 6 out of 9
- Higher alcohol content tends to mean higher quality
- White wines make up 75% of the dataset
- Very few wines score below 4 or above 7


## Why I Built This
This project was created to:
1. Learn how to build interactive dashboards
2. Practice data visualization
3. Explore real-world wine quality data
4. Compare custom coding vs AI-generated solutions

## Issues
- After adjusting the sidebar and choosing your specific filters, the user
  may need to reload the website in order to see the resulting visualization/data

## Data Source
Wine Quality Dataset from the UCI Machine Learning Repository


