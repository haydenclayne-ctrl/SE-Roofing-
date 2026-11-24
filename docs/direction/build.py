# Builds (1) single-file bundled mocks and (2) an unbundled static/ folder that links tokens.css + tokens.web.css + site.css.
import re,base64,os,shutil,urllib.request
D=os.path.dirname(os.path.abspath(__file__)); S=D+'/src'; A=D+'/assets'; LOGO=D+'/brand' if os.path.isdir(D+'/brand') else os.path.abspath(D+'/../brand')
rd=lambda p:open(p).read()
tokens=rd(S+'/tokens.css'); web=rd(S+'/tokens.web.css'); css=rd(S+'/site.css'); fonts=rd(A+'/fonts-embed.css')
hdr=rd(S+'/_header.html'); ftr=rd(S+'/_footer.html')
pages=[('home','mock-home.html','index.html'),('case-study','mock-case-study-FUTURE-TEMPLATE.html','../templates/case-study-template.html'),('concept-b-hero','concept-b-hero.html',None)]
def b64(path,mt): return 'data:%s;base64,%s'%(mt,base64.b64encode(open(path,'rb').read()).decode())
def fill(h): return h.replace('{{header}}',hdr).replace('{{footer}}',ftr)
# 1) bundled
for src,out,_ in pages:
    h=fill(rd(S+'/%s.html'%src))
    h=h.replace('{{fonts}}{{css}}',fonts+tokens+web+css).replace('{{fonts}}',fonts).replace('{{css}}',tokens+web+css)
    h=h.replace('{{logo-white}}',b64(LOGO+'/se-lockup-white.svg','image/svg+xml'))
    h=re.sub(r'\{\{img:([^}]+)\}\}',lambda m:b64(A+'/'+m.group(1),'image/png' if m.group(1).endswith('png') else 'image/jpeg'),h)
    open(D+'/'+out,'w').write(h); print(out,len(h)//1024,'KB')
# 2) static
T=D+'/static'; shutil.rmtree(T,ignore_errors=True)
for d in ['css','assets/img','assets/logo','assets/fonts']: os.makedirs(T+'/'+d)
open(T+'/css/tokens.css','w').write(tokens); open(T+'/css/tokens.web.css','w').write(web); open(T+'/css/site.css','w').write(css)
fc=rd(A+'/fonts.css'); out=[]
for sub,blk in re.findall(r'/\* (\S+) \*/\s*@font-face\s*{(.*?)}',fc,re.S):
    if sub!='latin': continue
    fam=re.search(r"font-family: '([^']+)'",blk).group(1); url=re.search(r'url\((.*?)\)',blk).group(1)
    fn=fam.lower()+'-latin.woff2'; p=T+'/assets/fonts/'+fn
    if not os.path.exists(p): urllib.request.urlretrieve(url,p)
    out.append('@font-face{'+blk.replace(url,'../assets/fonts/'+fn)+'}')
open(T+'/css/fonts.css','w').write('/* Interim Google Fonts (OFL): Figtree, Outfit. Swap via --se-font-* tokens. */\n'+'\n'.join(out))
for f in os.listdir(A):
    if f.endswith(('.jpg','.png')) and 'mock-only' not in f: shutil.copy(A+'/'+f,T+'/assets/img/'+f)
for f in os.listdir(LOGO):
    if f.startswith('se-lockup-white'): shutil.copy(LOGO+'/'+f,T+'/assets/logo/'+f)
links='</style><link rel="stylesheet" href="css/fonts.css"><link rel="stylesheet" href="css/tokens.css"><link rel="stylesheet" href="css/tokens.web.css"><link rel="stylesheet" href="css/site.css"><style>'
for src,_,out in pages:
    if not out: continue
    h=fill(rd(S+'/%s.html'%src)).replace('<style>{{fonts}}{{css}}</style>',links.replace('</style>','',1)[:-7])
    h=h.replace('{{logo-white}}','assets/logo/se-lockup-white.svg')
    h=re.sub(r'\{\{img:([^}]+)\}\}',r'assets/img/\1',h)
    if out.startswith('../'):
        h=h.replace('href="css/','href="../static/css/').replace('assets/img/','../static/assets/img/').replace('assets/logo/','../static/assets/logo/')
        os.makedirs(os.path.dirname(T+'/'+out),exist_ok=True)
    open(T+'/'+out,'w').write(h)
print('static ok', os.listdir(T))
