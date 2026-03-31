<!DOCTYPE html>
<html>
<head>
  
</head>
<body>

<h1>Product Intelligence Dashboard</h1>

<h2>📌 Project Overview</h2>
<p>
This is a <b>practice-based end-to-end data project</b> where I built a complete data pipeline using real-world tools and technologies.
The project focuses on collecting product data from multiple sources, cleaning it, analyzing it, and presenting insights through a web dashboard.
</p>

<h2>🎯 Objective</h2>
<p>The main goal of this project was to revise and strengthen core data skills:</p>
<ul>
<li>Web Scraping</li>
<li>API Integration</li>
<li>Data Cleaning</li>
<li>Data Analysis</li>
<li>Data Visualization</li>
<li>SQL Database Handling</li>
<li>Flask (Web Development)</li>
</ul>

<h2>⚙️ Technologies Used</h2>
<ul>
<li>Python</li>
<li>Pandas & NumPy</li>
<li>BeautifulSoup & Requests</li>
<li>API Integration</li>
<li>SQLite</li>
<li>Matplotlib</li>
<li>Flask</li>
<li>HTML</li>
</ul>

<h2>🔄 Project Workflow</h2>
<ol>
<li><b>Web Scraping:</b> Extracted product data (title, price, rating)</li>
<li><b>API Integration:</b> Fetched product data from API</li>
<li><b>Data Processing:</b> Cleaned and formatted data</li>
<li><b>Data Merging:</b> Combined datasets</li>
<li><b>Feature Engineering:</b> Added quantity & revenue</li>
<li><b>Database Storage:</b> Stored data in SQLite</li>
<li><b>Visualization:</b> Created charts</li>
<li><b>Dashboard:</b> Built using Flask</li>
</ol>

<h2>📊 Sample Data</h2>
<table border="1">
<tr>
<th>title</th>
<th>price</th>
<th>rating</th>
<th>source</th>
<th>random_quantity</th>
<th>revenue</th>
</tr>

<tr>
<td>Product A</td>
<td>1200</td>
<td>4</td>
<td>API</td>
<td>500</td>
<td>600000</td>
</tr>

<tr>
<td>Product B</td>
<td>800</td>
<td>3</td>
<td>Scraped</td>
<td>300</td>
<td>240000</td>
</tr>

<tr>
<td>Product C</td>
<td>2500</td>
<td>5</td>
<td>API</td>
<td>700</td>
<td>1750000</td>
</tr>
</table>

<h2>💡 Key Insights</h2>
<ul>
<li>API products generated higher revenue</li>
<li>Most products fall in low to mid price range</li>
<li>High-priced products contribute major revenue</li>
<li>No strong relation between price and rating</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
smart-product-intelligence-dashboard/
│
├── scraper.py
├── cleaning.py
├── analysis.py
├── visuals.py
├── database.py
├── app.py
│
├── data/
│   ├── scraped.json
│   ├── api.json
│   └── final_df.csv
│
├── templates/
│   ├── index.html
│   └── top.html
│
└── README.md
</pre>

<h2>🚀 How to Run</h2>
<ol>
<li>Clone the repository</li>
<li>Install dependencies:
<pre>pip install pandas numpy flask requests beautifulsoup4 matplotlib</pre>
</li>
<li>Run the app:
<pre>python app.py</pre>
</li>
<li>Open in browser:
<pre>http://127.0.0.1:5000</pre>
</li>
</ol>

<h2>📈 Learning Outcome</h2>
<p>
This project helped me gain hands-on experience in building complete data pipelines and working with real-world datasets.
</p>

<h2>🙌 Conclusion</h2>
<p>
This project helped me move from theory to practical implementation, strengthening my skills in data analysis and AI.
</p>

</body>
</html>
