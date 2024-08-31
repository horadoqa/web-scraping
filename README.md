# web-scraping

Web Scraping é uma técnica utilizada para extrair informações de páginas da internet de forma automatizada. Imagine que você queira coletar dados de preços de produtos de um e-commerce, informações de contato de empresas em um diretório online ou até mesmo acompanhar as notícias atualizadas de um portal de notícias. Fazer isso manualmente seria uma tarefa árdua e demorada, mas com o Web Scraping, é possível automatizar o processo e coletar grandes volumes de dados em pouco tempo.

## Por que Utilizar Python para Web Scraping?

Python é uma linguagem de programação que se destaca pela sua simplicidade e legibilidade, o que facilita o aprendizado e a implementação de projetos de Web Scraping. Além disso, possui uma comunidade ativa e uma vasta gama de bibliotecas especializadas que simplificam a extração de dados da web. Com Python, você pode criar scripts de Web Scraping robustos e eficientes, capazes de lidar com diferentes estruturas de páginas web e de contornar algumas das barreiras que podem ser encontradas, como JavaScript dinâmico e proteções contra bots.

## Opções de Bibliotecas para Web Scraping em Python

Existem diversas bibliotecas em Python que podem ser utilizadas para Web Scraping, cada uma com suas particularidades e vantagens. Algumas das mais populares incluem:

- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/): Ideal para projetos que envolvem a extração de dados de páginas HTML. É fácil de usar e muito eficiente para analisar e extrair informações de documentos HTML e XML. Neste guia, mostramos em mais detalhes como utilizar a biblioteca Beautiful Soup.
- [Selenium](https://selenium-python.readthedocs.io/): Além de ser uma ferramenta para testes automatizados de aplicações web, o Selenium é capaz de interagir com páginas web como se fosse um usuário real, o que é útil para lidar com páginas que utilizam muitos recursos de JavaScript.
- [Scrapy](https://scrapy.org/): Um framework de Web Scraping e crawling de alta eficiência e flexibilidade. É uma ótima opção para projetos mais complexos e para a coleta de dados em larga escala.
- Requests-HTML: Uma biblioteca que combina as funcionalidades de Requests e PyQuery, permitindo realizar requisições em páginas web e extrair dados de forma prática.

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
sudo apt install python3.8-ven
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
