# next steps:
~~- fix all failing tests due to changes in folder structure~~
- add make file
    ~~- formatter~~
    ~~- linter~~
    ~~- test~~

- files contain more than one major purporse, need to seperate out
    ~~- rename files approppriately~~
    ~~- add placeholder files~~
    ~~- move helper functions to cube module~~
    ~~- `cube_representation.py` should just represent cube state and basic moves, no solving~~
    ~~- we should then incorporate a `cross_solver.py` which uses Cube to solve cross~~
    ~~- and then make a`engine_solver.py` which contains the TreeNode~~ 

- make this project more OOP
    ~~- currently there is one class in cube_representation, make it multiple classes~~
    - potentially move these classes to different scripts
    - there is a lot of reused code in these scripts, make functions and reuse instead

- after restructuring files, align solvers work well and review codebase
- make files more oop based

- implement the BFS solver properly (treeify)
- revisit the compression algo
- front end visualizer (refer to ui_later notes)
- api
    - fastapi + pydantic
- docker container
- clean demo scripts
- dataclass

# later:
~~- set up git shortcuts~~
- metrics.py that evaluates functions (avg move count, etc)
- Need a good way to hash cube states to avoid revisiting
- creative ideas to explore:
    - randomizing 20 move scrambles, storing reverse as solutions, and teaching RL model the solutions
    - throwing in a random move when solving cross (to account for accidental moves) and monitor how that affects solve lengths
    - include an llm think-out-loud for the solver
    - an interactive hollow-knight-like game where when you hit a a cube, it gets more sovled. and you go around solving unsolved cubes. sometimes you can even throw a t-perm at it haha
- go down rabbit hole of git tab completion
    - will need to look into brew and zsh etc

