"""
Project 9: AI in Transportation
Student Name: Y. Prudhvi Naidu

This beginner-friendly Python script models transportation routes, calculates travel times
using fundamental Python arithmetic and functions, determines the fastest route using min(),
and generates a standalone, fully-responsive, interactive HTML dashboard ("index.html").
"""

import json


def travel_time(distance, speed):
    """
    Calculate estimated travel time in minutes.
    
    Formula: (distance in km / speed in km/h) * 60 minutes
    
    Parameters:
        distance (float): Route length in kilometers
        speed (float): Average travel speed in kilometers per hour
        
    Returns:
        float: Travel time in minutes
    """
    return (distance / speed) * 60


def main():
    # Step 1: Store 5 fictional routes as a list of dictionaries (all destined to Airport)
    routes = [
        {"name": "Central Station to Airport", "distance": 30.0, "speed": 50.0},
        {"name": "University to Airport", "distance": 18.0, "speed": 45.0},
        {"name": "Riverside to Airport", "distance": 12.0, "speed": 32.0},
        {"name": "Hillview to Airport", "distance": 20.0, "speed": 32.0},
        {"name": "Green Park to Airport", "distance": 10.0, "speed": 40.0},
    ]

    print("=" * 65)
    print("🚦 Project 9: AI in Transportation - Route Analysis")
    print("=" * 65)

    # Step 2: Use a loop to calculate and attach travel time for each route
    for route in routes:
        route["time"] = travel_time(route["distance"], route["speed"])
        print(f"• {route['name']}: {route['distance']:.1f} km @ {route['speed']:.1f} km/h -> {route['time']:.1f} mins")

    # Step 3: Use min(..., key=...) to find the fastest route
    # The key parameter instructs min() to compare items using the "time" value of each dictionary
    fastest_route = min(routes, key=lambda r: r["time"])

    print("-" * 65)
    print(f"⚡ Fastest Route: {fastest_route['name']} ({fastest_route['time']:.1f} minutes)")
    print("=" * 65)

    # Step 4: Build initial HTML table rows and CSS chart bars
    max_time = max(r["time"] for r in routes) if routes else 1.0

    table_rows_markup = ""
    chart_bars_markup = ""

    for route in routes:
        is_fastest = (route["name"] == fastest_route["name"])
        row_class = "fastest-row" if is_fastest else ""
        badge_html = '<span class="badge badge-fastest">⚡ Fastest Route</span>' if is_fastest else '<span class="badge badge-standard">Standard</span>'
        
        table_rows_markup += f"""
        <tr class="{row_class}">
            <td class="font-medium">{route['name']}</td>
            <td>{route['distance']:.1f} km</td>
            <td>{route['speed']:.1f} km/h</td>
            <td class="time-cell">{route['time']:.1f} min</td>
            <td>{badge_html}</td>
        </tr>"""

        # Calculate percentage width for CSS bar chart (relative to max travel time)
        bar_percentage = (route["time"] / max_time) * 100 if max_time > 0 else 0
        bar_class = "bar-fill fastest-bar" if is_fastest else "bar-fill"
        chart_bars_markup += f"""
        <div class="chart-item">
            <div class="chart-label-row">
                <span class="chart-route-name">{route['name']}</span>
                <span class="chart-route-time">{route['time']:.1f} min</span>
            </div>
            <div class="chart-track">
                <div class="{bar_class}" style="width: {bar_percentage:.1f}%;"></div>
            </div>
        </div>"""

    # Prepare JSON serializable list for browser JavaScript interactivity
    initial_routes_json = json.dumps(routes)

    # Step 5: Compose the complete HTML document using an f-string
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI in Transportation | Intelligent Route Optimisation</title>
    <style>
        :root {{
            --bg-primary: #0b1120;
            --bg-secondary: #131c31;
            --bg-card: #18233c;
            --bg-card-hover: #1e2c4a;
            --border-color: #273656;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --accent-cyan: #06b6d4;
            --accent-blue: #3b82f6;
            --accent-emerald: #10b981;
            --accent-emerald-glow: rgba(16, 185, 129, 0.25);
            --accent-amber: #f59e0b;
            --radius-lg: 14px;
            --radius-md: 8px;
            --radius-sm: 6px;
            --shadow-subtle: 0 4px 20px rgba(0, 0, 0, 0.35);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: radial-gradient(circle at 10% 20%, #0f172a 0%, var(--bg-primary) 90%);
            color: var(--text-main);
            line-height: 1.6;
            padding: 24px 16px 48px;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1080px;
            margin: 0 auto;
        }}

        /* Header & Intro */
        header {{
            text-align: center;
            margin-bottom: 32px;
            padding: 24px 16px;
        }}

        .tag-pill {{
            display: inline-block;
            background: rgba(6, 182, 212, 0.12);
            color: var(--accent-cyan);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            padding: 4px 14px;
            margin-bottom: 12px;
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 30%, var(--accent-cyan) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 14px;
            letter-spacing: -0.02em;
        }}

        .intro-text {{
            font-size: 1.05rem;
            color: var(--text-muted);
            max-width: 760px;
            margin: 0 auto;
        }}

        /* Dashboard Grid */
        .dashboard-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 24px;
            margin-bottom: 32px;
        }}

        @media (min-width: 840px) {{
            .dashboard-grid {{
                grid-template-columns: 1fr 1fr;
            }}
        }}

        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-subtle);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}

        .card:hover {{
            border-color: #3b4d75;
        }}

        .card-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--border-color);
        }}

        .card-title {{
            font-size: 1.25rem;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        /* Fastest Route Card */
        .fastest-card {{
            background: linear-gradient(145deg, var(--bg-card) 0%, rgba(16, 185, 129, 0.08) 100%);
            border: 1px solid rgba(16, 185, 129, 0.4);
            position: relative;
            overflow: hidden;
        }}

        .fastest-card::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-emerald), var(--accent-cyan));
        }}

        .fastest-meta-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-top: 16px;
            text-align: center;
        }}

        .fastest-meta-item {{
            background: rgba(11, 17, 32, 0.6);
            border-radius: var(--radius-md);
            padding: 12px 8px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}

        .fastest-meta-value {{
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--accent-emerald);
        }}

        .fastest-meta-label {{
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-top: 2px;
        }}

        /* Form Styling */
        .route-form {{
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .form-row {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 14px;
        }}

        @media (min-width: 500px) {{
            .form-row {{
                grid-template-columns: 1fr 1fr;
            }}
        }}

        .form-group {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        label {{
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-muted);
        }}

        input {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 10px 14px;
            border-radius: var(--radius-md);
            font-size: 0.95rem;
            outline: none;
            transition: border-color 0.2s, box-shadow 0.2s;
        }}

        input:focus {{
            border-color: var(--accent-cyan);
            box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.2);
        }}

        .btn-submit {{
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: #ffffff;
            font-weight: 700;
            font-size: 0.95rem;
            border: none;
            border-radius: var(--radius-md);
            padding: 12px 18px;
            cursor: pointer;
            transition: filter 0.2s ease, transform 0.1s ease;
            margin-top: 6px;
        }}

        .btn-submit:hover {{
            filter: brightness(1.12);
        }}

        .btn-submit:active {{
            transform: scale(0.98);
        }}

        .form-feedback {{
            font-size: 0.85rem;
            color: #ef4444;
            display: none;
            margin-top: 4px;
        }}

        /* Table Section */
        .table-card {{
            margin-bottom: 32px;
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.95rem;
        }}

        th {{
            background: var(--bg-secondary);
            color: var(--text-muted);
            padding: 14px 16px;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            border-bottom: 2px solid var(--border-color);
        }}

        td {{
            padding: 14px 16px;
            border-bottom: 1px solid var(--border-color);
            color: #cbd5e1;
        }}

        tbody tr {{
            transition: background 0.15s ease;
        }}

        tbody tr:hover {{
            background: rgba(255, 255, 255, 0.02);
        }}

        tr.fastest-row {{
            background: var(--accent-emerald-glow);
        }}

        tr.fastest-row td {{
            color: #ffffff;
            font-weight: 600;
        }}

        .font-medium {{
            font-weight: 600;
            color: #f8fafc;
        }}

        .time-cell {{
            font-weight: 700;
            color: var(--accent-cyan);
        }}

        tr.fastest-row .time-cell {{
            color: var(--accent-emerald);
        }}

        /* Badges */
        .badge {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
        }}

        .badge-fastest {{
            background: rgba(16, 185, 129, 0.2);
            color: var(--accent-emerald);
            border: 1px solid rgba(16, 185, 129, 0.4);
        }}

        .badge-standard {{
            background: rgba(148, 163, 184, 0.12);
            color: var(--text-muted);
            border: 1px solid rgba(148, 163, 184, 0.2);
        }}

        /* CSS Bar Chart */
        .chart-container {{
            display: flex;
            flex-direction: column;
            gap: 16px;
            padding: 8px 0;
        }}

        .chart-item {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .chart-label-row {{
            display: flex;
            justify-content: space-between;
            font-size: 0.88rem;
        }}

        .chart-route-name {{
            color: #e2e8f0;
            font-weight: 500;
        }}

        .chart-route-time {{
            color: var(--accent-cyan);
            font-weight: 700;
        }}

        .chart-track {{
            background: var(--bg-secondary);
            border-radius: 9999px;
            height: 12px;
            overflow: hidden;
            width: 100%;
        }}

        .bar-fill {{
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-cyan));
            height: 100%;
            border-radius: 9999px;
            transition: width 0.4s ease;
        }}

        .bar-fill.fastest-bar {{
            background: linear-gradient(90deg, #059669, var(--accent-emerald));
            box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
        }}

        /* Informational Sections */
        .info-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-bottom: 32px;
        }}

        @media (min-width: 768px) {{
            .info-grid {{
                grid-template-columns: repeat(3, 1fr);
            }}
        }}

        .info-card {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 20px;
        }}

        .info-card-num {{
            display: inline-block;
            width: 28px;
            height: 28px;
            line-height: 28px;
            text-align: center;
            background: rgba(6, 182, 212, 0.15);
            color: var(--accent-cyan);
            border-radius: 50%;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 12px;
        }}

        .info-card h3 {{
            font-size: 1.1rem;
            margin-bottom: 8px;
            color: #ffffff;
        }}

        .info-card p {{
            font-size: 0.9rem;
            color: var(--text-muted);
            line-height: 1.5;
        }}

        .autonomous-box {{
            background: linear-gradient(135deg, var(--bg-card) 0%, rgba(59, 130, 246, 0.08) 100%);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 24px;
            margin-bottom: 40px;
        }}

        .autonomous-box h2 {{
            font-size: 1.4rem;
            margin-bottom: 12px;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .autonomous-box p {{
            color: #cbd5e1;
            font-size: 0.95rem;
            line-height: 1.6;
        }}

        /* Footer */
        footer {{
            text-align: center;
            border-top: 1px solid var(--border-color);
            padding-top: 24px;
            color: var(--text-muted);
            font-size: 0.85rem;
        }}

        footer .student-credit {{
            color: var(--accent-cyan);
            font-weight: 600;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header>
            <span class="tag-pill">Python Fundamentals Lab</span>
            <h1>AI in Transportation</h1>
            <p class="intro-text">
                Modern artificial intelligence revolutionises urban transit by predicting traffic patterns in real time, 
                optimising commute routes dynamically, and elevating safety across transport networks through data-driven decisions.
            </p>
        </header>

        <!-- Top Grid: Fastest Route Summary & Interactive Add Route Form -->
        <div class="dashboard-grid">
            <!-- Fastest Route Summary Card -->
            <div class="card fastest-card" id="fastest-card-container">
                <div class="card-header">
                    <span class="card-title">⚡ Optimal Route Highlight</span>
                    <span class="badge badge-fastest" id="fastest-badge">Top Recommendation</span>
                </div>
                <div style="font-size: 0.9rem; color: var(--text-muted);">AI Selected Fastest Path:</div>
                <h3 id="fastest-name" style="font-size: 1.5rem; color: #ffffff; margin: 4px 0 12px;">{fastest_route['name']}</h3>
                <div class="fastest-meta-grid">
                    <div class="fastest-meta-item">
                        <div class="fastest-meta-value" id="fastest-time">{fastest_route['time']:.1f}</div>
                        <div class="fastest-meta-label">Est. Minutes</div>
                    </div>
                    <div class="fastest-meta-item">
                        <div class="fastest-meta-value" id="fastest-distance">{fastest_route['distance']:.1f}</div>
                        <div class="fastest-meta-label">Distance (km)</div>
                    </div>
                    <div class="fastest-meta-item">
                        <div class="fastest-meta-value" id="fastest-speed">{fastest_route['speed']:.1f}</div>
                        <div class="fastest-meta-label">Avg Speed (km/h)</div>
                    </div>
                </div>
            </div>

            <!-- Interactive Route Input Form -->
            <div class="card">
                <div class="card-header">
                    <span class="card-title">➕ Add Custom Route</span>
                    <span style="font-size: 0.8rem; color: var(--text-muted);">Client-side Live Simulation</span>
                </div>
                <form class="route-form" id="route-form">
                    <div class="form-group">
                        <label for="route-name">Route Name</label>
                        <input type="text" id="route-name" placeholder="e.g., North Station to Airport" required>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="route-distance">Distance (km)</label>
                            <input type="number" id="route-distance" step="0.1" min="0.1" placeholder="e.g., 15.5" required>
                        </div>
                        <div class="form-group">
                            <label for="route-speed">Average Speed (km/h)</label>
                            <input type="number" id="route-speed" step="0.1" min="0.1" placeholder="e.g., 42" required>
                        </div>
                    </div>
                    <button type="submit" class="btn-submit">Calculate & Add to Dashboard</button>
                    <div id="form-feedback" class="form-feedback">Please enter a valid distance and speed greater than zero.</div>
                </form>
            </div>
        </div>

        <!-- Route Table -->
        <div class="card table-card">
            <div class="card-header">
                <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                    <span class="card-title">🗺️ Evaluated Routes to Airport</span>
                    <span class="badge" style="background: rgba(6, 182, 212, 0.15); color: var(--accent-cyan); border: 1px solid rgba(6, 182, 212, 0.3);">📍 Destination: Airport</span>
                </div>
                <span style="font-size: 0.85rem; color: var(--text-muted);" id="route-count">5 Routes Monitored</span>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Route Name</th>
                        <th>Distance</th>
                        <th>Average Speed</th>
                        <th>Estimated Time</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody id="table-body">
{table_rows_markup}
                </tbody>
            </table>
        </div>

        <!-- Travel Time CSS Bar Chart -->
        <div class="card" style="margin-bottom: 32px;">
            <div class="card-header">
                <span class="card-title">📊 Travel Time Chart</span>
                <span style="font-size: 0.85rem; color: var(--text-muted);">Responsive Pure CSS Visualisation</span>
            </div>
            <div class="chart-container" id="chart-container">
{chart_bars_markup}
            </div>
        </div>

        <!-- How AI Helps in Transportation -->
        <h2 style="font-size: 1.5rem; margin-bottom: 16px; color: #ffffff;">How AI Helps in Transportation</h2>
        <div class="info-grid">
            <div class="info-card">
                <span class="info-card-num">01</span>
                <h3>Real-Time Traffic Prediction</h3>
                <p>
                    Machine learning algorithms ingest live IoT sensor data, GPS pings, and historical bottlenecks 
                    to predict congestion 30 to 60 minutes ahead, enabling signal re-timing before gridlock occurs.
                </p>
            </div>
            <div class="info-card">
                <span class="info-card-num">02</span>
                <h3>Intelligent Dynamic Routing</h3>
                <p>
                    Rather than relying solely on static road lengths, AI continuously recalibrates journeys using live speed 
                    deltas, weather events, and construction zones to recommend the true fastest path.
                </p>
            </div>
            <div class="info-card">
                <span class="info-card-num">03</span>
                <h3>Predictive Safety & Incident Prevention</h3>
                <p>
                    Computer vision sensors at road junctions spot sudden braking patterns, pedestrian hazards, and blind spots, 
                    proactively alerting drivers and automated emergency control centers.
                </p>
            </div>
        </div>

        <!-- AI and Autonomous Vehicles Section -->
        <div class="autonomous-box">
            <h2>🤖 AI and Autonomous Vehicles</h2>
            <p>
                Self-driving cars and autonomous delivery pods represent the frontier of AI in transportation. By combining 
                sensor fusion from LiDAR, radar, and HD optical cameras with high-speed deep neural networks, autonomous vehicles 
                construct a millimeter-accurate 360-degree understanding of their surroundings in milliseconds. AI-driven vehicle-to-everything 
                (V2X) communication allows autonomous fleets to coordinate merging, synchronize travel speeds, and maintain safe platooning distances—dramatically 
                reducing human reaction errors that cause over 90% of conventional road collisions.
            </p>
        </div>

        <!-- Footer -->
        <footer>
            <p>Project 9: AI in Transportation • Created by <span class="student-credit">Y. Prudhvi Naidu</span></p>
            <p style="margin-top: 4px; color: #64748b;">Built with Python Fundamentals: Dictionaries, Functions, min(key=...), and HTML f-strings.</p>
        </footer>
    </div>

    <!-- Client-side Interactive JavaScript -->
    <script>
        // Load initial routes passed from Python backend
        const routesData = {initial_routes_json};

        // Helper function matching Python travel_time formula
        function calculateTravelTime(distance, speed) {{
            return (distance / speed) * 60;
        }}

        // Render dashboard UI (Table, Fastest Card, Chart)
        function renderDashboard() {{
            if (!routesData || routesData.length === 0) return;

            // Find fastest route using JavaScript reduction (equivalent to Python min(..., key=...))
            let fastest = routesData.reduce((prev, curr) => (curr.time < prev.time ? curr : prev), routesData[0]);

            // 1. Update Fastest Route Summary Card
            document.getElementById('fastest-name').textContent = fastest.name;
            document.getElementById('fastest-time').textContent = fastest.time.toFixed(1);
            document.getElementById('fastest-distance').textContent = fastest.distance.toFixed(1);
            document.getElementById('fastest-speed').textContent = fastest.speed.toFixed(1);
            document.getElementById('route-count').textContent = `${{routesData.length}} Routes Monitored`;

            // 2. Render Table Rows
            const tbody = document.getElementById('table-body');
            tbody.innerHTML = '';
            routesData.forEach(route => {{
                const isFastest = (route.name === fastest.name && route.time === fastest.time);
                const tr = document.createElement('tr');
                if (isFastest) tr.className = 'fastest-row';

                tr.innerHTML = `
                    <td class="font-medium">${{escapeHtml(route.name)}}</td>
                    <td>${{route.distance.toFixed(1)}} km</td>
                    <td>${{route.speed.toFixed(1)}} km/h</td>
                    <td class="time-cell">${{route.time.toFixed(1)}} min</td>
                    <td>${{isFastest ? '<span class="badge badge-fastest">⚡ Fastest Route</span>' : '<span class="badge badge-standard">Standard</span>'}}</td>
                `;
                tbody.appendChild(tr);
            }});

            // 3. Render CSS Bar Chart
            const chartContainer = document.getElementById('chart-container');
            chartContainer.innerHTML = '';
            const maxTime = Math.max(...routesData.map(r => r.time), 1.0);

            routesData.forEach(route => {{
                const isFastest = (route.name === fastest.name && route.time === fastest.time);
                const percentage = ((route.time / maxTime) * 100).toFixed(1);

                const item = document.createElement('div');
                item.className = 'chart-item';
                item.innerHTML = `
                    <div class="chart-label-row">
                        <span class="chart-route-name">${{escapeHtml(route.name)}}</span>
                        <span class="chart-route-time">${{route.time.toFixed(1)}} min</span>
                    </div>
                    <div class="chart-track">
                        <div class="bar-fill ${{isFastest ? 'fastest-bar' : ''}}" style="width: ${{percentage}}%;"></div>
                    </div>
                `;
                chartContainer.appendChild(item);
            }});
        }}

        // Helper to prevent HTML injection in user input
        function escapeHtml(str) {{
            const div = document.createElement('div');
            div.textContent = str;
            return div.innerHTML;
        }}

        // Handle Interactive Form Submission
        document.getElementById('route-form').addEventListener('submit', function(e) {{
            e.preventDefault();
            const nameInput = document.getElementById('route-name');
            const distanceInput = document.getElementById('route-distance');
            const speedInput = document.getElementById('route-speed');
            const feedback = document.getElementById('form-feedback');

            const name = nameInput.value.trim();
            const distance = parseFloat(distanceInput.value);
            const speed = parseFloat(speedInput.value);

            // Validation: distance and speed must be strictly greater than 0
            if (!name || isNaN(distance) || isNaN(speed) || distance <= 0 || speed <= 0) {{
                feedback.style.display = 'block';
                return;
            }}

            feedback.style.display = 'none';

            // Calculate estimated time and add to in-memory routes list
            const time = calculateTravelTime(distance, speed);
            routesData.push({{
                name: name,
                distance: distance,
                speed: speed,
                time: time
            }});

            // Refresh table, fastest card, and chart immediately
            renderDashboard();

            // Reset form fields
            nameInput.value = '';
            distanceInput.value = '';
            speedInput.value = '';
            nameInput.focus();
        }});
    </script>
</body>
</html>
"""

    # Step 6: Use open() to write and save the generated HTML file
    output_filename = "index.html"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"✨ Successfully generated '{output_filename}' ({len(html_content):,} bytes).")
    print("🌐 Open 'index.html' in your browser to view the interactive dashboard.")


if __name__ == "__main__":
    main()
