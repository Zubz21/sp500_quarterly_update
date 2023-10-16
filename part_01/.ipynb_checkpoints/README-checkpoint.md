# S&P 500 Predictive Analysis


## Introduction:
---
The S&P 500 is one of the most widely followed equity indices in the world, reflecting the performance of 500 large companies listed on U.S. stock exchanges. Companies are periodically added and removed. This project aims to predict potential changes based on financial indicators.

## Problem Statement:
---
To predict which companies might be at risk of being delisted from the S&P 500 and suggest potential replacements using financial indicators and data analysis techniques.

## Data Collection:
---
We will be sourcing our data from Alpha Vantage, focusing on:

* 1000 stocks
* Quarterly earnings (net income) for the last 8 quarters.
* Monthly trading volume for the past 12 months.
* Market Capitalization.
* Time since the oldest data (an approximation for time since IPO or listing).
* Market Sentiment (NLP Piece)

## Models and Approach:
---
* Exploratory Data Analysis (EDA): We'll first analyze the distribution of our key metrics among current S&P 500 companies and those outside it.
* Feature Engineering: Construct composite metrics like average earnings growth over quarters, average trading volume, etc.
* Modeling: Given this is a classification problem (whether a company will be added or removed), we'll start with logistic regression and then explore tree-based models.
* Validation: Use historical changes in S&P 500 as our validation set.

## Hypotheses to Test:
---
* Companies with declining quarterly earnings over consecutive quarters are more likely to be delisted.
* Younger companies (based on our approximation of time since listing) are less likely to be added unless they have significant market capitalization or trading volumes.
* A company's market capitalization and trading volume relative to others might be strong indicators of its likelihood to be added or removed.

By the end of this project, we aim to provide an insightful analysis that can serve as a guiding tool for investors and market enthusiasts to anticipate the future composition of the S&P 500.

