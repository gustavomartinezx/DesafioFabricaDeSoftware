<h1> Desafio fábrica de software </h1>

<i><b>**O nome do país de origem tem que ser escrito da forma que se escreve no país de origem, ex: Estados Unidos - United States**</b></i>

<p>Esse projeto tem a API desenvolvida para a admnistração de uma loja, utilizando-se de três entidades: "Cliente", "Funcinário" e "Produto".</p>

<h2>Comandos utéis</h2>
<p>clone de repositório  <b>`git clone https://github.com/gustavomartinezx/DesafioFabricaDeSoftware`</b></p>
<p>criação do ambiente virtual <b>`python -m venv venv`</b></p>
<p>baixar as requisições <b>`pip install -r requirements.txt`</b></p>
<p>Rodar o servidor <b>`python manage.py runserver`</b></p>



<h2>Integração do seu banco de dados postgreSQL</h2>
<p> em settings.py troque a senha a qual foi designado ao seu DB, e crie uma nova database</p>
<p>
<p></p>DATABASES = {
<p>ㅤㅤ'default': {
<p>ㅤㅤㅤㅤ'ENGINE': 'django.db.backends.postgresql_psycopg2',
<p>ㅤㅤㅤㅤ 'NAME': 'lojadeprodutos', 
<p>ㅤㅤㅤㅤ'USER': 'postgres',
<p>ㅤㅤㅤㅤ <b>'PASSWORD': 'admin',</b>
<p>ㅤㅤㅤㅤ 'HOST': '127.0.0.1', 
<p>ㅤㅤㅤㅤ'PORT': '5432',
<p>ㅤㅤ}
<p>}
<p>Migre sua tabela para o DB<b> python manage.py migrate</b></p>

<h2>Projeto Loja de produtos</h2>
<p><i>APP pessoaFisica</i>: Recebe o campo Pessoa, o qual terá campos que serão herdados para as entidades "Cliente" e "Funcionário, utlizando-se do abstract=True para classe Meta, para que não haja repetição de código, utilizando-se de CharField para Nome, Sobrenone, CPF(com limite de 11 carácteres) e Sexo. O campo sexo é utilizado choices para ter a pré-definição de sexo Masculino e Feminino. 
<p><i>APP produto:</i> Recebe os campos Comprador e vendedor(utilizando-se de foreign key, a qual obtem a chave estrangeira do Cliente e Funcionário cadastrados pelo outro app. ), moeda(é um CharField com o read_only=True que irá ter o espaço para receber a API), Imagem(é um campo para colocar imagens, utilizando do pacote Pillow), Em estoque(Boolean Field) </p>
<p><i>O mopdelo foreing key utilizado para relacionar o produto com o Cliente e Funcionário de forma rápida, tendo seu método on_delete Cascade para não que não haja campos sem vínculos no DB</i></p>

<h2>API Rest Countries</h2>
<p>Para este projeto, foi utilizado uma API externa gratuíta para ter informações de dados do país, a qual irá pegar a moeda específica do país e irá preencher o campo de forma rápida e eficaz.</p>
<p>Com o viewset, há o método de GET Moeda, que irá fazer uma requisição baseado na informação pais residente do cliente, após receber o país pela API irá obter o câmbio específico da região, e com a função perfom_create irá ter uma averiguação se há um cliente registrado, para salvar um objeto com a moeda que foi definida. </p>
<p>Em primeira instância, a API não consegue realizar a busca do país escrevendo o nome do local diferente da língua deste mesmo país, por exemplo, não pode escrever Brazil, e sim, Brasil. Não pode Alemanha, e sim, Deutschland.</p>
