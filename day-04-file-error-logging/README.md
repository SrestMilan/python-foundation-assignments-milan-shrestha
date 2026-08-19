<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<h1>Day 4: Python Foundations</h1>

</head>
<body>


<h2>Topics Covered</h2>
<ul>
  <li>File Handling (I/0)</li>
  <li>Modules (csv,json)</li></li>
  <li>Custom Exceptions</li>
  <li>Exceptions Handling </li>
  <li>Logging Module</li>
  <li>List Comprehensions</li>
 
</ul>

<h2>Exercises</h2>
<ol>
  <li>
    <strong>Line & Word Counter</strong><br>
     Uses file handling with context managers, reading lines via readlines(), and counting words with split() on whitespace.
  </li>
  <li>
    <strong>Inventory Value from CSV</strong><br>
   Reads product data from a file, converts text values to numbers, and calculates the total inventory worth.
  </li>
  <li>
    <strong>JSON Library Filter</strong><br>
 Loads book records from a file, picks out available ones published after a given year, and saves their titles.
    
  </li>
  <li>
    <strong>Custom Exception Handling </strong><br>
   Checks if an age is valid, raises a clear error when it isn't, and handles that error gracefully.
  </li>
  <li>
    <strong>Order Pipeline with Logging</strong><br>
  Reads order data, validates each row, skips and records bad entries, then saves the good ones with totals.
  </li>
 
</ol>

<h2>What I Learned</h2>
<p>
I learned how to handle files safely using context managers, read and parse CSV data with DictReader, and load/dump structured JSON. I practiced converting string inputs to proper numeric types, building custom exception classes, and managing errors with try/except/else/finally. I also implemented logging with FileHandler and Formatter to track successes and failures instead of using print statements, while validating data row-by-row in a real processing pipeline.
</p>

<h2>Challenges Faced</h2>
<p>
 I struggled with remembering to assign json.load(f)'s return value to a variable instead of discarding it, which caused a NameError. I found it tricky to correctly convert CSV string values without breaking on invalid rows like "not_a_number". Setting up logging correctly, especially avoiding duplicate handlers on re-runs, took some trial and error. I also had to be careful catching specific exceptions like InvalidAgeError versus generic ValueError without mixing up their logic.
</p>

</body>
</html>
