import streamlit as st
import json
import base64

# --- IMMERSIVE VIEWPORT CONFIGURATION SETUP ---
st.set_page_config(
    page_title="Arena | Wheel of Fun Friday",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- EXPANDED 10-CATEGORY CONFIGURABLE ASSET MATRIX ---
CATEGORIES_DATA = {
    "RAPID_FIRE": {
        "name": "🎤 RAPID FIRE",
        "desc": "Answer 5 lightning-fast questions back-to-back!",
        "questions": [
            "Tea or Coffee?", "Mountains or Beach?", "Android or iPhone?", 
            "Early Bird or Night Owl?", "Work from Home or Office?", "Pizza or Biryani?", 
            "Netflix or YouTube?", "Summer or Winter?", "Books or Movies?", 
            "Morning workout or Evening workout?", "Instagram or LinkedIn?", 
            "City life or Village life?", "Cats or Dogs?", "Sweet or Spicy food?", "Train or Flight?"
        ]
    },
    "FUN_QA": {
        "name": "😂 FUN Q&A",
        "desc": "Time for some unfiltered, hilarious team bonding!",
        "questions": [
            "What's the funniest thing that happened this week?", "What's your most used emoji?", 
            "What's one app you can't live without?", "What's your weirdest habit?", 
            "What was your dream job as a child?", "What's your hidden talent?", 
            "The best advice you've ever received?", "What's your favorite weekend activity?", 
            "What's one skill you want to learn?", "What’s your biggest productivity hack?"
        ]
    },
    "WOULD_YOU_RATHER": {
        "name": "🤔 WOULD YOU RATHER",
        "desc": "Make an impossible choice live in front of the room!",
        "questions": [
            "Would you rather work from a beach or a mountain cabin?", "Would you rather have unlimited food or unlimited travel?", 
            "Would you rather never watch movies again or never use social media?", "Would you rather be invisible or read minds?", 
            "Would you rather travel to the past or future?", "Would you rather have meetings all day or emails all day?", 
            "Would you rather live on Mars or underwater?", "Would you rather always be early or always be late?", 
            "Would you rather have unlimited money or unlimited free time?"
        ]
    },
    "CEO_MODE": {
        "name": "👑 IF YOU WERE CEO",
        "desc": "You are running the empire for 24 hours. What changes?",
        "questions": [
            "If you were CEO for a day, what would be your first decision?", "What workplace policy would you introduce?", 
            "What would you improve for employees?", "How would you increase team happiness?", 
            "What office perk would you add?", "What process would you completely remove?", "What would be your company slogan?"
        ]
    },
    "CM_MODE": {
        "name": "🏛️ IF YOU WERE CHIEF MINISTER",
        "desc": "Take the oath of office! Real-world problem solving active.",
        "questions": [
            "What's the first thing you'd improve in your city?", "How would you solve traffic issues?", 
            "What public service would you launch?", "What new rule would you introduce?", 
            "How would you improve education?", "What would be your biggest priority?"
        ]
    },
    "CRICKETER_MODE": {
        "name": "🏏 CRICKETER MODE",
        "desc": "Walk out from the pavilion under stadium spotlights!",
        "questions": [
            "Which IPL team would you play for?", "Batter, Bowler or All-Rounder?", 
            "Which cricketer would be your mentor?", "What would be your signature celebration?", 
            "Which stadium would be your favorite?", "What jersey number would you choose?", 
            "Which cricket legend would you like to meet?"
        ]
    },
    "CELEBRITY_MODE": {
        "name": "🎬 CELEBRITY MODE",
        "desc": "Roll out the red carpet, the paparazzi have arrived!",
        "questions": [
            "Who would play you in a movie?", "What would your movie title be?", 
            "What genre would your film belong to?", "What would your stage name be?", 
            "Which celebrity would be your co-star?", "What would your acceptance speech sound like?"
        ]
    },
    "ALTERNATE_UNIVERSE": {
        "name": "🚀 ALTERNATE UNIVERSE",
        "desc": "Step through a dimensional rift into another reality!",
        "questions": [
            "If you were an astronaut, which planet would you visit?", "If you were a YouTuber, what content would you create?", 
            "If you were a superhero, what power would you choose?", "If you were a detective, what cases would you solve?", 
            "If you could instantly master one skill, what would it be?", "If you could live in any fictional world, which one?"
        ]
    },
    "PLOT_TWIST": {
        "name": "🎭 PLOT TWIST",
        "desc": "Spilling workplace lore with a creative sci-fi twist!",
        "questions": [
            "If your life was a movie, what would the title be?", "If Friday had a slogan, what would it be?", 
            "If the team became a band, what would its name be?", "Which teammate would survive a zombie apocalypse?", 
            "If your manager was a superhero, what would the superpower be?", "If work had a theme song, what would it be called?"
        ]
    },
    "FUN_FACT": {
        "name": "🌟 FUN FACT ABOUT YOURSELF",
        "desc": "Let down your guard and share a hidden story!",
        "questions": [
            "Tell us something nobody in the team knows about you.", "Share an unusual hobby.", 
            "What's a unique experience you've had?", "What's a surprising fact about yourself?", 
            "What's one thing on your bucket list?", "What's your proudest achievement outside work?"
        ]
    }
}

MEMBERS = [
    "Ajaz", "Amit", "Ankur", "Anushree", "Arpit", "Atharva", "Ayush", "Ayushma",
    "Bhabesh", "Gautam", "Jeet", "Kali", "Kartiki", "Obaiah", "Irfan", "Neha",
    "Nishank", "Prasad", "Pratik", "Pritesh", "Roshni", "Saket", "Sampada", "Shailavi",
    "Shubham", "Shubhangi", "Soham", "Sonali", "Soumyashree", "Swanand", "Vedant", "Yasmin"
]

# --- DATA SERIALIZATION LAYER ---
serialized_members = json.dumps(MEMBERS)
serialized_categories_pack = json.dumps(CATEGORIES_DATA)

# --- PURE ARCADE RENDERING RUNTIME ENGINE ---
game_show_engine = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wheel of Fun Friday - Arcade Stage</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=500;700;800&family=Space+Grotesk:wght=700;900&display=swap');

        /* STRUCTURAL VIEWPORT RESET MECHANICS */
        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        html, body {
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            background: #04050f;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #F8FAFC;
        }

        /* RESPONSIVE LAYOUT MATRIX FOR 1366 & 1920 SCREEN ENGINE */
        .game-stage {
            position: relative;
            width: 100vw;
            height: 100vh;
            background: radial-gradient(circle at 50% 35%, #151b3a 0%, #0a0d22 60%, #04050f 100%);
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
            letter-spacing: -1.5px;
            background: linear-gradient(135deg, #FFE259 0%, #FFA751 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
            filter: drop-shadow(0 4px 10px rgba(255, 167, 81, 0.3));
        }
        .stage-header p {
            font-size: clamp(0.7rem, 1.5vh, 0.9rem);
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #6366f1;
            font-weight: 800;
            margin-top: 2px;
        }

        /* SCALED HERO WHEEL THEATER FRAME */
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
            width: 102%;
            height: 102%;
            border-radius: 50%;
            background: radial-gradient(circle, transparent 65%, #A37000 68%, #FFD700 73%, #FFA500 78%, #7851A9 83%, #201440 100%);
            box-shadow: 
                0 20px 45px rgba(0, 0, 0, 0.7),
                inset 0 0 30px rgba(255, 215, 0, 0.5),
                0 0 40px rgba(124, 58, 237, 0.25);
            z-index: 3;
            pointer-events: none;
        }

        #wheelCanvas {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            z-index: 2;
        }

        /* SYNCHRONIZED TOP ANGLE POINTER PIN */
        .premium-pointer {
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%) rotate(0deg);
            width: clamp(30px, 5vh, 42px);
            height: clamp(40px, 6.5vh, 52px);
            background: linear-gradient(185deg, #FFFFFF 0%, #FFD700 30%, #D4AF37 70%, #8B6508 100%);
            clip-path: polygon(50% 100%, 0 0, 100% 0);
            filter: drop-shadow(0 8px 10px rgba(0,0,0,0.5));
            z-index: 8;
            transform-origin: 50% 15%;
            transition: transform 0.1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .center-hub {
            position: absolute;
            width: clamp(60px, 11vh, 84px);
            height: clamp(60px, 11vh, 84px);
            border-radius: 50%;
            background: radial-gradient(circle, #FFFFFF 0%, #FFF4B0 20%, #FFD700 60%, #B8860B 90%, #5E4500 100%);
            box-shadow: 0 6px 20px rgba(0,0,0,0.5), 0 0 25px rgba(255, 215, 0, 0.7);
            z-index: 6;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: clamp(1.2rem, 2.5vh, 1.8rem);
            animation: hubGlowPulse 2s infinite ease-in-out;
        }

        @keyframes hubGlowPulse {
            0%, 100% { box-shadow: 0 6px 20px rgba(0,0,0,0.5), 0 0 15px rgba(255, 215, 0, 0.5); }
            50% { box-shadow: 0 6px 20px rgba(0,0,0,0.5), 0 0 35px rgba(255, 215, 0, 0.9); transform: scale(1.02); }
        }

        .spin-trigger-wrapper {
            z-index: 10;
            height: 12vh;
            display: flex;
            align-items: center;
        }

        .spin-cta-btn {
            outline: none;
            border: none;
            background: linear-gradient(180deg, #FF6EA7 0%, #FF3D81 40%, #D61254 100%);
            color: #FFF;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 900;
            font-size: clamp(1.1rem, 2.5vh, 1.5rem);
            letter-spacing: 1px;
            padding: clamp(12px, 2vh, 18px) clamp(40px, 6vw, 65px);
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 
                0 10px 0 #9E0034,
                0 15px 30px rgba(255, 61, 129, 0.35);
            text-transform: uppercase;
            transition: transform 0.1s;
        }

        .spin-cta-btn:hover { transform: scale(1.03); }
        .spin-cta-btn:active {
            transform: translateY(6px);
            box-shadow: 0 4px 0 #9E0034, 0 8px 15px rgba(255, 61, 129, 0.5);
        }

        /* STAGED CELEBRATION DISPATCH ENGINE OVERLAY */
        .celebration-screen {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: 100;
            background: rgba(4, 5, 15, 0.95);
            backdrop-filter: blur(25px);
            opacity: 0; pointer-events: none;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2vh 2vw;
            transition: opacity 0.5s ease-out;
        }
        .celebration-screen.active { opacity: 1; pointer-events: auto; }

        #celebrationCanvas {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 101;
        }

        /* ORCHESTRATED STEP CONTROLLER WINDOW */
        .card-stage {
            position: relative;
            z-index: 105;
            width: 100%;
            max-width: 580px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        /* INTERACTION GLASSMORPHIC CONTAINER CARD UNITS */
        .flow-card {
            width: 100%;
            background: rgba(18, 24, 54, 0.85);
            border: 2px solid rgba(255, 215, 0, 0.3);
            border-radius: 28px;
            padding: clamp(20px, 4vh, 35px);
            text-align: center;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.7);
            display: none;
            animation: cardZoomIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.2) forwards;
        }
        .flow-card.visible { display: block; }

        @keyframes cardZoomIn {
            from { transform: scale(0.8) translateY(30px); opacity: 0; }
            to { transform: scale(1) translateY(0); opacity: 1; }
        }

        .avatar-circle-halo {
            width: clamp(80px, 12vh, 110px);
            height: clamp(80px, 12vh, 110px);
            border-radius: 50%;
            margin: 0 auto 15px auto;
            background: linear-gradient(135deg, #FFD700 0%, #FF3D81 100%);
            padding: 3px;
            box-shadow: 0 8px 20px rgba(255, 61, 129, 0.4);
        }
        .avatar-inner {
            width: 100%; height: 100%;
            border-radius: 50%; background: #0B1020;
            display: flex; align-items: center; justify-content: center;
            font-size: clamp(2rem, 5vh, 3.2rem);
        }

        .spotlight-sub {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: clamp(0.8rem, 1.8vh, 1.05rem);
            color: #FFD700; letter-spacing: 3px;
            text-transform: uppercase; margin-bottom: 4px;
        }
        .spotlight-name {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 900;
            font-size: clamp(2.2rem, 6vh, 3.8rem);
            color: #FFF; letter-spacing: -1.5px;
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
            margin-bottom: 12px; text-transform: uppercase;
        }

        .loot-badge {
            display: inline-flex;
            background: rgba(255, 215, 0, 0.12);
            border: 1.5px solid #FFD700;
            padding: 6px 22px; border-radius: 50px;
            color: #FFD700; font-weight: 800;
            font-size: clamp(0.9rem, 1.8vh, 1.1rem);
        }

        /* RAPID FIRE INTEGRATED DYNAMIC CARD SLIDER VIEWPORT */
        .rapid-fire-wrapper {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 25px;
            margin-top: 15px;
            width: 100%;
            position: relative;
            min-height: 140px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .rapid-card {
            display: none;
            font-size: clamp(1.3rem, 2.8vh, 1.8rem);
            font-weight: 800;
            font-family: 'Space Grotesk', sans-serif;
            color: #FFE259;
            text-align: center;
            animation: rapidCardShift 0.3s ease-out;
        }
        .rapid-card.active-sub { display: block; }
        
        @keyframes rapidCardShift {
            from { opacity: 0; transform: scale(0.9) translateY(10px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .rapid-badge-counter {
            position: absolute;
            top: -12px;
            background: #EC4899;
            color: white;
            font-weight: 800;
            font-size: 0.75rem;
            padding: 3px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* CHOSEN QUESTIONS VIEWPORT */
        .chosen-question-box {
            background: rgba(6, 182, 214, 0.08);
            border: 2px solid rgba(6, 182, 214, 0.3);
            border-radius: 20px;
            padding: 25px;
            margin-top: 20px;
            font-size: clamp(1.2rem, 2.5vh, 1.6rem);
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 800;
            color: #FFF;
            line-height: 1.4;
        }

        /* CONTROL FLOW SYSTEM ACTIONS PLATFORM */
        .flow-actions {
            margin-top: 25px;
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 15px;
        }
        .action-step-btn {
            background: linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%);
            border: none; outline: none; color: #FFF;
            font-family: 'Space Grotesk', sans-serif; font-weight: 900;
            font-size: clamp(1rem, 2vh, 1.2rem);
            padding: clamp(10px, 1.8vh, 15px) clamp(35px, 4vw, 50px);
            border-radius: 50px; cursor: pointer;
            box-shadow: 0 8px 20px rgba(6, 182, 214, 0.3);
            text-transform: uppercase; letter-spacing: 1px;
            transition: transform 0.1s;
        }
        .action-step-btn:hover { transform: scale(1.03); }
    </style>
</head>
<body>

    <div class="game-stage">
        <canvas class="bg-particles" id="ambientEngine"></canvas>
        
        <div class="stage-header">
            <h1>🎡 Wheel of Fun Friday</h1>
            <p>Premium Reward Terminal</p>
        </div>

        <div class="wheel-theater" id="wheelTheater">
            <div class="premium-pointer" id="pointerPin"></div>
            <div class="gold-rim"></div>
            <div class="center-hub">⭐</div>
            <canvas id="wheelCanvas" width="600" height="600"></canvas>
        </div>

        <div class="spin-trigger-wrapper">
            <button class="spin-cta-btn" id="megaSpinBtn">🎡 Spin the Wheel</button>
        </div>
    </div>

    <div class="celebration-screen" id="victoryScreen">
        <canvas id="celebrationCanvas"></canvas>
        
        <div class="card-stage" id="cardMatrix">
            
            <div class="flow-card" id="flowStep1">
                <div class="avatar-circle-halo"><div class="avatar-inner">👑</div></div>
                <p class="spotlight-sub">🏆 Today's Spotlight</p>
                <h2 class="spotlight-name" id="championTarget">PLAYER</h2>
                <div class="loot-badge">✨ +100 FUN POINTS</div>
            </div>

            <div class="flow-card" id="flowStep2">
                <p id="flowCategoryContext" style="color:#FFD700; font-family:'Space Grotesk'; font-weight:800; font-size:0.9rem; letter-spacing:3px; text-transform:uppercase; margin-bottom:5px;">Category Selection</p>
                <h3 id="categoryTarget" style="font-size:clamp(1.8rem, 4vh, 2.4rem); font-family:'Space Grotesk'; font-weight:900; color:#FFF; margin-bottom:5px;">ACTIVITY</h3>
                <p id="categoryDesc" style="color:#94A3B8; font-size:clamp(0.8rem, 1.6vh, 0.95rem); line-height:1.4; max-width:440px; margin:0 auto 15px auto;"></p>
                
                <div id="standardQuestionBox" class="chosen-question-box"></div>

                <div id="rapidFireBox" class="rapid-fire-wrapper" style="display:none;">
                    <div class="rapid-badge-counter" id="rapidProgress">Question 1 of 5</div>
                    <div class="rapid-card" id="rc1"></div>
                    <div class="rapid-card" id="rc2"></div>
                    <div class="rapid-card" id="rc3"></div>
                    <div class="rapid-card" id="rc4"></div>
                    <div class="rapid-card" id="rc5"></div>
                </div>
            </div>

            <div class="flow-actions">
                <button class="action-step-btn" id="rapidNextBtn" style="display:none; background:linear-gradient(135deg, #EC4899 0%, #F43F5E 100%); box-shadow:0 8px 20px rgba(236,72,153,0.35);">Next Question ⚡</button>
                <button class="action-step-btn" id="flowNextBtn">Continue</button>
            </div>
        </div>
    </div>

    <script>
        // --- SAFE DATA STRINGS RETRIEVED NATIVELY FROM STREAMLIT RUNTIME ---
        const players = __PLAYERS_PLACEHOLDER__;
        const categoriesPack = __CATEGORIES_PLACEHOLDER__;

        const segmentGradients = [
            ["#7C3AED", "#4C1D95"], ["#EC4899", "#9D174D"], 
            ["#3B82F6", "#1E3A8A"], ["#06B6D4", "#0891B2"]  
        ];

        const canvas = document.getElementById("wheelCanvas");
        const ctx = canvas.getContext("2d");
        let currentAngleOffset = 0;
        let isSpinning = false;
        
        let currentWorkflowStep = 1;
        let selectedCategoryKey = "";
        let currentRapidQuestionIdx = 0;

        // HIGH-DENSITY DYNAMIC FONTS WHEEL GENERATOR ENGINE
        function drawWheel() {
            const cx = canvas.width / 2;
            const cy = canvas.height / 2;
            const radius = canvas.width / 2 - 10;
            const numSlices = players.length;
            const sliceAngle = (2 * Math.PI) / numSlices;
            
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            for (let i = 0; i < numSlices; i++) {
                const startAngle = currentAngleOffset + (i * sliceAngle);
                const endAngle = startAngle + sliceAngle;

                const fillGrad = ctx.createRadialGradient(cx, cy, radius * 0.2, cx, cy, radius);
                const colors = segmentGradients[i % segmentGradients.length];
                fillGrad.addColorStop(0, colors[0]);
                fillGrad.addColorStop(0.85, colors[1]);
                fillGrad.addColorStop(1, "#020308");

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
                
                ctx.fillText(nameStr, radius - 30, 0);
                ctx.restore();
            }
        }

        // --- AMBIENT BACKGROUND STARS PARTICLES LAYER ---
        const bgCanvas = document.getElementById("ambientEngine");
        const bgCtx = bgCanvas.getContext("2d");
        let ambientStars = [];

        function resizeAmbientCanvas() {
            bgCanvas.width = window.innerWidth;
            bgCanvas.height = window.innerHeight;
        }
        window.addEventListener("resize", resizeAmbientCanvas);
        resizeAmbientCanvas();

        for(let i=0; i<45; i++) {
            ambientStars.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                size: Math.random() * 2 + 1,
                alpha: Math.random(),
                speed: Math.random() * 0.015 + 0.004
            });
        }

        function loopAmbientBackground() {
            bgCtx.clearRect(0, 0, bgCanvas.width, bgCanvas.height);
            ambientStars.forEach(s => {
                s.alpha += s.speed;
                if(s.alpha > 1 || s.alpha < 0) s.speed = -s.speed;
                bgCtx.beginPath();
                bgCtx.arc(s.x, s.y, s.size, 0, Math.PI*2);
                bgCtx.fillStyle = `rgba(255, 226, 89, ${Math.abs(s.alpha)})`;
                bgCtx.fill();
            });
            requestAnimationFrame(loopAmbientBackground);
        }
        loopAmbientBackground();

        // --- MATH RECTIFIED POINTER PHYSICS SYSTEMS ---
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

            let momentumForce = Math.random() * 0.2 + 0.35; 
            const decayFactor = 0.993; 
            const cutOffThreshold = 0.001;

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

        // --- MATH SYNCHRONIZED WINNER EXTRACTION MATRIX ---
        function evaluateSynchronizedWinner() {
            const numSlices = players.length;
            const sliceAngle = (2 * Math.PI) / numSlices;
            
            let exactTargetAngle = (1.5 * Math.PI - currentAngleOffset) % (2 * Math.PI);
            if (exactTargetAngle < 0) exactTargetAngle += 2 * Math.PI;

            const strictWinnerIndex = Math.floor(exactTargetAngle / sliceAngle) % numSlices;
            const trueWinner = players[strictWinnerIndex];

            // Randomly pick 1 out of the 10 categories available
            const categoryKeys = Object.keys(categoriesPack);
            selectedCategoryKey = categoryKeys[Math.floor(Math.random() * categoryKeys.length)];
            const selectedCategory = categoriesPack[selectedCategoryKey];
            
            // Randomly select target questions
            const shuffledPool = [...selectedCategory.questions].sort(() => 0.5 - Math.random());

            document.getElementById("championTarget").innerText = trueWinner;
            document.getElementById("categoryTarget").innerText = selectedCategory.name;
            document.getElementById("categoryDesc").innerText = selectedCategory.desc;
            
            // Setup layouts depending on execution logic blocks
            if (selectedCategoryKey === "RAPID_FIRE") {
                document.getElementById("standardQuestionBox").style.display = "none";
                document.getElementById("rapidFireBox").style.display = "flex";
                
                // Populate the 5 hidden slots natively
                for (let idx = 1; idx <= 5; idx++) {
                    document.getElementById(`rc${idx}`).innerText = shuffledPool[idx - 1];
                }
                currentRapidQuestionIdx = 1;
            } else {
                document.getElementById("rapidFireBox").style.display = "none";
                document.getElementById("standardQuestionBox").style.display = "block";
                document.getElementById("standardQuestionBox").innerText = shuffledPool[0];
            }

            triggerStagedShowSequence();
        }

        // --- STEP-BASED INTERACTIVE WORKFLOW OPERATOR ENGINE ---
        let fireworks = [];
        const celCanvas = document.getElementById("celebrationCanvas");
        const celCtx = celCanvas.getContext("2d");

        function triggerStagedShowSequence() {
            celCanvas.width = window.innerWidth;
            celCanvas.height = window.innerHeight;
            
            currentWorkflowStep = 1;
            document.getElementById("victoryScreen").classList.add("active");
            
            updateWorkflowDisplayVisibility();
            initializeFireworkSparks();
            loopCelebrationScreen();
        }

        function updateWorkflowDisplayVisibility() {
            document.getElementById("flowStep1").classList.remove("visible");
            document.getElementById("flowStep2").classList.remove("visible");
            
            const actionBtn = document.getElementById("flowNextBtn");
            const rapidBtn = document.getElementById("rapidNextBtn");

            if (currentWorkflowStep === 1) {
                document.getElementById("flowStep1").classList.add("visible");
                actionBtn.innerText = "Reveal Challenge";
                actionBtn.style.display = "inline-block";
                rapidBtn.style.display = "none";
            } else if (currentWorkflowStep === 2) {
                document.getElementById("flowStep2").classList.add("visible");
                
                if (selectedCategoryKey === "RAPID_FIRE") {
                    actionBtn.style.display = "none"; // Hide main continue until sequence drops complete
                    rapidBtn.style.display = "inline-block";
                    renderActiveRapidCard();
                } else {
                    actionBtn.innerText = "Spin Next Round";
                    actionBtn.style.display = "inline-block";
                    rapidBtn.style.display = "none";
                }
            }
        }

        function renderActiveRapidCard() {
            for (let idx = 1; idx <= 5; idx++) {
                document.getElementById(`rc${idx}`).classList.remove("active-sub");
            }
            document.getElementById(`rc${currentRapidQuestionIdx}`).classList.add("active-sub");
            document.getElementById("rapidProgress").innerText = `Question ${currentRapidQuestionIdx} of 5`;
        }

        document.getElementById("rapidNextBtn").addEventListener("click", () => {
            if (currentRapidQuestionIdx < 5) {
                currentRapidQuestionIdx++;
                renderActiveRapidCard();
            } else {
                // Rapid sequence done, expose exit route controller 
                document.getElementById("rapidNextBtn").style.display = "none";
                const actionBtn = document.getElementById("flowNextBtn");
                actionBtn.innerText = "Spin Next Round";
                actionBtn.style.display = "inline-block";
            }
        });

        document.getElementById("flowNextBtn").addEventListener("click", () => {
            if (currentWorkflowStep < 2) {
                currentWorkflowStep++;
                updateWorkflowDisplayVisibility();
            } else {
                document.getElementById("victoryScreen").classList.remove("active");
                fireworks = [];
                document.getElementById("megaSpinBtn").disabled = false;
            }
        });

        // --- RENDER SELECTION CELEBRATORY VISUAL EFFECTS ENGINE ---
        function initializeFireworkSparks() {
            for (let i = 0; i < 70; i++) {
                fireworks.push({
                    x: Math.random() * celCanvas.width,
                    y: celCanvas.height + Math.random() * 80,
                    targetY: Math.random() * (celCanvas.height * 0.55) + 50,
                    speed: Math.random() * 4 + 5,
                    color: ["#FFD700", "#FF3D81", "#06B6D4", "#7C3AED", "#10B981"][Math.floor(Math.random() * 5)],
                    exploded: false,
                    sparks: []
                });
            }
        }

        function loopCelebrationScreen() {
            celCtx.clearRect(0, 0, celCanvas.width, celCanvas.height);
            let holdsActiveAnimFrame = false;

            fireworks.forEach(f => {
                if (!f.exploded) {
                    holdsActiveAnimFrame = true;
                    f.y -= f.speed;
                    if (f.y <= f.targetY) {
                        f.exploded = true;
                        for (let s = 0; s < 20; s++) {
                            f.sparks.push({
                                x: f.x, y: f.y,
                                vx: (Math.random() - 0.5) * 6,
                                vy: (Math.random() - 0.5) * 6,
                                size: Math.random() * 2.5 + 1.5,
                                alpha: 1
                            });
                        }
                    } else {
                        celCtx.beginPath();
                        celCtx.arc(f.x, f.y, 3, 0, Math.PI * 2);
                        celCtx.fillStyle = f.color;
                        celCtx.fill();
                    }
                } else {
                    f.sparks.forEach(p => {
                        if (p.alpha > 0) {
                            holdsActiveAnimFrame = true;
                            p.x += p.vx; p.y += p.vy; p.alpha -= 0.015; p.vy += 0.04;
                            celCtx.beginPath();
                            celCtx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                            celCtx.fillStyle = f.color;
                            celCtx.globalAlpha = Math.max(0, p.alpha);
                            celCtx.fill();
                            celCtx.globalAlpha = 1.0;
                        }
                    });
                }
            });

            if (holdsActiveAnimFrame || document.getElementById("victoryScreen").classList.contains("active")) {
                requestAnimationFrame(loopCelebrationScreen);
            }
        }

        // Initialize frame
        drawWheel();
    </script>
</body>
</html>
"""

# --- CONTEXT STRING DATA INTERPOLATION PIPELINE ---
game_show_engine = game_show_engine.replace("__PLAYERS_PLACEHOLDER__", serialized_members)
game_show_engine = game_show_engine.replace("__CATEGORIES_PLACEHOLDER__", serialized_categories_pack)

# --- BASE64 DATA PACKAGED PIPELINE ---

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
# ADD THESE LINES INSTEAD
import streamlit.components.v1 as components
components.html(game_show_engine, height=900, scrolling=False)
