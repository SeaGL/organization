Making of 2018 SeaGL Keynote Videos
===================================

This document provides notes on the preparation, equipment, recording,
and postproduction process used to make the videos of the SeaGL 2018
Keynotes linked in this [seagl.org
blog](https://seagl.org/news/2019/01/21/Keynote_Videos_Available.html).

Some of the details are specific to the [Broadway Performance
Hall](https://www.openstreetmap.org/#map=19/47.61567/-122.32185) at
[Seattle Central College](https://seattlecentral.edu/) where the
keynotes were delivered, but it should provide a starting point for
future improvements filming there or at other venues on a close to zero
budget.

Equipment
---------

Arrange to borrow or rent the following:

-   Camcorder similar to the Canon HDVCAM HRF32 used for the linked 2018
    videos.

-   A sturdy tripod.

-   Headphones / earbuds for use with camcorder.

-   [Shure A96F](https://www.shure.com/en-US/products/accessories/a96f)
    Camcorder Interface (SeaGL owns one of these). Note that the
    camcorder must have a microphone input jack.

-   Optional second camcorder / tripod.

-   Optional still camera / high quality phone cameras.

-   Optional tape (to block off seating and cross traffic in front of
    camera).

Arrangements
------------

Arrange ahead with SeaGL's Seattle Central College contact to have a
microphone level audio cable with a male XLR jack dropped from sound
board to the back row of the theater. The Shure A96F will plug into this
and the microphone jack in the camcorder and provide excellent sound
quality for the video. They can also supply 110V AC power for the
camcorder.

Arrange to enter the hall 1 hour before the 1st day's keynote start to
setting up and do a sound check (theater staff will be doing same) and
adjust camera for audio, framing, focus, and exposure. 30 minutes should
be enough for the second day.

If you are unfamiliar with the camcorder, download a manual and try it
out ahead of time if possible. Look for how to monitor / adjust the
audio, set focus and exposure, etc. The sound engineer will be able to
adjust the output from microphone cable they provide to a compatible
level for the camcorder.

Setup and Recording
-------------------

-   Set camera (on tripod and plugged into AC for backup) for manual
    focus and exposure for best results. The 2018 videos were shot from
    the back row. It will be easier / faster to transfer the recorded
    video to a computer for postprocessing if you record to the
    removable SD card rather than the camera's built in memory.

-   Zoom in so both screen and speaker are in frame.

-   Focus on screen (speaker will be somewhat out of focus due to low
    light / depth of field).

-   During sound checks, do a quick recording and check for audio and
    video quality (record on the removable flash and preview on laptop
    if possible).

-   Start recording before first keynote starts and let it roll between
    speakers to avoid missing anything.

-   On both camcorders we used (2017 and 2018), the cameras chopped the
    video into multiple \~30 minute clips which were joined and edited
    in postproduction. Don't try and do this in camera.

-   For second camera, consider either a wider view (worked well for the
    video we used for the Community Builder Award), or if you want to
    get fancy in postproduction, a closer view of the speaker with
    exposure adjusted for them vs. the slides (probably can't get both
    right in one shot).

Postproduction
--------------

Get current year's blank conference slide template at 1920x1080 pixels
(to match camcorder's resolution), and download the matching fonts.

Use an editor such as [GIMP](https://www.gimp.org/), to produce title
frames for each video.

Use a video editor (such as the video editor in
[Blender](https://www.blender.org/)) to splice together the clips from
the camera into separate keynotes and prepend the title frames.

A second camcorder and still camera shots were used postproduction for
the Community Builder Award. Note that although the house audio was
reasonable quality on the second camera, the audio from the primary
camera (hooked to the sound board output) was superior and used for that
video.

If the video editor doesn't produce video in an open source format, use
[ffmpeg to
convert](https://superuser.com/questions/1096841/how-do-i-convert-mp4-to-ogv-while-still-retaining-the-same-quality-using-ffmpeg)
so you can also supply an open source version. After some
experimentation the following command line was used with ffmpeg version
2.8.11 on Ubuntu:
```
ffmpeg -i /media/SeaGL-processed/keynote1.mp4 -c:v libtheora -q:v 7 -c:a libvorbis -q:a 4 keynote.ogv
```
Upload the videos to an open source friendly location. In 2018 this was
archive.org. Blog and Tweet the location via SeaGL channels.
