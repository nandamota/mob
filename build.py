"""Gera index.html (GitHub Pages) a partir de app.html (fonte única, também publicada no Claude)."""
src = open("app.html", encoding="utf-8").read()
head = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#6B3F6E">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="MOB">
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" href="favicon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}</style>
</head>
<body>
"""
open("index.html", "w", encoding="utf-8").write(head + src + "\n</body>\n</html>\n")
print("index.html gerado")

# Atualiza a skill com a versão atual do app e gera o .zip para instalar no Claude
import shutil, os, zipfile
shutil.copy("app.html", "skill/grafico-mob/assets/app.html")
os.makedirs("dist", exist_ok=True)
with zipfile.ZipFile("dist/grafico-mob.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk("skill/grafico-mob"):
        for f in files:
            full = os.path.join(root, f)
            z.write(full, os.path.relpath(full, "skill"))
print("dist/grafico-mob.zip gerado")

# Kit para enviar às amigas: guia (passo 1) + skill (passo 2).
# A skill vai como .zip separado dentro do kit, porque o Claude só aceita o .zip com a skill sozinha.
with zipfile.ZipFile("dist/kit-grafico-mob.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write("guia/COMECE-AQUI.html", "1-COMECE-AQUI.html")
    z.write("dist/grafico-mob.zip", "2-grafico-mob.zip")
print("dist/kit-grafico-mob.zip gerado")

# Ícone MOB no kit (passo 3), para criar o atalho na tela inicial
with zipfile.ZipFile("dist/kit-grafico-mob.zip", "a", zipfile.ZIP_DEFLATED) as z:
    z.write("icon-512.png", "3-icone-MOB.png")
print("ícone adicionado ao kit")
