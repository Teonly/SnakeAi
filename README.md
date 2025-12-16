## Snake AI

Project Overview / Visão Geral (EN/PT)

EN:  
Snake AI is a personal Python project based on the classic Snake game, built using the Pygame library. The project includes a complete, playable version of Snake and an AI-controlled version developed on top of the same codebase. The main idea is to use the game as a testbed to experiment with logic, decision-making, and basic artificial intelligence techniques in a controlled and visual environment.

PT:  
Snake AI é um projeto pessoal em Python baseado no jogo clássico Snake, desenvolvido com a biblioteca Pygame. O projeto conta com uma versão totalmente jogável pelo usuário e uma versão controlada por inteligência artificial, construída sobre a mesma base de código. A ideia principal é usar o jogo como um ambiente de testes para experimentar lógica, tomada de decisão e conceitos básicos de IA de forma visual e controlada.

---

Key Features / Recursos Principais (EN/PT)

EN:
- Snake gameplay with grid-based movement
- Manual keyboard control and AI-controlled gameplay
- Snake growth, food spawning, and collision handling
- Score system and progressive difficulty
- Game Over state with restart or quit option
- Code structured to allow easy switching between human and AI control

PT:
- Jogabilidade do Snake com movimento em malha
- Controle manual por teclado e controle por IA
- Crescimento da cobra, geração de comida e colisões
- Sistema de pontuação e dificuldade progressiva
- Estado de Game Over com opção de reinício ou de sair
- Código estruturado para alternar facilmente entre jogador humano e IA

---

Game Logic / Lógica do Jogo (EN/PT)

EN:  
The game runs on a discrete grid. Direction changes are restricted to prevent instant reversal, keeping the classic Snake behavior. Collisions with walls or the snake’s own body end the game. The same core logic is shared by both the player-controlled and AI-controlled versions, ensuring consistent behavior.

PT:  
O jogo funciona sobre uma malha discreta. As mudanças de direção são restringidas para evitar inversões instantâneas, mantendo o comportamento clássico do Snake. Colisões com paredes ou com o próprio corpo encerram o jogo. A mesma lógica central é usada tanto na versão manual quanto na versão com IA, garantindo consistência.

---

Architecture / Arquitetura (EN/PT)

EN:
- Python as the main language
- Pygame handling rendering, input, and timing
- Central game loop with decoupled control logic
- AI module responsible only for decision-making
- Shared game state between player and AI

PT:
- Python como linguagem principal
- Pygame responsável por renderização, entrada e temporização
- Loop principal com lógica de controle desacoplada
- Módulo de IA responsável apenas pela tomada de decisão
- Estado do jogo compartilhado entre jogador e IA

---

Pygame Library / Biblioteca Pygame (EN/PT)

EN:  
Pygame is a Python library focused on game development and multimedia applications. It provides simple and direct access to graphics, keyboard input, timers, and sound, which makes it ideal for small 2D games and learning projects like this one.

Documentation and learning resources:  
https://www.pygame.org  
https://www.pygame.org/docs/

PT:  
Pygame é uma biblioteca Python voltada para desenvolvimento de jogos e aplicações multimídia. Ela oferece acesso simples a gráficos, teclado, temporizadores e som, o que a torna ideal para jogos 2D pequenos e projetos de aprendizado como este.

Documentação e materiais de estudo:  
https://www.pygame.org  
https://www.pygame.org/docs/

---

Technologies / Tecnologias (EN/PT)

EN:
- Python 3
- Pygame
- Basic AI decision logic
- Grid-based game mechanics

PT:
- Python 3
- Pygame
- Lógica básica de decisão para IA
- Mecânica de jogo baseada em malha

---

Status / Status Atual (EN/PT)

EN:  
The project is actively being developed. The core game is stable and complete, and the AI logic is implemented and continuously refined. The code intentionally stays close to the original implementation to preserve clarity and make experimentation easier.

PT:  
O projeto está em desenvolvimento ativo. O jogo base está estável e completo, e a lógica da IA está implementada e sendo refinada continuamente. O código foi mantido próximo da implementação original para facilitar a leitura e a experimentação.

---

Known Limitations / Limitações Conhecidas (EN/PT)

EN:
- AI behavior is intentionally simple and deterministic
- No advanced pathfinding or learning algorithms yet
- Focus is on logic clarity rather than performance optimization

PT:
- O comportamento da IA é propositalmente simples e determinístico
- Ainda não há algoritmos avançados de pathfinding ou aprendizado
- O foco está na clareza da lógica, não na otimização de performance

---

Future Plans / Planos Futuros (EN/PT)

EN:
- Improve AI decision-making strategies
- Experiment with heuristic-based and rule-based approaches
- Refactor code for better separation of concerns
- Add visualization tools for AI behavior and decisions

PT:
- Melhorar as estratégias de decisão da IA
- Experimentar abordagens heurísticas e baseadas em regras
- Refatorar o código para melhor separação de responsabilidades
- Adicionar visualizações para o comportamento e decisões da IA
