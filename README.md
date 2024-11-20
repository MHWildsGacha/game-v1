# MHWildsGacha Project

Este é um projeto de gacha de cartas baseado no jogo **Monster Hunter Wilds**. O projeto usa uma arquitetura de microservices, onde cada serviço é responsável por diferentes partes do jogo, como a geração de cartas, o sistema de gacha e a gestão de usuários.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:


- **docs/**: Fica a  documentação do projeto e arquitetura.

- **infra/**: Contém arquivos relacionados à infraestrutura (Ou vai ter no futuro)

- **scripts/**: Scripts para automatizar tarefas.

- **services/**: Contém os microservices principais

- **Makefile**: Arquivo para automação de tarefas comuns no projeto.

## Como Rodar o Projeto

make run

(Eu não sei como se anda uso makefile enquanto usando docker, mas tá ai)

### Usando Docker

```bash
docker compose up --build
```
