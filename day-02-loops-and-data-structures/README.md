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