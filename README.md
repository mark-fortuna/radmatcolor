# radmatcolor
Recolor your radiant inputs for MCNP model renders.

## What is raidant?
Radiant is a thread-parallel utility for rendering images of MCNP geometry models in a 3-D perspective. The code generates raster images using the ray tracing capabilities of the Lava library that was developed with the ADVANTG software. The ray tracer supports all MCNP5 geometry features, including universes, lattices, and transformations. Radiant makes no approximations when constructing the raster image. The color of each pixel is determined directly from the output of the ray tracer. Images are written in the space-efficient Portable Network Graphics (PNG) format. Radiant can render images at arbitrary resolutions. Anti-aliasing can be applied to produce very high-quality images. Options are provided to control the color and visibility of each material defined in the problem. The geometry can be clipped by one or more arbitrarily oriented planes to expose internal details. The direction of the planar light source can also be altered to affect the shading of surfaces displayed in the image - [source](https://rsicc.ornl.gov/codes/ccc/ccc8/ccc-854-01.html).

[VisIt](https://visit-dav.github.io/visit-website/index.html) can be used to generate radiant inputs. VisIt assigns each material a color. Additionaly, different densities of the same material get assigned different colors. That's where radmatcolor comes in - it can recolor your radiant input according to the material.

## When to use?
Radmatcolor is usefull when specific colors should represent specific materials, or when more instances of the same material with different densities are present, but should be the same color.

It's a valuable tool when presenting MCNP model history. When new cells are added or older ones are modified, the renders can end up seemingly random colors.

## How to use?
Radmat color requires a color dictionary: a .csv (somma separated values) file in which each material is assigned a RGBA color. The first column of this file should be the material number, the other four columns for RGBA values. RGBA values for desired colors can be generated using tools such as [RGBA Color Picker](https://rgbacolorpicker.com).

### Running from terminal
Run in folder with files:

`python radmatcolor.py <input_name> <material_color_directory> [<output_name>]`


Example:

`python radmatcolor.py radiant.inp color_dict.csv radiant-recolored.inp`

## Further improvements
1. A way to change material visibility should be added. Maybe if in the first column a minus ("-") sign is present, that material's vsibility should be turned off (eg: -3, turns of material 3).
2. Different material densities could be represented with the same color, but different shades. Less dens cells could be a lighter shade.


