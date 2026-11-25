---
name: grafico-mob
description: Cria e abre o "Meu Gráfico MOB", app de registro diário do Método de Ovulação Billings (MOB) no modelo da folha CENPLAFAM, com cadastro, gráfico de ciclos lado a lado, dúvidas para a instrutora e PDF. Use sempre que a pessoa pedir o gráfico MOB, gráfico Billings, gráfico do ciclo, registrar muco/sensação, método Billings, CENPLAFAM ou "meu gráfico", e também para tirar dúvidas sobre como preencher o gráfico (cores, símbolos, ápice, PBI, regras).
---

# Meu Gráfico MOB

Esta skill entrega à pessoa o próprio app "Meu Gráfico MOB", publicado **na conta dela**, para que os registros fiquem salvos e privados para ela. O app já faz tudo sozinho na primeira abertura: **cadastro → mini explicação → visualização do gráfico**. Não refaça esse fluxo no chat.

Fale sempre em português do Brasil, com frases curtas e acolhedoras. A pessoa provavelmente não é técnica: não mencione arquivos, capacidades, HTML ou banco de dados, a menos que ela pergunte.

## 1. Quando a pessoa pede o gráfico

### Primeiro, veja se ela já tem um
Se a ferramenta `Artifact` estiver disponível, liste os artifacts dela (`action: "list"`) e procure um com o título **"Meu Gráfico MOB"**.
- Se existir: abra esse (`action: "open"` com a URL) e diga que o gráfico dela está ali, com os registros salvos. **Não publique outro**, senão ela fica com dois gráficos e registros separados.
- Se ela pediu para **atualizar** o app (nova versão), leia o artifact existente (`action: "read"`) e publique `assets/app.html` com `url` dessa mesma artifact. Os registros dela continuam salvos, porque ficam no banco da artifact e não no HTML.

### Se ela ainda não tem
Publique o arquivo `assets/app.html` desta skill **sem alterar nada**, assim:
- `file_path`: o caminho de `assets/app.html` dentro da pasta desta skill (leia o arquivo inteiro antes, como a ferramenta exige)
- `icon`: `"flower"`
- `description`: `"Registro diário do Método de Ovulação Billings, com dúvidas para a instrutora e PDF."`
- `capabilities`: `{"db": {}, "user": {}, "downloads": true, "dictation": {}}`

Depois de publicar, ofereça fixar na barra lateral (`action: "pin"`) para ela achar fácil. Explique em poucas linhas:
1. Na primeira vez o app pede um mini cadastro e mostra como funciona.
2. Os registros ficam salvos na conta Claude dela, visíveis só para ela.
3. Lembretes: no Perfil do app há botões para colocar o lembrete diário e o acompanhamento mensal no Google Agenda.
4. Para ditar: no computador (Chrome), o botão de microfone do app funciona. No celular, use o microfone do teclado.
5. O link é só dela. Não precisa compartilhar com ninguém, a não ser que queira mostrar à instrutora. Para a instrutora, o melhor é o PDF.
6. Para ficar como app no celular: mostre o link completo do gráfico para ela copiar. No Android, abrir o link no Chrome → ⋮ → "Adicionar à tela inicial" (ou "Instalar app"). No iPhone, abrir no Safari → Compartilhar → "Adicionar à Tela de Início".

### Se a ferramenta `Artifact` não existir (chat comum)
Crie um artifact HTML com o conteúdo de `assets/app.html`. Nesse modo os registros ficam salvos **só no navegador/aparelho** em que ela usar. Avise com clareza que ela deve usar sempre o mesmo aparelho e fazer de vez em quando **Perfil → Salvar cópia**.

## 2. Dúvidas sobre o método

Responda com base em `references/metodo.md`, que resume as cores, os símbolos e as regras como estão no app. Regras de ouro:
- Explique o que o gráfico mostra; **não diga se um dia é fértil ou infértil para ela decidir ter ou não relação**. Isso é papel da instrutora credenciada. Quando a dúvida for sobre a decisão, sugira anotar na aba **Instrutora** do app para levar ao acompanhamento.
- Não substitua a instrutora nem contradiga orientações que ela já deu.
- Assuntos de saúde fora do método (sangramento muito diferente do habitual, dor forte, suspeita de gravidez com sintomas) → orientar a procurar um médico.

## 3. Registrar pelo chat

Se ela descrever o dia no chat ("hoje seca, nada vejo, cólica"), diga que o jeito mais rápido é escrever exatamente isso no campo **“Fale ou escreva como foi o dia”** do app, que ele preenche o selo, a cor e os sintomas sozinho. Abra o gráfico dela para facilitar.
