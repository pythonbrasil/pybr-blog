# pythonbrasilblog

Blog oficial da Python Brasil - [https://blog.pythonbrasil.org.br/](https://blog.pythonbrasil.org.br/)

Esse blog é feito através do gerador de páginas estático do Python, o Pelican.

Caso queira colaborar, basta seguir esses passos:

### Processo de instalação:


Provavelmente irá aparecer em seu terminal algo como *(project-name)$*, agora vamos clonar o repositório do projeto:

> git clone git@github.com:pythonbrasil/pythonbrasilblog.git

> cd pythonbrasilblog

> git submodule update --init --recursive

Pronto! Você já está na pasta do projeto! Agora vamos instalar os programas necessários. Crie um [venv](https://docs.python.org/3/library/venv.html) com o nome que desejar, acesse a pasta e ative o virtualenv (Considerando os comandos em sistemas Linux e OS X):

> python3 -m venv venv

> source venv/bin/activate

> pip install -r requirements.txt

Legal, agora já instalei todos os programas, vamos fazê-lo rodar em nosso computador?

> make serve

O *make html* irá gerar o HTML e o *make serve* irá criar o servidor. Basta acessar *localhost:8000* e pronto! O site já está rodando em seu computador localmente!

Agora basta fazer as modificações na pasta *content/pages*, rodar os comandos *make html* e *make serve* e suas alterações já serão visíveis.

Resta então fazer o commit de suas alterações em seu repositório local e enviar-nos o Pull Request! o/

Mais informações sobre como funciona o Pelican, indicamos o artigo - [http://mindbending.org/pt/instalando-o-pelican](http://mindbending.org/pt/instalando-o-pelican).
