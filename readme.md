# CGOL Twitter

Tweeting via Conway's Game of Life

![Tweeting Zendegi #Reshto](img/screenshot.png)

## Description

This is a computer based on [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), which can print basic English letters or hard-coded pixels on its 32x32 display.

## Inspiration

This project is forked from the remarkable work of Nicolas Loizeau's [nicolasloizeau/scalable-gol-computer](https://github.com/nicolasloizeau/scalable-gol-computer). However, the original implementation supports Assembly-based programming only. With this project, I've added an Assembly generator to make it easier to display characters and other shapes.

## How to run

[Golly](https://golly.sourceforge.io/) is a free program for exploring Conway's Game of Life and many other types of cellular automata: [Download from Sourceforge](https://sourceforge.net/projects/golly/files/golly/golly-4.3/)

> [!CAUTION]  
> Game of life computer uses a LOT of Ram and CPU. In order to run the scripts on this repository, make sure you have at least 16GB of Ram and 4 CPU cores.

After running the program, click `File -> Run Script...` and select one of the scripts on this repo.

Also, Python 3 should be installed. *Note: On first run, Golly may not detect the system's Python installation. You will be prompted to manually specify the Python executable path.*

## Scripts

- `universal.py`: Universal Tweeter. Write your desired sentence and watch it being displayed. **Warning: Keep the sentence very short.** Longer sentences tend to use more than 256MB of Ram which is unavailable. Golly will throw a `file not found` error in that case.
- `draw.py`: Used to display hard-coded pixels. Useful when drawing a shape or non-English words. Again, use small designs to conserve memory.
- `preview.py`: Before attempting to run and display your drawing, you may want to preview the results on a 32x32 display. Run this script to generate an array of coordinates (for example `[(11, 9), (11, 12), (11, 13),...]`) and paste it in `draw.py`.
- `hello.py` and `hi.py`: Sample scripts to display hello and hi.

## License

Feel free to use, modify, and distribute this project as permitted under the MIT license terms.