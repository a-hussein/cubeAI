# backlog:
- testing
    - overall test coverage
    - `move_notation_converter()`
    - `cross_solver.treeify()`
    - `helpers.cross_solver()`
    - `helpers.compress_moves()`

- api implementation
    - fastapi + pydantic

- demo script
    - create a .py script that all you do is add moves and it does scramble -> visualize -> solution -> visualize
        - this is  equivalent to converting the `demo/many_scrambles.ipynb` notebook into a .py script and seeing the summary
        - turn this into a `make demo moves` command that creats a script that does above

- misc
    - docker container
    - run thousands of cubes and see if any solve in more than 8 moves
    - try/exceptions where needed

- refactoring
    - `enginer_solver.py`
    - instead of using indices of lists, should really be leveraging:
        - data classes
        - named tuples
    - treeify function
        - `if len(_all_moves) <= 6:` in `src/cube/cross_solver.py` as some solves taking 8 moves to solve
            - need to revisit what it really means to set this upper bound as it drastically impacts compute time

- visualizer
    - allow visualizer to read in cubestate, this would be amazing for reading in cubes im experiementing on as opposed to tracking the moves to get there
        - likely can not for now, so maybe create a metadata/history db of moves done to scramble and pass into prepend moves?

- random creative ideas to explore:
    - randomizing 20 move scrambles, storing reverse as solutions, and teaching RL model the solutions
    - throwing in a random move when solving cross (to account for accidental moves) and monitor how that affects solve lengths
    - implement an llm think-out-loud for the solver
    - an interactive hollow-knight-esq game where when you hit a a cube, it gets more sovled
        - go around solving unsolved cubes
        - sometimes you can even throw a t-perm at it as a shade sould attack haha


