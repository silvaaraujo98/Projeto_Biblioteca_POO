# Sistema de Gerenciamento de Biblioteca

## Descrição Geral

O objetivo deste projeto é desenvolver um sistema de gerenciamento para uma biblioteca. Este sistema permitirá a administração de livros, usuários (membros da biblioteca), empréstimos e devoluções de livros.

## Funcionalidades

- Gestão de Livros
- Gestão de Usuários
- Gestão de Empréstimos
- Relatórios

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/biblioteca_project.git

## Sobre o Projeto:
## Projeto: Sistema de Gerenciamento de Biblioteca

### Descrição Geral

O objetivo deste projeto é desenvolver um sistema de gerenciamento para uma biblioteca. Este sistema permitirá a administração de livros, usuários (membros da biblioteca), empréstimos e devoluções de livros. O projeto será modular e permitirá futuras expansões, como a adição de funcionalidades para gerenciar funcionários, multas por atraso, entre outros.

### Requisitos Funcionais

1. **Gestão de Livros**:
    - Adicionar novos livros ao sistema.
    - Atualizar informações dos livros.
    - Remover livros do sistema.
    - Consultar informações de livros.
2. **Gestão de Usuários**:
    - Adicionar novos usuários ao sistema.
    - Atualizar informações dos usuários.
    - Remover usuários do sistema.
    - Consultar informações dos usuários.
3. **Gestão de Empréstimos**:
    - Registrar novos empréstimos.
    - Registrar devoluções de livros.
    - Consultar status de empréstimos.
4. **Relatórios**:
    - Gerar relatórios de livros disponíveis.
    - Gerar relatórios de livros emprestados.
    - Gerar relatórios de usuários com empréstimos ativos.

### Estrutura do Sistema

### Classes

1. **Livro**
    - Atributos:
        - `titulo`
        - `autor`
        - `isbn`
        - `ano_publicacao`
        - `numero_exemplares`
    - Métodos:
        - `adicionar_exemplares()`
        - `remover_exemplares()`
        - `emprestar_exemplar()`
        - `devolver_exemplar()`
2. **Usuario**
    - Atributos:
        - `nome`
        - `cpf`
        - `email`
        - `telefone`
        - `endereco`
        - `livros_emprestados` (lista de livros emprestados)
    - Métodos:
        - `atualizar_informacoes()`
        - `adicionar_livro_emprestado()`
        - `remover_livro_emprestado()`
3. **Emprestimo**
    - Atributos:
        - `usuario`
        - `livro`
        - `data_emprestimo`
        - `data_devolucao`
    - Métodos:
        - `registrar_emprestimo()`
        - `registrar_devolucao()`
        - `verificar_status()`
4. **Biblioteca**
    - Atributos:
        - `livros` (lista de objetos Livro)
        - `usuarios` (lista de objetos Usuario)
        - `emprestimos` (lista de objetos Emprestimo)
    - Métodos:
        - `adicionar_livro()`
        - `remover_livro()`
        - `buscar_livro()`
        - `adicionar_usuario()`
        - `remover_usuario()`
        - `buscar_usuario()`
        - `registrar_emprestimo()`
        - `registrar_devolucao()`
        - `gerar_relatorio_livros_disponiveis()`
        - `gerar_relatorio_livros_emprestados()`
        - `gerar_relatorio_usuarios_com_emprestimos()`

### Conceitos Utilizados

1. **Encapsulamento**:
    - Uso de atributos privados e métodos getters e setters.
    - Proteção de dados sensíveis dos objetos (livros e usuários).
2. **Herança**:
    - Possibilidade de criar subclasses para diferentes tipos de usuários (ex. Aluno, Professor) e livros (ex. LivroFisico, Ebook).
3. **Polimorfismo**:
    - Implementação de métodos que podem ser sobrescritos em subclasses, permitindo comportamentos específicos.
4. **Abstração**:
    - Criação de classes abstratas para definir interfaces comuns a serem implementadas por subclasses.
5. **Composição**:
    - Uso de objetos de outras classes dentro das classes principais (ex. `Emprestimo` contendo um objeto `Livro` e um objeto `Usuario`).
6. **Métodos e Atributos de Classe**:
    - Uso de métodos e atributos que pertencem à classe em vez de instâncias individuais (ex. contagem de livros totais na biblioteca).
7. **Propriedades (Properties)**:
    - Uso do decorador `@property` para definir métodos que podem ser acessados como atributos.

### Fluxo do Sistema

1. **Adicionar Livros**:
    - Administrador insere dados do livro no sistema.
    - Sistema cria um objeto `Livro` e adiciona à lista de livros da `Biblioteca`.
2. **Registrar Usuários**:
    - Administrador insere dados do usuário no sistema.
    - Sistema cria um objeto `Usuario` e adiciona à lista de usuários da `Biblioteca`.
3. **Registrar Empréstimos**:
    - Usuário solicita um livro.
    - Sistema verifica disponibilidade do livro.
    - Sistema cria um objeto `Emprestimo` e atualiza as listas de livros emprestados do `Usuario` e da `Biblioteca`.
4. **Registrar Devoluções**:
    - Usuário devolve um livro.
    - Sistema atualiza o status do `Emprestimo` e a lista de livros disponíveis.
5. **Gerar Relatórios**:
    - Administrador solicita relatórios específicos.
    - Sistema gera relatórios baseados nos dados dos objetos `Livro`, `Usuario` e `Emprestimo`.

Esse projeto envolve uma série de atividades que permitirão a você aplicar e consolidar conhecimentos em POO, abordando desde conceitos básicos até intermediários, proporcionando uma experiência completa e prática em desenvolvimento orientado a objetos.

