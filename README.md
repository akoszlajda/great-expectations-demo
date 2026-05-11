Great Expectations 1.1.1 (GX) Demo - all in one box

A. What for?
  To verify how Great Expectations (Python library) can truely and constantly validate data and improve data quality.
  
B. What was done?
  1. test_personal_data.py - Python script presenting from one script among other email regex validations
  2. test_sales_quality.py - Python script presenting walidation of data frame imported from csv file among other time format validation
  3. sales_2024_01.csv - sample csv file used by 2nd script
  
  Key notes:
  - GX 1.1.1
  - Python 3.11.8 (compatible with GX 1.1.1)
  - Venv used to create virtual environment
  - Jupyter for running scripts
  - Free version of ChatGPT for Q&A sessions
  - In GX 1.1.1 following sctructure needs to be implemented:
    Context
     -> Datasource
      -> Asset
       -> Batch Definition
        -> Batch
         -> Validator
          -> Expectations

C. Date of creation: 11-05-2026
D. Author: Adam Koszlajda, akoszlajda@gmail.com
