upload_mp4s:=$(wildcard uploads/*.mp4)
preview_mp4s:=$(patsubst uploads/%.mp4,preview/%.preview.mp4,$(upload_mp4s))
preview_jpgs:=$(patsubst uploads/%.mp4,preview/%.jpg,$(upload_mp4s))

preview: preview/index.html $(preview_jpgs) $(preview_mp4s)

preview/index.html: seagl2023.ia.csv
	./tasks/generate-preview-index.py "$<" "$@"

preview/%.jpg: uploads/%.mp4
	ffmpeg \
	  -hide_banner \
	  -loglevel 'error' \
	  -i "$<" \
	  -frames:v '1' \
	  -update '1' \
	  "$@"

preview/%.preview.mp4: uploads/%.mp4
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
	  --branch '2023-internet-archive' \
	  'https://github.com/SeaGL/seagl.github.io.git' \
	  "$@"
	git -C "$@" sparse-checkout set --no-cone '_archive-sessions/2023'
	git -C "$@" checkout

seagl2023.ia.csv: resources/seagl-website
	./tasks/generate-uploads-spreadsheet.py "$</_archive-sessions/2023" > "$@"
