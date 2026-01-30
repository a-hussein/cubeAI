# Rubik's Cube Cross Solver

## Overview
I am working on developing a Rubik's Cube solver that solves the cross portion of the CFOP method in an intuitive manner in 8 moves or less. I used to compete in tournaments when I was younger (my WCA profile can be found [here](https://www.worldcubeassociation.org/persons/2013HUSS01)).

I solve the rubik's cube using the CFOP method (Cross / F2L / OLL / PLL) and average ~15 seconds. As mentioned, this project focuses on the "cross" portion which is practice is "algorithmic" than other parts of learning the CFOP method, and more intuitive in nature. However, when creating the solver via code, was actually quite algorithmic when translating processed into modular steps.

## Major Features
- Go through this [demo notebook](demo/interact_with_cube.ipynb) for an interactive walkthrough of the most important cube features such as:
    - cube object
    - cube state
    - scrambling a cube
    - visualizing a cube
    - generating a cross solution
- One can also use the following `make` command to run a demo on a specific scramble, eg:
    - `make demo moves="R U F"`

### Sample Scramble
`F2 L D2 L' R2 U2 B2 R' U2 F2 R' D B2 R F2 B' L F U D'`
<video src="https://github.com/user-attachments/assets/d570fe33-23ff-42eb-afc6-cc4a635ec0ca" autoplay loop muted playsinline></video>

### Sample Solution (notice the white-cross is now solved)
`F U2 B2 R B Dp Bp`
<video src="https://github.com/user-attachments/assets/7a423272-eec1-4390-912a-fc489f709142" autoplay loop muted playsinline></video>


## Developer Notes
- always run `make clean` before pushing any code
- this project uses the Twizzle cube editor for visualization, which is powered by
[cubing.js](https://github.com/cubing/cubing.js), an open-source project

## Backlog
- A list of outstanding backlog items can be found [here](backlog.md)

## Run with Docker
"build once, run anywhere”

- After cloning the repo and entering into the repo root, run the below:
    - Build the Docker Image: `docker build -t cubeai:dev .`
    - Run Container (and delete): `docker run --rm -it cubeai:dev`
    - Run Custom Scrambles: `docker run --rm -it cubeai:dev make demo moves="<moves>"`
        - Insert your moves where it says `<moves>`, for example: `docker run --rm -it cubeai:dev make demo moves="R U Fp"`
