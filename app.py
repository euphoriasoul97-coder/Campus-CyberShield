
import streamlit as st
import random
import base64
import json
import html
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Campus Cyber Shield v6", page_icon="🛡️", layout="centered")

st.markdown('<style>\n@import url(\'https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Rajdhani:wght@500;600;700&display=swap\');\n:root { --accent:#22d3ee; --accent2:#818cf8; }\n.stApp{background:radial-gradient(circle at 15% 15%,rgba(0,229,255,.16),transparent 25%),radial-gradient(circle at 85% 25%,rgba(124,58,237,.20),transparent 27%),linear-gradient(135deg,#030712,#071326 50%,#020617);color:#f5f7ff}.stApp:before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.18;background-image:linear-gradient(rgba(0,229,255,.12) 1px,transparent 1px),linear-gradient(90deg,rgba(0,229,255,.12) 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(to bottom,black,transparent)}.block-container{max-width:1100px;padding-top:1.2rem;padding-bottom:3rem}\n.hero{padding:30px;border-radius:26px;background:linear-gradient(135deg,rgba(8,24,48,.97),rgba(16,24,58,.94));border:1px solid rgba(0,229,255,.35);box-shadow:0 0 35px rgba(0,229,255,.10),0 20px 60px rgba(0,0,0,.45);margin-bottom:20px;position:relative;overflow:hidden}.hero:after{content:"/// CYBER DEFENSE TRAINING ///";position:absolute;right:20px;bottom:12px;font:700 11px Orbitron,sans-serif;color:rgba(0,229,255,.38);letter-spacing:2px}.hero h1{font-family:Orbitron,sans-serif;letter-spacing:1px}.badge,.level-chip{display:inline-block;padding:6px 13px;border-radius:999px;background:rgba(0,229,255,.10);color:#67e8f9;font-size:11px;border:1px solid rgba(103,232,249,.35);font-family:Orbitron,sans-serif;letter-spacing:1px}.small{color:#a8b6d3}\n.game-hud{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:12px 0 18px}.hud-card{background:rgba(8,20,40,.88);border:1px solid rgba(99,102,241,.30);border-radius:15px;padding:11px 14px}.hud-label{color:#8ea2c7;font-size:10px;letter-spacing:1.5px;font-family:Orbitron,sans-serif}.hud-value{color:#f8fbff;font:800 19px Orbitron,sans-serif;margin-top:3px}.message-card{padding:26px;border-radius:20px;background:linear-gradient(145deg,rgba(248,250,252,.98),rgba(226,232,240,.98));color:#172033;border:1px solid rgba(255,255,255,.8);border-left:6px solid var(--accent);box-shadow:0 15px 40px rgba(0,0,0,.30)}.game-panel,.investigate{padding:18px;border-radius:18px;background:rgba(8,18,38,.78);border:1px solid rgba(56,189,248,.18);margin-top:15px}.investigate{background:linear-gradient(145deg,rgba(10,28,50,.94),rgba(10,18,38,.90));border-radius:20px}.mission-title{font-family:Orbitron,sans-serif;letter-spacing:1px;color:#67e8f9}div.stButton>button{border-radius:14px!important;min-height:48px!important;font-family:Rajdhani,sans-serif!important;font-size:17px!important;font-weight:700!important}div.stButton>button:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,229,255,.15)}.mission-map{display:flex;gap:6px;margin:12px 0 18px}.map-node{flex:1;text-align:center;padding:9px 3px;border-radius:12px;font:700 9px Orbitron,sans-serif;border:1px solid rgba(103,232,249,.18);background:rgba(8,18,38,.72);color:#7890b8}.map-node.active{color:#67e8f9;border-color:rgba(103,232,249,.6);box-shadow:0 0 18px rgba(34,211,238,.15)}.map-node.done{color:#86efac;border-color:rgba(34,197,94,.35)}.shield-wrap{height:12px;border-radius:999px;background:rgba(255,255,255,.08);overflow:hidden;border:1px solid rgba(103,232,249,.18)}.shield-fill{height:100%;background:linear-gradient(90deg,#ef4444,#f59e0b,#22d3ee)}.clue-card{padding:15px;border-radius:16px;background:rgba(8,20,40,.88);border:1px solid rgba(103,232,249,.20);min-height:130px}.clue-card.revealed{border-color:rgba(34,197,94,.42);box-shadow:0 0 18px rgba(34,197,94,.08)}.clue-label{font:700 10px Orbitron,sans-serif;letter-spacing:1px;color:#8ea2c7}.clue-value{margin-top:7px;color:#f1f5f9;font-size:14px;line-height:1.35}.boss-card{padding:22px;border-radius:20px;background:linear-gradient(145deg,rgba(49,17,68,.95),rgba(18,18,50,.96));border:1px solid rgba(244,114,182,.35);box-shadow:0 0 30px rgba(168,85,247,.12)}.achievement{padding:13px 15px;border-radius:14px;background:rgba(8,20,40,.82);border:1px solid rgba(167,139,250,.28);margin:7px 0}.coin{color:#fde68a;font-family:Orbitron,sans-serif}.level-banner{margin:10px 0 16px;padding:14px 18px;border-radius:16px;background:linear-gradient(90deg,rgba(34,211,238,.10),rgba(129,140,248,.12));border:1px solid rgba(103,232,249,.25);display:flex;justify-content:space-between;align-items:center}.level-main{font:800 18px Orbitron,sans-serif;color:#e0f2fe}.level-sub{font-size:12px;color:#93a8ca}.profile-card{padding:18px;border-radius:20px;background:linear-gradient(145deg,rgba(9,25,46,.96),rgba(14,18,48,.92));border:1px solid rgba(129,140,248,.28)}.certificate{padding:35px;border-radius:24px;background:linear-gradient(145deg,#071326,#11183a);border:2px solid rgba(103,232,249,.45);text-align:center;box-shadow:0 0 40px rgba(34,211,238,.12)}@media(max-width:800px){.game-hud{grid-template-columns:repeat(2,1fr)}}\n</style>', unsafe_allow_html=True)

SCENARIOS = [
{"sender":"Campus IT Support","email":"it-support@campus.edu","subject":"Urgent: Account Verification Required",
"message":"Your campus account requires immediate verification. Confirm your student information within 30 minutes to avoid temporary suspension.",
"answer":"Phishing","difficulty":"Easy",
"explanation":"The message creates urgency and asks for account verification unexpectedly.",
"clues":["Urgent deadline","Threat of suspension","Unexpected verification request"]},

{"sender":"University Library","email":"library@campus.edu","subject":"Library Book Reminder",
"message":"One library book is due for return. Please check your account through the official university library portal.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"It does not request passwords, OTPs, payment, or sensitive information and points students to the official portal.",
"clues":["No password requested","No payment requested","Official portal mentioned"]},

{"sender":"Student Scholarship Office","email":"scholarship.verify@gmail.com","subject":"URGENT: Scholarship Cancellation",
"message":"You have been selected for a scholarship. Verify your student account within 30 minutes or the scholarship will be permanently cancelled.",
"answer":"Phishing","difficulty":"Easy",
"explanation":"A generic email address, pressure, and an unexpected verification request are warning signs.",
"clues":["Generic email address","Very short deadline","Threat of losing scholarship"]},

{"sender":"Examination Cell","email":"exams@campus.edu","subject":"Examination Timetable Update",
"message":"The updated examination timetable is available. Please check the examination section of the official university website.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"The message gives information without requesting sensitive data and directs students to the official website.",
"clues":["No sensitive information requested","Official website","No pressure"]},

{"sender":"Student Account Team","email":"student.account.help@outlook.com","subject":"Account Suspension Notice",
"message":"Your student account will be permanently disabled today. Reply with your username, password and verification code immediately.",
"answer":"Phishing","difficulty":"Easy",
"explanation":"Legitimate support should not ask students to send passwords or verification codes by email.",
"clues":["Requests password","Requests verification code","Non-institutional address"]},

{"sender":"Campus Events Team","email":"events@campus.edu","subject":"Cultural Fest Registration",
"message":"Registration for the annual cultural fest is open. Visit the student activities section of the official campus website to register.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"The message uses an institutional address and directs students to the normal campus website.",
"clues":["Institutional address","Normal event information","Official website"]},

{"sender":"Campus Wi-Fi Admin","email":"wifi-secure@campus-support.com","subject":"Wi-Fi Password Expiry",
"message":"Your Wi-Fi password expires in 10 minutes. Click the attached link and enter your current password to keep access.",
"answer":"Phishing","difficulty":"Medium",
"explanation":"The unusual domain, extreme urgency, and request for a current password are strong warning signs.",
"clues":["Unusual domain","10-minute deadline","Requests current password"]},

{"sender":"Accounts Office","email":"accounts@campus.edu","subject":"Fee Receipt Available",
"message":"Your semester fee receipt is now available. Sign in through the usual student portal to view or download it.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"Students are directed to the normal portal rather than being asked to send credentials.",
"clues":["Usual portal","No credential request","Routine campus transaction"]},

{"sender":"Campus Placement Cell","email":"placements@campus.edu","subject":"Placement Workshop",
"message":"A placement preparation workshop will be held Friday at 3 PM in Seminar Hall 2. Details are available on the placement portal.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"This is routine informational communication and contains no suspicious request for credentials or money.",
"clues":["Routine information","Official address","No sensitive request"]},

{"sender":"Campus Help Desk","email":"helpdesk.campus.edu@gmail.com","subject":"Your Account Has Been Hacked",
"message":"We detected suspicious activity. Send your OTP immediately so our security team can protect your account.",
"answer":"Phishing","difficulty":"Medium",
"explanation":"An OTP is a security credential and should never be sent to someone by email.",
"clues":["Requests OTP","Fear-based wording","Generic email address"]},

{"sender":"Hostel Office","email":"hostel@campus.edu","subject":"Hostel Maintenance Notice",
"message":"Water supply maintenance is scheduled from 2 PM to 4 PM tomorrow. Please plan accordingly.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"It is a normal operational notice and does not ask for personal information.",
"clues":["Routine notice","No link","No sensitive request"]},

{"sender":"Exam Results Team","email":"results-check@outlook.com","subject":"Your Result Is Ready — Pay ₹499",
"message":"Your examination result is ready. Pay ₹499 through the link below within 15 minutes to unlock your marks.",
"answer":"Phishing","difficulty":"Medium",
"explanation":"Unexpected payment, urgency, and a non-institutional address are suspicious.",
"clues":["Unexpected payment","Urgent deadline","Non-institutional address"]},

{"sender":"Campus Health Centre","email":"health@campus.edu","subject":"Health Centre Timings",
"message":"The campus health centre will operate from 8 AM to 6 PM this week. Please check the official campus page for updates.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"The message provides routine information and directs students to an official source.",
"clues":["Routine information","Official source","No credential request"]},

{"sender":"IT Security Desk","email":"security@campus.edu","subject":"Security Awareness Exercise",
"message":"As part of this week's security awareness exercise, please review the phishing examples on the official IT security page. Do not submit passwords or OTPs.",
"answer":"Genuine","difficulty":"Medium",
"explanation":"It explicitly directs students to an official security page and tells them not to share credentials.",
"clues":["Official security page","No credential request","Awareness-focused"]},

{"sender":"Campus ID Services","email":"campus-id@campus.edu","subject":"ID Card Collection",
"message":"Your replacement ID card is ready. Please collect it from the ID office with your existing student identification.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"This is a normal in-person administrative instruction with no suspicious link or credential request.",
"clues":["Normal administrative process","In-person collection","No password request"]},

{"sender":"Admin Portal","email":"admin.portal.verify@protonmail.com","subject":"Final Warning: Portal Locked",
"message":"Your portal will be locked permanently unless you confirm your username, password and security code using the attached form.",
"answer":"Phishing","difficulty":"Hard",
"explanation":"It requests multiple authentication secrets and uses a threatening final-warning style.",
"clues":["Requests password","Requests security code","Threatening language","Suspicious email provider"]},

{"sender":"Student Council","email":"studentcouncil@campus.edu","subject":"Club Fair Schedule",
"message":"The student club fair will take place in the main auditorium on Saturday. The schedule is posted on the student council page.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"It is routine event information with an official student organization address and no sensitive request.",
"clues":["Routine event","Official organization address","No sensitive data"]},

{"sender":"Campus Finance","email":"finance-alert@campus.edu","subject":"Refund Processing Notice",
"message":"A fee refund has been approved. Please log in to your normal student portal to view the refund status. We will never ask for your password by email.",
"answer":"Genuine","difficulty":"Medium",
"explanation":"It uses the normal portal and explicitly states that passwords will not be requested by email.",
"clues":["Normal portal","No password request","Clear security practice"]},

{"sender":"Free Laptop Grant","email":"grant2026@fastmail.com","subject":"Congratulations! You Won a Laptop",
"message":"You have been randomly selected for a free laptop. Pay a ₹199 processing fee today and send your student ID photo to claim it.",
"answer":"Phishing","difficulty":"Hard",
"explanation":"An unexpected prize combined with a payment request and a demand for an ID image is suspicious.",
"clues":["Unexpected prize","Processing fee","Requests ID image","External email address"]},

{"sender":"Campus Transport Office","email":"transport@campus.edu","subject":"Bus Route Change",
"message":"Route 4 will use Gate 2 instead of Gate 1 tomorrow morning because of maintenance. No action is required.",
"answer":"Genuine","difficulty":"Easy",
"explanation":"This is a routine operational announcement and asks students to do nothing sensitive.",
"clues":["Routine notice","Official address","No action involving credentials"]}
]

APP_VERSION = "v6.0 — Investigation Edition"
SAVE_FILE = Path(__file__).parent / "campus_cyber_shield_saves.json"
THEMES = {
    "Neon Grid":{"cost":0,"accent":"#22d3ee","accent2":"#818cf8"},
    "Stealth Blue":{"cost":20,"accent":"#60a5fa","accent2":"#38bdf8"},
    "Purple Pulse":{"cost":35,"accent":"#c084fc","accent2":"#a78bfa"},
    "Emerald Ops":{"cost":50,"accent":"#34d399","accent2":"#22c55e"},
}
BOSS={"sender":"Campus Digital Services","email":"security-alert@campus-digital-support.com","subject":"Final Security Verification","message":"Your student account has been selected for a mandatory security upgrade. Review the sender details, inspect every evidence item, and decide whether this message is safe.","answer":"Phishing","explanation":"The sender domain is not the official campus domain, the message creates pressure around a security upgrade, and a genuine security process should be verified through the normal official portal."}

def read_saves():
    try:
        return json.loads(SAVE_FILE.read_text(encoding="utf-8")) if SAVE_FILE.exists() else {}
    except Exception: return {}

def write_saves(data):
    try: SAVE_FILE.write_text(json.dumps(data,indent=2),encoding="utf-8")
    except Exception: pass

def save_profile():
    codename=st.session_state.get("codename","").strip()
    if not codename: return
    saves=read_saves()
    saves[codename.lower()]={"codename":codename,"xp":st.session_state.xp,"credits":st.session_state.credits,"best_streak":st.session_state.best_streak,"achievements":st.session_state.achievements,"theme":st.session_state.theme,"unlocked_themes":st.session_state.unlocked_themes,"last_saved":datetime.now().isoformat(timespec="seconds")}
    write_saves(saves)

def load_profile(codename):
    return read_saves().get(codename.strip().lower())

defaults={"screen":"home","codename":"","started":False,"index":0,"score":0,"answered":False,"correct":False,"order":list(range(len(SCENARIOS))),"show_hint":False,"answers":[],"streak":0,"best_streak":0,"xp":0,"sound_event":None,"lives":3,"boss_done":False,"boss_answered":False,"boss_correct":False,"boss_clues_seen":[],"achievements":[],"theme":"Neon Grid","unlocked_themes":["Neon Grid"],"investigated":[],"loaded_notice":""}
for k,v in defaults.items():
    if k not in st.session_state: st.session_state[k]=v

def play_sound(filename):
    path=Path(__file__).parent/filename
    if path.exists():
        data=base64.b64encode(path.read_bytes()).decode("utf-8")
        st.markdown(f'<audio autoplay><source src="data:audio/wav;base64,{data}" type="audio/wav"></audio>',unsafe_allow_html=True)

def play_background_music():
    path=Path(__file__).parent/"cyber_ambience.wav"
    if path.exists():
        data=base64.b64encode(path.read_bytes()).decode("utf-8")
        st.markdown(f'<audio autoplay loop><source src="data:audio/wav;base64,{data}" type="audio/wav"></audio>',unsafe_allow_html=True)

def award_achievements():
    a=st.session_state.achievements
    if st.session_state.best_streak>=5 and "5 IN A ROW" not in a:a.append("5 IN A ROW")
    if st.session_state.score>=10 and "THREAT HUNTER" not in a:a.append("THREAT HUNTER")
    if st.session_state.score>=15 and "CYBER DEFENDER" not in a:a.append("CYBER DEFENDER")
    if st.session_state.score>=20 and "SHIELD COMMANDER" not in a:a.append("SHIELD COMMANDER")
    if st.session_state.lives==3 and st.session_state.score>=5 and "PERFECT LEVEL" not in a:a.append("PERFECT LEVEL")
    save_profile()

def render_map(level):
    names=["ROOKIE","HUNTER","DEFENDER","COMMANDER"]
    st.markdown('<div class="mission-map">'+''.join(f'<div class="map-node {"done" if i<level else "active" if i==level else ""}">{i}. {n}</div>' for i,n in enumerate(names,1))+'</div>',unsafe_allow_html=True)

def current_level():
    q=st.session_state.index+1
    if q<=5:return 1,"ROOKIE SCANNER","🟢"
    if q<=10:return 2,"THREAT HUNTER","🔵"
    if q<=15:return 3,"CYBER DEFENDER","🟣"
    return 4,"SHIELD COMMANDER","🔴"

def scenario_link(s):
    return "https://campus-login-verify.example/secure-check" if s["answer"]=="Phishing" else "https://portal.campus.edu/student-services"

def urgency_text(s):
    text=(s["subject"]+" "+s["message"]).lower()
    words=["urgent","immediately","30 minutes","10 minutes","today","15 minutes","final warning","permanently","expires"]
    return "HIGH — pressure or deadline detected" if any(w in text for w in words) else "LOW — routine/no pressure detected"

def content_signal(s):
    text=s["message"].lower()
    if any(w in text for w in ["password","otp","verification code","security code"]):return "Credential/security-secret request detected"
    if "₹" in s["message"] or "pay" in text or "fee" in text:return "Payment or financial request detected"
    if "official" in text or "normal student portal" in text:return "Directs the user toward a normal official channel"
    return "Routine informational content"

def evidence_items(s):
    return [("👤","SENDER",s["sender"]),("🌐","DOMAIN",s["email"]),("🔗","LINK",scenario_link(s)),("⏱️","URGENCY",urgency_text(s)),("🧠","CONTENT",content_signal(s))]

theme=THEMES.get(st.session_state.theme,THEMES["Neon Grid"])
st.markdown(f'<style>:root{{--accent:{theme["accent"]};--accent2:{theme["accent2"]};}}</style>',unsafe_allow_html=True)

st.markdown(f'''<div class="hero"><span class="badge">CYBER AWARENESS • CAMPUS EDITION • {APP_VERSION}</span><h1>🛡️ Campus Cyber Shield</h1><p style="font-size:19px">Interactive Phishing Investigation Simulator</p><p class="small">Inspect the evidence. Think before you click. Protect the campus.</p></div>''',unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 👤 PLAYER PROFILE")
    if st.session_state.codename:
        st.markdown(f'<div class="profile-card"><span class="badge">CODENAME</span><h2>{html.escape(st.session_state.codename)}</h2><p>⭐ XP <b>{st.session_state.xp}</b><br>🪙 Credits <b>{st.session_state.credits}</b><br>🔥 Best Streak <b>{st.session_state.best_streak}</b><br>🎨 Theme <b>{html.escape(st.session_state.theme)}</b></p></div>',unsafe_allow_html=True)
        if st.button("🏠 Home / Profile",use_container_width=True):st.session_state.screen="home";st.rerun()
        if st.button("💾 Save Progress",use_container_width=True):save_profile();st.success("Progress saved.")
        if st.button("🧹 Reset Profile",use_container_width=True):
            st.session_state.codename="";st.session_state.xp=0;st.session_state.credits=0;st.session_state.best_streak=0;st.session_state.achievements=[];st.session_state.theme="Neon Grid";st.session_state.unlocked_themes=["Neon Grid"];st.session_state.screen="home";st.session_state.started=False;st.rerun()
    else: st.info("Create a codename on the home screen to activate your player profile.")
    st.divider();st.caption("Progress is stored in the app's local save file and can be restored on the same persistent deployment.")

if st.session_state.screen=="home":
    st.subheader("🎯 Your Mission")
    st.write("Campus Cyber Shield v6 turns phishing awareness into an interactive investigation. You must inspect evidence before making each decision.")
    c1,c2,c3,c4=st.columns(4);c1.metric("Cases","20");c2.metric("Evidence / case","5");c3.metric("Final Boss","1");c4.metric("Themes","4")
    st.markdown('<div class="game-panel"><div class="mission-title">🔍 INVESTIGATION MODE</div><p>Inspect <b>Sender</b>, <b>Domain</b>, <b>Link</b>, <b>Urgency</b> and <b>Message Content</b>.</p><p class="small">The Genuine / Phishing decision unlocks only after all evidence is reviewed.</p></div>',unsafe_allow_html=True)
    st.subheader("👤 Create / Load Player")
    codename=st.text_input("Codename",value=st.session_state.codename,placeholder="Example: CYBERFOX")
    col1,col2=st.columns(2)
    with col1:
        if st.button("🚀 Start New Mission",use_container_width=True,type="primary"):
            st.session_state.codename=codename.strip() or "CADET"
            st.session_state.xp=0;st.session_state.credits=0;st.session_state.best_streak=0;st.session_state.achievements=[];st.session_state.theme="Neon Grid";st.session_state.unlocked_themes=["Neon Grid"]
            st.session_state.started=True;st.session_state.screen="game";st.session_state.index=0;st.session_state.score=0;st.session_state.answers=[];st.session_state.streak=0;st.session_state.lives=3;st.session_state.answered=False;st.session_state.investigated=[];st.session_state.order=list(range(len(SCENARIOS)));random.shuffle(st.session_state.order);save_profile();st.rerun()
    with col2:
        if st.button("📂 Load Saved Profile",use_container_width=True):
            p=load_profile(codename.strip())
            if p:
                for key in ["codename","xp","credits","best_streak","achievements","theme","unlocked_themes"]:st.session_state[key]=p.get(key,st.session_state[key])
                st.session_state.loaded_notice="Profile loaded successfully."
            else:st.session_state.loaded_notice="No saved profile found for that codename."
            st.rerun()
    if st.session_state.loaded_notice:st.info(st.session_state.loaded_notice)
    st.subheader("🗺️ Campaign");render_map(1)
    st.write("**Level 1:** Rookie Scanner → **Level 2:** Threat Hunter → **Level 3:** Cyber Defender → **Level 4:** Shield Commander")
    st.write("Complete 20 investigations, then face the Elite Threat Boss.")
    if st.session_state.codename:
        st.divider();st.subheader("🎨 Theme Locker")
        for name,info in THEMES.items():
            unlocked=name in st.session_state.unlocked_themes
            c1,c2,c3=st.columns([2,1,1]);c1.write(f"**{name}**");c2.write("FREE" if info["cost"]==0 else f"🪙 {info['cost']}")
            with c3:
                if unlocked:
                    if st.button("ACTIVE" if name==st.session_state.theme else "USE",key="home_theme_"+name,use_container_width=True):st.session_state.theme=name;save_profile();st.rerun()
                elif st.button("UNLOCK",key="home_buy_"+name,use_container_width=True):
                    if st.session_state.credits>=info["cost"]:st.session_state.credits-=info["cost"];st.session_state.unlocked_themes.append(name);st.session_state.theme=name;save_profile();st.rerun()
                    else:st.warning("Not enough Cyber Credits yet.")

elif st.session_state.screen=="game" and st.session_state.index<len(SCENARIOS):
    play_background_music()
    qnum=st.session_state.index+1;scenario=SCENARIOS[st.session_state.order[st.session_state.index]];level_num,level_name,level_color=current_level()
    st.markdown(f'<div class="level-banner"><div><div class="level-main">{level_color} LEVEL {level_num} — {level_name}</div><div class="level-sub">Case {((qnum-1)%5)+1} of 5 • Investigation required</div></div><div class="level-chip">XP {st.session_state.xp}</div></div>',unsafe_allow_html=True)
    render_map(level_num);st.progress(qnum/20,text=f"MISSION PROGRESS // {qnum}/20")
    st.markdown(f'<div class="game-hud"><div class="hud-card"><div class="hud-label">SCORE</div><div class="hud-value">{st.session_state.score:02d}</div></div><div class="hud-card"><div class="hud-label">XP</div><div class="hud-value">{st.session_state.xp:03d}</div></div><div class="hud-card"><div class="hud-label">STREAK</div><div class="hud-value">🔥 {st.session_state.streak}</div></div><div class="hud-card"><div class="hud-label">CREDITS</div><div class="hud-value">🪙 {st.session_state.credits}</div></div><div class="hud-card"><div class="hud-label">CASE</div><div class="hud-value">{qnum:02d}/20</div></div></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="game-panel"><div class="mission-title">🛡️ SHIELD ENERGY</div><div class="shield-wrap"><div class="shield-fill" style="width:{st.session_state.lives/3*100}%"></div></div><p class="small">Lives remaining: {("❤️ "*st.session_state.lives) if st.session_state.lives else "💔"} • <span class="coin">🪙 {st.session_state.credits} Cyber Credits</span></p></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="mission-title">📡 INCIDENT {qnum:02d} // INVESTIGATE</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="message-card"><b>From:</b> {scenario["sender"]}<br><b>Email:</b> {scenario["email"]}<br><b>Subject:</b> {scenario["subject"]}<br><br>{scenario["message"]}</div>',unsafe_allow_html=True)
    st.markdown('<div class="investigate"><div class="mission-title">🔍 EVIDENCE BOARD</div><p class="small">Inspect all five evidence items before making your classification.</p></div>',unsafe_allow_html=True)
    evidence=evidence_items(scenario)
    cols=st.columns(5)
    for i,(icon,label,value) in enumerate(evidence):
        with cols[i]:
            revealed=i in st.session_state.investigated
            st.markdown(f'<div class="clue-card {("revealed" if revealed else "")}"><div class="clue-label">{icon} {label}</div><div class="clue-value">{html.escape(str(value)) if revealed else "LOCKED — INSPECT"}</div></div>',unsafe_allow_html=True)
            if not revealed and st.button(f"Inspect {i+1}",key=f"inspect_{qnum}_{i}",use_container_width=True):st.session_state.investigated.append(i);st.rerun()
    if len(st.session_state.investigated)<5:
        st.warning(f"🔒 Classification locked — inspect {5-len(st.session_state.investigated)} more evidence item(s).")
    elif not st.session_state.answered:
        st.success("✅ Evidence complete. You may now classify the incident.")
        a,b=st.columns(2)
        for col,choice,emoji in [(a,"Genuine","🟢"),(b,"Phishing","🔴")]:
            with col:
                if st.button(f"{emoji} {choice.upper()}",key=f"case_{qnum}_{choice}",use_container_width=True):
                    st.session_state.answered=True;st.session_state.correct=scenario["answer"]==choice
                    if st.session_state.correct:
                        st.session_state.score+=1;st.session_state.streak+=1;st.session_state.best_streak=max(st.session_state.best_streak,st.session_state.streak);st.session_state.xp+=10+(st.session_state.streak-1)*2;st.session_state.credits+=5+st.session_state.streak;st.session_state.sound_event="correct"
                    else:st.session_state.streak=0;st.session_state.lives=max(0,st.session_state.lives-1);st.session_state.sound_event="wrong"
                    st.session_state.answers.append({"question":qnum,"your_answer":choice,"correct_answer":scenario["answer"],"correct":st.session_state.correct})
                    award_achievements();st.rerun()
    else:
        if st.session_state.correct:
            st.success(f"⚡ CORRECT! +{10+max(st.session_state.streak-1,0)*2} XP • 🔥 {st.session_state.streak} streak")
            if st.session_state.sound_event=="correct":play_sound("correct.wav")
        else:
            st.error(f"💥 MISS! The correct classification was **{scenario['answer']}**.")
            if st.session_state.sound_event=="wrong":play_sound("wrong.wav")
        st.session_state.sound_event=None;st.subheader("🧠 Analyst Debrief");st.write(scenario["explanation"]);st.subheader("🚩 Why the Evidence Matters")
        for clue in scenario["clues"]:st.markdown(f'<div class="clue-card">🚩 {clue}</div>',unsafe_allow_html=True)
        if not st.session_state.show_hint:
            if st.button("💡 Reveal Analyst Hint",use_container_width=True):st.session_state.show_hint=True;st.rerun()
        else:st.info("Hint: Compare the sender/domain with the expected channel, look for pressure, and watch for requests for credentials, money, or unusual information.")
        if qnum<20:
            if st.button("➡️ Next Investigation",use_container_width=True,type="primary"):
                st.session_state.index+=1;st.session_state.answered=False;st.session_state.correct=False;st.session_state.show_hint=False;st.session_state.investigated=[];save_profile();st.rerun()
        else:
            if st.button("👑 Enter Elite Threat Boss",use_container_width=True,type="primary"):
                st.session_state.screen="boss";save_profile();st.rerun()

elif st.session_state.screen=="boss" and not st.session_state.boss_done:
    play_background_music()
    st.markdown('<div class="boss-card"><div class="badge">FINAL ENCOUNTER</div><h2>👑 ELITE THREAT // BOSS</h2><p>Five evidence checks. One final decision. No shortcuts.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="mission-title">🔐 BOSS MESSAGE</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="message-card"><b>From:</b> {BOSS["sender"]}<br><b>Email:</b> {BOSS["email"]}<br><b>Subject:</b> {BOSS["subject"]}<br><br>{BOSS["message"]}</div>',unsafe_allow_html=True)
    boss_evidence=[("👤","SENDER","Compare the displayed organization name with the actual sender."),("🌐","DOMAIN","The email uses campus-digital-support.com rather than the official campus domain."),("🔗","CHANNEL","A security upgrade should be verified through the normal official portal."),("⏱️","URGENCY","Security language can create pressure to act before checking."),("🧠","REQUEST","Treat unexpected account-verification or credential requests as high-risk.")]
    cols=st.columns(5)
    for i,(icon,title,body) in enumerate(boss_evidence):
        with cols[i]:
            seen=i in st.session_state.boss_clues_seen
            st.markdown(f'<div class="clue-card {("revealed" if seen else "")}"><div class="clue-label">{icon} {title}</div><div class="clue-value">{body if seen else "LOCKED"}</div></div>',unsafe_allow_html=True)
            if not seen and st.button(f"Inspect {i+1}",key=f"boss_{i}",use_container_width=True):st.session_state.boss_clues_seen.append(i);st.rerun()
    if len(st.session_state.boss_clues_seen)<5:st.warning(f"🔒 Final decision locked — inspect {5-len(st.session_state.boss_clues_seen)} more evidence item(s).")
    elif not st.session_state.boss_answered:
        st.success("All boss evidence inspected. Make your final decision.")
        a,b=st.columns(2)
        with a:
            if st.button("🟢 GENUINE",key="boss_genuine",use_container_width=True):
                st.session_state.boss_answered=True;st.session_state.boss_correct=False;st.session_state.lives=max(0,st.session_state.lives-1);st.session_state.streak=0;play_sound("wrong.wav");save_profile();st.rerun()
        with b:
            if st.button("🔴 PHISHING",key="boss_phishing",use_container_width=True):
                st.session_state.boss_answered=True;st.session_state.boss_correct=True;st.session_state.score+=1;st.session_state.xp+=50;st.session_state.credits+=25
                if "CYBER GUARDIAN" not in st.session_state.achievements:st.session_state.achievements.append("CYBER GUARDIAN")
                play_sound("correct.wav");save_profile();st.rerun()
    else:
        if st.session_state.boss_correct:st.success("🏆 BOSS DEFEATED! +50 XP • +25 Cyber Credits • CYBER GUARDIAN unlocked")
        else:st.error("💥 BOSS HIT! The Elite Threat was phishing.")
        st.write(BOSS["explanation"])
        if st.button("🏁 Generate Cyber Defender Certificate",type="primary",use_container_width=True):st.session_state.boss_done=True;st.session_state.screen="results";save_profile();st.rerun()

elif st.session_state.screen=="results":
    score=st.session_state.score;total=21;accuracy=score/total*100
    level="ROOKIE SCANNER" if score<6 else ("THREAT HUNTER" if score<11 else ("CYBER DEFENDER" if score<17 else "SHIELD COMMANDER"))
    st.subheader("🏁 Mission Complete!")
    a,b,c,d=st.columns(4);a.metric("Final Score",f"{score}/{total}");b.metric("Accuracy",f"{accuracy:.0f}%");c.metric("XP",st.session_state.xp);d.metric("Credits",st.session_state.credits)
    st.markdown(f'<div class="certificate"><div class="badge">CAMPUS CYBER SHIELD</div><h1 style="font-family:Orbitron">🛡️ CYBER DEFENDER</h1><p style="font-size:18px">Completion Certificate</p><hr><h2>{html.escape(st.session_state.codename)}</h2><p>has completed the Campus Cyber Shield Investigation Campaign</p><p><b>Final Level:</b> {level} • <b>Score:</b> {score}/{total} • <b>Accuracy:</b> {accuracy:.0f}%</p><p><b>XP:</b> {st.session_state.xp} • <b>Best Streak:</b> 🔥 {st.session_state.best_streak}</p><p><b>Achievements:</b> {len(st.session_state.achievements)}</p><p class="small">Campus Cyber Shield v6 • Investigation Edition</p></div>',unsafe_allow_html=True)
    cert_html=f'''<!doctype html><html><head><meta charset="utf-8"><title>Campus Cyber Shield Certificate</title><style>body{{background:#030712;color:#eef2ff;font-family:Arial;padding:50px}}.card{{max-width:800px;margin:auto;padding:50px;border:3px solid #22d3ee;border-radius:28px;text-align:center;background:#071326}}h1{{font-size:42px;color:#67e8f9}}h2{{font-size:34px}}.stats{{font-size:18px;line-height:2}}</style></head><body><div class="card"><p>CAMPUS CYBER SHIELD</p><h1>CYBER DEFENDER</h1><p>Completion Certificate</p><h2>{html.escape(st.session_state.codename)}</h2><p>has completed the Campus Cyber Shield Investigation Campaign.</p><div class="stats"><b>Final Level:</b> {html.escape(level)}<br><b>Score:</b> {score}/{total}<br><b>Accuracy:</b> {accuracy:.0f}%<br><b>XP:</b> {st.session_state.xp}<br><b>Best Streak:</b> {st.session_state.best_streak}<br><b>Achievements:</b> {len(st.session_state.achievements)}</div></div></body></html>'''
    st.download_button("📥 Download Certificate (HTML)",data=cert_html,file_name=f"Cyber_Defender_{st.session_state.codename}.html",mime="text/html",use_container_width=True)
    st.subheader("🏆 Achievements")
    for ach in st.session_state.achievements:st.markdown(f'<div class="achievement">🏆 <b>{html.escape(ach)}</b></div>',unsafe_allow_html=True)
    if not st.session_state.achievements:st.info("No achievements unlocked.")
    st.divider();st.subheader("📊 Investigation Review")
    for item in st.session_state.answers:st.write(f'**Case {item["question"]}:** {"✅ Correct" if item["correct"] else "❌ Correct answer: "+item["correct_answer"]}')
    if st.button("🔄 Start Another Mission",use_container_width=True,type="primary"):
        st.session_state.screen="game";st.session_state.started=True;st.session_state.index=0;st.session_state.score=0;st.session_state.answers=[];st.session_state.streak=0;st.session_state.lives=3;st.session_state.answered=False;st.session_state.correct=False;st.session_state.investigated=[];st.session_state.boss_done=False;st.session_state.boss_answered=False;st.session_state.boss_clues_seen=[];st.session_state.order=list(range(len(SCENARIOS)));random.shuffle(st.session_state.order);save_profile();st.rerun()
    if st.button("🏠 Return to Home",use_container_width=True):st.session_state.screen="home";st.rerun()
