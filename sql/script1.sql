
CREATE DATABASE IF NOT EXISTS retail_sales_db;

USE retail_sales_db;

SELECT COUNT(*) 
FROM retail_sales;

SELECT * 
FROM retail_sales
LIMIT 10;

DESCRIBE retail_sales;

USE retail_sales_db;

SELECT
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT `Order ID`) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity_Sold,
    AVG(Sales) AS Average_Sales
FROM retail_sales;

SELECT
    Category,
    SUM(Sales) AS Total_Revenue
FROM retail_sales
GROUP BY Category
ORDER BY Total_Revenue DESC;

SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY Category
ORDER BY Total_Profit DESC;

SELECT
    Region,
    SUM(Sales) AS Total_Revenue
FROM retail_sales
GROUP BY Region
ORDER BY Total_Revenue DESC;

SELECT
    Region,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY Region
ORDER BY Total_Profit DESC;

SELECT
    `Customer Segment`,
    SUM(Sales) AS Total_Revenue
FROM retail_sales
GROUP BY `Customer Segment`
ORDER BY Total_Revenue DESC;

SELECT
    `Customer Segment`,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY `Customer Segment`
ORDER BY Total_Profit DESC;

SELECT 
    `Sub-Category`, SUM(Sales) AS Total_Revenue
FROM
    retail_sales
GROUP BY `Sub-Category`
ORDER BY Total_Revenue DESC;

SELECT
    `Sub-Category`,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY `Sub-Category`
ORDER BY Total_Profit DESC;

SELECT
    Discount,
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM retail_sales
GROUP BY Discount
ORDER BY Discount;

SELECT
    `Ship Mode`,
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM retail_sales
GROUP BY `Ship Mode`
ORDER BY Total_Revenue DESC;

SELECT
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Sales_Month,
    SUM(Sales) AS Monthly_Revenue,
    SUM(Profit) AS Monthly_Profit
FROM retail_sales
GROUP BY Sales_Month
ORDER BY Sales_Month;

SELECT
    City,
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit
FROM retail_sales
GROUP BY City
ORDER BY Total_Revenue DESC;

