import streamlit as st
import json
import base64
import streamlit.components.v1 as components

# --- IMMERSIVE VIEWPORT CONFIGURATION SETUP ---
st.set_page_config(
    page_title="Arena | Tongue Twister Friday",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CURATED TONGUE TWISTERS ASSET MATRIX ---
TONGUE_TWISTERS = [
    "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked.",
    "She sells sea shells by the sea shore. The shells she sells are surely seashells.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "Betty Botter bought some butter but she said the butter's bitter.",
    "Unique New York, New York's unique, you know New York is unique.",
    "I scream, you scream, we all scream for ice cream!",
    "Red lorry, yellow lorry, red lorry, yellow lorry.",
    "Six sleek swans swam swiftly southwards.",
    "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn't fuzzy, was he?",
    "Pad kid poured curd pulled cod.",
    "Can you can a can as a canner can can a can?",
    "Which witch wished which wicked wish?",
    "Fred fed Ted bread, and Ted fed Fred bread.",
    "Lesser leather never weathered wetter weather better.",
    "A loyal warrior headed to a royal warrior battle."
]

MEMBERS = [
    "Ajaz", "Amit", "Ankur", "Anushree", "Arpit", "Atharva", "Ayush", "Ayushma",
    "Bhabesh", "Gautam", "Jeet", "Kartiki", "Obaiah", "Irfan", "Neha",
    "Nishank", "Prasad", "Pratik", "Pritesh", "Roshni", "Saket", "Sampada", "Shailavi",
    "Shubham", "Shubhangi", "Soham", "Sonali", "Soumyashree", "Swanand", "Vedant", "Yasmin"
]

# --- DATA SERIALIZATION LAYER ---
serialized_members = json.dumps(MEMBERS)
serialized_twisters = json.dumps(TONGUE_TWISTERS)

# --- LUXURY MIDNIGHT CARNIVAL ENGINE RUNTIME ---
game_show_engine = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tongue Twister Friday - Luxury Stage</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=500;700;800&family=Space+Grotesk:wght=700;900&family=JetBrains+Mono:wght=700&display=swap');

        /* STRUCTURAL VIEWPORT RESET MECHANICS */
        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        html, body {
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            background: #020827;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #F8FAFC;
        }

        /* PREMIUM radial CONTEXT THEATER STAGE */
        .game-stage {
            position: relative;
            width: 100vw;
            height: 100vh;
            background: radial-gradient(circle at center, #08145C 0%, #030B35 40%, #020827 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            padding: 3vh 2vw;
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
            height: 10vh;
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

        /* HERO WHEEL THEATER METALLIC FRAME */
        .wheel-theater {
            position: relative;
            width: clamp(320px, 62vh, 520px);
            height: clamp(320px, 62vh, 520px);
            z-index: 5;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: auto 0;
        }

        .gold-rim {
            position: absolute;
            width: 101.5%;
            height: 101.5%;
            border-radius: 50%;
            background: radial-gradient(circle, transparent 65%, #E6A800 66%, #FFC107 72%, #FFE76A 76%, #FFC107 82%, transparent 86%);
            box-shadow: 
                0 0 20px rgba(255,215,0,.6),
                0 0 50px rgba(255,215,0,.3),
                0 20px 45px rgba(0, 0, 0, 0.6);
            z-index: 3;
            pointer-events: none;
        }

        #wheelCanvas {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            z-index: 2;
        }

        /* GOLDEN TRIANGLE POINTER INDICATOR */
        .premium-pointer {
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%) rotate(0deg);
            width: clamp(30px, 5vh, 42px);
            height: clamp(40px, 6.5vh, 52px);
            background: linear-gradient(185deg, #FFF3B0 0%, #FFD700 50%, #D4AF37 100%);
            clip-path: polygon(50% 100%, 0 0, 100% 0);
            filter: drop-shadow(0 0 15px rgba(255,215,0,.8));
            z-index: 8;
            transform-origin: 50% 15%;
            transition: transform 0.1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        /* GOLD COIN CENTER HUB */
        .center-hub {
            position: absolute;
            width: clamp(60px, 11vh, 84px);
            height: clamp(60px, 11vh, 84px);
            border-radius: 50%;
            background: radial-gradient(circle, #FFF9C4 0%, #FFE082 40%, #FFD700 75%, #F4C430 100%);
            box-shadow: 
                inset 0 0 12px rgba(255,255,255,0.8),
                0 6px 20px rgba(0,0,0,0.6), 
                0 0 25px rgba(255, 215, 0, 0.6);
            z-index: 6;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: clamp(1.2rem, 2.5vh, 1.8rem);
            animation: hubGlowPulse 2s infinite ease-in-out;
        }

        @keyframes hubGlowPulse {
            0%, 100% { box-shadow: inset 0 0 12px rgba(255,255,255,0.8), 0 6px 20px rgba(0,0,0,0.6), 0 0 15px rgba(255, 215, 0, 0.4); }
            50% { box-shadow: inset 0 0 12px rgba(255,255,255,0.8), 0 6px 20px rgba(0,0,0,0.6), 0 0 35px rgba(255, 215, 0, 0.8); transform: scale(1.02); }
        }

        .spin-trigger-wrapper {
            z-index: 10;
            height: 12vh;
            display: flex;
            align-items: center;
        }

        /* HOT PINK GAMING ACTION BUTTON */
        .spin-cta-btn {
            outline: none;
            border: none;
            background: linear-gradient(180deg, #FF5FA2 0%, #FF4081 50%, #D81B60 100%);
            color: #FFF;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 900;
            font-size: clamp(1.1rem, 2.5vh, 1.5rem);
            letter-spacing: 1.5px;
            padding: clamp(12px, 2vh, 18px) clamp(40px, 6vw, 65px);
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 
                0 8px 0 #A01347,
                0 15px 30px rgba(255, 64, 129, 0.5);
            text-transform: uppercase;
            transition: transform 0.1s;
        }
        .spin-cta-btn:hover { transform: scale(1.03); filter: brightness(1.05); }
        .spin-cta-btn:active {
            transform: translateY(6px);
            box-shadow: 0 2px 0 #A01347, 0 8px 15px rgba(255, 64, 129, 0.5);
        }

        /* CARNIVAL GLASSMORPHIC INTERACTION CARDS */
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
            max-width: 720px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .flow-card {
            width: 100%;
            background: rgba(11, 19, 62, 0.75);
            border: 2px solid rgba(255, 213, 79, 0.2);
            border-radius: 32px;
            padding: clamp(30px, 5vh, 50px);
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
            width: clamp(80px, 11vh, 100px);
            height: clamp(80px, 11vh, 100px);
            border-radius: 50%;
            margin: 0 auto 20px auto;
            background: linear-gradient(135deg, #FFD54F 0%, #D63384 100%);
            padding: 3px;
            box-shadow: 0 8px 25px rgba(255, 193, 7, 0.3);
        }
        .avatar-inner {
            width: 100%; height: 100%;
            border-radius: 50%; background: #050D45;
            display: flex; align-items: center; justify-content: center;
            font-size: clamp(2rem, 4.5vh, 2.5rem);
        }

        .spotlight-sub {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: clamp(0.85rem, 1.8vh, 1.1rem);
            color: #FFC107; letter-spacing: 4px;
            text-transform: uppercase; margin-bottom: 8px;
        }
        .spotlight-name {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 900;
            font-size: clamp(2.5rem, 6.5vh, 4rem);
            color: #FFF; letter-spacing: -1px;
            text-shadow: 0 0 25px rgba(255, 213, 79, 0.3);
            margin-bottom: 30px; text-transform: uppercase;
        }

        /* TEXT DISPLAY CONFIG MATRIX */
        .twister-display-box {
            background: rgba(2, 8, 39, 0.7);
            border: 2px solid rgba(255, 213, 79, 0.25);
            border-radius: 24px;
            padding: clamp(25px, 4vh, 40px);
            margin: 25px 0;
            font-size: clamp(1.4rem, 3.2vh, 2.1rem);
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            color: #F8FAFC;
            line-height: 1.5;
            box-shadow: inset 0 4px 12px rgba(0,0,0,0.5);
        }

        .timer-viewport {
            font-family: 'JetBrains Mono', monospace;
            font-size: clamp(3.2rem, 7.5vh, 4.8rem);
            font-weight: 700;
            color: #FFC107;
            margin: 15px 0 25px 0;
            background: rgba(0, 0, 0, 0.4);
            padding: 10px 35px;
            border-radius: 18px;
            display: inline-block;
            letter-spacing: -1px;
            border: 1px solid rgba(255, 213, 79, 0.1);
        }

        .flow-actions {
            margin-top: 25px;
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .btn-base {
            border: none; outline: none; color: #FFF;
            font-family: 'Space Grotesk', sans-serif; font-weight: 900;
            font-size: clamp(0.95rem, 2vh, 1.15rem);
            padding: clamp(14px, 2.2vh, 18px) clamp(35px, 4.5vw, 50px);
            border-radius: 50px; cursor: pointer;
            text-transform: uppercase; letter-spacing: 1.5px;
            transition: all 0.15s ease-out;
            display: inline-flex; align-items: center; gap: 8px;
        }
        .btn-base:hover { transform: scale(1.02); filter: brightness(1.1); }
        .btn-base:active { transform: scale(0.98); }

        .btn-green  { background: linear-gradient(135deg, #10B981 0%, #059669 100%); box-shadow: 0 8px 20px rgba(16,185,129,0.3); }
        .btn-red    { background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%); box-shadow: 0 8px 20px rgba(239,68,68,0.3); }
        .btn-blue   { background: linear-gradient(180deg, #FF5FA2 0%, #FF4081 50%, #D81B60 100%); box-shadow: 0 8px 20px rgba(255,64,129,0.3); width: 85%; justify-content: center; font-size: 1.25rem; border-radius: 20px; }
        .btn-orange { background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%); box-shadow: 0 8px 20px rgba(245,158,11,0.3); }
        .btn-purple { background: linear-gradient(135deg, #6C2BD9 0%, #4F46E5 100%); box-shadow: 0 8px 20px rgba(108,43,217,0.3); }
    </style>
</head>
<body>

    <div class="game-stage">
        <canvas class="bg-particles" id="ambientEngine"></canvas>
        
        <div class="stage-header">
            <h1>Tongue Twister Friday</h1>
            <p>Standup Arena Edition</p>
        </div>

        <div class="wheel-theater" id="wheelTheater">
            <div class="premium-pointer" id="pointerPin"></div>
            <div class="gold-rim"></div>
            <div class="center-hub">⭐</div>
            <canvas id="wheelCanvas" width="600" height="600"></canvas>
        </div>

        <div class="spin-trigger-wrapper">
            <button class="spin-cta-btn" id="megaSpinBtn">🎡 Spin Roster</button>
        </div>
    </div>

    <div class="celebration-screen" id="victoryScreen">
        <canvas id="celebrationCanvas"></canvas>
        
        <div class="card-stage" id="cardMatrix">
            
            <div class="flow-card" id="flowStep1">
                <div class="avatar-circle-halo"><div class="avatar-inner">🏆</div></div>
                <p class="spotlight-sub">🏆 Today's Spotlight</p>
                <h2 class="spotlight-name" id="championTarget">PLAYER NAME</h2>
                
                <div class="flow-actions">
                    <button class="btn-base btn-green" id="isPresentBtn">✅ Present</button>
                    <button class="btn-base btn-red" id="isAbsentBtn">❌ Not Available</button>
                </div>
            </div>

            <div class="flow-card" id="flowStep2">
                <p class="spotlight-sub" id="revealSubheading">PREPARE YOURSELF...</p>
                <h2 id="revealPlayerTitle" style="font-size: 2.2rem; margin-bottom: 25px; font-family:'Space Grotesk'; text-transform:uppercase;"></h2>
                <button class="btn-base btn-blue" id="revealChallengeBtn">⚡ Reveal Challenge</button>
            </div>

            <div class="flow-card" id="flowStep3">
                <p class="spotlight-sub">🔴 LIVE CHALLENGE STAGE</p>
                <div class="twister-display-box" id="targetTwisterBox">Populating assets...</div>
                
                <div class="timer-viewport" id="stopwatchDisplay">00:00.00</div>
                
                <div class="flow-actions" id="timerControlsGroup">
                    <button class="btn-base btn-orange" id="startTimerBtn">▶ Start Timer</button>
                    <button class="btn-base btn-red" id="stopTimerBtn" disabled style="opacity:0.5;">⏹ Stop Timer</button>
                </div>

                <div class="flow-actions" id="exitGroup" style="display:none; margin-top:20px;">
                    <button class="btn-base btn-purple" id="backToWheelBtn">🔙 Back To Wheel</button>
                </div>
            </div>

        </div>
    </div>

    <script>
        const players = __PLAYERS_PLACEHOLDER__;
        const twisterPool = __TWISTERS_PLACEHOLDER__;

        // JEWEL-TONE WHEEL SEGMENT REPEATING SPECIFICATION PATTERN
        const segmentGradients = [
            ["#6C2BD9", "#6120C2"], // Purple
            ["#D63384", "#E83E8C"], // Magenta Pink
            ["#2F62CC", "#3867D6"], // Royal Blue
            ["#18A8D8", "#22B8CF"]  // Cyan Blue
        ];

        const canvas = document.getElementById("wheelCanvas");
        const ctx = canvas.getContext("2d");
        let currentAngleOffset = 0;
        let isSpinning = false;
        
        let activeSelectedPlayer = "";
        let activeSelectedTwister = "";
        
        let startTime = 0;
        let elapsedInterval = null;
        let dynamicTimeTrack = 0;

        const participationHistory = [];

        function drawWheel() {
            const cx = canvas.width / 2;
            const cy = canvas.height / 2;
            const radius = canvas.width / 2 - 12;
            const numSlices = players.length;
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
                ctx.moveTo(cx, cy);
                ctx.arc(cx, cy, radius, startAngle, endAngle);
                ctx.fillStyle = fillGrad;
                ctx.fill();

                ctx.lineWidth = 1;
                ctx.strokeStyle = "rgba(255, 255, 255, 0.15)";
                ctx.stroke();

                ctx.save();
                ctx.translate(cx, cy);
                ctx.rotate(startAngle + sliceAngle / 2);
                ctx.fillStyle = "#FFFFFF";
                
                const computedFontSize = Math.max(9, Math.min(14, parseFloat(380 / numSlices)));
                ctx.font = `800 ${computedFontSize}px 'Plus Jakarta Sans', sans-serif`;
                ctx.textAlign = "right";
                ctx.textBaseline = "middle";
                
                let nameStr = players[i];
                const maxCharacterLength = Math.floor(radius * 0.05);
                if (nameStr.length > maxCharacterLength) {
                    nameStr = nameStr.substring(0, maxCharacterLength - 2) + "..";
                }
                
                ctx.fillText(nameStr, radius - 35, 0);
                ctx.restore();
            }
        }

        // --- GOLDEN SPARKS FLOATING PARTICLE ENGINE ---
        const bgCanvas = document.getElementById("ambientEngine");
        const bgCtx = bgCanvas.getContext("2d");
        let ambientStars = [];

        function resizeAmbientCanvas() {
            bgCanvas.width = window.innerWidth;
            bgCanvas.height = window.innerHeight;
        }
        window.addEventListener("resize", resizeAmbientCanvas);
        resizeAmbientCanvas();

        // Jewel-toned / Metallic Gold Spark Palette Config
        const goldRGBs = [
            {r: 255, g: 213, b: 74},  // #FFD54A
            {r: 255, g: 193, b: 7},   // #FFC107
            {r: 255, g: 235, b: 59}   // #FFEB3B
        ];

        for(let i=0; i<50; i++) {
            const baseColor = goldRGBs[Math.floor(Math.random() * goldRGBs.length)];
            ambientStars.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                size: Math.random() * 2.5 + 1,
                alpha: Math.random() * 0.4 + 0.4, // Map initial bounds inside 0.4 - 0.8
                speed: Math.random() * 0.008 + 0.003,
                colorProfile: baseColor
            });
        }

        function loopAmbientBackground() {
            bgCtx.clearRect(0, 0, bgCanvas.width, bgCanvas.height);
            ambientStars.forEach(s => {
                s.alpha += s.speed;
                // Clamp oscillator constraints precisely between 0.4 and 0.8 opacity bounds
                if(s.alpha > 0.8 || s.alpha < 0.4) {
                    s.speed = -s.speed;
                }
                bgCtx.beginPath();
                bgCtx.arc(s.x, s.y, s.size, 0, Math.PI*2);
                bgCtx.fillStyle = `rgba(${s.colorProfile.r}, ${s.colorProfile.g}, ${s.colorProfile.b}, ${Math.max(0.4, Math.min(0.8, s.alpha))})`;
                bgCtx.fill();
            });
            requestAnimationFrame(loopAmbientBackground);
        }
        loopAmbientBackground();

        // --- MATH RECTIFIED POINTER INDICATOR SYSTEM ---
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
            if (isSpinning) return;
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
            switchWorkflowUIVisibility("flowStep1");
            
            initializeConfettiSparks();
            loopCelebrationScreen();
        }

        function switchWorkflowUIVisibility(visibleStepId) {
            document.getElementById("flowStep1").classList.remove("visible");
            document.getElementById("flowStep2").classList.remove("visible");
            document.getElementById("flowStep3").classList.remove("visible");
            
            document.getElementById(visibleStepId).classList.add("visible");
        }

        document.getElementById("isAbsentBtn").addEventListener("click", () => {
            dismissOverlayToWheel();
        });

        document.getElementById("isPresentBtn").addEventListener("click", () => {
            document.getElementById("revealPlayerTitle").innerText = activeSelectedPlayer;
            switchWorkflowUIVisibility("flowStep2");
        });

        document.getElementById("revealChallengeBtn").addEventListener("click", () => {
            const randomIdx = Math.floor(Math.random() * twisterPool.length);
            activeSelectedTwister = twisterPool[randomIdx];

            document.getElementById("targetTwisterBox").innerText = activeSelectedTwister;
            resetStopwatchUI();
            switchWorkflowUIVisibility("flowStep3");
        });

        // --- HIGH-PRECISION RUNTIME TIMING SYSTEM ---
        function resetStopwatchUI() {
            clearInterval(elapsedInterval);
            dynamicTimeTrack = 0;
            document.getElementById("stopwatchDisplay").innerText = "00:00.00";
            document.getElementById("stopwatchDisplay").style.color = "#FFC107";
            
            document.getElementById("startTimerBtn").disabled = false;
            document.getElementById("startTimerBtn").style.opacity = "1";
            document.getElementById("stopTimerBtn").disabled = true;
            document.getElementById("stopTimerBtn").style.opacity = "0.5";
            
            document.getElementById("timerControlsGroup").style.display = "flex";
            document.getElementById("exitGroup").style.display = "none";
        }

        document.getElementById("startTimerBtn").addEventListener("click", () => {
            document.getElementById("startTimerBtn").disabled = true;
            document.getElementById("startTimerBtn").style.opacity = "0.5";
            document.getElementById("stopTimerBtn").disabled = false;
            document.getElementById("stopTimerBtn").style.opacity = "1";
            
            startTime = Date.now();
            elapsedInterval = setInterval(() => {
                dynamicTimeTrack = Date.now() - startTime;
                document.getElementById("stopwatchDisplay").innerText = formatMillisecondsToTimeStr(dynamicTimeTrack);
            }, 10);
        });

        document.getElementById("stopTimerBtn").addEventListener("click", () => {
            clearInterval(elapsedInterval);
            document.getElementById("stopTimerBtn").disabled = true;
            document.getElementById("stopTimerBtn").style.opacity = "0.5";
            
            const structuredFinalTimeString = formatMillisecondsToTimeStr(dynamicTimeTrack);
            document.getElementById("stopwatchDisplay").innerText = structuredFinalTimeString;
            document.getElementById("stopwatchDisplay").style.color = "#10B981";
            
            participationHistory.push({
                name: activeSelectedPlayer,
                tongue_twister: activeSelectedTwister,
                completion_time: structuredFinalTimeString
            });

            document.getElementById("timerControlsGroup").style.display = "none";
            document.getElementById("exitGroup").style.display = "flex";
        });

        document.getElementById("backToWheelBtn").addEventListener("click", () => {
            dismissOverlayToWheel();
        });

        function dismissOverlayToWheel() {
            document.getElementById("victoryScreen").classList.remove("active");
            confettiSparks = [];
            document.getElementById("megaSpinBtn").disabled = false;
        }

        function formatMillisecondsToTimeStr(durationMs) {
            let milliseconds = parseInt((durationMs % 1000) / 10),
                seconds = parseInt((durationMs / 1000) % 60),
                minutes = parseInt((durationMs / (1000 * 60)) % 60);

            minutes = (minutes < 10) ? "0" + minutes : minutes;
            seconds = (seconds < 10) ? "0" + seconds : seconds;
            milliseconds = (milliseconds < 10) ? "0" + milliseconds : milliseconds;

            return minutes + ":" + seconds + "." + milliseconds;
        }

        // --- LUXURY PARTY ENGINE GOLD AND JEWEL CONFETTI SPILL ---
        let confettiSparks = [];
        const celCanvas = document.getElementById("celebrationCanvas");
        const celCtx = celCanvas.getContext("2d");

        function initializeConfettiSparks() {
            celCanvas.width = window.innerWidth;
            celCanvas.height = window.innerHeight;
            confettiSparks = [];

            const colorPalette = ["#FFD700", "#FF4081", "#6C2BD9", "#2F62CC", "#22B8CF"];
            for (let i = 0; i < 120; i++) {
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

        // INITIALIZE APP VIEWPORT DEFAULT FRAME STATE
        drawWheel();
    </script>
</body>
</html>
"""

# --- CONTEXT STRING DATA INTERPOLATION PIPELINE ---
game_show_engine = game_show_engine.replace("__PLAYERS_PLACEHOLDER__", serialized_members)
game_show_engine = game_show_engine.replace("__TWISTERS_PLACEHOLDER__", serialized_twisters)

# --- CSS FULL-SCREEN IFRAME PORT BUFFER SAFEGUARD OVERRIDES ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"], .main, .block-container {
            padding: 0 !important; margin: 0 !important; max-width: 100vw !important; height: 100vh !important; overflow: hidden !important;
        }
        [data-testid="stHeader"], [data-testid="stToolbar"] { visibility: hidden !important; display: none !important; }
        iframe { border: none !important; width: 100vw !important; height: 100vh !important; overflow: hidden !important; display: block !important; }
        div[data-testid="stBlock"] { padding: 0 !important; }
    </style>
""", unsafe_allow_html=True)

# --- BASE64 DATA PACKAGED PIPELINE MOUNT ---
def run_app_securely(html_string):
    b64_html = base64.b64encode(html_string.encode('utf-8')).decode('utf-8')
    data_uri = f"data:text/html;base64,{b64_html}"
    components.iframe(src=data_uri, height=950, scrolling=False)

# Render once
run_app_securely(game_show_engine)
