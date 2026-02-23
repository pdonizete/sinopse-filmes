#!/usr/bin/env python3
"""
Filmes - Cliente para buscar sinopses de filmes via terminal

Uso: python filmes.py "Nome do Filme"

Exemplo: python filmes.py "O Poderoso Chefão"
"""

import os
import sys
import argparse
from typing import Optional
import requests
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()


def get_api_key() -> str:
    """Obtém a chave da API OMDB das variáveis de ambiente."""
    api_key = os.environ.get('OMDB_API_KEY')
    if not api_key:
        print("❌ Erro: Chave da API não encontrada!")
        print("\n👉 Configure a variável de ambiente OMDB_API_KEY:")
        print("   export OMDB_API_KEY='sua_chave_aqui'")
        print("\n📖 Veja o README.md para instruções de como obter uma chave grátis.")
        sys.exit(1)
    return api_key


def buscar_filme(nome_filme: str, api_key: str) -> Optional[dict]:
    """Busca os dados do filme na API OMDB."""
    base_url = "http://www.omdbapi.com/"
    params = {
        't': nome_filme,
        'apikey': api_key,
        'plot': 'full'  # Retorna sinopse completa
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('Response') == 'False':
            return None
        
        return data
    except requests.exceptions.Timeout:
        print("❌ Erro: A API demorou muito para responder.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Problema de conexão com a internet.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        return None


def formatar_nota(nota: str) -> str:
    """Formata a nota do IMDB com cor baseada no valor."""
    try:
        nota_float = float(nota)
        if nota_float >= 8.0:
            return f"⭐ {nota}/10 (Excelente)"
        elif nota_float >= 7.0:
            return f"👍 {nota}/10 (Bom)"
        elif nota_float >= 5.0:
            return f"😐 {nota}/10 (Regular)"
        else:
            return f"👎 {nota}/10 (Ruim)"
    except ValueError:
        return f"❓ {nota}/10"


def exibir_filme(data: dict) -> None:
    """Exibe as informações do filme formatadas."""
    titulo = data.get('Title', 'N/A')
    ano = data.get('Year', 'N/A')
    sinopse = data.get('Plot', 'Sinopse não disponível')
    diretor = data.get('Director', 'N/A')
    atores = data.get('Actors', 'N/A')
    nota = data.get('imdbRating', 'N/A')
    genero = data.get('Genre', 'N/A')
    duracao = data.get('Runtime', 'N/A')
    pais = data.get('Country', 'N/A')
    
    print("\n" + "="*70)
    print(f"🎬  {titulo} ({ano})")
    print("="*70)
    print(f"\n📚 Gênero: {genero}")
    print(f"🎥 Diretor: {diretor}")
    print(f"👥 Atores principais: {atores}")
    print(f"⏱️  Duração: {duracao}")
    print(f"🌍 País: {pais}")
    print(f"\n📊 Nota IMDB: {formatar_nota(nota)}")
    print(f"\n📝 SINOPSE:")
    print("-"*70)
    print(f"{sinopse}")
    print("="*70)
    print()


def main() -> None:
    """Função principal do programa."""
    parser = argparse.ArgumentParser(
        description='Busca sinopses de filmes via terminal',
        epilog='Exemplo: python filmes.py "O Poderoso Chefão"'
    )
    parser.add_argument(
        'filme',
        type=str,
        nargs='+',
        help='Nome do filme entre aspas'
    )
    
    args = parser.parse_args()
    nome_filme = ' '.join(args.filme)
    
    print(f"\n🔍 Buscando: \"{nome_filme}\"...")
    
    api_key = get_api_key()
    dados_filme = buscar_filme(nome_filme, api_key)
    
    if dados_filme:
        exibir_filme(dados_filme)
    else:
        print(f"\n❌ Filme '{nome_filme}' não encontrado.")
        print("💡 Dica: Tente usar o título original em inglês.")
        sys.exit(1)


if __name__ == '__main__':
    main()
