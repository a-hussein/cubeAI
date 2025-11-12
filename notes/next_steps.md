# next steps:
~~- fix all failing tests due to changes in folder structure~~
- add make file
    - formatter
    - linter
    - test
- scripts are way too long, need to condense and make it more oop
- revisit tree alg
- revisit the compression algo
- front end visualizer
- once implemented, create an easy to use demo file showing cross solves
- connect to some type of UI that alreadt exists via API to visualize
- pydantic / dataclass
- creative ideas to explore:
    - randomizing 20 move scrambles, storing reverse as solutions, and teaching RL model the solutions
    - throwing in a random move when solving cross (to account for accidental moves) and monitor how that affects solve lengths
    - include an llm think-out-loud for the solver
    - an interactive hollow knight game-like where when you hit a a cube, it gets more sovled. and you go around solving unsolved cubes. sometimes you can even throw a t-perm at it haha