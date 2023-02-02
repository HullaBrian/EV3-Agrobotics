# Pathfinding
## Creating a New Path
### Creating the File
- Under the `paths` directory, create a .txt file with the exact name of the challenge mentioned in the files of the `challenges/instructions` directory. If you do not name this file correctly, then it will not load properly into the program.
- If creating a test path, then create a .txt file in the `paths/testing` directory.

### Writing the Path
The starting line of each path file may (it does not have to) start with an initial angle specified. If there is not an initial angle specified in the file, then the program will assume it to be 0.

Each of the following line(s) will have the coordinate of the next tile separated by one space.

Below are two examples:

```
90
29 29
30 27
28 34
```
```
29 29
30 27
28 34
```
