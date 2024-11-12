# Procedure

## Upload to the Internet Archive

Dependencies:

- [FFmpeg]
- [Git]
- [Internet Archive CLI]
- [Make]
- [Python] and dependencies of [`generate-ia-csv.py`](./tasks/generate-ia-csv.py)
- videos at `uploads/${IDENTIFIER}.mp4`

Procedure:

1. Generate a [bulk upload spreadsheet] from the session archive:

   ```bash
   make 'seagl2023.ia.csv'
   ```

1. Generate a preview of the uploads:

   ```bash
   make 'preview'
   ```

1. Review the spreadsheet and preview for correctness.

1. Authenticate as [@seagl-video-team]:

   ```bash
   ia configure
   ```

1. Upload:

   ```bash
   ia upload --spreadsheet 'seagl2023.ia.csv'
   ```

[@seagl-video-team]: https://archive.org/details/@seagl-video-team
[bulk upload spreadsheet]: https://archive.org/developers/internetarchive/cli.html#bulk-uploading
[FFmpeg]: https://www.ffmpeg.org/
[Git]: https://git-scm.com
[Internet Archive CLI]: https://archive.org/developers/internetarchive/cli.html
[Make]: https://www.gnu.org/software/make/
[Python]: https://www.python.org/
