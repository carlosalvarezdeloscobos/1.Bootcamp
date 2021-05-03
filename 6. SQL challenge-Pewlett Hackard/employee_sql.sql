---HMWK

--SECTION I create tables & import data

-- TABLE 1 DEPARTMENT NUMBER
CREATE TABLE departments (
  dept_no VARCHAR(30) NOT NULL PRIMARY KEY,
  dept_name VARCHAR(30) NOT NULL
  
);


-- Table  2 ID AND DEPT NO
CREATE TABLE dept_emplo (
  emp_no VARCHAR(30) NOT NULL,
  dept_no VARCHAR(30) NOT NULL 
);

-- Table  3 DEPT_MANAGER
CREATE TABLE dept_manager (
  dept_no VARCHAR(30) NOT NULL, 
  emp_no VARCHAR(30) NOT NULL

);


-- Table  6 TITLES
CREATE TABLE titles (
  title_id VARCHAR(30) NOT NULL,
  title  VARCHAR(30) NOT NULL

);

-- Table  4 EMPLOYEES
CREATE TABLE employee (
  emp_no VARCHAR(30) NOT NULL,
  emp_title_id VARCHAR(30) NOT NULL,
  birth_date DATE NOT NULL,
  fn VARCHAR(30) NOT NULL,
  last_name  VARCHAR(30) NOT NULL,
  sex VARCHAR(30) NOT NULL,
  hire_date DATE NOT NULL 
);

-- Table  5 SALARY
CREATE TABLE people (
  emp_no VARCHAR(30) NOT NULL,
  salary INT
);


SELECT * FROM employee


--section II List the following details of each employee: employee number, last name, first name, sex, and salary
SELECT employee.emp_no ,employee.last_name , employee.fn , employee.sex, people.salary
FROM people
INNER JOIN employee ON
employee.emp_no= people.emp_no

--section III List first name, last name, and hire date for employees who were hired in 1986.

SELECT fn, last_name,EXTRACT(YEAR FROM hire_date) FROM employee
WHERE EXTRACT(YEAR FROM hire_date)= '1986'

-- section IV List the MANAGER of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name.

SELECT dept_manager.dept_no,dept_manager.emp_no,employee.emp_no, employee.fn , employee.last_name ,departments.dept_name,departments.dept_no
FROM dept_manager
LEFT JOIN employee 
ON dept_manager.emp_no= employee.emp_no
INNER JOIN departments
ON departments.dept_no=dept_manager.dept_no
ORDER BY departments.dept_name

-- section V List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT employee.emp_no, employee.fn , employee.last_name ,dept_emplo.emp_no,dept_emplo.dept_no,departments.dept_name,departments.dept_no
FROM employee
LEFT JOIN dept_emplo
ON employee.emp_no=dept_emplo.emp_no
INNER JOIN departments
ON departments.dept_no=dept_emplo.dept_no

--section VI List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT fn, last_name ,sex
FROM employee
WHERE fn = 'Hercules' 


--section VII List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT employee.emp_no, employee.fn , employee.last_name ,dept_emplo.emp_no,dept_emplo.dept_no,departments.dept_no,departments.dept_name
FROM employee
INNER JOIN dept_emplo
ON employee.emp_no=dept_emplo.emp_no
LEFT JOIN departments
ON departments.dept_no= dept_emplo.dept_no
WHERE dept_name = 'Sales'

-- section VIII List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT employee.emp_no, employee.fn , employee.last_name ,dept_emplo.emp_no,dept_emplo.dept_no,departments.dept_no,departments.dept_name
FROM employee
INNER JOIN dept_emplo
ON employee.emp_no=dept_emplo.emp_no
LEFT JOIN departments
ON departments.dept_no= dept_emplo.dept_no
WHERE dept_name = 'Sales'
OR dept_name ='Development'


--section IX descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(last_name) 
FROM employee
GROUP BY last_name;




