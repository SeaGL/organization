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
   - Choose File → Export Project → Time in seconds (CSV).
   - Name the EDL the same as the raw recording, but with the extension `.edl.csv`.
1. Export marked segments:
   - Export mode: Separate files
   - Output container format: MP4
   - Output folder: `01-assembled`
   - Output file name template: `${SEG_LABEL}${EXT}`
   - Smart cut: No
   - Keyframe cut: Yes
1. Upload the EDL to the shared storage alongside the raw recordings.

Checklist:

- Segment:
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-08 10-34-49.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-08 11-32-16.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-08 14-02-39.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-08 14-29-11.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-08 16-30-15.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-08 17-00-44.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-09 11-42-34.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-09 12-00-57.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-09 12-58-11.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-09 13-27-38.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/332/2024-11-09 14-20-01.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-08 10-36-09.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-08 11-31-19.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-08 14-01-16.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-08 14-29-13.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-08 14-31-39.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-09 08-45-58.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-09 08-57-53.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-09 09-58-52.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-09 10-29-05.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-09 11-00-56.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-09 13-34-11.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/334/2024-11-09 13-57-45.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-08 14-49-20.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-08 14-52-04.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-08 17-06-37.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-08 17-30-23.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-08 19-31-54.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-09 08-54-08.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-09 09-59-19.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-09 10-29-16.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/340/2024-11-09 10-54-59.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum/2024-11-09 16-08-28.mkv`
  - [x] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum/PRIVATE/AVCHD/BDMV/STREAM/00000.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum/PRIVATE/AVCHD/BDMV/STREAM/00001.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum/PRIVATE/AVCHD/BDMV/STREAM/00002.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum/PRIVATE/AVCHD/BDMV/STREAM/00003.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum/PRIVATE/AVCHD/BDMV/STREAM/00004.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum/PRIVATE/AVCHD/BDMV/STREAM/00005.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder/AVCHD/BDMV/STREAM/00000.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder/AVCHD/BDMV/STREAM/00001.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder/AVCHD/BDMV/STREAM/00002.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder/AVCHD/BDMV/STREAM/00003.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder/AVCHD/BDMV/STREAM/00004.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder/AVCHD/BDMV/STREAM/00005.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00000.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00001.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00002.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00003.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00004.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00005.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00006.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00007.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00008.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00009.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_2/AVCHD/BDMV/STREAM/00010.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00000.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00001.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00002.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00003.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00004.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00005.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00006.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00007.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00008.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00009.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00010.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00011.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00012.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00013.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00014.MTS`
  - [ ] `s3://cloud.seagl.org/seagl2024-raw-videos/Lyceum_camcorder_3/AVCHD/BDMV/STREAM/00015.MTS`
- Export:
  - [ ] `01-assembled/SeaGL2024-A_talk_that_begins_with_an_obvious_statement_about_Open_Source.mp4`
  - [x] `01-assembled/SeaGL2024-According_to_my_research.mp4`
  - [x] `01-assembled/SeaGL2024-AI_Ethics_Through_The_Lens_of_Animism.mp4`
  - [ ] `01-assembled/SeaGL2024-Alpine_on_LoongArch.mp4`
  - [x] `01-assembled/SeaGL2024-Apache_SeaTunnel.mp4`
  - [x] `01-assembled/SeaGL2024-Bash_Variable_Expansion.mp4`
  - [x] `01-assembled/SeaGL2024-Building_my_first_open_source_software_with_AI.mp4`
  - [ ] `01-assembled/SeaGL2024-Can_LLMs_double_the_number_of_open_source_developers.mp4`
  - [x] `01-assembled/SeaGL2024-Code_by_Mail.mp4`
  - [x] `01-assembled/SeaGL2024-Coreboot.mp4`
  - [x] `01-assembled/SeaGL2024-Culling_Seagull_Records.mp4`
  - [x] `01-assembled/SeaGL2024-Digital_Whiteboarding_for_Developers.mp4`
  - [x] `01-assembled/SeaGL2024-FediTest.mp4`
  - [ ] `01-assembled/SeaGL2024-FLO_Conscience.mp4`
  - [x] `01-assembled/SeaGL2024-From_bytes_to_bits.mp4`
  - [ ] `01-assembled/SeaGL2024-From_Terrafied_to_Terrafirm.mp4`
  - [ ] `01-assembled/SeaGL2024-geoCML.mp4`
  - [ ] `01-assembled/SeaGL2024-GNU_Linux_Loves_All.mp4`
  - [x] `01-assembled/SeaGL2024-Hands_On_Tensegrity.mp4`
  - [x] `01-assembled/SeaGL2024-How_do_you_share_your_Open_Source_Hardware_project.mp4`
  - [x] `01-assembled/SeaGL2024-How_to_Solve_Brand_New_Problems.mp4`
  - [x] `01-assembled/SeaGL2024-Introduction_to_postmarketOS.mp4`
  - [x] `01-assembled/SeaGL2024-Its_About_Time_to_talk_to_your_loved_ones_about_personal_data_management.mp4`
  - [ ] `01-assembled/SeaGL2024-MicroMirror_CDN.mp4`
  - [ ] `01-assembled/SeaGL2024-Morias_Race_Libre_Movie_made_with_Libre_Software.mp4`
  - [x] `01-assembled/SeaGL2024-Mosh_and_tmux.mp4`
  - [x] `01-assembled/SeaGL2024-My_Pi_in_the_Sky.mp4`
  - [x] `01-assembled/SeaGL2024-NixOS_is_terrible_and_also_I_can_never_go_back.mp4`
  - [ ] `01-assembled/SeaGL2024-Nurturing_the_Next_Generation_of_Open_Source_Contributors.mp4`
  - [x] `01-assembled/SeaGL2024-Open_Source_Governance_By_Example.mp4`
  - [x] `01-assembled/SeaGL2024-Open_Source_Hygiene.mp4`
  - [ ] `01-assembled/SeaGL2024-Presentation_Roulette.mp4`
  - [x] `01-assembled/SeaGL2024-Steadfast_Self_Hosting_Workshop.mp4`
  - [ ] `01-assembled/SeaGL2024-Temporal_Data.mp4`
  - [x] `01-assembled/SeaGL2024-The_Business_Case_for_Open_Source_Software_for_IT_Leadership_Skeptics.mp4`
  - [x] `01-assembled/SeaGL2024-The_Cathedral_and_the_Bizarre.mp4`
  - [x] `01-assembled/SeaGL2024-The_free_software_movement.mp4`
  - [x] `01-assembled/SeaGL2024-Troubleshooting_home_LANs_using_Linux_Network_Tools.mp4`
  - [x] `01-assembled/SeaGL2024-Two_Ways_to_Trustworthy.mp4`
  - [x] `01-assembled/SeaGL2024-We_Are_All_That_We_Have.mp4`
  - [ ] `01-assembled/SeaGL2024-Who_chooses_the_requirements.mp4`
  - [ ] `01-assembled/SeaGL2024-Will_your_open_source_project_run_on.mp4`
  - [ ] `01-assembled/SeaGL2024-Zero_instrumentation_observability_based_on_eBPF.mp4`

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
