# Procedure

## I. Define Internet Archive identifiers

Records in the Internet Archive must be assigned a globally unique name called an [*identifier*][identifier], which is prominently used in URLs and filenames.

1. For each conference session, define an identifier fulfilling the following constraints:
   - Allowed characters:
     - First: `0`–`9`, `A`–`Z`, `a`–`z`
     - Rest: `0`–`9`, `A`–`Z`, `a`–`z`, `_`, `-`, `.`
   - Length:
     - Hard limit: 100 characters
     - Preferred: up to 80 characters
   - Begin with a name common to the conference.
   - Convey the session title, abbreviated as necessary.
   - Do not include the presenter’s name; a person’s name may change over time, but an identifier may not.
   - Prefer to represent spaces with `_`. Identifiers are occasionally displayed with `_` automatically replaced by ` `.
1. Stage the identifiers in SeaGL’s [archive] under a branch named `2024-internet-archive`.

## II. Prepare upload manifest

Dependencies:

- [Git]
- [Python] and dependencies of [`generate-uploads-manifest.py`](./tasks/generate-uploads-manifest.py)

Procedure:

1. Generate a [bulk upload manifest] from the session archive:

   ```bash
   make 'seagl2024.ia.csv'
   ```

## III. Isolate sessions

Dependencies:

- [LosslessCut](https://github.com/mifi/lossless-cut)

For each raw recording:

1. Open the raw recording in LosslessCut.
1. For each session contained, mark a segment:
   - Start the segment at the beginning of the introduction.
   - End the segment at the end of the presentation.
   - Label the segment with the Internet Archive identifier.
1. Export an edit decision list (EDL):
   - Choose File → Export Project → LosslessCut (CSV).
   - Name the EDL the same as the raw recording, but with the extension `.edl.csv`.
1. Export marked segments:
   - Export mode: Separate files
   - Output container format: MP4
   - Output folder: `01-assembled`
   - Output file name template: `${SEG_LABEL}${EXT}`
   - Smart cut: No
   - Keyframe cut: Yes
1. Upload the EDL to the shared storage alongside the raw recordings.

## IV. Normalize audio

Dependencies:

- [ffmpeg-normalize]

Procedure:

1. Normalize audio to [EBU R 128]:

   ```bash
   make '02-normalized'
   ```

## V. Review

Dependencies:

- [FFmpeg]
- [Python]

Procedure:

1. Generate a preview of the uploads:

   ```bash
   make '03-preview'
   ```

1. Review the upload manifest and preview.

## VI. Upload to the Internet Archive

Dependencies:

- [Internet Archive CLI]

Procedure:

1. Authenticate as [@seagl-video-team]:

   ```bash
   ia configure
   ```

1. Upload:

   ```bash
   ia upload --spreadsheet 'seagl2024.ia.csv'
   ```

## VII. Publish SeaGL archive

Merge the `2024-internet-archive` branch containing the staged [archive].

[@seagl-video-team]: https://archive.org/details/@seagl-video-team
[archive]: https://seagl.org/archive
[bulk upload manifest]: https://archive.org/developers/internetarchive/cli.html#bulk-uploading
[EBU R 128]: https://en.wikipedia.org/wiki/EBU_R_128
[FFmpeg]: https://www.ffmpeg.org/
[ffmpeg-normalize]: https://github.com/slhck/ffmpeg-normalize
[Git]: https://git-scm.com
[identifier]: https://archive.org/developers/metadata-schema/#archive-org-identifiers
[Internet Archive CLI]: https://archive.org/developers/internetarchive/cli.html
[Python]: https://www.python.org/
