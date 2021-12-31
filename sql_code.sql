/*Here table name is : employees*/

SELECT e.EmployeeName,
       e.Salary,
FROM employees e
WHERE Salary >
    (SELECT avg(Salary)
     FROM employees
