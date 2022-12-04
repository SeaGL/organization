#!/usr/bin/env bash
set -Eeuo pipefail

mkdir -p 'export'

for input in cuts/*.mp4; do
  output="export/${input##*/}"

  mp4="title-screens/${input##*/}"
  png="${mp4%.mp4}.png"

  echo "Render $output"

  trap 'rm -f "$mp4"' EXIT
  ffmpeg -hide_banner -loglevel warning -y \
    -f 'lavfi' -i 'anullsrc' \
    -framerate '30' -loop '1' -i "$png" \
    -c:v 'libx264' \
    -c:a 'aac' \
    -t '3' \
    -pix_fmt 'yuv420p' \
    -video_track_timescale '90000' \
    "$mp4"

  ffmpeg -hide_banner -loglevel warning -y \
    -safe '0' \
    -f 'concat' \
    -i <( printf 'file %s\nfile %s' "$(readlink -f "$mp4")" "$(readlink -f "$input")" ) \
    -c 'copy' \
    -movflags '+faststart' \
    "$output"
done
