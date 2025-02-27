**Descrição do Projeto:**

Este projeto tem como objetivo monitorar o número de inscritos de um canal do YouTube e notificar automaticamente o usuário sempre que houver uma alteração nesse número. Ele utiliza o Selenium WebDriver para acessar o canal do YouTube e extrair a quantidade atual de inscritos, além de enviar um e-mail de alerta sempre que o número de inscritos mudar. O projeto também registra as alterações em um arquivo de log, incluindo a data, hora e a quantidade de inscritos, garantindo o acompanhamento histórico das mudanças.

### Funcionalidades principais:
1. **Monitoramento Automático**: O programa verifica periodicamente o número de inscritos no canal do YouTube.
2. **Notificação por E-mail**: Sempre que o número de inscritos mudar, o sistema envia um e-mail de alerta para o destinatário configurado.
3. **Registro em Log**: O número de inscritos é registrado no arquivo `subscribe.log` com a data e hora da alteração, criando um histórico de mudanças.
4. **Execução em Modo Headless**: O Selenium é configurado para rodar em modo headless, ou seja, sem abrir uma janela de navegador, garantindo que o monitoramento aconteça de forma invisível e sem interferir nas operações do sistema.
5. **Verificação Periódica**: A cada 10 minutos, o programa verifica se houve alterações no número de inscritos e age de acordo.

### Tecnologias Utilizadas:
- **Selenium WebDriver**: Para automatizar o processo de navegação e captura do número de inscritos no YouTube.
- **Python**: Linguagem principal para a implementação do script.
- **SMTP**: Para enviar e-mails de alerta usando a conta de e-mail configurada.
- **Log de Arquivo**: Para registrar as mudanças no número de inscritos no arquivo `subscribe.log`.

### Como funciona:
1. O script acessa o canal do YouTube especificado e coleta o número de inscritos.
2. A cada 10 minutos, ele verifica se houve alteração no número de inscritos. Caso haja alteração, ele envia um e-mail de alerta e registra a alteração no arquivo de log.
3. O script continua rodando indefinidamente, verificando o número de inscritos e enviando notificações em caso de mudanças.

Este projeto pode ser útil para qualquer pessoa ou organização que queira monitorar de forma automatizada e receber notificações sobre as mudanças no número de inscritos de um canal do YouTube.