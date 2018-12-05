# Imager

haha. get it?

# Usage

All of the scrapers are written for Python 3 and take no arguments. They
all use the same directory scheme and structure:

    <image size>
      ┗ <image host>-<image name>.png

Image size will either be small (length under 300px),
medium (under 600), large (under 2000), or huge (2000+).

Image host is the URL the image was taken from, e.g. imgur.

Image name is the URL the image was hosted at, e.g. 123456.

An example directory structure looks something like this:

    medium
      ┗ imgur-123456.png
