import os
import json
import re

base_stitch_dir = r"C:\PERSONAL\major project\WayMate\stitch_ui\stitch_waymate_airport_ride_sharing_ui"
output_dir = r"C:\PERSONAL\major project\WayMate\android\ui-tester"
os.makedirs(output_dir, exist_ok=True)

dirs = sorted([d for d in os.listdir(base_stitch_dir) if os.path.isdir(os.path.join(base_stitch_dir, d))])

screens = []
screen_mapping = {}

screen_names = {
    "01_splash_screen": "01 Splash Screen",
    "02_onboarding": "02 Onboarding Carousel",
    "03_login_otp": "03 Mobile & OTP Login",
    "04_home_dashboard": "04 Home Dashboard",
    "05_flight_details": "05 Flight Details",
    "06_final_destination": "06 Final Destination",
    "07_passenger_details": "07 Passenger Details",
    "08_luggage_details": "08 Luggage Details",
    "09_language_preference": "09 Language Preference",
    "10_finding_your_pool": "10 Finding Your Pool",
    "11_pool_available": "11 Pool Available",
    "12_vehicle_details": "12 Vehicle Details",
    "13_pool_passengers": "13 Pool Passengers",
    "14_driver_details": "14 Driver Details",
    "15_pool_confirmation": "15 Pool Confirmation",
    "16_live_cab_tracking": "16 Live Cab Tracking",
    "17_journey_in_progress": "17 Journey In Progress",
    "18_ride_completed": "18 Ride Completed",
    "19_payment_razorpay": "19 Razorpay Payment",
    "20_rating_feedback": "20 Rating & Feedback",
    "21_my_trips": "21 My Trips",
    "22_notifications": "22 Notifications",
    "23_profile": "23 User Profile"
}

# Corresponding Compose files
compose_files = {
    "01_splash_screen": "com.waymate.app.screens.SplashScreen (AuthScreens.kt)",
    "02_onboarding": "com.waymate.app.screens.OnboardingScreen (AuthScreens.kt)",
    "03_login_otp": "com.waymate.app.screens.LoginOtpScreen (AuthScreens.kt)",
    "04_home_dashboard": "com.waymate.app.screens.HomeDashboardScreen (HomeDashboardScreen.kt)",
    "05_flight_details": "com.waymate.app.screens.FlightDetailsScreen (BookingFlowScreens.kt)",
    "06_final_destination": "com.waymate.app.screens.FinalDestinationScreen (BookingFlowScreens.kt)",
    "07_passenger_details": "com.waymate.app.screens.PassengerDetailsScreen (BookingFlowScreens.kt)",
    "08_luggage_details": "com.waymate.app.screens.LuggageDetailsScreen (BookingFlowScreens.kt)",
    "09_language_preference": "com.waymate.app.screens.LanguagePreferenceScreen (BookingFlowScreens.kt)",
    "10_finding_your_pool": "com.waymate.app.screens.FindingPoolScreen (PoolMatchingScreens.kt)",
    "11_pool_available": "com.waymate.app.screens.PoolAvailableScreen (PoolMatchingScreens.kt)",
    "12_vehicle_details": "com.waymate.app.screens.VehicleDetailsScreen (PoolMatchingScreens.kt)",
    "13_pool_passengers": "com.waymate.app.screens.PoolPassengersScreen (PoolMatchingScreens.kt)",
    "14_driver_details": "com.waymate.app.screens.DriverDetailsScreen (PoolMatchingScreens.kt)",
    "15_pool_confirmation": "com.waymate.app.screens.PoolConfirmationScreen (PoolMatchingScreens.kt)",
    "16_live_cab_tracking": "com.waymate.app.screens.LiveTrackingScreen (RideTrackingScreens.kt)",
    "17_journey_in_progress": "com.waymate.app.screens.JourneyProgressScreen (RideTrackingScreens.kt)",
    "18_ride_completed": "com.waymate.app.screens.RideCompletedScreen (RideTrackingScreens.kt)",
    "19_payment_razorpay": "com.waymate.app.screens.PaymentRazorpayScreen (PaymentAndFeedbackScreens.kt)",
    "20_rating_feedback": "com.waymate.app.screens.RatingFeedbackScreen (PaymentAndFeedbackScreens.kt)",
    "21_my_trips": "com.waymate.app.screens.MyTripsScreen (AccountScreens.kt)",
    "22_notifications": "com.waymate.app.screens.NotificationsScreen (AccountScreens.kt)",
    "23_profile": "com.waymate.app.screens.ProfileScreen (AccountScreens.kt)"
}

injection_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a, button').forEach(el => {
        el.addEventListener('click', function(e) {
            const href = el.getAttribute('href') || '';
            const text = el.innerText || '';
            
            // Send click intent to parent frame
            window.parent.postMessage({
                type: 'WAYMATE_NAV',
                href: href,
                text: text.trim()
            }, '*');
            
            if (href && (href.startsWith('#') || href.startsWith('javascript:'))) {
                return;
            }
            if (href) {
                e.preventDefault();
            }
        });
    });
});
</script>
"""

screens_data = []

for idx, d in enumerate(dirs):
    html_path = os.path.join(base_stitch_dir, d, "code.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # Inject our communication script right before </body>
        if "</body>" in html_content:
            html_content = html_content.replace("</body>", injection_script + "</body>")
        else:
            html_content += injection_script
            
        screen_id = f"screen_{idx}"
        screen_file = f"{screen_id}.html"
        with open(os.path.join(output_dir, screen_file), "w", encoding="utf-8") as f_out:
            f_out.write(html_content)
            
        screens_data.append({
            "id": idx,
            "folder": d,
            "title": screen_names.get(d, d),
            "file": screen_file,
            "compose": compose_files.get(d, "")
        })

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WayMate Android UI Tester — 23 Jetpack Compose Screens</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Red+Hat+Text:wght@500;600;700&family=Instrument+Sans:wght@400;500;600;700&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=block" rel="stylesheet">
  <style>
    body {{ font-family: 'Instrument Sans', sans-serif; background-color: #1C1B18; color: #FAF7F0; }}
    .phone-container {{
      width: 390px;
      height: 844px;
      border-radius: 46px;
      box-shadow: 0 25px 60px rgba(0,0,0,0.6), 0 0 0 12px #2A2824, 0 0 0 14px #44403C;
      overflow: hidden;
      position: relative;
      background: #F3EBDD;
    }}
    .phone-notch {{
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 130px;
      height: 28px;
      background: #2A2824;
      border-bottom-left-radius: 16px;
      border-bottom-right-radius: 16px;
      z-index: 50;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }}
    .notch-camera {{ width: 10px; height: 10px; border-radius: 50%; background: #111; }}
    .notch-speaker {{ width: 44px; height: 4px; border-radius: 4px; background: #1a1a1a; }}
    .custom-scroll::-webkit-scrollbar {{ width: 6px; }}
    .custom-scroll::-webkit-scrollbar-thumb {{ background: #32302D; border-radius: 3px; }}
  </style>
</head>
<body class="min-h-screen flex flex-col h-screen overflow-hidden">
  <!-- Top App Bar -->
  <header class="h-14 bg-[#24231F] border-b border-[#32302D] px-6 flex items-center justify-between shrink-0">
    <div class="flex items-center gap-3">
      <div class="w-8 h-8 rounded-lg bg-[#F3EBDD] text-[#1C1B18] flex items-center justify-center font-bold">
        <span class="material-symbols-outlined text-[20px]">flight_land</span>
      </div>
      <div>
        <h1 class="font-bold text-base tracking-wide flex items-center gap-2">
          WayMate <span class="text-xs px-2 py-0.5 rounded-full bg-[#526B50] text-[#FAF7F0] font-mono">Jetpack Compose UI Tester</span>
        </h1>
      </div>
    </div>

    <!-- Active Screen Pill & Controls -->
    <div class="flex items-center gap-4">
      <div class="flex items-center gap-2 bg-[#1C1B18] px-3 py-1.5 rounded-xl border border-[#32302D]">
        <button onclick="prevScreen()" class="p-1 hover:bg-[#32302D] rounded text-sm text-[#FAF7F0] flex items-center" title="Previous Screen">
          <span class="material-symbols-outlined text-[18px]">chevron_left</span>
        </button>
        <span id="screen-badge" class="font-mono text-xs font-semibold px-2 py-0.5 bg-[#FAF7F0] text-[#1C1B18] rounded-md">1 / 23</span>
        <button onclick="nextScreen()" class="p-1 hover:bg-[#32302D] rounded text-sm text-[#FAF7F0] flex items-center" title="Next Screen">
          <span class="material-symbols-outlined text-[18px]">chevron_right</span>
        </button>
      </div>

      <button id="view-mode-btn" onclick="toggleViewMode()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#32302D] hover:bg-[#44403C] text-xs font-semibold transition-all">
        <span class="material-symbols-outlined text-[16px]">smartphone</span>
        <span id="view-mode-label">Mobile Frame (390px)</span>
      </button>
    </div>
  </header>

  <!-- Main Workspace -->
  <div class="flex flex-1 overflow-hidden">
    <!-- Left Navigation Sidebar -->
    <aside class="w-80 bg-[#1C1B18] border-r border-[#2A2824] flex flex-col shrink-0">
      <div class="p-4 border-b border-[#2A2824]">
        <h2 class="text-xs uppercase font-mono tracking-wider text-[#A39E93]">All 23 Screens & Flows</h2>
        <p class="text-xs text-[#716C63] mt-1">Click any screen to jump test directly.</p>
      </div>

      <nav id="screen-nav-list" class="flex-1 overflow-y-auto custom-scroll p-3 space-y-1">
        <!-- Rendered by JS -->
      </nav>

      <div class="p-4 border-t border-[#2A2824] bg-[#161513]">
        <div class="text-xs font-mono text-[#A39E93] mb-1">Kotlin Architecture</div>
        <div id="compose-path" class="text-xs text-[#FAF7F0] font-mono break-all line-clamp-2">
          com.waymate.app.screens.SplashScreen
        </div>
      </div>
    </aside>

    <!-- Center Phone Stage -->
    <main class="flex-1 bg-[#12110F] flex items-center justify-center p-6 overflow-auto">
      <div id="phone-frame" class="phone-container transition-all duration-300">
        <div class="phone-notch">
          <div class="notch-speaker"></div>
          <div class="notch-camera"></div>
        </div>
        <iframe id="screen-iframe" class="w-full h-full border-0 pt-4" src="screen_0.html"></iframe>
      </div>
    </main>
  </div>

  <script>
    const screens = {json.dumps(screens_data)};
    let currentIndex = 0;
    let isFullWidth = false;

    function renderScreenList() {{
      const container = document.getElementById('screen-nav-list');
      container.innerHTML = screens.map((s, idx) => `
        <button onclick="loadScreen(${{idx}})" 
          id="nav-item-${{idx}}" 
          class="w-full text-left px-3 py-2 rounded-xl text-xs flex items-center justify-between transition-all ${{idx === currentIndex ? 'bg-[#FAF7F0] text-[#1C1B18] font-bold shadow-md' : 'text-[#D8CEBD] hover:bg-[#2A2824]'}}">
          <span class="truncate">${{s.title}}</span>
          <span class="text-[10px] font-mono opacity-60">#${{idx + 1}}</span>
        </button>
      `).join('');
    }}

    function loadScreen(index) {{
      if (index < 0 || index >= screens.length) return;
      currentIndex = index;
      const s = screens[currentIndex];
      
      document.getElementById('screen-iframe').src = s.file;
      document.getElementById('screen-badge').innerText = `${{currentIndex + 1}} / ${{screens.length}}`;
      document.getElementById('compose-path').innerText = s.compose;

      // Update active nav class
      document.querySelectorAll('#screen-nav-list button').forEach((btn, idx) => {{
        if (idx === currentIndex) {{
          btn.className = "w-full text-left px-3 py-2 rounded-xl text-xs flex items-center justify-between transition-all bg-[#FAF7F0] text-[#1C1B18] font-bold shadow-md";
        }} else {{
          btn.className = "w-full text-left px-3 py-2 rounded-xl text-xs flex items-center justify-between transition-all text-[#D8CEBD] hover:bg-[#2A2824]";
        }}
      }});
    }}

    function nextScreen() {{
      if (currentIndex < screens.length - 1) loadScreen(currentIndex + 1);
    }}

    function prevScreen() {{
      if (currentIndex > 0) loadScreen(currentIndex - 1);
    }}

    function toggleViewMode() {{
      const frame = document.getElementById('phone-frame');
      const label = document.getElementById('view-mode-label');
      isFullWidth = !isFullWidth;
      if (isFullWidth) {{
        frame.style.width = '100%';
        frame.style.height = '100%';
        frame.style.borderRadius = '16px';
        frame.style.boxShadow = 'none';
        label.innerText = 'Full Canvas View';
      }} else {{
        frame.style.width = '390px';
        frame.style.height = '844px';
        frame.style.borderRadius = '46px';
        frame.style.boxShadow = '0 25px 60px rgba(0,0,0,0.6), 0 0 0 12px #2A2824, 0 0 0 14px #44403C';
        label.innerText = 'Mobile Frame (390px)';
      }}
    }}

    // Intercept navigation from inside the child screen iframe
    window.addEventListener('message', function(event) {{
      if (event.data && event.data.type === 'WAYMATE_NAV') {{
        const href = (event.data.href || '').toLowerCase();
        const text = (event.data.text || '').toLowerCase();
        
        // Match next steps in the flow
        if (currentIndex === 0) {{ // Splash -> Onboarding
          loadScreen(1);
        }} else if (currentIndex === 1) {{ // Onboarding -> Login
          loadScreen(2);
        }} else if (currentIndex === 2) {{ // Login -> Home
          loadScreen(3);
        }} else if (currentIndex === 3) {{ // Home
          if (text.includes('trips') || href.includes('my-trips')) loadScreen(20);
          else if (text.includes('profile') || href.includes('profile')) loadScreen(22);
          else if (text.includes('notifications') || href.includes('notification')) loadScreen(21);
          else if (text.includes('view pool') || href.includes('pool-available')) loadScreen(10);
          else loadScreen(4); // Flight Details
        }} else if (currentIndex >= 4 && currentIndex <= 8) {{ // Booking flow 5 steps
          if (currentIndex === 8) loadScreen(9); // Find pool
          else loadScreen(currentIndex + 1);
        }} else if (currentIndex === 9) {{ // Finding Pool -> Available
          loadScreen(10);
        }} else if (currentIndex === 10) {{ // Pool Available
          if (text.includes('vehicle') || href.includes('vehicle')) loadScreen(11);
          else if (text.includes('passenger') || href.includes('passenger')) loadScreen(12);
          else if (text.includes('driver') || href.includes('driver')) loadScreen(13);
          else loadScreen(14); // Confirmation
        }} else if (currentIndex >= 11 && currentIndex <= 13) {{ // Detail screens -> back to 10
          loadScreen(10);
        }} else if (currentIndex === 14) {{ // Confirmation -> Live Tracking
          loadScreen(15);
        }} else if (currentIndex === 15) {{ // Live Tracking -> In Progress
          loadScreen(16);
        }} else if (currentIndex === 16) {{ // In Progress -> Completed
          loadScreen(17);
        }} else if (currentIndex === 17) {{ // Completed -> Payment
          loadScreen(18);
        }} else if (currentIndex === 18) {{ // Payment -> Rating
          loadScreen(19);
        }} else if (currentIndex === 19) {{ // Rating -> Home
          loadScreen(3);
        }} else {{
          // Default bottom nav or back
          if (href.includes('home')) loadScreen(3);
          else if (href.includes('trips')) loadScreen(20);
          else if (href.includes('notification')) loadScreen(21);
          else if (href.includes('profile')) loadScreen(22);
          else nextScreen();
        }}
      }}
    }});

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight') nextScreen();
      if (e.key === 'ArrowLeft') prevScreen();
    }});

    renderScreenList();
    loadScreen(0);
  </script>
</body>
</html>
"""

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("UI Tester successfully built at:", os.path.join(output_dir, "index.html"))

