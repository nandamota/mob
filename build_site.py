"""Gera a pasta site/ para o repositório mobpratico (GitHub Pages):
index.html (guia), grafico-mob.zip (skill) e ícones.
Rode depois de build.py."""
import os, shutil

SITE_URL = "https://lirio-studio.github.io/mobpratico/"
os.makedirs("site", exist_ok=True)
g = open("guia/COMECE-AQUI.html", encoding="utf-8").read()

def rep(a, b, n=1):
    global g
    assert g.count(a) >= n, a[:60]
    g = g.replace(a, b)

# cabeçalho: ícone da aba e prévia no WhatsApp
rep('<title>Como instalar o Gráfico MOB</title>', '''<title>Como instalar o Gráfico MOB</title>
<meta name="description" content="Passo a passo para instalar o Gráfico MOB no Claude: registro diário do Método de Ovulação Billings.">
<meta property="og:title" content="Gráfico MOB · Como instalar">
<meta property="og:description" content="Seu gráfico do Método Billings no Claude. Passo a passo de 10 minutos.">
<meta property="og:image" content="''' + SITE_URL + '''og.png">
<meta property="og:url" content="''' + SITE_URL + '''">
<meta property="og:type" content="website">
<meta name="theme-color" content="#6B3F6E">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">''')

# no site, a skill é baixada por um botão (não vem num kit)
rep('''      <li>O arquivo <span class="k">2-grafico-mob.zip</span>, que veio junto com este guia. <b>Não abra nem descompacte esse arquivo.</b> Ele será enviado inteiro no passo 3.</li>''',
    '''      <li>O arquivo da skill, que você baixa aqui embaixo. <b>Não abra nem descompacte esse arquivo.</b> Ele será enviado inteiro no passo 3.</li>
    </ul>
    <a class="btn dl" href="grafico-mob.zip" download>
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>
      Baixar a skill (grafico-mob.zip)</a>
    <p class="dlhint">No celular, o arquivo vai para a pasta <b>Downloads</b> (no iPhone, app <b>Arquivos → Downloads</b>).</p>
    <ul style="display:none">''')
rep('2-grafico-mob.zip', 'grafico-mob.zip', 1)
rep('Se você descompactou sem querer, baixe o kit de novo.', 'Se você descompactou sem querer, baixe o arquivo de novo nesta página.')
rep('<i>HTML</i>1-COMECE-AQUI.html', '<i>PDF</i>outro-arquivo.pdf')
rep('</style>', '''.btn.dl{margin-top:12px;width:100%;justify-content:center}
.dlhint{font-size:.8rem;color:var(--muted);margin:8px 0 0;text-align:center}
</style>''')

open("site/index.html", "w", encoding="utf-8").write(g)
shutil.copy("dist/grafico-mob.zip", "site/grafico-mob.zip")
for src, dst in [("brand/mob-64.png", "favicon.png"), ("brand/mob-180.png", "apple-touch-icon.png"), ("brand/mob-512.png", "icon-512.png")]:
    shutil.copy(src, "site/" + dst)
if os.path.exists("site/logo.svg"):
    os.remove("site/logo.svg")
open("site/README.md", "w", encoding="utf-8").write(
    "# MOB Prático\n\nPasso a passo para instalar o **Gráfico MOB** no Claude.\n\n"
    "- Site: " + SITE_URL + "\n- Skill: `grafico-mob.zip`\n\n"
    "Gerado a partir do repositório `mob` (`python3 build.py && python3 build_site.py`).\n")
print("site/ gerado")
