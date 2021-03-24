--
-- @lc app=leetcode id=586 lang=mysql
--
-- [586] Customer Placing the Largest Number of Orders
--
-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/
--
-- database
-- Easy (75.27%)
-- Likes:    135
-- Dislikes: 14
-- Total Accepted:    38.3K
-- Total Submissions: 50.8K
-- Testcase Example:  '{"headers":{"orders":["order_number","customer_number"]},"rows":{"orders":[[1,1],[2,2],[3,3],[4,3]]}}'
--
-- Table: Orders
--
--
-- +-----------------+----------+
-- | Column Name     | Type     |
-- +-----------------+----------+
-- | order_number    | int      |
-- | customer_number | int      |
-- +-----------------+----------+
-- order_number is the primary key for this table.
-- This table contains information about the order ID and the customer ID.
--
--
--
--
-- Write an SQL query to find the customer_number for the customer who has
-- placed the largest number of orders.
--
-- It is guaranteed that exactly one customer will have placed more orders than
-- any other customer.
--
-- The query result format is in the following example:
--
--
--
--
-- Orders table:
-- +--------------+-----------------+
-- | order_number | customer_number |
-- +--------------+-----------------+
-- | 1            | 1               |
-- | 2            | 2               |
-- | 3            | 3               |
-- | 4            | 3               |
-- +--------------+-----------------+
--
-- Result table:
-- +-----------------+
-- | customer_number |
-- +-----------------+
-- | 3               |
-- +-----------------+
-- The customer with number 3 has two orders, which is greater than either
-- customer 1 or 2 because each of them only has one order.
-- So the result is customer_number 3.
--
--
--
-- Follow up: What if more than one customer have the largest number of orders,
-- can you find all the customer_number in this case?
--

-- @lc code=start
select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1

-- @lc code=end

