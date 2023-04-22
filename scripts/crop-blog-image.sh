#/bin/env bash

# crop-blog-image.sh -- crop image to right size for blog
# INSTALL
#  brew install graphicsmagick

set -euo pipefail  # bash strict mode

image=$1
gm convert "$image" -crop 1200x630+0+0 "$image"-crop.png