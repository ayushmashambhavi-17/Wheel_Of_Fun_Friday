import base64
import json
import os
import streamlit as st
import streamlit.components.v1 as components

# --- VIEWPORT & CONFIGURATION ---
st.set_page_config(
    page_title="Arena | Name Picker Wheel",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- SAFE LOGO ASSET LOADER ---
LOGO_BASE64 = ""
logo_path = "ufo_logo.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        LOGO_BASE64 = base64.b64encode(image_file.read()).decode()

# --- CURATED TEAM ROSTER ASSET MATRIX ---
MEMBERS = [
    "Ajaz",
    "Amit",
    "Ankur",
    "Bhabesh",
    "Gautam",
    "Jeet",
    "Kartiki",
    "Obaiah",
    "Irfan",
    "Neha",
    "Nishank",
    "Prasad",
    "Pratik",
    "Pritesh",
    "Roshni",
    "Sampada",
    "Shailavi",
    "Shubham",
    "Shubhangi",
    "Soham",
    "Sonali",
    "Soumyashree",
    "Swanand",
    "Vedant",
    "Yasmin",
]

serialized_members = json.dumps(MEMBERS)

# --- LUXURY MIDNIGHT CARNIVAL ENGINE RUNTIME ---
game_show_engine = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Name Picker Wheel Arena</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=Space+Grotesk:wght@700;900&display=swap');

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        html, body {
            width: 100%;
            height: 100vh;
            overflow: hidden;
            background: #020827;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #F8FAFC;
        }

        .game-stage {
            position: relative;
            width: 100vw;
            height: 100vh;
            background: radial-gradient(circle at center, #08145C 0%, #030B35 40%, #020827 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 2vh 2vw;
            gap: 1.5vh;
        }

        .bg-particles {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .stage-header {
            text-align: center;
            z-index: 10;
        }
        .stage-header h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 900;
            font-size: clamp(1.8rem, 4vh, 2.6rem);
            letter-spacing: -1px;
            background: linear-gradient(135deg, #FFD54F 0%, #FFC107 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
            filter: drop-shadow(0 0 15px rgba(255,193,7,.5));
        }
        .stage-header p {
            font-size: clamp(0.7rem, 1.5vh, 0.9rem);
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #E83E8C;
            font-weight: 800;
            margin-top: 2px;
        }

        .wheel-theater {
            position: relative;
            width: clamp(260px, 50vh, 420px);
            height: clamp(260px, 50vh, 420px);
            z-index: 5;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .gold-rim {
            position: absolute;
            width: 101.5%;
            height: 101.5%;
            border-radius: 50%;
            background: radial-gradient(circle, transparent 65%, #E6A800 66%, #FFC107 72%, #FFE76A 76%, #FFC107 82%, transparent 86%);
            box-shadow: 0 0 20px rgba(255,215,0,.6), 0 0 50px rgba(255,215,0,.3), 0 20px 45px rgba(0, 0, 0, 0.6);
            z-index: 3;
            pointer-events: none;
        }

        #wheelCanvas {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            z-index: 2;
        }

        .premium-pointer {
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%) rotate(0deg);
            width: clamp(24px, 4vh, 34px);
            height: clamp(32px, 5.5vh, 42px);
            background: linear-gradient(185deg, #FFF3B0 0%, #FFD700 50%, #D4AF37 100%);
            clip-path: polygon(50% 100%, 0 0, 100% 0);
            filter: drop-shadow(0 0 15px rgba(255,215,0,.8));
            z-index: 8;
            transform-origin: 50% 15%;
            transition: transform 0.1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .center-hub {
            position: absolute;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: #ffffff;
            box-shadow: 0 0 20px rgba(255,255,255,0.5), 0 0 40px rgba(255,215,0,0.5), 0 5px 25px rgba(0,0,0,0.6);
            z-index: 6;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .center-logo {
            width: 92%;
            height: 92%;
            object-fit: contain;
        }

        .spin-trigger-wrapper {
            z-index: 10;
            display: flex;
            align-items: center;
        }

        .spin-cta-btn {
            outline: none;
            border: none;
            background: linear-gradient(180deg, #FF5FA2 0%, #FF4081 50%, #D81B60 100%);
            color: #FFF;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 900;
            font-size: clamp(1.1rem, 2.5vh, 1.5rem);
            letter-spacing: 1.5px;
            padding: clamp(10px, 1.8vh, 14px) clamp(35px, 5vw, 55px);
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 8px 0 #A01347, 0 15px 30px rgba(255, 64, 129, 0.5);
            text-transform: uppercase;
            transition: transform 0.1s;
        }
        .spin-cta-btn:hover { transform: scale(1.03); filter: brightness(1.05); }
        .spin-cta-btn:active {
            transform: translateY(6px);
            box-shadow: 0 2px 0 #A01347, 0 8px 15px rgba(255, 64, 129, 0.5);
        }

        .celebration-screen {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: 100;
            background: rgba(2, 8, 39, 0.96);
            backdrop-filter: blur(30px);
            opacity: 0; pointer-events: none;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2vh 2vw;
            transition: opacity 0.4s ease-out;
        }
        .celebration-screen.active { opacity: 1; pointer-events: auto; }

        #celebrationCanvas {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 101;
        }

        .card-stage {
            position: relative;
            z-index: 105;
            width: 100%;
            max-width: 500px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .flow-card {
            width: 100%;
            background: rgba(11, 19, 62, 0.85);
            border: 2px solid rgba(255, 213, 79, 0.3);
            border-radius: 32px;
            padding: clamp(30px, 5vh, 45px);
            text-align: center;
            box-shadow: 0 35px 75px rgba(0, 0, 0, 0.8), inset 0 1px 1px rgba(255,255,255,0.08);
            display: none;
            animation: cardZoomIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.15) forwards;
        }
        .flow-card.visible { display: block; }

        @keyframes cardZoomIn {
            from { transform: scale(0.92) translateY(20px); opacity: 0; }
            to { transform: scale(1) translateY(0); opacity: 1; }
        }

        .avatar-circle-halo {
            width: clamp(70px, 10vh, 90px);
            height: clamp(70px, 10vh, 90px);
            border-radius: 50%;
            margin: 0 auto 15px auto;
            background: linear-gradient(135deg, #FFD54F 0%, #D63384 100%);
            padding: 3px;
            box-shadow: 0 8px 25px rgba(255, 193, 7, 0.3);
        }
        .avatar-inner {
            width: 100%; height: 100%;
            border-radius: 50%; background: #050D45;
            display: flex; align-items: center; justify-content: center;
            font-size: clamp(1.8rem, 4vh, 2.2rem);
        }

        .spotlight-sub {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: clamp(0.8rem, 1.8vh, 1.1rem);
            color: #FFC107; letter-spacing: 4px;
            text-transform: uppercase; margin-bottom: 6px;
        }
        .spotlight-name {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 900;
            font-size: clamp(2.2rem, 6vh, 3.8rem);
            color: #FFF; letter-spacing: -1px;
            text-shadow: 0 0 25px rgba(255, 213, 79, 0.4);
            margin-bottom: 25px; text-transform: uppercase;
        }

        .flow-actions {
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .btn-base {
            border: none; outline: none; color: #FFF;
            font-family: 'Space Grotesk', sans-serif; font-weight: 900;
            font-size: clamp(0.9rem, 2vh, 1.15rem);
            padding: clamp(12px, 2vh, 16px) clamp(25px, 4vw, 40px);
            border-radius: 50px; cursor: pointer;
            text-transform: uppercase; letter-spacing: 1.5px;
            transition: all 0.15s ease-out;
            display: inline-flex; align-items: center; gap: 8px;
        }
        .btn-base:hover { transform: scale(1.03); filter: brightness(1.1); }
        .btn-base:active { transform: scale(0.98); }

        .btn-green  { background: linear-gradient(135deg, #10B981 0%, #059669 100%); box-shadow: 0 8px 20px rgba(16,185,129,0.3); }
        .btn-red    { background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%); box-shadow: 0 8px 20px rgba(239,68,68,0.3); }
        .btn-purple { background: linear-gradient(135deg, #6C2BD9 0%, #4F46E5 100%); box-shadow: 0 8px 20px rgba(108,43,217,0.3); width: 85%; justify-content: center; }
    </style>
</head>
<body>

    <div class="game-stage">
        <canvas class="bg-particles" id="ambientEngine"></canvas>
        
        <div class="stage-header">
            <h1>UK LM DAIS TEAM</h1>
            <p>Lucky Name Picker Wheel</p>
        </div>

        <div class="wheel-theater" id="wheelTheater">
            <div class="premium-pointer" id="pointerPin"></div>
            <div class="gold-rim"></div>
            <div class="center-hub">
                <img src="data:image/png;base64,__LOGO_BASE64__" class="center-logo" alt="Logo"/>
            </div>
            <canvas id="wheelCanvas" width="600" height="600"></canvas>
        </div>

        <div class="spin-trigger-wrapper">
            <button class="spin-cta-btn" id="megaSpinBtn">🎡 Spin Roster</button>
        </div>
    </div>

    <div class="celebration-screen" id="victoryScreen">
        <canvas id="celebrationCanvas"></canvas>
        <div class="card-stage" id="cardMatrix">
            <div class="flow-card visible" id="flowStep1">
                <div class="avatar-circle-halo"><div class="avatar-inner">⭐</div></div>
                <p class="spotlight-sub">Selected Winner</p>
                <h2 class="spotlight-name" id="championTarget">PLAYER NAME</h2>
                <div class="flow-actions">
                    <button class="btn-base btn-green" id="isPresentBtn">✅ Accept / Present</button>
                    <button class="btn-base btn-red" id="isAbsentBtn">❌ Not Available</button>
                </div>
            </div>

            <div class="flow-card" id="flowStep2">
                <div class="avatar-circle-halo" style="background: linear-gradient(135deg, #10B981 0%, #3B82F6 100%);"><div class="avatar-inner">🔥</div></div>
                <p class="spotlight-sub" style="color: #10B981;">The Stage Is Yours!</p>
                <h2 class="spotlight-name" id="turnPlayerTitle">IT'S YOUR TURN!</h2>
                <div class="flow-actions" style="margin-top: 10px;">
                    <button class="btn-base btn-purple" id="backToWheelBtn">🔙 Back To Wheel</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let players = __PLAYERS_PLACEHOLDER__;
        const segmentGradients = [
            ["#6C2BD9", "#6120C2"],
            ["#D63384", "#E83E8C"],
            ["#2F62CC", "#3867D6"],
            ["#18A8D8", "#22B8CF"]
        ];

        const canvas = document.getElementById("wheelCanvas");
        const ctx = canvas.getContext("2d");
        let currentAngleOffset = 0;
        let isSpinning = false;
        let activeSelectedPlayer = "";

        function drawWheel() {
            const cx = canvas.width / 2;
            const cy = canvas.height / 2;
            const radius = canvas.width / 2 - 10;
            const centerGap = 65;
            const numSlices = players.length;
            if (numSlices === 0) return;
            const sliceAngle = (2 * Math.PI) / numSlices;
            
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            for (let i = 0; i < numSlices; i++) {
                const startAngle = currentAngleOffset + (i * sliceAngle);
                const endAngle = startAngle + sliceAngle;

                const fillGrad = ctx.createRadialGradient(cx, cy, radius * 0.15, cx, cy, radius);
                const colors = segmentGradients[i % segmentGradients.length];
                fillGrad.addColorStop(0, colors[0]);
                fillGrad.addColorStop(0.88, colors[1]);
                fillGrad.addColorStop(1, "#020827");

                ctx.beginPath();
                ctx.arc(cx, cy, radius, startAngle, endAngle, false);
                ctx.arc(cx, cy, centerGap, endAngle, startAngle, true);
                ctx.closePath();
                
                ctx.fillStyle = fillGrad;
                ctx.fill();
                ctx.lineWidth = 1;
                ctx.strokeStyle = "rgba(255, 255, 255, 0.15)";
                ctx.stroke();

                ctx.save();
                ctx.translate(cx, cy);
                ctx.rotate(startAngle + sliceAngle / 2);
                ctx.fillStyle = "#FFFFFF";
                
                const computedFontSize = Math.max(9, Math.min(13, parseFloat(340 / numSlices)));
                ctx.font = `800 ${computedFontSize}px 'Plus Jakarta Sans', sans-serif`;
                ctx.textAlign = "right";
                ctx.textBaseline = "middle";
                
                let nameStr = players[i];
                const maxCharacterLength = Math.floor(radius * 0.05);
                if (nameStr.length > maxCharacterLength) {
                    nameStr = nameStr.substring(0, maxCharacterLength - 2) + "..";
                }
                
                ctx.fillText(nameStr, radius - 20, 0);
                ctx.restore();
            }
        }

        const bgCanvas = document.getElementById("ambientEngine");
        const bgCtx = bgCanvas.getContext("2d");
        let ambientStars = [];

        function resizeAmbientCanvas() {
            bgCanvas.width = window.innerWidth;
            bgCanvas.height = window.innerHeight;
        }
        window.addEventListener("resize", resizeAmbientCanvas);
        resizeAmbientCanvas();

        const goldRGBs = [{r: 255, g: 213, b: 74}, {r: 255, g: 193, b: 7}, {r: 255, g: 235, b: 59}];
        for(let i=0; i<35; i++) {
            ambientStars.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                size: Math.random() * 2.5 + 1,
                alpha: Math.random() * 0.4 + 0.4,
                speed: Math.random() * 0.008 + 0.003,
                colorProfile: goldRGBs[Math.floor(Math.random() * goldRGBs.length)]
            });
        }

        function loopAmbientBackground() {
            bgCtx.clearRect(0, 0, bgCanvas.width, bgCanvas.height);
            ambientStars.forEach(s => {
                s.alpha += s.speed;
                if(s.alpha > 0.8 || s.alpha < 0.4) { s.speed = -s.speed; }
                bgCtx.beginPath();
                bgCtx.arc(s.x, s.y, s.size, 0, Math.PI*2);
                bgCtx.fillStyle = `rgba(${s.colorProfile.r}, ${s.colorProfile.g}, ${s.colorProfile.b}, ${Math.max(0.4, Math.min(0.8, s.alpha))})`;
                bgCtx.fill();
            });
            requestAnimationFrame(loopAmbientBackground);
        }
        loopAmbientBackground();

        const pointerPin = document.getElementById("pointerPin");
        let lastSegmentLogged = -1;

        function runPointerVisualFeedback(velocity) {
            if (velocity > 0.015) {
                const numSlices = players.length;
                const sliceAngle = (2 * Math.PI) / numSlices;
                const normalizedAngle = (1.5 * Math.PI - currentAngleOffset) % (2 * Math.PI);
                const standardAngle = normalizedAngle < 0 ? normalizedAngle + 2 * Math.PI : normalizedAngle;
                const activeIndex = Math.floor(standardAngle / sliceAngle) % numSlices;

                if (activeIndex !== lastSegmentLogged) {
                    lastSegmentLogged = activeIndex;
                    pointerPin.style.transform = "translateX(-50%) rotate(-18deg)";
                    setTimeout(() => pointerPin.style.transform = "translateX(-50%) rotate(0deg)", 50);
                }
            }
        }

        document.getElementById("megaSpinBtn").addEventListener("click", () => {
            if (isSpinning || players.length === 0) return;
            isSpinning = true;
            document.getElementById("megaSpinBtn").disabled = true;

            let momentumForce = Math.random() * 0.22 + 0.38; 
            const decayFactor = 0.985; 
            const cutOffThreshold = 0.0008;

            function processFrame() {
                momentumForce *= decayFactor;
                currentAngleOffset += momentumForce;
                currentAngleOffset %= (2 * Math.PI);
                
                drawWheel();
                runPointerVisualFeedback(momentumForce);

                if (momentumForce > cutOffThreshold) {
                    requestAnimationFrame(processFrame);
                } else {
                    isSpinning = false;
                    evaluateSynchronizedWinner();
                }
            }
            processFrame();
        });

        function evaluateSynchronizedWinner() {
            const numSlices = players.length;
            const sliceAngle = (2 * Math.PI) / numSlices;
            let exactTargetAngle = (1.5 * Math.PI - currentAngleOffset) % (2 * Math.PI);
            if (exactTargetAngle < 0) exactTargetAngle += 2 * Math.PI;

            const strictWinnerIndex = Math.floor(exactTargetAngle / sliceAngle) % numSlices;
            activeSelectedPlayer = players[strictWinnerIndex];

            document.getElementById("championTarget").innerText = activeSelectedPlayer;
            document.getElementById("victoryScreen").classList.add("active");
            document.getElementById("flowStep1").classList.add("visible");
            document.getElementById("flowStep2").classList.remove("visible");
            
            initializeConfettiSparks();
            loopCelebrationScreen();
        }

        document.getElementById("isPresentBtn").addEventListener("click", () => {
            players = players.filter(p => p !== activeSelectedPlayer);
            drawWheel();
            document.getElementById("flowStep1").classList.remove("visible");
            document.getElementById("flowStep2").classList.add("visible");
            document.getElementById("turnPlayerTitle").innerText = activeSelectedPlayer + ", IT'S YOUR TURN!";
        });

        document.getElementById("isAbsentBtn").addEventListener("click", () => {
            players = players.filter(p => p !== activeSelectedPlayer);
            drawWheel();
            dismissOverlayToWheel();
        });

        document.getElementById("backToWheelBtn").addEventListener("click", () => {
            dismissOverlayToWheel();
        });

        function dismissOverlayToWheel() {
            document.getElementById("victoryScreen").classList.remove("active");
            confettiSparks = [];
            document.getElementById("megaSpinBtn").disabled = false;
        }

        let confettiSparks = [];
        const celCanvas = document.getElementById("celebrationCanvas");
        const celCtx = celCanvas.getContext("2d");

        function initializeConfettiSparks() {
            celCanvas.width = window.innerWidth;
            celCanvas.height = window.innerHeight;
            confettiSparks = [];
            const colorPalette = ["#FFD700", "#FF4081", "#6C2BD9", "#2F62CC", "#22B8CF"];
            for (let i = 0; i < 80; i++) {
                confettiSparks.push({
                    x: Math.random() * celCanvas.width,
                    y: Math.random() * -60 - 20,
                    rotation: Math.random() * 360,
                    rotationSpeed: (Math.random() - 0.5) * 10,
                    vx: (Math.random() - 0.5) * 4,
                    vy: Math.random() * 5 + 4,
                    width: Math.random() * 8 + 6,
                    height: Math.random() * 12 + 8,
                    color: colorPalette[Math.floor(Math.random() * colorPalette.length)]
                });
            }
        }

        function loopCelebrationScreen() {
            celCtx.clearRect(0, 0, celCanvas.width, celCanvas.height);
            let hasActiveConfetti = false;

            confettiSparks.forEach(p => {
                if (p.y < celCanvas.height + 20) {
                    hasActiveConfetti = true;
                    p.y += p.vy;
                    p.x += p.vx;
                    p.rotation += p.rotationSpeed;

                    celCtx.save();
                    celCtx.translate(p.x, p.y);
                    celCtx.rotate((p.rotation * Math.PI) / 180);
                    celCtx.fillStyle = p.color;
                    celCtx.fillRect(-p.width / 2, -p.height / 2, p.width, p.height);
                    celCtx.restore();
                }
            });

            if (hasActiveConfetti && document.getElementById("victoryScreen").classList.contains("active")) {
                requestAnimationFrame(loopCelebrationScreen);
            }
        }

        drawWheel();
    </script>
</body>
</html>
"""

# --- INJECT DATA PLACEHOLDERS ---
game_show_engine = game_show_engine.replace(
    "__PLAYERS_PLACEHOLDER__", serialized_members
)
game_show_engine = game_show_engine.replace("__LOGO_BASE64__", LOGO_BASE64)

# --- STREAMLIT CSS OVERRIDES & MOUNT ---
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"], .main, .block-container {
            padding: 0 !important; margin: 0 !important; max-width: 100vw !important; height: 100vh !important; overflow: hidden !important;
        }
        [data-testid="stHeader"], [data-testid="stToolbar"] { visibility: hidden !important; display: none !important; }
        div[data-testid="stBlock"] { padding: 0 !important; }
    </style>
""",
    unsafe_allow_html=True,
)

components.html(game_show_engine, height=850, scrolling=False)
