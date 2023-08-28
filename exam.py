#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


import mysql.connector as syed


# In[3]:


mydb = syed.connect(host = 'localhost',user='root',passwd="ammi")


# In[ ]:


mydb


# In[4]:


cursor = mydb.cursor()


# In[ ]:





# In[ ]:


11 answer


# In[ ]:


CREATE TABLE Student (
    ID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(20) NOT NULL,
    Age INT NOT NULL,
    Address VARCHAR(25)
);

INSERT INTO Student (ID, Name, Age, Address) VALUES
(1, 'John Doe', 20, '123 Main St, City A'),
(2, 'Jane Smith', 22, '456 Elm St, City B'),
(3, 'Michael Johnson', 21, '789 Oak St, City C'),
(4, 'Emily Brown', 23, '101 Pine St, City D'),
(5, 'William Wilson', 19, '555 Maple St, City E');


# In[ ]:


12 answer


# In[ ]:


SELECT * FROM Student
ORDER BY Age
LIMIT 1;


# In[ ]:


13


# In[ ]:


SELECT
    p.first_name,
    p.last_name,
    a.city,
    a.state
FROM
    Person p
JOIN
    Address a ON p.personalid = a.personalid;


# In[ ]:


14


# In[ ]:


SELECT MAX(Age) AS SecondHighestAge
FROM Student
WHERE Age < (SELECT MAX(Age) FROM Student);


# In[ ]:


15


# In[ ]:


SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT n-1, 1;


# In[ ]:


19 answer


# In[ ]:


SELECT
    c.CustomerName,
    COUNT(o.OrderID) AS OrderCount
FROM
    Customers c
JOIN
    Orders o ON c.CustomerID = o.CustomerID
GROUP BY
    c.CustomerID, c.CustomerName
ORDER BY
    OrderCount DESC, c.CustomerName ASC
LIMIT 5;


# In[ ]:


20 answer


# In[ ]:


SELECT
    b.title AS BookTitle,
    SUM(o.quantity) AS TotalQuantitySold
FROM
    books b
JOIN
    orders o ON b.book_id = o.book_id
GROUP BY
    b.book_id, b.title
ORDER BY
    TotalQuantitySold DESC
LIMIT 3;


# In[ ]:




