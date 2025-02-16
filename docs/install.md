# SETUP

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

## Se você estiver usando uma versão mais antiga do Python ou do pip, pode ser útil atualizar também:

```bash
pip install --upgrade pip
```

Isolar o ambiente:

```bash
python3 -m venv ./venv && source venv/bin/activate
```

## Instalando dependências

- [requests](https://pypi.org/project/requests/)
beautifulsoup4
selenium


```bash
pip install wheel requests beautifulsoup4 selenium pyautogui
```

## Passos para configurar o Xvfb:

Instalar o Xvfb: No terminal, execute o seguinte para instalar o Xvfb no seu sistema Linux:

```bash
sudo apt-get install xvfb

## Executar o script com o Xvfb: Para rodar o script com o Xvfb, use o comando:

```bash
xvfb-run python3 youtube.py
```

