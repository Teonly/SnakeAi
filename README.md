# Snake AI

## Project Overview / Visão Geral (EN/PT)

**EN:**  
Snake AI is a personal Python project based on the classic Snake game, developed using the Pygame library. The project includes a fully playable human-controlled version and an AI-controlled version built on top of the same codebase.  
The main purpose is to use the game as a test environment to experiment with logic, decision-making, and basic artificial intelligence strategies in a simple, visual, and controlled scenario.

**PT:**  
Snake AI é um projeto pessoal em Python baseado no jogo clássico Snake, desenvolvido com a biblioteca Pygame. O projeto inclui uma versão totalmente jogável pelo usuário e uma versão controlada por inteligência artificial, ambas construídas sobre a mesma base de código.  
O objetivo principal é usar o jogo como um ambiente de testes para experimentar lógica, tomada de decisão e conceitos básicos de inteligência artificial de forma simples, visual e controlada.

---

## Key Features / Recursos Principais (EN/PT)

**EN:**
- Classic Snake gameplay with grid-based movement  
- Manual keyboard control and AI-controlled gameplay  
- Snake growth, food spawning, and collision handling  
- Score system with progressive difficulty  
- Game Over state with restart or quit options  
- Code structured to easily switch between human and AI control  

**PT:**
- Jogabilidade clássica do Snake com movimento baseado em malha  
- Controle manual por teclado e controle por IA  
- Crescimento da cobra, geração de comida e tratamento de colisões  
- Sistema de pontuação com dificuldade progressiva  
- Estado de Game Over com opção de reiniciar ou sair  
- Código estruturado para alternar facilmente entre controle humano e IA  

---

## Game Logic / Lógica do Jogo (EN/PT)

**EN:**  
The game runs on a  grid. Direction changes are restricted to prevent instant reversal, preserving classic Snake behavior.  
Collisions with walls or with the snake’s own body result in a Game Over. Both the player-controlled and AI-controlled versions share the same core game logic, ensuring consistent mechanics and behavior.

**PT:**  
O jogo funciona sobre uma malha. As mudanças de direção são limitadas para evitar inversões instantâneas, mantendo o comportamento clássico do Snake.  
Colisões com as paredes ou com o próprio corpo encerram o jogo. Tanto a versão controlada pelo jogador quanto a versão com IA compartilham a mesma lógica central, garantindo consistência nas mecânicas.

---

## Architecture / Arquitetura (EN/PT)

**EN:**
- Python as the main programming language  
- Pygame handling rendering, input, and timing  
- Central game loop with decoupled control logic  
- AI logic isolated and responsible only for decision-making  
- Shared game state between human and AI modes  

**PT:**
- Python como linguagem principal  
- Pygame responsável pela renderização, entrada de dados e temporização  
- Loop principal do jogo com lógica de controle desacoplada  
- Lógica da IA isolada, responsável apenas pela tomada de decisão  
- Estado do jogo compartilhado entre os modos humano e IA  

---

## Pygame Library / Biblioteca Pygame (EN/PT)

**EN:**  
Pygame is a Python library focused on game development and multimedia applications. It provides straightforward access to graphics, keyboard input, timers, and sound, making it well-suited for small 2D games and learning-focused projects like this one.

**PT:**  
Pygame é uma biblioteca Python voltada para o desenvolvimento de jogos e aplicações multimídia. Ela oferece acesso simples a gráficos, entrada de teclado, temporizadores e som, sendo ideal para jogos 2D pequenos e projetos com foco em aprendizado como este.


Documentation and learning resources/Documentação e materiais de estudo:    

- https://www.pygame.org  
- https://www.pygame.org/docs/  



---

## Technologies / Tecnologias (EN/PT)

**EN:**
- Python 3  
- Pygame  
- Basic AI decision-making logic  
- Grid-based game mechanics  

**PT:**
- Python 3  
- Pygame  
- Lógica básica de decisão para IA  
- Mecânicas de jogo baseadas em malha  

---

## Status / Status Atual (EN/PT)

**EN:**  
The project is under active development. The core game is stable and fully functional, while the AI logic is implemented and continuously refined. The code intentionally remains close to the original implementation to preserve clarity and make experimentation easier.

**PT:**  
O projeto está em desenvolvimento ativo. O jogo base está estável e completo, enquanto a lógica da IA já está implementada e sendo refinada continuamente. O código foi mantido próximo da implementação original para facilitar a leitura, o entendimento e a experimentação.

---

## Known Limitations / Limitações Conhecidas (EN/PT)

**EN:**
- AI behavior is intentionally simple and deterministic  
- No advanced pathfinding or learning algorithms implemented yet  
- Focus is on logic clarity rather than performance optimization  

**PT:**
- O comportamento da IA é propositalmente simples e determinístico  
- Ainda não há algoritmos avançados de pathfinding ou aprendizado  
- O foco está na clareza da lógica, não na otimização de desempenho  

---

## Future Plans / Planos Futuros (EN/PT)

**EN:**
- Improve AI decision-making strategies  
- Experiment with heuristic-based and rule-based approaches  
- Refactor code for better separation of concerns  
- Add visualization tools for AI behavior and decision processes  

**PT:**
- Melhorar as estratégias de tomada de decisão da IA  
- Experimentar abordagens heurísticas e baseadas em regras  
- Refatorar o código para melhor separação de responsabilidades  
- Adicionar visualizações para o comportamento e as decisões da IA  
