import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Control Panel",
    page_icon="🗂️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit default padding
st.markdown("""
<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { display: none !important; }
    footer { display: none !important; }
    #MainMenu { display: none !important; }
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css"/>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Sora:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --red:#E24B4A;--red-bg:#FCEBEB;--red-dark:#791F1F;--red-border:#F09595;
  --yellow:#BA7517;--yellow-bg:#FAEEDA;--yellow-dark:#633806;--yellow-border:#FAC775;
  --green:#3B6D11;--green-bg:#EAF3DE;--green-border:#C0DD97;
  --blue-bg:#E6F1FB;--blue-dark:#0C447C;--blue-border:#85B7EB;
  --bg:#f5f4f0;--surface:#fff;--border:#e0dfd8;--text:#1a1a1a;--text2:#6b6b6b;
  --font:'Sora',sans-serif;--mono:'JetBrains Mono',monospace;
}
body{font-family:var(--font);background:var(--bg);color:var(--text);min-height:100vh}
#app{max-width:720px;margin:0 auto;background:var(--surface);min-height:100vh;border-left:.5px solid var(--border);border-right:.5px solid var(--border)}
#hdr{padding:14px 16px 10px;border-bottom:.5px solid var(--border);display:flex;align-items:center;gap:10px}
#hdr .logo{font-family:var(--mono);font-size:16px;font-weight:600;letter-spacing:-.01em}
#hdr .sub{font-size:11px;color:var(--text2);margin-top:1px}
.hdr-right{margin-left:auto;display:flex;align-items:center;gap:8px}
#badge-total{font-size:11px;font-weight:700;background:var(--red);color:#fff;border-radius:20px;padding:2px 9px}
#badge-total.hidden{display:none}
.btn-muteall{font-family:var(--font);font-size:11px;font-weight:600;padding:5px 11px;border-radius:7px;border:1.5px solid var(--border);background:var(--surface);cursor:pointer;color:var(--text2);display:flex;align-items:center;gap:5px}
.btn-muteall:hover{background:#f0efe8}
.btn-muteall.muted{background:#f0efe8;color:#aaa;border-color:var(--border)}
#tabs{display:flex;gap:5px;padding:12px 16px 0;overflow-x:auto}
.tab-btn{font-family:var(--font);font-size:12px;font-weight:600;padding:6px 13px;border-radius:8px;border:1.5px solid var(--border);background:var(--surface);cursor:pointer;color:var(--text2);white-space:nowrap;transition:.15s}
.tab-btn.active{background:var(--text);color:var(--surface);border-color:transparent}
.tab-btn:hover:not(.active){background:#f0efe8}
.tab-badge{display:inline-block;font-size:10px;font-weight:700;background:var(--red);color:#fff;border-radius:10px;padding:1px 6px;margin-left:4px;vertical-align:1px}
#panels{padding:14px 16px}
.panel{display:none}.panel.active{display:block}
.sec-hdr{display:flex;align-items:center;gap:7px;margin:16px 0 8px}
.sec-hdr:first-child{margin-top:0}
.sec-title{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--text2)}
.sec-count{font-size:10px;font-weight:700;background:var(--red);color:#fff;border-radius:10px;padding:1px 6px}
.sec-count.yellow{background:var(--yellow)}
.al{border-radius:10px;padding:11px 14px;margin-bottom:7px;display:flex;align-items:flex-start;gap:10px;border:1.5px solid transparent}
.al.red{background:var(--red-bg);border-color:var(--red-border);animation:pulse-r 1.8s infinite}
.al.yellow{background:var(--yellow-bg);border-color:var(--yellow-border);animation:pulse-y 2.5s infinite}
.al.expired{background:#791F1F;border-color:#501313;color:#fff;animation:blink .8s infinite}
@keyframes pulse-r{0%,100%{box-shadow:0 0 0 0 rgba(226,75,74,.45)}50%{box-shadow:0 0 0 6px rgba(226,75,74,0)}}
@keyframes pulse-y{0%,100%{box-shadow:0 0 0 0 rgba(186,117,23,.35)}50%{box-shadow:0 0 0 6px rgba(186,117,23,0)}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.al-icon{font-size:17px;flex-shrink:0;margin-top:1px}
.al-body{flex:1;min-width:0}
.al-title{font-size:13px;font-weight:600;line-height:1.3}
.al-sub{font-size:11px;opacity:.7;margin-top:2px}
.al-actions{display:flex;align-items:center;gap:5px;margin-top:7px;flex-wrap:wrap}
.btn-done{font-family:var(--font);font-size:11px;font-weight:700;padding:4px 10px;border-radius:6px;border:1.5px solid currentColor;background:transparent;cursor:pointer;color:inherit}
.btn-done:hover{background:rgba(0,0,0,.07)}
.al.expired .btn-done,.al.expired .btn-ext{color:#fff;border-color:rgba(255,255,255,.5)}
.btn-ext{font-family:var(--font);font-size:11px;font-weight:600;padding:4px 10px;border-radius:6px;border:1.5px solid currentColor;background:transparent;cursor:pointer;color:inherit;opacity:.8}
.btn-mute-item{font-family:var(--font);font-size:10px;font-weight:600;padding:3px 8px;border-radius:5px;border:1.5px solid currentColor;background:transparent;cursor:pointer;color:inherit;opacity:.5;margin-left:auto}
.btn-mute-item:hover{opacity:.9}
.al.muted{animation:none !important;opacity:.6}
.al.muted .btn-mute-item{opacity:1}
.card{background:var(--surface);border-radius:11px;border:.5px solid var(--border);padding:12px 14px;margin-bottom:7px}
.card-row{display:flex;align-items:center;gap:8px}
.card-title{font-size:13px;font-weight:600;flex:1}
.card-sub{font-size:11px;color:var(--text2);margin-top:2px}
.tag{font-size:10px;font-weight:700;padding:3px 8px;border-radius:5px;letter-spacing:.03em}
.tag.alta{background:var(--red-bg);color:var(--red-dark)}
.tag.media{background:var(--yellow-bg);color:var(--yellow-dark)}
.tag.baixa{background:var(--green-bg);color:var(--green)}
.tag.ok{background:var(--green-bg);color:var(--green)}
.tag.vencido{background:var(--red-bg);color:var(--red-dark)}
.tag.andamento{background:var(--blue-bg);color:var(--blue-dark)}
.btn-sm{font-family:var(--font);font-size:11px;font-weight:600;padding:4px 9px;border-radius:6px;border:1.5px solid var(--border);background:transparent;cursor:pointer;color:var(--text)}
.btn-sm:hover{background:#f0efe8}
.btn-sm.del{border-color:var(--red-border);color:var(--red-dark)}
.btn-add{display:flex;align-items:center;gap:6px;width:100%;padding:10px 13px;background:#f0efe8;border:1.5px dashed var(--border);border-radius:10px;cursor:pointer;font-family:var(--font);font-size:12px;font-weight:600;color:var(--text2);margin-top:4px}
.btn-add:hover{background:#e8e7e0;border-style:solid}
.empty{text-align:center;padding:24px 0;color:var(--text2);font-size:12px}
.empty i{font-size:28px;display:block;margin-bottom:6px;opacity:.35}
#modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);align-items:flex-start;justify-content:center;z-index:100;overflow-y:auto;padding:20px}
#modal-bg.open{display:flex}
.modal{background:var(--surface);border-radius:13px;padding:20px;width:100%;max-width:420px;margin:auto;border:.5px solid var(--border)}
.modal h3{font-size:14px;font-weight:700;margin-bottom:14px}
.field{margin-bottom:11px}
.field label{font-size:11px;font-weight:700;color:var(--text2);display:block;margin-bottom:4px;letter-spacing:.04em;text-transform:uppercase}
.field input,.field select{width:100%;padding:8px 10px;border-radius:7px;font-family:var(--font);font-size:13px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);outline:none}
.field input:focus,.field select:focus{border-color:var(--text)}
.field-row{display:flex;gap:8px}
.field-row .field{flex:1}
.modal-btns{display:flex;gap:7px;justify-content:flex-end;margin-top:14px}
.btn-prim{font-family:var(--font);font-size:13px;font-weight:600;padding:7px 16px;border-radius:7px;background:var(--text);color:var(--surface);border:none;cursor:pointer}
.btn-canc{font-family:var(--font);font-size:13px;font-weight:500;padding:7px 13px;border-radius:7px;background:transparent;color:var(--text2);border:1.5px solid var(--border);cursor:pointer}
.divider{height:.5px;background:var(--border);margin:10px 0}
.client-row{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:.5px solid var(--border)}
.client-row:last-child{border:none}
.info-box{background:#f0efe8;border-radius:8px;padding:10px 12px;font-size:11px;color:var(--text2);margin-bottom:12px;display:flex;align-items:flex-start;gap:7px}
#pror-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);align-items:center;justify-content:center;z-index:200;padding:20px}
#pror-bg.open{display:flex}
.pror-box{background:var(--surface);border-radius:13px;padding:20px;width:100%;max-width:300px;border:.5px solid var(--border)}
.pror-box h3{font-size:14px;font-weight:700;margin-bottom:14px}
.pror-tabs{display:flex;gap:6px;margin-bottom:12px}
.pror-tab{font-family:var(--font);font-size:12px;font-weight:600;padding:5px 14px;border-radius:7px;border:1.5px solid var(--border);background:var(--surface);cursor:pointer;color:var(--text2)}
.pror-tab.active{background:var(--text);color:var(--surface);border-color:transparent}
.pror-input-row{display:flex;align-items:center;gap:10px}
.pror-input-row input{width:80px;padding:8px 10px;border-radius:7px;font-family:var(--font);font-size:14px;font-weight:600;border:1.5px solid var(--border);background:var(--surface);color:var(--text);text-align:center;outline:none}
.pror-input-row span{font-size:13px;color:var(--text2)}
</style>
</head>
<body>
<div id="app">

<div id="hdr">
  <div>
    <div class="logo"><i class="ti ti-layout-dashboard" style="font-size:15px;vertical-align:-1px;margin-right:6px"></i>Control Panel</div>
    <div class="sub">Gerenciador interno de trabalho</div>
  </div>
  <div class="hdr-right">
    <span id="badge-total" class="hidden">0</span>
    <button class="btn-muteall" id="btn-muteall" onclick="toggleMuteAll()">
      <i class="ti ti-volume" id="mute-icon"></i><span id="mute-label">Som ativo</span>
    </button>
  </div>
</div>

<div id="tabs">
  <button class="tab-btn active" onclick="switchTab('home')"><i class="ti ti-home" style="font-size:12px;vertical-align:-1px;margin-right:4px"></i>Início</button>
  <button class="tab-btn" onclick="switchTab('faturas')"><i class="ti ti-receipt" style="font-size:12px;vertical-align:-1px;margin-right:4px"></i>Faturas<span class="tab-badge hidden" id="tb-faturas">0</span></button>
  <button class="tab-btn" onclick="switchTab('chamados')"><i class="ti ti-ticket" style="font-size:12px;vertical-align:-1px;margin-right:4px"></i>Chamados<span class="tab-badge hidden" id="tb-chamados">0</span></button>
  <button class="tab-btn" onclick="switchTab('tarefas')"><i class="ti ti-check" style="font-size:12px;vertical-align:-1px;margin-right:4px"></i>Tarefas<span class="tab-badge hidden" id="tb-tarefas">0</span></button>
</div>

<div id="panels">
  <div id="panel-home" class="panel active"><div id="home-content"></div></div>
  <div id="panel-faturas" class="panel">
    <div id="fat-info" class="info-box">
      <i class="ti ti-info-circle" style="font-size:14px;flex-shrink:0;margin-top:1px"></i>
      <span id="fat-info-text"></span>
    </div>
    <div id="fat-list"></div>
    <button class="btn-add" onclick="openModal('cliente')"><i class="ti ti-user-plus"></i>Cadastrar cliente para fatura</button>
  </div>
  <div id="panel-chamados" class="panel">
    <div id="cha-list"></div>
    <button class="btn-add" onclick="openModal('chamado')"><i class="ti ti-plus"></i>Novo chamado</button>
  </div>
  <div id="panel-tarefas" class="panel">
    <div id="tar-list"></div>
    <button class="btn-add" onclick="openModal('tarefa')"><i class="ti ti-plus"></i>Nova tarefa</button>
  </div>
</div>

<div id="modal-bg" onclick="closeMBg(event)">
  <div class="modal">
    <h3 id="modal-title"></h3>
    <div id="modal-body"></div>
    <div class="modal-btns">
      <button class="btn-canc" onclick="closeModal()">Cancelar</button>
      <button class="btn-prim" onclick="saveModal()">Salvar</button>
    </div>
  </div>
</div>

<div id="pror-bg" onclick="closeProrBg(event)">
  <div class="pror-box">
    <h3><i class="ti ti-clock-edit" style="font-size:14px;vertical-align:-1px;margin-right:5px"></i>Prorrogar prazo</h3>
    <div class="pror-tabs">
      <button class="pror-tab active" id="pror-tab-h" onclick="setProrMode('h')">Horas</button>
      <button class="pror-tab" id="pror-tab-d" onclick="setProrMode('d')">Dias úteis</button>
    </div>
    <div class="pror-input-row">
      <input type="number" id="pror-val" min="1" max="999" value="4"/>
      <span id="pror-unit-label">horas</span>
    </div>
    <div class="modal-btns">
      <button class="btn-canc" onclick="closePror()">Cancelar</button>
      <button class="btn-prim" onclick="confirmPror()">Confirmar</button>
    </div>
  </div>
</div>

</div><!-- #app -->

<script>
const ALERT_INTERVAL=600000, SND_N='cp_snd_n', SND_E='cp_snd_e';
const S={
  clients:JSON.parse(localStorage.getItem('cp_cli')||'[]'),
  chamados:JSON.parse(localStorage.getItem('cp_cha')||'[]'),
  tarefas:JSON.parse(localStorage.getItem('cp_tar')||'[]'),
  fatDone:JSON.parse(localStorage.getItem('cp_fd')||'{}'),
  mutedItems:JSON.parse(localStorage.getItem('cp_muted')||'{}'),
  muteAll:JSON.parse(localStorage.getItem('cp_muteall')||'false'),
  save(){
    localStorage.setItem('cp_cli',JSON.stringify(this.clients));
    localStorage.setItem('cp_cha',JSON.stringify(this.chamados));
    localStorage.setItem('cp_tar',JSON.stringify(this.tarefas));
    localStorage.setItem('cp_fd',JSON.stringify(this.fatDone));
    localStorage.setItem('cp_muted',JSON.stringify(this.mutedItems));
    localStorage.setItem('cp_muteall',JSON.stringify(this.muteAll));
  }
};
let modalType=null,prorIdx=null,prorType=null,prorMode='h';

function getFaturaAlertDate(t){const n=new Date(),d=new Date(n.getFullYear(),n.getMonth(),t);while(d.getDay()===0||d.getDay()===6)d.setDate(d.getDate()+1);return d;}
function isFaturaAlertToday(){const t=new Date();t.setHours(0,0,0,0);for(const b of[1,16]){const a=getFaturaAlertDate(b);a.setHours(0,0,0,0);if(a.getTime()===t.getTime())return true;}return false;}
function nextFaturaLabel(){const n=new Date();n.setHours(0,0,0,0);const c=[];for(const b of[1,16]){let d=getFaturaAlertDate(b);d.setHours(0,0,0,0);if(d>=n)c.push(d);const nm=new Date(n.getFullYear(),n.getMonth()+1,b);while(nm.getDay()===0||nm.getDay()===6)nm.setDate(nm.getDate()+1);nm.setHours(0,0,0,0);c.push(nm);}c.sort((a,b)=>a-b);const nx=c.find(d=>d>=n)||c[0];const diff=Math.round((nx-n)/86400000);const fmt=nx.toLocaleDateString('pt-BR',{day:'2-digit',month:'long'});if(diff===0)return`Hoje (${fmt}) — dia de faturamento!`;if(diff===1)return`Amanhã (${fmt})`;return`${fmt} — em ${diff} dia(s)`;}
function todayKey(){return new Date().toDateString();}
function isExpired(dl){return dl&&Date.now()>new Date(dl).getTime();}
function msLeft(dl){return dl?new Date(dl).getTime()-Date.now():null;}
function formatMsLeft(ms){if(ms===null)return'—';const abs=Math.abs(ms),neg=ms<0,h=Math.floor(abs/3600000),d=Math.floor(h/24),m=Math.floor((abs%3600000)/60000);const l=d>0?`${d}d ${h%24}h`:h>0?`${h}h ${m}min`:`${m}min`;return neg?`Vencido há ${l}`:`${l} restantes`;}
function formatDeadline(iso){const d=new Date(iso);return d.toLocaleDateString('pt-BR')+' às '+d.toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'});}
function isMuted(t,id){return S.muteAll||!!S.mutedItems[`${t}_${id}`];}
function toggleMuteItem(t,id){const k=`${t}_${id}`;S.mutedItems[k]=!S.mutedItems[k];S.save();renderAll();}
function toggleMuteAll(){S.muteAll=!S.muteAll;S.save();renderAll();}

// ---- SONS COM WEB AUDIO API ----
function beep(freq,dur,vol=0.15){
  try{
    const ac=new(window.AudioContext||window.webkitAudioContext)();
    const o=ac.createOscillator(),g=ac.createGain();
    o.connect(g);g.connect(ac.destination);o.frequency.value=freq;
    g.gain.setValueAtTime(0,ac.currentTime);
    g.gain.linearRampToValueAtTime(vol,ac.currentTime+0.03);
    g.gain.linearRampToValueAtTime(0,ac.currentTime+dur);
    o.start(ac.currentTime);o.stop(ac.currentTime+dur+0.05);
  }catch(e){}
}
// Alerta normal: 3 bipes ascendentes (pendência ativa)
function playAlert(){[0,.2,.4].forEach(t=>setTimeout(()=>beep(880,.18),t*1000));}
// Alerta expirado: sirene pulsante (mais urgente)
function playExpired(){[700,900,700,900,700].forEach((f,i)=>setTimeout(()=>beep(f,.22,.22),i*180));}
// Confirmação: acorde ascendente (feito)
function playDone(){[523,659,784].forEach((f,i)=>setTimeout(()=>beep(f,.18,.1),i*120));}

function getLastSound(k){return parseInt(localStorage.getItem(k)||'0');}
function setLastSound(k){localStorage.setItem(k,Date.now().toString());}

function collectAlerts(){
  const items=[],td=todayKey();
  if(isFaturaAlertToday()){S.clients.forEach((c,i)=>{if(!S.fatDone[`${c}_${td}`])items.push({type:'fatura',id:`fat_${i}`,cls:'red',icon:'ti-receipt',title:`Enviar fatura para ${c}`,sub:'Dia de faturamento (ajustado para dia útil)',expired:false,actions:[{label:'✓ Feito',fn:`markFatDone('${c}','${td}')`}]});});}
  S.chamados.forEach((ch,i)=>{if(ch.done)return;const exp=isExpired(ch.deadline),ms=msLeft(ch.deadline);if(exp||(ms!==null&&ms<7200000))items.push({type:'chamado',id:`cha_${i}`,cls:exp?'red':'yellow',icon:'ti-ticket',title:`Chamado #${ch.ticket} · Pedido ${ch.pedido}`,sub:formatMsLeft(ms),expired:exp,actions:[{label:'⏱ Prorrogar',fn:`openPror('chamado',${i})`},{label:'✓ Feito',fn:`doneChamado(${i})`}]});});
  S.tarefas.forEach((t,i)=>{if(t.done)return;const exp=isExpired(t.deadline),ms=msLeft(t.deadline),urgente=exp||(ms!==null&&ms<7200000),proxima=!exp&&ms!==null&&ms<86400000*2;
    if(t.prioridade==='alta'){if(exp)items.push({type:'tarefa',id:`tar_${i}`,cls:'expired',icon:'ti-flag',title:`⚠ PRAZO ENCERRADO — ${t.titulo}`,sub:`Vencido há ${formatMsLeft(ms).replace('Vencido há ','')} · Alta prioridade`,expired:true,actions:[{label:'⏱ Prorrogar',fn:`openPror('tarefa',${i})`},{label:'✓ Feito',fn:`doneTarefa(${i})`}]});else if(urgente||proxima)items.push({type:'tarefa',id:`tar_${i}`,cls:'red',icon:'ti-flag',title:`Tarefa urgente: ${t.titulo}`,sub:`Alta prioridade · ${formatMsLeft(ms)}`,expired:false,actions:[{label:'⏱ Prorrogar',fn:`openPror('tarefa',${i})`},{label:'✓ Feito',fn:`doneTarefa(${i})`}]});}
    else if(t.prioridade==='media'){if(exp)items.push({type:'tarefa',id:`tar_${i}`,cls:'red',icon:'ti-flag-2',title:`⚠ PRAZO ENCERRADO — ${t.titulo}`,sub:`Vencido há ${formatMsLeft(ms).replace('Vencido há ','')} · Média prioridade`,expired:true,actions:[{label:'⏱ Prorrogar',fn:`openPror('tarefa',${i})`},{label:'✓ Feito',fn:`doneTarefa(${i})`}]});else if(urgente||proxima)items.push({type:'tarefa',id:`tar_${i}`,cls:'yellow',icon:'ti-flag-2',title:`Tarefa: ${t.titulo}`,sub:`Média prioridade · ${formatMsLeft(ms)}`,expired:false,actions:[{label:'⏱ Prorrogar',fn:`openPror('tarefa',${i})`},{label:'✓ Feito',fn:`doneTarefa(${i})`}]});}
    else if(t.prioridade==='baixa'){if(exp)items.push({type:'tarefa',id:`tar_bl_${i}`,cls:'red',icon:'ti-flag-3',title:`⚠ PRAZO ENCERRADO — ${t.titulo}`,sub:`Vencido há ${formatMsLeft(ms).replace('Vencido há ','')} · Baixa prioridade`,expired:true,actions:[{label:'⏱ Prorrogar',fn:`openPror('tarefa',${i})`},{label:'✓ Feito',fn:`doneTarefa(${i})`}]});else if(urgente)items.push({type:'tarefa',id:`tar_bl_${i}`,cls:'yellow',icon:'ti-flag-3',title:`Tarefa: ${t.titulo}`,sub:`Baixa prioridade · ${formatMsLeft(ms)}`,expired:false,actions:[{label:'⏱ Prorrogar',fn:`openPror('tarefa',${i})`},{label:'✓ Feito',fn:`doneTarefa(${i})`}]});}
  });
  return items;
}

function renderHome(){
  const items=collectAlerts(),el=document.getElementById('home-content');
  const urgent=items.filter(i=>i.cls==='red'||i.cls==='expired'),attn=items.filter(i=>i.cls==='yellow');
  let html='';
  function renderSection(list,label,countCls){if(!list.length)return'';let h=`<div class="sec-hdr"><span class="sec-title">${label}</span><span class="sec-count ${countCls}">${list.length}</span></div>`;list.forEach(item=>{const mt=isMuted(item.type,item.id);const btns=item.actions.map(a=>`<button class="btn-done" onclick="${a.fn}">${a.label}</button>`).join('');const mb=`<button class="btn-mute-item" onclick="toggleMuteItem('${item.type}','${item.id.replace(/'/g,"\\'")}')"><i class="ti ${mt?'ti-volume-off':'ti-volume-3'}"></i> ${mt?'Mutado':'Mutar'}</button>`;h+=`<div class="al ${item.cls}${mt?' muted':''}"><i class="ti ${item.icon} al-icon"></i><div class="al-body"><div class="al-title">${item.title}</div><div class="al-sub">${item.sub}</div><div class="al-actions">${btns}${mb}</div></div></div>`;});return h;}
  if(!items.length){html='<div class="empty" style="padding:32px 0"><i class="ti ti-circle-check" style="color:#3B6D11;opacity:.7"></i>Tudo em dia! Nenhum alerta pendente.</div>';}
  else{html+=renderSection(urgent,'Atenção imediata','');html+=renderSection(attn,'Acompanhamento','yellow');}
  const allCha=S.chamados.filter(c=>!c.done),allT=S.tarefas.filter(t=>!t.done);
  if(allCha.length||allT.length){html+=`<div class="divider" style="margin:14px 0 10px"></div><div class="sec-hdr"><span class="sec-title">Todas as pendências</span></div>`;
    allCha.forEach((ch,i)=>{const exp=isExpired(ch.deadline),ms=msLeft(ch.deadline);html+=`<div class="card"><div class="card-row"><i class="ti ti-ticket" style="font-size:15px;color:#6b6b6b"></i><div style="flex:1"><div class="card-title">#${ch.ticket} · Pedido ${ch.pedido}</div><div class="card-sub">${ch.deadline?formatDeadline(ch.deadline):'Sem prazo'} · ${formatMsLeft(ms)}</div></div><span class="tag ${exp?'vencido':'andamento'}">${exp?'VENCIDO':'EM DIA'}</span><button class="btn-sm" onclick="openPror('chamado',${i})" style="margin-left:6px"><i class="ti ti-clock-edit"></i></button><button class="btn-sm" onclick="doneChamado(${i})" style="margin-left:4px">✓</button></div></div>`;});
    allT.forEach((t,i)=>{const exp=isExpired(t.deadline),ms=msLeft(t.deadline);html+=`<div class="card"><div class="card-row"><i class="ti ti-flag" style="font-size:15px;color:#6b6b6b"></i><div style="flex:1"><div class="card-title">${t.titulo}</div><div class="card-sub">${t.deadline?formatDeadline(t.deadline):'Sem prazo'} · ${formatMsLeft(ms)}</div></div><span class="tag ${exp?'vencido':t.prioridade}">${exp?'VENCIDO':t.prioridade.toUpperCase()}</span><button class="btn-sm" onclick="openPror('tarefa',${i})" style="margin-left:6px"><i class="ti ti-clock-edit"></i></button><button class="btn-sm" onclick="doneTarefa(${i})" style="margin-left:4px">✓</button></div></div>`;});
  }
  el.innerHTML=html;updateBadges(items);
}

function updateBadges(items){const n=items.length,el=document.getElementById('badge-total');if(n>0){el.textContent=n+(n===1?' alerta':' alertas');el.classList.remove('hidden')}else el.classList.add('hidden');function b(id,n){const x=document.getElementById(id);if(n>0){x.textContent=n;x.classList.remove('hidden')}else x.classList.add('hidden')}b('tb-faturas',items.filter(i=>i.type==='fatura').length);b('tb-chamados',items.filter(i=>i.type==='chamado').length);b('tb-tarefas',items.filter(i=>i.type==='tarefa').length);}
function updateMuteBtn(){document.getElementById('mute-icon').className=S.muteAll?'ti ti-volume-off':'ti ti-volume';document.getElementById('mute-label').textContent=S.muteAll?'Som mutado':'Som ativo';document.getElementById('btn-muteall').classList.toggle('muted',S.muteAll);}

function renderFaturas(){
  document.getElementById('fat-info-text').textContent=`Próximo lembrete de fatura: ${nextFaturaLabel()}. Os alertas dos dias 01 e 16 são movidos para o próximo dia útil se caírem em fim de semana.`;
  const el=document.getElementById('fat-list');if(!S.clients.length){el.innerHTML='<div class="empty"><i class="ti ti-users"></i>Nenhum cliente cadastrado</div>';return;}
  const td=todayKey(),isAD=isFaturaAlertToday();
  el.innerHTML=S.clients.map((c,i)=>{const done=S.fatDone[`${c}_${td}`];return`<div class="card"><div class="card-row"><i class="ti ti-building" style="font-size:15px;color:#6b6b6b"></i><div style="flex:1"><div class="card-title" style="${done?'text-decoration:line-through;opacity:.45':''}">${c}</div><div class="card-sub">${isAD&&!done?'Hoje é dia de faturamento':'Próximo: '+nextFaturaLabel()}</div></div><span class="tag ${isAD&&!done?'alta':'ok'}">${isAD&&!done?'HOJE':'OK'}</span><button class="btn-sm del" onclick="removeCli(${i})" style="margin-left:6px"><i class="ti ti-trash"></i></button></div></div>`;}).join('');
}
function renderChamados(){
  const el=document.getElementById('cha-list'),ativos=S.chamados.filter(c=>!c.done);
  if(!ativos.length){el.innerHTML='<div class="empty"><i class="ti ti-ticket"></i>Nenhum chamado aberto</div>';return;}
  el.innerHTML=ativos.map(ch=>{const i=S.chamados.indexOf(ch),exp=isExpired(ch.deadline),ms=msLeft(ch.deadline);return`<div class="card"><div class="card-row"><i class="ti ti-ticket" style="font-size:15px;color:#6b6b6b"></i><div style="flex:1"><div class="card-title">#${ch.ticket} · Pedido ${ch.pedido}</div><div class="card-sub">${ch.deadline?formatDeadline(ch.deadline):'Sem prazo'} · ${formatMsLeft(ms)}</div></div><span class="tag ${exp?'vencido':'andamento'}">${exp?'VENCIDO':'EM DIA'}</span><button class="btn-sm" onclick="openPror('chamado',${i})" style="margin-left:6px"><i class="ti ti-clock-edit"></i></button><button class="btn-sm" onclick="doneChamado(${i})" style="margin-left:4px">✓ Feito</button></div></div>`;}).join('');
}
function renderTarefas(){
  const el=document.getElementById('tar-list'),ativas=S.tarefas.filter(t=>!t.done);
  if(!ativas.length){el.innerHTML='<div class="empty"><i class="ti ti-check"></i>Nenhuma tarefa pendente</div>';return;}
  const ord=['alta','media','baixa'];
  el.innerHTML=[...ativas].sort((a,b)=>ord.indexOf(a.prioridade)-ord.indexOf(b.prioridade)).map(t=>{const i=S.tarefas.indexOf(t),exp=isExpired(t.deadline),ms=msLeft(t.deadline);return`<div class="card"><div class="card-row"><i class="ti ti-flag" style="font-size:15px;color:#6b6b6b"></i><div style="flex:1"><div class="card-title">${t.titulo}</div><div class="card-sub">${t.deadline?formatDeadline(t.deadline):'Sem prazo'} · ${formatMsLeft(ms)}</div></div><span class="tag ${exp?'vencido':t.prioridade}">${exp?'VENCIDO':t.prioridade.toUpperCase()}</span><button class="btn-sm" onclick="openPror('tarefa',${i})" style="margin-left:6px"><i class="ti ti-clock-edit"></i></button><button class="btn-sm" onclick="doneTarefa(${i})" style="margin-left:4px">✓ Feito</button></div></div>`;}).join('');
}
function renderAll(){renderHome();renderFaturas();renderChamados();renderTarefas();updateMuteBtn();}

function markFatDone(c,td){playDone();S.fatDone[`${c}_${td}`]=true;S.save();renderAll();}
function doneChamado(i){playDone();S.chamados[i].done=true;S.save();renderAll();}
function doneTarefa(i){playDone();S.tarefas[i].done=true;S.save();renderAll();}
function removeCli(i){S.clients.splice(i,1);S.save();renderAll();}

function openPror(type,i){prorType=type;prorIdx=i;prorMode='h';document.getElementById('pror-val').value=4;document.getElementById('pror-tab-h').classList.add('active');document.getElementById('pror-tab-d').classList.remove('active');document.getElementById('pror-unit-label').textContent='horas';document.getElementById('pror-bg').classList.add('open');}
function closePror(){document.getElementById('pror-bg').classList.remove('open');prorIdx=null;prorType=null;}
function closeProrBg(e){if(e.target.id==='pror-bg')closePror();}
function setProrMode(m){prorMode=m;document.getElementById('pror-tab-h').classList.toggle('active',m==='h');document.getElementById('pror-tab-d').classList.toggle('active',m==='d');document.getElementById('pror-unit-label').textContent=m==='h'?'horas':'dias úteis';document.getElementById('pror-val').value=m==='h'?4:2;}
function confirmPror(){const val=parseInt(document.getElementById('pror-val').value)||1;const obj=prorType==='chamado'?S.chamados[prorIdx]:S.tarefas[prorIdx];const base=obj.deadline&&new Date(obj.deadline)>new Date()?new Date(obj.deadline):new Date();if(prorMode==='h'){base.setTime(base.getTime()+val*3600000);}else{let added=0,cur=new Date(base);while(added<val){cur.setDate(cur.getDate()+1);if(cur.getDay()!==0&&cur.getDay()!==6)added++;}base.setTime(cur.getTime());}obj.deadline=base.toISOString();S.save();closePror();renderAll();}

function switchTab(t){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));document.querySelector(`.tab-btn[onclick*="'${t}'"]`).classList.add('active');document.getElementById(`panel-${t}`).classList.add('active');}

function openModal(type){
  modalType=type;
  document.getElementById('modal-title').textContent={chamado:'Novo chamado',tarefa:'Nova tarefa',cliente:'Cadastrar cliente'}[type];
  const now=new Date(),todayStr=now.toISOString().split('T')[0],timeStr=now.toTimeString().slice(0,5);
  const hint=`<div style="font-size:11px;color:#6b6b6b;margin-top:-6px;margin-bottom:8px"><i class="ti ti-info-circle" style="font-size:12px;vertical-align:-1px;margin-right:3px"></i>O alerta disparará ao atingir essa data e horário (Brasília)</div>`;
  const bodies={
    chamado:`<div class="field-row"><div class="field"><label>Número do ticket</label><input id="m-ticket" placeholder="TKT-001"/></div><div class="field"><label>Número do pedido</label><input id="m-pedido" placeholder="PED-001"/></div></div><div class="field"><label>Data limite</label><input id="m-data" type="date" value="${todayStr}"/></div><div class="field"><label>Horário limite</label><input id="m-hora" type="time" value="${timeStr}"/></div>${hint}`,
    tarefa:`<div class="field"><label>Título</label><input id="m-titulo" placeholder="Ex: Revisar relatório"/></div><div class="field"><label>Prioridade</label><select id="m-pri"><option value="alta">Alta — urgente</option><option value="media" selected>Média</option><option value="baixa">Baixa</option></select></div><div class="field"><label>Data limite</label><input id="m-data" type="date" value="${todayStr}"/></div><div class="field"><label>Horário limite</label><input id="m-hora" type="time" value="${timeStr}"/></div>${hint}`,
    cliente:`<div class="field"><label>Nome do cliente</label><input id="m-cli" placeholder="Ex: Empresa ABC"/></div>`
  };
  document.getElementById('modal-body').innerHTML=bodies[type];
  if(type==='tarefa'){const d=new Date();d.setDate(d.getDate()+3);document.getElementById('m-data').value=d.toISOString().split('T')[0];}
  document.getElementById('modal-bg').classList.add('open');
}
function closeModal(){document.getElementById('modal-bg').classList.remove('open');}
function closeMBg(e){if(e.target.id==='modal-bg')closeModal();}
function saveModal(){
  if(modalType==='chamado'){const t=document.getElementById('m-ticket').value.trim(),p=document.getElementById('m-pedido').value.trim(),data=document.getElementById('m-data').value,hora=document.getElementById('m-hora').value;if(!t||!p||!data||!hora)return alert('Preencha todos os campos.');S.chamados.push({ticket:t,pedido:p,deadline:new Date(`${data}T${hora}:00`).toISOString(),createdAt:new Date().toISOString(),done:false});}
  else if(modalType==='tarefa'){const t=document.getElementById('m-titulo').value.trim(),pr=document.getElementById('m-pri').value,data=document.getElementById('m-data').value,hora=document.getElementById('m-hora').value;if(!t||!data||!hora)return alert('Preencha todos os campos.');S.tarefas.push({titulo:t,prioridade:pr,deadline:new Date(`${data}T${hora}:00`).toISOString(),createdAt:new Date().toISOString(),done:false});}
  else if(modalType==='cliente'){const c=document.getElementById('m-cli').value.trim();if(!c)return alert('Digite o nome do cliente.');S.clients.push(c);}
  S.save();closeModal();renderAll();
}

function checkAndAlert(){
  if(S.muteAll)return;
  const items=collectAlerts();if(!items.length)return;
  const nm=items.filter(i=>!isMuted(i.type,i.id));if(!nm.length)return;
  const now=Date.now(),hasExp=nm.some(i=>i.expired);
  if(hasExp){if(now-getLastSound(SND_E)>=ALERT_INTERVAL){setLastSound(SND_E);playExpired();}}
  else{if(now-getLastSound(SND_N)>=ALERT_INTERVAL){setLastSound(SND_N);playAlert();}}
}

renderAll();
// Toca na abertura se houver alertas e já passaram 10min desde o último som
setTimeout(()=>{
  const items=collectAlerts();if(!items.length||S.muteAll)return;
  const nm=items.filter(i=>!isMuted(i.type,i.id));if(!nm.length)return;
  const hasExp=nm.some(i=>i.expired),key=hasExp?SND_E:SND_N;
  if(Date.now()-getLastSound(key)>=ALERT_INTERVAL){setLastSound(key);if(hasExp)playExpired();else playAlert();}
},800);
setInterval(checkAndAlert,10000);  // verifica a cada 10s, dispara a cada 10min
setInterval(renderHome,30000);     // atualiza contadores regressivos a cada 30s
</script>
</body>
</html>"""

components.html(HTML, height=800, scrolling=True)
