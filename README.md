# Rubik's Cube Cross Solver

## Overview
I am working on developing a Rubik's Cube solver that solves the cross portion of the CFOP method in an intuitive manner in 8 moves or less. I used to compete in tournaments when I was younger (my WCA profile can be found [here](https://www.worldcubeassociation.org/persons/2013HUSS01)).

I solve the rubik's cube using the CFOP method (Cross / F2L / OLL / PLL) and average ~15 seconds. As mentioned, this project focuses on the "cross" portion which is less "algorithmic" than other parts of learning the CFOP method, and more intuitive in nature.

## Major Features
- Go through this [demo notebook](demo/interact_with_cube.ipynb) for an interactive walk through of the important cube features such as:
    - scrambling a cube
    - cli-implemtnation for visualizing a cube
    - function-based implemtnation for visualizing a cube
    - generating a scrmable for the cross portion of the cube

### Sample Scramble
Sample Scramble: 

`F2 L D2 L' R2 U2 B2 R' U2 F2 R' D B2 R F2 B' L F U D'`
<video src="assets/scramble.mov" autoplay loop muted playsinline></video>


### Sample Solution


## Developer Notes
- always run `make clean` before pushing any code

- this project uses the Twizzle cube editor for visualization, which is powered by
[cubing.js](https://github.com/cubing/cubing.js), an open-source project

## Backlog
- A list of outstanding backlog items can be found [here](backlog.md)



