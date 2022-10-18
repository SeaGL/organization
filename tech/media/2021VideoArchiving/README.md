# SeaGL 2021 video archiving

## Resources

- Issue tracker: [SeaGL/tech](https://github.com/SeaGL/tech/issues)
- Internet Archive collection: [seagl](https://archive.org/details/seagl)
- Shared storage:
    - [StreamYard recordings](https://nextcloud.seagl.org/index.php/apps/files/?dir=/AmazonS3/seagl2021-raw-videos-from-streamyard)
- Tooling:
    - [LosslessCut](https://github.com/mifi/lossless-cut)
    - [AACGain](https://aacgain.altosdesign.com/)
    - [Internet Archive CLI](https://archive.org/services/docs/api/internetarchive/cli.html#bulk-uploading)

## Video preparation

### Trimming

1. Open the StreamYard recording in LosslessCut and mark edits:
    - Start the segment at the beginning of the introduction.
    - End the segment at the end of the presentation.
    - If the video contains multiple presentations, separate them into multiple segments.
1. Export an edit decision list (EDL):
    - Choose File → Export Project → LosslessCut (CSV).
    - Name the file the same as the video, but with the extension `.edl.csv`.
1. Upload the EDL to the shared storage.

### Volume normalization

If necessary:

1. Open the trimmed video in LosslessCut and mark audio segments.
1. Export the audio segments:
    - Tracks: audio only
    - Format: M4A
    - Cut mode: Normal cut
1. Run `aacgain -c -r <path…>` on all audio segments.
1. Create a merged audio track: Tools → Merge files
1. Add the merged audio track: Tracks → Include more tracks
1. Clear the audio segment marks: Edit → Segments → Clear all segments
1. Export the complete video:
    - Tracks: video and merged audio (not the original audio)
    - Format: MP4

### Status

- Recording: `Fri-09_00-SeaGL, Elana Hashman, Marie Nordin - Welcome to SeaGL 2021 and Keynotes.mp4`
    - Notes:
        - Seeking in the StreamYard file sometimes glitches around 1:30–2:00
        - Introduction was interrupted and restarted
        - Low volume on Marie Nordin’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Fri-10_10-Athan Spathas, Aaron Wolf, and Wm Salt Hale-FLOSS daily — but FLO all the time.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-10_10-Bri Hatch-SSH from your DevOps CI_CD securely.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-10_10-Dawn E. Collett-The Stories We Don't Tell.mp4`
    - Notes:
        - Contains burned-in captions during presentation
        - Low volume on Dawn E. Collett’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Fri-10_45-der.hans-Intro to jq_ grep for JSON.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-10_45-Mark Wong-PostgreSQL Participation in Google's Summer of Code.mp4`
    - Notes:
        - Low volume on Mark Wong’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Fri-10_45-Molly de Blanc-Predictive Modeling and Privacy.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-11_30-Lightning Talks.mp4`
    - Notes:
        - Low volume on Kaylea Champion’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Fri-13_15-davidmstokes-JSON Document Validation in MySQL 8.0.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-13_15-der.hans-Introduction to Nextcloud.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-13_15-Ski-Lessons Learned from a Ransomware Attack.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-14_00-Deb Nicholson-Responding Thoughtfully to a Crisis.mp4`
    - Notes:
        - AV problems at the beginning. I’ve preserved some of it since it’s relevant to the presentation.
        - The EDL contains multiple segments that should be merged during export.
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-14_00-Elior Sterling-Developing on Nextcloud.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-15_30-Bri Hatch-Good Shell Patterns.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-15_30-Georg Link and Lara-Building and Supporting Open Source Communities Through Metrics.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Fri-15_30-Shauna Gordon-McKeon-Software Tools for Collective Self-Governance.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-09_30-Christine Lemmer-Webber and Dr. Morgan Lemmer-Webber, Cory Doctorow - Keynotes!.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-10_00-davidmstokes-Understanding the MySQL Authentication Process.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-10_00-Dawn E. Collett-Free Security for Open-Source Projects.mp4`
    - Notes:
        - Contains burned-in captions during presentation
        - Low volume on Dawn E. Collett’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Sat-10_00-Shauna Gordon-McKeon-Know Your Rights as a Tech Worker.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-10_45-Aeva Black-Walking The Cultural Tightrope.mp4`
    - Notes:
        - Low volume on Aeva Black’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Sat-10_45-Francois Caen and Troy Perkins-Building cloud networks_ Terraform or Ansible_.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-10_45-Tobie Langel-Does open source need its own Priority of Constituencies_.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-11_30-Aeva Black-Computing Confidentially in the Clouds.mp4`
    - Notes:
        - Low volume on Aeva Black’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Sat-11_30-Dmitry Dolgov-Sounds of Open Source archaeology_ processing sound with sox.mp4` and `Dmitry rescheduled.mp4`
    - Notes:
        - First recording was aborted partway though due to AV issues
        - Both recordings have out of sync audio
        - Neither recording has an introduction or Q&A

- Recording: `Sat-13_15-Brian Callahan-Stories from reviving and extending a university's information security pro.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-13_15-jberkus-Open Source Governance_ Six Types and Three Models.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-13_15-Thierry Bultel-Cross debugging on Linux _ A history, current state of the art and  coming .mp4`
    - Notes:
        - Low volume on Thierry Bultel-Cross’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Sat-14_00-Jim Hall-Open Source Business Practices.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-14_00-Richard Littauer-Birds by Starlight_ Tracking Nocturnal Flight Calls Using Open Source Sof.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-14_00-Vagrant Cascadian-Debugging Reproducible Builds One Day at a Time.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-15_30-Ben Cotton-Your bug tracker and you.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-15_30-Katie McLaughlin-Expressive Security.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

- Recording: `Sat-15_30-Stephen Michel-Technically Biased_ Taking Free Software's Niche Appeal Mainstream.mp4`
    - [x] EDL created
    - [x] trimmed video exported
    - [ ] volume normalized

- Recording: `Sat-16_30-Cory Doctorow-Seize the Means of Computation.mp4`
    - Notes:
        - Low volume on Cory Doctorow’s audio
    - [x] EDL created
    - [x] trimmed video exported
    - [x] volume normalized

## Add title screens

- [x] Prepend [title screens](https://github.com/SeaGL/tech/issues/28) to exported videos: [`generate-titles`](./generate-titles)

## Upload to Internet Archive

- [x] Prepare CSV of bulk upload metadata: [`seagl2021.ia.csv`](./seagl2021.ia.csv)
- [x] Bulk upload as [@seagl-video-team](https://archive.org/details/@seagl-video-team): `ia upload --spreadsheet 'seagl2021.ia.csv'`
