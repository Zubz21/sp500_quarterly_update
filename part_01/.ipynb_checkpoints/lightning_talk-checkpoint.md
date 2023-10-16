# Lightning Talk
# Problem Statement:
---
Predict which companies in the S&P 500 might be at risk of being delisted and suggest potential replacements based on an analysis of various financial indicators including earnings, trading volume, market capitalization, and time since IPO.

# Audience:
---
Investors, financial analysts, fund managers, and anyone interested in the stock market's dynamics, especially those tracking or investing in index funds.

# Success Metric:
---
The accuracy with which the model can match historical additions and deletions from the S&P 500. A post-analysis after the next quarterly review of the index to see how many of our predictions align with actual changes.

# Data Source & Format:
---
The data will be fetched using the Alpha Vantage API. The acquired data will be in JSON format which we will convert and store in a structured dataframe.

# Challenges & Mitigation:
---
* Data Limitations: Alpha Vantage provides limited data. We may not have all historical IPO dates, requiring approximations.
* Qualitative Factors: The S&P 500's criteria for inclusion/exclusion isn't purely quantitative. There are subjective decisions. To mitigate, our focus will be largely on the quantifiable metrics, while acknowledging this limitation.
* API Limitations: Rate limits and data request constraints. We'll include pauses in our data collection routines to prevent hitting these limits.

# Feasibility:
---
With 22 days, constructing the data pipeline, performing exploratory data analysis, modeling, and validation can be tight. However, by focusing on a subset of key indicators and establishing a clear workflow early on, it should be feasible.