# Chatbot-LIA-SAEC

## Ambiente de Desenvolvimento

Para o desenvolvimento, é necessário a utilização do python 3.7 e a versão mais recente da biblioteca da RASA, contudo como sabemos que é possível que algumas pessoas não tenham instalado certas coisas em suas máquinas locais, recomendados um ambiente online de desenvolvimento para este projeto, já que, desta forma, a maioria dos problemas é contornado e o resultado fica disponível online

### Gitpod

O gitpod é um ambiente de desenvolvimento em nuvem gratuito (para repositórios públicos) que estaremos utilizando neste projeto. Para abrir um repositório em um ambiente deles, basta acessar **gitpod.io#{URL_GIT_REPO}**

[<img height="26px" src="gitpod-icon.png" target="_blank" />](https://www.gitpod.io#https://github.com/Liga-IA/Chatbot-LIA-SAEC)

### Versões das Dependências

- Para o gerenciamento de pacotes será utilizado o pipenv (para instalá-lo basta apenas executar `$ pip install pipenv`).
- Será utilizado python 3.7
- RASA:
  - Pacote RASA: 2.8.10
  - RASA SDK: 2.8.2

### Instalação e setup do ambiente

Note que para executar comandos do RASA localmente pode ser que seja necessário o uso do `pipenv run` caso `rasa ....` não seja reconhecido como comando no seu terminal.

- `$ pipenv --python 3.7`
- `$ pipenv shell`
- `$ pipenv install rasa==2.8.10`

  - Instala o RASA
  - Demora um pouco, entre 15 a 30 minutos dependendo da sua internet

- caso esteja executando localmente: `$ pipenv run rasa init` | caso esteja no gitpod: `$ rasa init`
  - inicia o projeto
- caso esteja executando localmente: `$ pipenv run rasa shell` | caso esteja no gitpod: `$ rasa shell`
  - Aqui ele executa o bot pra conversar pela CLI, caso queira testar

Caso esteja com preguiça de fazer isso, pode copiar o pipfile e depois só rodar `pipenv install` 😁

### Disponibilizando a API do bot online para integrar ao site

Caso esteja executando localmente, os procedimentos aqui apenas serão visivei em sua rede local, a não ser que implemente um tunnel das portas utilizadas para a rede externa. Por isso recomendamos o uso do gitpod, ou outra plataforma que permita o acesso às portas via HTTPS

`$ rasa run -m models --enable-api --cors "*"`

Isso vai iniciar a API do chatbot na porta `5005`.

## Integrando com o site

Adicione o segunte script na tag `body` do seu html

```
  <div
    data-root-element-id="storybook-preview-wrapper"
    data-websocket-url="{URL_PORT5005_API}" id="rasa-chat-widget"></div>
  <script src="https://unpkg.com/@rasahq/rasa-chat" type="application/javascript"></script>
```

https://chat-widget-docs.rasa.com/?path=/docs/rasa-chat-widget--widget
