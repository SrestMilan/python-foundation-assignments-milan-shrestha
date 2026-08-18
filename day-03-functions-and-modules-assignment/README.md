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
    <strong>Batch Processor</strong><br>
     iterate value from 1-0 and check checkpoint in every 3 batches.
  </li>
  <li>
    <strong>Retry Simulation</strong><br>
    Simulated retries with a loop, tracking success and stopping early.
  </li>
  <li>
    <strong>Clean Numeric Values</strong><br>
    Filtered a mixed list to keep only valid integers, removing invalid types like text and empty values.
    
  </li>
  <li>
    <strong>Sales List Analysis </strong><br>
    Sorted, filtered, and taxed a sales list, then calculated total and average revenue across all months.
  </li>
  <li>
    <strong>Dataset Comparison</strong><br>
  Compared two datasets to find combined, shared, and exclusive items between them using set operations.
  </li>
  <li>
    <strong>Student Score Dictionary</strong><br>
 Filtered passing students, found the topper, and calculated the class average from a dictionary of scores.
  </li>
  <li>
    <strong>Nested Order Summary</strong><br>
Summarized nested order data by filtering completed orders, totaling revenue, counting pending ones, and adding a new order
  </li>
  <li>
    <strong>Stretch: Contact Book Menu </strong><br>
  Interactive contact book with add, search, delete, and display options using a menu loop.
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
I strengthened my command of Python's core iteration constructs, using for and while loops alongside break and continue for precise flow control during sequential and retry-based processing. I applied isinstance() for type validation while cleaning mixed-type datasets, and built list and dictionary comprehensions to concisely filter and transform data, replacing verbose loop-based logic. I leveraged built-in functions like sorted(), sum(), len(), and max() with lambda keys for aggregation and ranking tasks. I practiced set operations—union, intersection, and difference—to compare datasets efficiently, and iterated nested dictionaries to summarize grouped records. Finally, I implemented a menu-driven interactive contact book using safe membership checks (in) to prevent runtime exceptions on missing keys.
</p>

<h2>Challenges Faced</h2>
<p>
I found it challenging to understand how key=lambda item: item[1] directed comparisons by value instead of by key. Structuring a while True loop carefully to avoid infinite loops was another hurdle, along with ensuring break only triggered on the correct exit condition. I also had to think through how to handle missing dictionary keys safely, using membership checks like if name in contacts to avoid runtime crashes. Keeping code organized and avoiding variable name clashes took some extra care as well.
</p>

</body>
</html>
