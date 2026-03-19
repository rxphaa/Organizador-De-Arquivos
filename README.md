# 📁 Organizador de Séries

Script Python para organizar automaticamente episódios de séries em pastas por série e temporada.

---

## 💡 O que o script faz

Varre uma pasta com episódios bagunçados e os organiza automaticamente na estrutura:

```
📂 Nome da Série
└── 📂 Temporada 01
    ├── episodio1.mkv
    └── episodio2.mkv
```

Compatível com dois formatos de nome de arquivo:
- `Chicago.Fire.S14E08.1080p.mkv`
- `The Rookie S07E03 Out of Pocket 1080p.mkv`

---

## ▶️ Como rodar

**Pré-requisitos:** Python 3.6+

Não é necessário instalar nenhuma biblioteca externa — o script usa apenas módulos nativos do Python (`pathlib`, `shutil`, `re`).

**Passos:**

1. Clone o repositório ou baixe o arquivo `organizador.py`
2. Coloque o script na mesma pasta dos episódios
3. Execute:

```bash
python organizador.py
```

---

## 🔄 Exemplo de resultado

**Antes:**
```
📂 Series
├── Chicago.Fire.S14E08.1080p.WEB.mkv
├── Chicago.Fire.S14E09.1080p.WEB.mkv
├── The.Rookie.S08E01.1080p.mkv
└── The Rookie S07E03 Out of Pocket 1080p.mkv
```

**Depois:**
```
📂 Series
├── 📂 Chicago Fire
│   └── 📂 Temporada 14
│       ├── Chicago.Fire.S14E08.1080p.WEB.mkv
│       └── Chicago.Fire.S14E09.1080p.WEB.mkv
└── 📂 The Rookie
    ├── 📂 Temporada 07
    │   └── The Rookie S07E03 Out of Pocket 1080p.mkv
    └── 📂 Temporada 08
        └── The.Rookie.S08E01.1080p.mkv
```

---

## 🛠️ Tecnologias utilizadas

- `pathlib` — navegação de caminhos
- `re` — expressões regulares para identificar série e temporada
- `shutil` — movimentação de arquivos# Organizador-De-Arquivos
Script Python para organizar episódios de séries automaticamente em pastas por série e temporada. Utiliza Regex, Pathlib e Shutil.
