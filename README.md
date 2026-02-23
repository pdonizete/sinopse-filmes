# 🎬 Filmes - Cliente para Terminal

Um cliente Python simples para buscar sinopses de filmes diretamente pelo terminal, usando a API OMDb.

---

## 📋 Requisitos

- Python 3.7+
- Biblioteca `requests`
- Chave da API OMDb (gratuita)

---

## 🔑 Como Obter a Chave da API (OMDb)

A OMDb (Open Movie Database) oferece uma API gratuita para buscar informações sobre filmes.

### Passos para obter sua chave:

1. **Acesse o site oficial:**
   ```
   http://www.omdbapi.com/apikey.aspx
   ```

2. **Preencha o formulário:**
   - **Email:** Seu endereço de email válido
   - **Nome:** Seu nome completo
   - **Uso:** Selecione "Educational/Personal" (uso educacional/pessoal) — é gratuito!

3. **Confirme seu email:**
   - Você receberá um email com um link de ativação
   - Clique no link para confirmar

4. **Receba sua chave:**
   - A chave será enviada por email (formato: `xxxxxxxx`)
   - Pode demorar alguns minutos

---

## ⚙️ Configuração

### Opção 1: Variável de Ambiente (Recomendado)

Adicione ao seu arquivo `~/.bashrc` ou `~/.zshrc`:

```bash
export OMDB_API_KEY='sua_chave_aqui'
```

Depois, recarregue:
```bash
source ~/.bashrc
```

### Opção 2: Arquivo .env (Mais Fácil!)

1. Copie o arquivo de exemplo:
   ```bash
   cp .env.example .env
   ```

2. Edite o arquivo `.env` com sua chave:
   ```
   OMDB_API_KEY=sua_chave_aqui
   ```

3. ✅ Pronto! O script carrega automaticamente do arquivo `.env`
   - Não precisa exportar variável manualmente
   - Só editar o arquivo e usar!

---

## 🚀 Instalação

1. **Clone ou baixe o projeto:**
   ```bash
   cd ~/projetos/filmes
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure sua chave da API:**
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com sua chave
   ```

---

## 🎯 Uso

### Buscar um filme:

```bash
python filmes.py "O Poderoso Chefão"
```

```bash
python filmes.py "The Dark Knight"
```

```bash
python filmes.py "Inception"
```

### Dicas:

- Use aspas para títulos com espaços
- Se o título em português não funcionar, tente o título original em inglês
- A API retorna o primeiro resultado que encontrar

---

## 📄 Saída Exemplo

```
======================================================================
🎬  The Godfather (1972)
======================================================================

📚 Gênero: Crime, Drama
🎥 Diretor: Francis Ford Coppola
👥 Atores principais: Marlon Brando, Al Pacino, James Caan
⏱️  Duração: 175 min
🌍 País: USA

📊 Nota IMDB: ⭐ 9.2/10 (Excelente)

📝 SINOPSE:
----------------------------------------------------------------------
The aging patriarch of an organized crime dynasty transfers control...
======================================================================
```

---

## 🐛 Solução de Problemas

| Erro | Solução |
|------|---------|
| "Chave da API não encontrada" | Configure a variável `OMDB_API_KEY` |
| "Filme não encontrado" | Tente o título em inglês |
| "Problema de conexão" | Verifique sua internet |
| "API demorou muito" | Tente novamente mais tarde |

---

## 📚 Sobre a API OMDb

- **Limite gratuito:** 1.000 requisições/dia
- **Documentação:** http://www.omdbapi.com/
- **Formato:** JSON
- **Dados:** Títulos, sinopses, elenco, notas, posters, etc.

---

## 📝 Licença

Uso pessoal/educacional.

---

**Feito com 🎬 por Claude Code**
