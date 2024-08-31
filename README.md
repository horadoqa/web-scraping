# web-scraping

Web Scraping é uma técnica utilizada para extrair informações de páginas da internet de forma automatizada. Imagine que você queira coletar dados de preços de produtos de um e-commerce, informações de contato de empresas em um diretório online ou até mesmo acompanhar as notícias atualizadas de um portal de notícias. Fazer isso manualmente seria uma tarefa árdua e demorada, mas com o Web Scraping, é possível automatizar o processo e coletar grandes volumes de dados em pouco tempo.

## Como fazer Web Scraping no Python?

É mais fácil do que se pode imaginar. As etapas básicas do Web Scraping com Python são:

- Encontre a URL que você deseja raspar;
- Inspecione a página;
- Encontre os dados que deseja extrair;
- Escreva o código;
- Execute o código e extraia os dados;
- Armazene os dados no formato necessário.

## Instalar o PIP

```bash
sudo apt install -y python3-pip
```

## Isolando o ambiente

Instalar venv

```bash
sudo apt install python3.10-venv
```

Isolar o ambiente:

```bash
python3 -m venv ./venv && source venv/bin/activate
```

## Instalando dependências

- [requests](https://pypi.org/project/requests/)
- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) 

```bash
pip install requests
```
