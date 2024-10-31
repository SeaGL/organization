# The original audio doesn’t perfectly loop, so trim it to a loopable interval
assets/loop.flac:
	ffmpeg \
	  -hide_banner \
	  -i 'assets/CC0 1.0 · Zane Little · Stumble Around.mp3' \
	  -t '139.370792' \
	  -sample_fmt 's16' \
	  -compression_level '12' \
	  'assets/loop.flac'

interstitial.mp4: assets/loop.flac
	./tasks/render
