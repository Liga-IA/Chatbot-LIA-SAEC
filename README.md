# Chatbot-LIA-SAEC

## Ambiente de Desenvolvimento
Para o desenvolvimento, é necessário a utilização do python 3.7 e a versão mais recente da biblioteca da RASA, contudo como sabemos que é possível que algumas possas não tenham instalado certas coisas em suas maquinas locais, recomentados um ambiente online de desinvolvimento para este projeto, já que, desta forma, a maioria dos problemas é contornado e o resultado fica disponível online

### Gitpod
O gitpod é um ambiente de desenvolvimento em núvem gratuido (para repositórios públicos) que estaremos utilizando neste projeto. Para abrir um repositório em um ambiente deles, basta acessar **gitpod.io#{URL_GIT_REPO}**

<a href="www.gitpod.io#https://github.com/Liga-IA/Chatbot-LIA-SAEC" 
   target="_blank">
  <img src="https://user-images.githubusercontent.com/42501669/139507006-625831cd-349f-4ae0-9356-38505cb8c2f2.png" 
        alt="IMAGE ALT TEXT HERE" width="auto" height="32" border="10" />
</a>

### Versões das Dependências

- Para o gerenciamento de pacotes será utilizado o pipenv (para instalá-lo basta apenas executar `$ pip install pipenv`).
- Será utilizado python 3.7
- RASA:    
  - Pacote RASA: 2.8.10
  - RASA SDK: 2.8.2

### Instalação e setup do ambiente

- `$ pipenv install rasa`
    - Instala o RASA
    - Demora um pouco, entre 15 a 30 minutos dependendo da sua internet
- `$ pipenv shell`
- caso esteja executando localmente: `$ pipenv run rasa init` | caso esteja no gitpod: `$ rasa init`
    - inicia o projeto
- caso esteja executando localmente: `$ pipenv run rasa shell` | caso esteja no gitpod: `$ rasa shell`
    - Aqui ele executa o bot pra conversar pela CLI, caso queira testar

### Disponibilizando a API do bot online para integrar ao site

Caso esteja executando localmente, os procedimentos aqui apenas serão visivei em sua rede local, a não ser que implemente um tunnel das portas utilizadas para a rede externa. Por isso recomendamos o uso do gitpod, ou outra plataforma que permita o acesso às portas via HTTPS

`$ rasa run -m models --enable-api --cors "*"`

Isso vai iniciar a API do chatbot na porta `5005`, note que para executar comendos do RASA localmente pode ser que seja necessário o uso do `pipenv run` caso `rasa ....` não seja reconhecido como comando no seu terminal.
 
