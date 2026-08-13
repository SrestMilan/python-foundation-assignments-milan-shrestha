<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day 02 — Loops and Data Structures</title>
<style>
  :root {
    --bg: #0d1117;
    --bg-panel: #11161d;
    --ink: #c9d1d9;
    --ink-dim: #8b949e;
    --accent: #58a6ff;
    --accent-soft: #1f2937;
    --ok: #3fb950;
    --border: #21262d;
    --mono: "SFMono-Regular", "JetBrains Mono", Consolas, "Courier New", monospace;
    --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: var(--sans);
    line-height: 1.6;
  }

  .wrap {
    max-width: 820px;
    margin: 0 auto;
    padding: 64px 24px 96px;
  }

  header.top { margin-bottom: 48px; }

  .eyebrow {
    font-family: var(--mono);
    font-size: 12px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 0 0 12px;
  }

  h1 {
    font-size: 34px;
    line-height: 1.2;
    margin: 0 0 8px;
    letter-spacing: -0.01em;
  }

  .subtitle { color: var(--ink-dim); font-size: 15px; margin: 0; }

  section { margin-top: 56px; }

  h2 {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--ink-dim);
    border-bottom: 1px solid var(--border);
    padding-bottom: 12px;
    margin: 0 0 20px;
    font-family: var(--mono);
  }

  h2::before { content: "// "; color: var(--accent); }

  ul, ol { padding-left: 22px; margin: 0; }
  li { margin-bottom: 10px; }
  li::marker { color: var(--accent); }

  code {
    font-family: var(--mono);
    font-size: 0.88em;
    background: var(--accent-soft);
    color: #e6edf3;
    padding: 2px 6px;
    border-radius: 4px;
  }

  .exercise-list { list-style: none; padding: 0; counter-reset: ex; }

  .exercise-list li {
    counter-increment: ex;
    position: relative;
    padding: 14px 16px 14px 52px;
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 10px;
  }

  .exercise-list li::before {
    content: counter(ex, decimal-leading-zero);
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent);
  }

  .exercise-list li::marker { content: none; }

  .exercise-title { color: #e6edf3; font-weight: 600; }

  .stretch-badge {
    display: inline-block;
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.06em;
    color: var(--ok);
    border: 1px solid var(--ok);
    border-radius: 4px;
    padding: 1px 6px;
    margin-right: 8px;
    vertical-align: middle;
  }

  pre {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 18px 20px;
    overflow-x: auto;
    font-family: var(--mono);
    font-size: 13px;
    color: #e6edf3;
    line-height: 1.55;
  }

  .step { margin-bottom: 24px; }

  .step-label {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent);
    margin-bottom: 6px;
  }

  .menu-key { display: inline-flex; align-items: center; gap: 10px; margin: 4px 0; }

  .menu-key kbd {
    font-family: var(--mono);
    background: var(--accent-soft);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 2px 8px;
    color: #e6edf3;
    font-size: 12px;
  }

  footer {
    margin-top: 72px;
    padding-top: 20px;
    border-top: 1px solid var(--border);
    color: var(--ink-dim);
    font-size: 13px;
    font-family: var(--mono);
  }

  @media (max-width: 560px) {
    .wrap { padding: 40px 18px 72px; }
    h1 { font-size: 26px; }
  }
</style>
</head>
<body>
<div class="wrap">

  <header class="top">
    <p class="eyebrow">30 Days of Python &middot; Log Entry</p>
    <h1>Day 02 — Loops and Data Structures</h1>
    <p class="subtitle">A working log of exercises, concepts, and gotchas from today's session.</p>
  </header>

  <section>
    <h2>Topics Covered</h2>
    <ul>
      <li><code>for</code> loops and <code>range()</code></li>
      <li><code>while</code> loops and <code>break</code></li>
      <li>Modulo operator (<code>%</code>) for patterns</li>
      <li>Cleaning data with loops and <code>isinstance()</code></li>
      <li>List comprehensions</li>
      <li>Built-in functions: <code>sorted()</code>, <code>sum()</code>, <code>len()</code>, <code>max()</code></li>
      <li>Set operations: union, intersection, difference</li>
      <li>Dictionaries: iteration, filtering, and comprehensions</li>
      <li>Nested dictionaries</li>
      <li>Simple interactive menu using <code>while True</code> and <code>break</code></li>
    </ul>
  </section>

  <section>
    <h2>Exercises Completed</h2>
    <ol class="exercise-list">
      <li><span class="exercise-title">Batch Processor</span> — Loop through batches 1–10 and print a checkpoint every 3 batches.</li>
      <li><span class="exercise-title">Retry Simulation</span> — Simulate up to 3 retry attempts with early exit on success.</li>
      <li><span class="exercise-title">Clean Numeric Values</span> — Filter a mixed list to keep only valid integers (loop + list comprehension).</li>
      <li><span class="exercise-title">Sales List Analysis</span> — Sort sales, filter high values, add tax, compute total and average.</li>
      <li><span class="exercise-title">Dataset Comparison</span> — Use sets to find union, intersection, and differences between two datasets.</li>
      <li><span class="exercise-title">Student Score Dictionary</span> — Iterate over a dictionary, filter passing students, find top student, compute average.</li>
      <li><span class="exercise-title">Nested Order Summary</span> — Work with nested dictionaries to summarize orders and add a new order.</li>
      <li><span class="stretch-badge">Stretch</span><span class="exercise-title">Contact Book Menu</span> — Interactive contact book with add, search, delete, display, and exit options.</li>
    </ol>
  </section>

  <section>
    <h2>What I Learned</h2>
    <ul>
      <li>How to control loop execution using conditions and <code>break</code>.</li>
      <li>How to use the modulo operator to trigger actions at regular intervals.</li>
      <li>How to clean messy data by checking types with <code>isinstance()</code> and skipping invalid entries.</li>
      <li>How list and dictionary comprehensions can replace longer loops for filtering and transforming data.</li>
      <li>How to use set operations to compare groups of items.</li>
      <li>How to work with nested dictionaries and extract aggregated information (totals, counts, averages).</li>
      <li>How to build a simple text-based menu that keeps running until the user chooses to exit.</li>
    </ul>
  </section>

  <section>
    <h2>Challenges Faced</h2>
    <ul>
      <li>Understanding how <code>key=lambda item: item[1]</code> works with <code>max()</code> on dictionary items.</li>
      <li>Making sure loops stop correctly (avoiding infinite loops in the menu).</li>
      <li>Handling missing contacts in the contact book without crashing (using <code>if name in contacts</code>).</li>
      <li>Organizing code so each exercise is clear and easy to run separately.</li>
    </ul>
  </section>

  <section>
    <h2>How to Run the Programs</h2>

    <div class="step">
      <div class="step-label">1. Clone or open your GitHub repository</div>
      <pre>git clone &lt;your-repo-url&gt;
cd &lt;repo-folder&gt;/day-02-loops-and-data-structures</pre>
    </div>

    <div class="step">
      <div class="step-label">2. Make sure you have Python installed</div>
      <pre>python --version
# or
python3 --version</pre>
    </div>

python exercise-02-retry-simulation.ipynb
python exercise-03-clean-values.ipynb
python exercise-04-sales-analysis.ipynb
python exercise-05-dataset-comparison.ipynb
python exercise-06-student-scores.ipynb
python exercise-07-order-summary.ipynb
python stretch-contact-book.ipynb</pre>
      <p style="color:var(--ink-dim); font-size:14px; margin-top:10px;">On some systems you may need <code>python3</code> instead of <code>python</code>.</p>
    </div>

  </section>

  <footer>
    All scripts are self-contained and do not require any external libraries beyond standard Python.
  </footer>

</div>
</body>
</html>
