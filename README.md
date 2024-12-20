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

#### Todos

- [x] Sortear o gacha
- [ ] Interface visual
- [ ] Sistema de usuários
- [ ] Banco de dados


#### Exemplos de requisições

Para listar todas as cartas:

    localhost:8000/cards

        Resposta:

            [{
                "card_number": 1,
                "id": 1,
                "name": "Rathalos"
            },
            {"card_number": 2,
            "id": 2,
            "name": "Aiden"}
            ]


Para listar carta especifica: 
    
    localhost:8000/cards/{id} #1 por exemplo
    Retorno:
            [{
                "card_number": 1,
                "id": 1
                ...
            }]

Para listar a carta sorteada:

    localhost:8000/cards/gacha

    Retorno:
        [{
            "card_number": 4,
            "card_id": 4,
            "name": "Tigrex",
            "card-type": "Monster",
            "rarity": "SSR",}]


Se a carta não existir:

    localhost:8000/cards/{id} #99 por exemplo
        Resposta:

            {
    "detail": "Card not found"
            }
