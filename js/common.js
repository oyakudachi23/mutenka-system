async function loadTools(){
  const base = location.pathname.includes('/tools/') ? '../data/tools.csv' : 'data/tools.csv';
  const text = await fetch(base).then(r=>r.text());
  const [header,...lines]=text.trim().split('\n');
  const keys=header.split(',');
  return lines.map(line=>{
    const cols=[];let cur='';let inQ=false;
    for(let i=0;i<line.length;i++){
      const c=line[i];
      if(c==='"') inQ=!inQ;
      else if(c===','&&!inQ){cols.push(cur);cur='';}
      else cur+=c;
    }
    cols.push(cur);
    const obj={};keys.forEach((k,i)=>obj[k]=cols[i]||'');
    return obj;
  });
}
function toolRow(t){
return `<tr><td>${t.name}</td><td>${t.category}</td><td>${t.features}</td><td>${t.price}</td><td>${t.free_plan}</td><td><a class="button" href="${t.official_url}" target="_blank" rel="noopener">公式サイトを見る</a></td></tr>`
}
