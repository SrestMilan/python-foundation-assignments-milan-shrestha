<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 3 — Functions and Modules</title>
    <style>
        :root {
            --bg: #ffffff;
            --text: #1f2328;
            --muted: #57606a;
            --border: #d0d7de;
            --code-bg: #f6f8fa;
            --accent: #0969da;
            --checked: #1a7f37;
        }
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            max-width: 860px;
            margin: 48px auto;
            padding: 0 24px;
            line-height: 1.6;
            color: var(--text);
            background: var(--bg);
        }
        h1 {
            font-size: 2rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.4em;
            margin-top: 0;
        }
        h2 {
            font-size: 1.4rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.3em;
            margin-top: 2em;
        }
        h3 {
            font-size: 1.15rem;
            margin-top: 1.6em;
            color: var(--accent);
        }
        code {
            background: var(--code-bg);
            padding: 0.15em 0.4em;
            border-radius: 6px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: 0.9em;
        }
        pre {
            background: var(--code-bg);
            padding: 14px 16px;
            border-radius: 8px;
            overflow-x: auto;
            border: 1px solid var(--border);
        }
        pre code {
            background: none;
            padding: 0;
            font-size: 0.85em;
        }
        ul, ol {
            padding-left: 1.6em;
        }
        li {
            margin: 0.3em 0;
        }
        .status-list {
            list-style: none;
            padding-left: 0;
        }
        .status-list li {
            display: flex;
            align-items: center;
            gap: 0.5em;
        }
        .status-list li::before {
            content: "✔";
            color: var(--checked);
            font-weight: bold;
        }
        .file-tree {
            font-family: "SFMono-Regular", Consolas, Menlo, monospace;
            background: var(--code-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 14px 16px;
            font-size: 0.9em;
            white-space: pre;
        }
        strong { color: var(--text); }
    </style>
</head>
<body>

    <h1>Day 3 — Functions and Modules</h1>

    <h2>Overview</h2>
    <p>
        This folder contains my Day 3 Python assignments focused on
        <strong>Functions and Modules</strong>.
    </p>
    <p>
        The exercises cover default arguments, <code>*args</code>, built-in functions,
        multiple return values, variable scope, the <code>global</code> keyword,
        custom modules, and Python's standard library modules.
    </p>

    <h2>Topics Covered</h2>
    <ul>
        <li>Functions with default arguments</li>
        <li>Variable-length arguments using <code>*args</code></li>
        <li>Built-in functions: <code>min()</code>, <code>max()</code>, <code>sum()</code>, and <code>sorted()</code></li>
        <li>Multiple return values</li>
        <li>Global variables and the <code>global</code> keyword</li>
        <li>Creating and importing custom Python modules</li>
        <li>Using the <code>random</code> module</li>
        <li>Using the <code>datetime</code> module</li>
    </ul>

    <h2>Exercises</h2>

    <h3>Question 1 — Simple Interest Calculator</h3>
    <p>
        Created a <code>calculate_simple_interest()</code> function using default
        arguments for the interest rate and time.
    </p>
    <p>Formula:</p>
    <pre><code>Interest = (Principal × Rate × Time) / 100</code></pre>

    <h3>Question 2 — Class Average</h3>
    <p>
        Created a <code>class_average()</code> function using <code>*args</code>
        to accept any number of scores.
    </p>
    <p>The function calculates the average and returns <code>0</code> when no scores are provided.</p>

    <h3>Question 3 — Analyze Numbers</h3>
    <p>Created an <code>analyze_numbers()</code> function that returns:</p>
    <ol>
        <li>Smallest number</li>
        <li>Largest number</li>
        <li>Sum of all numbers</li>
        <li>Numbers sorted in descending order</li>
    </ol>
    <p>
        The solution uses Python's built-in <code>min()</code>, <code>max()</code>,
        <code>sum()</code>, and <code>sorted()</code> functions.
    </p>

    <h3>Question 4 — Shared Booking Counter</h3>
    <p>
        Created a simple booking system using a global variable called
        <code>total_seats_booked</code>.
    </p>
    <p>
        The <code>book_seats()</code> function increases the total number of booked
        seats, while <code>reset_bookings()</code> resets the counter to zero.
    </p>
    <p>Both functions demonstrate the use of the <code>global</code> keyword.</p>

    <h3>Question 5 — Temperature Report Module</h3>
    <p>Created a custom module named <code>temperature_utils.py</code>.</p>
    <p>The module contains:</p>
    <ul>
        <li><code>celsius_to_fahrenheit()</code></li>
        <li><code>fahrenheit_to_celsius()</code></li>
        <li><code>MODULE_VERSION</code></li>
    </ul>
    <p>
        The notebook also uses the <code>random</code> module to generate Celsius
        temperatures and the <code>datetime</code> module to display the current date.
    </p>

    <h2>Files</h2>
    <div class="file-tree">day-03/
│
├── functions_and_modules.ipynb
└── temperature_utils.py</div>

    <h2>Key Learning</h2>
    <p>
        Through these exercises, I practiced creating reusable functions, working
        with different types of function arguments, managing variable scope,
        returning multiple values, and creating custom Python modules.
    </p>

    <h2>Status</h2>
    <ul class="status-list">
        <li>Question 1 — Simple Interest Calculator</li>
        <li>Question 2 — Class Average</li>
        <li>Question 3 — Analyze Numbers</li>
        <li>Question 4 — Shared Booking Counter</li>
        <li>Question 5 — Temperature Report Module</li>
    </ul>

</body>
</html>