from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html><html lang="id"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Untuk Uni Nabila ❤️</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');
body{margin:0; min-height:100vh; background: radial-gradient(circle at top, #ffdde1, #ee9ca7, #ff6a88); font-family:'Poppins', sans-serif; display:flex; justify-content:center; align-items:center; padding:20px;}
.card{background:rgba(255,255,255,0.92); backdrop-filter: blur(15px); max-width:440px; width:100%; border-radius:35px; padding:35px 28px; text-align:center; box-shadow:0 25px 80px rgba(255,50,100,0.35); animation:pop 1.2s ease;}
@keyframes pop{0%{transform:scale(0.7) translateY(60px); opacity:0}100%{transform:scale(1) translateY(0); opacity:1}}
h1{font-family:'Dancing Script', cursive; font-size:2.8em; color:#ff2e6a; margin:0;}
.nama{font-family:'Dancing Script', cursive; font-size:2.3em; background:linear-gradient(90deg,#ff2e6a,#ff8fab); -webkit-background-clip:text; -webkit-text-fill-color:transparent; display:block; margin:5px 0 10px;}
.foto-utama{width:190px; height:190px; object-fit:cover; border-radius:50%; border:6px solid white; box-shadow:0 15px 35px rgba(255,46,106,0.4); margin:15px auto; display:block;}
.gallery{display:flex; gap:10px; justify-content:center; margin:18px 0;} .gallery img{width:88px; height:88px; object-fit:cover; border-radius:18px; border:3px solid white; box-shadow:0 8px 20px rgba(0,0,0,0.15); cursor:pointer; transition:0.3s;} .gallery img:hover{transform:scale(1.15);}
p{color:#5a3a42; line-height:1.7;} .btn{margin-top:18px; background:linear-gradient(90deg,#ff5a8a,#ff2e6a); color:white; border:none; padding:15px 32px; border-radius:50px; font-size:1.1em; cursor:pointer; width:100%; box-shadow:0 12px 25px rgba(255,46,106,0.4);} #surat{display:none; margin-top:22px; text-align:left; background:#fff5f7; padding:20px; border-radius:20px; border:1.5px dashed #ffb3c6;}
.player{position:fixed; bottom:18px; left:50%; transform:translateX(-50%); background:rgba(255,255,255,0.95); padding:10px 18px; border-radius:50px; display:flex; gap:12px; align-items:center; box-shadow:0 10px 30px rgba(0,0,0,0.2); z-index:20;}
.player button{border:none; background:linear-gradient(90deg,#ff5a8a,#ff2e6a); color:white; width:42px; height:42px; border-radius:50%; cursor:pointer; font-size:18px;}
.hearts{position:fixed; inset:0; pointer-events:none;} .heart{position:absolute; animation:fall linear forwards;} @keyframes fall{0%{transform:translateY(-10vh)}100%{transform:translateY(110vh)}}
</style></head><body>
<div class="hearts" id="hearts"></div>
<div class="card">
<h1>Haii ❤️</h1><span class="nama">Uni Nabila</span>
<img id="mainPhoto" class="foto-utama" src="/foto/nabila1.jpg">
<div class="gallery">
<img src="/foto/nabila1.jpg" onclick="ganti(this.src)">
<img src="/foto/nabila2.jpg" onclick="ganti(this.src)">
<img src="/foto/nabila3.jpg" onclick="ganti(this.src)">
</div>
<p>Website ini aku buat khusus buat kamu, Uni. Ada lagu cinta buat kamu ✨</p>
<button class="btn" onclick="bukaSurat()">Buka Surat Cinta + Lagu 💌🎵</button>
<div id="surat"><p><b>Untuk Uni Nabila Tersayang,</b><br><br>
Makasih udah jadi cewe paling cantik, baik, dan sabar di hidup aku.<br><br>
Setiap liat senyum Sayang, dunia rasanya berhenti sebentar.<br><br>
Aku janji bakal jaga Sayang, bikin Sayang bahagia selamanya.<br><br>
<span style="color:#ff2e6a; font-weight:600;">Aku sayang Uni Nabila, banyak banget ❤️</span><br><br>
- Randi Farhan Al-Khair -
</p></div>
</div>
<div class="player"><button id="musicBtn" onclick="toggleMusic()">🎵</button><span style="font-size:0.85em; color:#ff2e6a; font-weight:600;">Lagu buat Uni</span></div>
<audio id="bgMusic" loop><source src="/foto/lagu.mp3"><source src="https://cdn.pixabay.com/download/audio/2022/06/07/audio_b9bd4170e8.mp3?filename=romantic-piano-110858.mp3"></audio>
<script>
let playing=false;
function bukaSurat(){document.getElementById('surat').style.display='block'; let a=document.getElementById('bgMusic'); a.volume=0.6; a.play().then(()=>{playing=true; document.getElementById('musicBtn').innerHTML='⏸️';}).catch(()=>{}); for(let i=0;i<45;i++) setTimeout(buatHati,i*80);}
function ganti(src){document.getElementById('mainPhoto').src=src; for(let i=0;i<8;i++) buatHati();}
function buatHati(){const h=document.createElement('div'); h.className='heart'; h.innerHTML=['❤️','💖','💗'][Math.floor(Math.random()*3)]; h.style.left=Math.random()*100+'vw'; h.style.top='-5vh'; h.style.animationDuration=(Math.random()*3+3)+'s'; h.style.fontSize=(Math.random()*20+15)+'px'; document.getElementById('hearts').appendChild(h); setTimeout(()=>h.remove(),6000);}
function toggleMusic(){const a=document.getElementById('bgMusic'); const b=document.getElementById('musicBtn'); if(!playing){a.play(); b.innerHTML='⏸️'; playing=true;}else{a.pause(); b.innerHTML='🎵'; playing=false;}}
setInterval(buatHati,350);
</script></body></html>
    """

@app.route('/foto/<path:nama>')
def foto(nama):
    return send_from_directory('.', nama)

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)