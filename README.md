# squaregrid
Wrapper of matplotlib's GridSpec module which allows for the easy spawning of several different of configurations of square plots of varying sizes.

## Basic Usage 
SquareGrid has a few plotting styles that you can access. These are 
- TriGrid: One primary panel with two minor panels. Minor panels can be located to the left, top, bottom, or right. 
- QuadGrid: One primary panel with three minor panels (same positioning arguments as TriGrid)
- QuintGrid: One primary panel with four minor panels. Can be placed left, right, or center. 
- LGrid: One primary plot with 5 minor panels, arranged in an "L" shape around the primary. (Position primary in upper left/right, bottom left/right)
- UGrid: One primary with 7 minor panels, arranged in a U shape or n shape around the primary. 

## Initialization 

After importing `squaregrid.SquareGrid`, you can initilize a plot by calling the class and specififying a figure width:
```
sg = SquareGrid(figure_width=5)
```
Because of this module's obsession with square panels, the figure width also constrains the figure height, which is automatically calculated in order to maintain square panels. 

Next, you can run any of the methods above to generate your figure and axes: 
```
fig, axes = sg.QuintGrid(primary='middle')
```
The figure and axis object returned by this method are free for you to interact with as you normally wood -- plotting them immediately will show the orientation of the subplots with respect to each other. The `SquareGrid` object also retains a copy of the empty figure axes which can be useful. 


