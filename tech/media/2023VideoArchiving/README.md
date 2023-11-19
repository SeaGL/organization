# Procedure

## Upload to the Internet Archive

Dependencies:

- [Internet Archive CLI]
- Python dependencies of [`generate-ia-csv.py`](./generate-ia-csv.py)
- Source of the session archive [containing Internet Archive identifiers](https://github.com/SeaGL/seagl.github.io/pull/418)

Procedure:

1. Generate a [bulk upload spreadsheet] from the session archive:

   ```bash
   ./generate-ia-csv.py "$SEAGL_WEBSITE/_archive-sessions/2023" > 'seagl2023.ia.csv'
   ```

1. Review the spreadsheet for correctness.

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
[Internet Archive CLI]: https://archive.org/services/docs/api/internetarchive/cli.html
