# 🌐 DesafioAPIs_SquadBerthaLutz

Este projeto utiliza bibliotecas Python gerenciadas através de um arquivo `requirements.txt` 📋 para padronizar as versões usadas. Siga os passos abaixo para configurar seu ambiente de desenvolvimento.

## 🛠️ Configuração do Ambiente Virtual

Para garantir que todas as bibliotecas e versões corretas sejam instaladas, recomendamos o uso de um ambiente virtual (venv) 🐍. Veja abaixo como configurá-lo de acordo com seu sistema operacional.

### 1. 🌀 Criar o Ambiente Virtual

- **Windows**: 
  ```bash
  python -m venv venv
  ```

- **macOS/Linux**: 
  ```bash
  python3 -m venv venv
  ```

### 2. ⚙️ Ativar o Ambiente Virtual

- **Windows**: 
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**: 
  ```bash
  source venv/bin/activate
  ```

### 3. 📦 Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. ❌ Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, desative o ambiente virtual com o comando:

```bash
deactivate
```

## 📂 Estrutura dos Templates

Os arquivos HTML devem ser armazenados na pasta `templates` 🗂️. Certifique-se de manter essa estrutura para que o projeto funcione corretamente.

### Estrutura de arquivos:

- **characters.html**: Página para exibir a lista de personagens da API Rick and Morty.
- **profile.html**: Exibe o perfil detalhado de cada personagem.
- **episodes.html**: Página que lista os episódios da série.
- **episode.html**: Exibe detalhes de um episódio específico.
- **locations.html**: Exibe uma lista de localizações do universo Rick and Morty.
- **location.html**: Mostra detalhes de uma localização específica.
- **layout.html**: Template base usado pelas outras páginas.
- **nav.html**: Barra de navegação.

## 🧪 Testes Realizados

Durante os testes, as seguintes validações foram feitas para garantir que o projeto funciona corretamente:

### 1. **Configuração do Ambiente e Instalação de Dependências**
   - O ambiente virtual foi criado e ativado com sucesso.
   - As dependências foram instaladas corretamente utilizando o arquivo `requirements.txt`.

### 2. **Testes de Funcionalidade nas Rotas**
   - **Rota Principal ("/")**: Verificou-se que a lista de personagens da API Rick and Morty está sendo exibida corretamente na página inicial. A imagem de cada personagem e o botão para ver o perfil funcionam conforme esperado.
   - **Rota de Perfil ("/profile/<id>")**: A página de perfil para cada personagem está funcionando corretamente, mostrando detalhes do personagem e listando os episódios em que ele aparece, com links para visualização dos episódios.
   - **Rota de Episódios ("/episodes")**: A lista de episódios da série está sendo exibida. Cada episódio é clicável e leva à página de detalhes.
   - **Rota de Detalhe de Episódio ("/episodes/<id>")**: A página de detalhe de cada episódio exibe corretamente o nome, data de exibição, código do episódio e os personagens relacionados.
   - **Rota de Localizações ("/locations")**: A listagem de localizações do universo Rick and Morty está funcionando e os links levam aos detalhes de cada local.
   - **Rota de Detalhes da Localização ("/location/<id>")**: Exibe corretamente as informações da localização, incluindo o nome, tipo, dimensão e os residentes, com links para os perfis dos personagens.

### 3. **Testes Visuais**
   - Todos os templates HTML estão sendo renderizados corretamente, utilizando o framework Bootstrap para estilizar as tabelas e a interface visual do projeto.
   - A barra de navegação está funcional, permitindo a navegação entre diferentes páginas da aplicação.

### 4. **Interação com a API Rick and Morty**
   - A comunicação com a API está funcionando sem erros. Todos os dados solicitados (personagens, episódios, locais) estão sendo carregados e exibidos corretamente nas páginas correspondentes.

---

## 🚀 Conclusão

Este projeto implementa uma interface visual que interage com a API Rick and Morty para exibir personagens, episódios e localizações do universo da série. Siga os passos de instalação para rodar o projeto localmente e explore as funcionalidades oferecidas. 

