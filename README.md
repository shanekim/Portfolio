# Portfolio

### Washington Alloy

#### Product Recommendation Engine

Washington Alloy has +3000 unique inventory items across the nationwide warehouses. In order to help salesperson to increase sales by recommending the right products, it's important to identify similar purchase pattern among different customers and rank the score of recommendation results. I used Matrix Factorization model which learns latent features and interaction between customers and products. This way, recommendations are both customer-specific and item-specific.

Refer to: Matrix Factorization based Recommendation.ipynb


#### Web Scraper for Marketing Campaign

Launching a new product always needs right marketing campaigns. We chose to perform a direct mail postcard marketing, and in order to collect all of potential customers' geographical information such as address, phone number, etc, I built Python web scrapers that automatically type zipcode, hit the search button, load a full page with infinite scroll, and create dataframes that are stored in AWS RDS and DynamoDB.

Refer to: dealer_scraper - Copy.py, dealer_dynamodb - Copy.py


#### Streamlining Inventory Management Process

A variety of item selections is one of the most important competitive edges. And it's critical to always keep adequate stocking levels across all the warehouses. Acumatica ERP solution retains all of related datasets; however, data points were very spread out so I used Python and SQL, joining all required tables and clean/manipulate/transform them in order to improve data quality. 

Result: Created a clear high-level visual dashboard that tracks stock levels and financial performance at multiple granularity levels (Customer, Inventory ID, Date, etc)

Refer to: Inventory management - Stock Transfer_.ipynb


### Projects from Columbia University & Dataquest

Refer to: Kaggle Project.ipynb

Refer to: Decision Tree & Bias-Variance Tradeoff.ipynb

Refer to: K-nearest Neighbors.ipynb

Refer to: Simple project - Predicting bike rentals.ipynb
