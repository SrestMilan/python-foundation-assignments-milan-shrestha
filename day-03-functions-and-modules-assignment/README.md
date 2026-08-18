<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<h1>Day 3: Python Foundations</h1>

</head>
<body>


<h2>Topics Covered</h2>
<ul>
  <li>Functions</li>
  <li>Modules</li></li>
  <li>Standard library</li>
  <li>Variable and Constants </li>
  <li>Operators and Expression</li>
  <li>String Formatting</li>
  <li>Data Structures</li>
</ul>

<h2>Exercises</h2>
<ol>
  <li>
    <strong>Simple Interest Calculator</strong><br>
     Calculated interest using default and keyword arguments, with rate and time falling back to preset  values when omitted.
  </li>
  <li>
    <strong>Class Average using *args</strong><br>
   Averaged any number of scores using variable-length arguments, handling the zero-scores case with exception handling.
  </li>
  <li>
    <strong>Analyze Numbers</strong><br>
 Found the min, max, sum, and descending sort of a number list, returning all four values at once via tuple unpacking.
    
  </li>
  <li>
    <strong>Shared Booking Counter </strong><br>
   Tracked a running total of booked seats across multiple function calls using a global variable, with a reset option.
  </li>
  <li>
    <strong>Temperature Report Module</strong><br>
  Built a custom module for Celsius-Fahrenheit conversion, then combined it with random and datetime to generate and print a randomized temperature report.
  </li>
 
</ol>

<h2>How to Run</h2>
<p>Each exercise is provided as a Python file. Run an exercise using:</p>
<p>For example:</p>
<pre><code>python exercise-01-batch-proecessor.py</code></pre>
<pre><code>python exercise-02-data-retry-simulation.py</code></pre>
<pre><code>python exercise-03-clean-values.py</code></pre>
<pre><code>python exercise-04-sales-analyis.py</code></pre>
<pre><code>python exercise-05-dataset-comparison.py</code></pre>
<pre><code>python exercise-06-student-scores.py</code></pre>
<pre><code>python exercise-05-order-summary.py</code></pre>
<pre><code>python stretch-contact-book.py</code></pre>

<h2>What I Learned</h2>
<p>
I faced challenges understanding when to use the global keyword versus creating local variables, and initially confused how *args collects arguments into a tuple. Handling the zero-scores edge case with ZeroDivisionError required careful thought. Creating a module and importing it correctly took some trial and error, especially ensuring file paths matched. Combining random, datetime, and my own module together while formatting output with f-strings and strftime() also took extra practice to get right.
</p>

<h2>Challenges Faced</h2>
<p>
I found it challenging to understand how key=lambda item: item[1] directed comparisons by value instead of by key. Structuring a while True loop carefully to avoid infinite loops was another hurdle, along with ensuring break only triggered on the correct exit condition. I also had to think through how to handle missing dictionary keys safely, using membership checks like if name in contacts to avoid runtime crashes. Keeping code organized and avoiding variable name clashes took some extra care as well.
</p>

</body>
</html>
