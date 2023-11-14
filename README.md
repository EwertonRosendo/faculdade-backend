Django REST API
Este é um projeto simples de Django para criar uma API REST para gerenciamento de usuários e senhas.

Instalação
1.Certifique-se de ter o Python instalado. Se não, você pode baixá-lo aqui.

2.Clone este repositório:
git clone https://github.com/seu-usuario/nome-do-repositorio.git

3.Navegue até o diretório do projeto:
cd nome-do-repositorio

4.Instale as dependências:
pip install -r requirements.txt

5.Aplique as migrações do Django:
python manage.py migrate

6.Execute o servidor de desenvolvimento:
python manage.py runserver

A API estará disponível em http://127.0.0.1:8000/.

Endpoints
Usuários
GET /users/

Retorna a lista de todos os usuários.
POST /users/

Cria um novo usuário. Enviar dados no formato JSON:
{
  "username": "nome_de_usuario",
  "email": "email@example.com",
  "password": "senha_segura"
}

PUT /users/{id}/

Atualiza um usuário existente. Enviar dados no formato JSON:
{
  "username": "novo_nome_de_usuario",
  "email": "novo_email@example.com",
  "password": "nova_senha_segura"
}
DELETE /users/{id}/

Exclui um usuário existente.
Senhas
GET /passwords/

Retorna a lista de todas as senhas.
POST /passwords/

Gera e salva uma nova senha para um usuário. Enviar dados no formato JSON:
{
  "user_id": 1,
  "lenghtPassword": 12
}
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.