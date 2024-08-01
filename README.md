# RENOMEAR UPPER
🎈RENOMEIE SEUS ARQUIVOS PARA UPPER.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
Este é um simples executável feito em Python que permite renomear todos os arquivos em um diretório para letras maiúsculas e substituir espaços por sublinhados. Essa ferramenta pode ser útil para padronizar nomes de arquivos em um diretório.

## EXECUTANDO O PROJETO:
- Navegue até o diretório `./CODIGO`, e execute o arquivo Python com o comando:
```bash
python CODIGO.py
```
- Clique no botão `SELECIONAR` para escolher o diretório contendo os arquivos que você deseja renomear.
- Após selecionar o diretório, o programa renomeará automaticamente todos os arquivos no diretório para letras maiúsculas e substituirá espaços por sublinhados.
- Uma mensagem informará se a operação foi concluída com sucesso ou se ocorreu algum erro.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
- Este arquivo executável está disponível apenas para `Windows X64`. Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-w`: Especifica que o executável será do tipo "windowed", ou seja, sem exibir uma janela de console.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -w -F CODIGO.py
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)



