assembled_mp4s:=$(wildcard 01-assembled/*.mp4)
normalized_mp4s:=$(patsubst 01-assembled/%.mp4,02-normalized/%.mp4,$(assembled_mp4s))
preview_mp4s:=$(patsubst 01-assembled/%.mp4,03-preview/%.preview.mp4,$(assembled_mp4s))
preview_jpgs:=$(patsubst 01-assembled/%.mp4,03-preview/%.jpg,$(assembled_mp4s))

.DEFAULT_GOAL := 03-preview

02-normalized: $(normalized_mp4s)

02-normalized/%.mp4: 01-assembled/%.mp4
	ffmpeg-normalize \
	  --verbose \
	  --output "$@" \
	  --audio-codec 'aac' \
	  --sample-rate '48000' \
	  --extension 'mp4' \
	  "$<"

03-preview: 03-preview/index.html $(preview_jpgs) $(preview_mp4s)

03-preview/index.html: seagl2024.ia.csv
	./tasks/generate-preview-index.py '02-normalized' "$<" "$@"

03-preview/%.jpg: 02-normalized/%.mp4
	ffmpeg \
	  -hide_banner \
	  -loglevel 'error' \
	  -i "$<" \
	  -frames:v '1' \
	  -update '1' \
	  "$@"

03-preview/%.preview.mp4: 02-normalized/%.mp4
	env SVT_LOG='1' \
	  ffmpeg \
	    -hide_banner \
	    -loglevel 'warning' \
	    -i "$<" \
	    -vf 'scale=640x360,fps=fps=15' \
	    -c:v 'libsvtav1' \
	    -g '120' \
	    -qp '60' \
	    -preset '10' \
	    -ac '1' \
	    -c:a 'libopus' \
	    -b:a '24k' \
	    "$@"

resources/seagl-website:
	git clone \
	  --no-checkout \
	  --depth '1' \
	  --filter 'tree:0' \
	  --branch '2024-internet-archive' \
	  'https://github.com/SeaGL/seagl.github.io.git' \
	  "$@"
	git -C "$@" sparse-checkout set --no-cone '_archive-sessions/2024'
	git -C "$@" checkout

seagl2024.ia.csv: resources/seagl-website
	./tasks/generate-uploads-spreadsheet.py \
	  "$</_archive-sessions/2024" \
	  '02-normalized' \
	> "$@"
