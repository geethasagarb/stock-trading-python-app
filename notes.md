# Stock Trading Python App - Notes

## Project Overview
This project fetches stock ticker data from the Polygon API and exports it to CSV format.

## Current Status
- ✅ Basic API integration with Polygon.io
- ✅ Pagination handling for large datasets
- ✅ CSV export functionality
- ✅ Schema matching with example ticker format

## API Details
- **Endpoint**: `https://api.polygon.io/v3/reference/tickers`
- **Market**: stocks
- **Status**: active tickers only
- **Limit**: 1000 per request
- **Sort**: by ticker symbol

## Data Schema
The CSV output includes the following fields:
- `ticker` - Stock symbol
- `name` - Company name
- `market` - Market type (stocks)
- `locale` - Geographic region (us)
- `primary_exchange` - Exchange code (e.g., XNAS)
- `type` - Security type (e.g., CS for Common Stock)
- `active` - Trading status
- `currency_name` - Currency (usd)
- `cik` - Central Index Key
- `composite_figi` - Composite FIGI identifier
- `share_class_figi` - Share class FIGI identifier
- `last_updated_utc` - Last update timestamp

## Notes Section
*Add your notes, observations, and ideas here:*

### [Date] - [Your Note Title]
- Note content goes here
- Additional thoughts
- Questions or next steps

---

## TODO Items
- [ ] Add error handling for API responses
- [ ] Implement data validation
- [ ] Add logging functionality
- [ ] Consider data filtering options
- [ ] Add progress indicators for large datasets

## Resources
- [Polygon.io API Documentation](https://polygon.io/docs)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)


# How do data pipelines work
# Data pipeline is the ability to have a flow of information that can be translated into insight and knowledge so that the business can make a better decision.

# example: someone clicking buttons on my app and that generates events and then those events are pumped into a database and then enriched with other data. then we how many clicks in particular location ?

# RDBMS and Data Lake architecture
# Now with data lake arch - consolidating all of data form production, hubspot, 3rd party and clicks data into one -- s3 if in amazon, gcp, azure etc.

# CRON is the technology that allows data pipelines to schedule and this causes the magic. This is the automation part.

# Fundamental component of 90% of data pipelines and data engineering.
# CRON based on computers clock and based on a number of seconds since January 1st 1970 every 80,000 ish seconds would be once a day.

# CRON runs all the time in the background whether you click or not. these are based on epochs and starts from 1970 before that -ve numbers.

# CRON - fundamental technology behind all of the pipeline tools like Airflow and Dagster, prefect and mage and Data Bricks workflows etc.

# CRON allows all these tools to schedule to run pipelines to run once a day or once an hour.

# another scenario where fraud detection is a example of pipeline where it needs to run in real time. 

# whats the diff between cron and realtime ? -- Realtime does not run on schedule and they run all the time. 
# Real time listens and just waits for events to come in and process.
# expensive and harder  to maintain, complicated and require lot more technical skills.

# 3rd type of pipeline - which runs on demand -- example like pipeline gets triggered when someone does signup to start build their profile.

