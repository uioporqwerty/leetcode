--
-- @lc app=leetcode id=577 lang=mysql
--
-- [577] Employee Bonus
--
-- https://leetcode.com/problems/employee-bonus/description/
--
-- database
-- Easy (71.35%)
-- Likes:    108
-- Dislikes: 58
-- Total Accepted:    35.9K
-- Total Submissions: 50K
-- Testcase Example:  '{"headers": {"Employee": ["EmpId", "Name", "Supervisor", "Salary"], "Bonus": ["EmpId", "Bonus"]}, "rows": {"Employee": [[3, "Brad", null, 4000], [1, "John", 3, 1000], [2, "Dan", 3, 2000], [4, "Thomas", 3, 4000]], "Bonus": [[2, 500], [4, 2000]]}}'
--
-- Select all employee's name and bonus whose bonus is < 1000.
--
-- Table:Employee
--
--
-- +-------+--------+-----------+--------+
-- | empId |  name  | supervisor| salary |
-- +-------+--------+-----------+--------+
-- |   1   | John   |  3        | 1000   |
-- |   2   | Dan    |  3        | 2000   |
-- |   3   | Brad   |  null     | 4000   |
-- |   4   | Thomas |  3        | 4000   |
-- +-------+--------+-----------+--------+
-- empId is the primary key column for this table.
--
--
-- Table: Bonus
--
--
-- +-------+-------+
-- | empId | bonus |
-- +-------+-------+
-- | 2     | 500   |
-- | 4     | 2000  |
-- +-------+-------+
-- empId is the primary key column for this table.
--
--
-- Example ouput:
--
--
-- +-------+-------+
-- | name  | bonus |
-- +-------+-------+
-- | John  | null  |
-- | Dan   | 500   |
-- | Brad  | null  |
-- +-------+-------+
--
--
--

-- @lc code=start
select employee.name as name, bonus.bonus
from employee
    left join bonus
    on bonus.empId = employee.empId
where bonus.bonus < 1000 or bonus.bonus is null

-- @lc code=end

