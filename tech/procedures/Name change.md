# Name change

The names of conference presenters and volunteers are recorded throughout SeaGL’s infrastructure. When someone’s name changes, they may request that SeaGL updated its data accordingly.

## Procedure

Before proceeding, confirm that the person would like their name updated, i.e. don’t assume.

  - Know the correct spelling and preferred usage of their name(s) and pronouns.
  - Consider other information that might need to be updated at the same time, such as email addresses, social media handles, profile images, or biographies.
  - Determine whether it’s sufficient to update only published information or if thoroughly rewriting version history is also necessary.

Review and update as necessary:

 1. Google Workspace:
     1. Staff email:
          - [ ] Name
          - [ ] Email address
          - [ ] Profile image
     1. Documents:
          - [ ] Miscellaneous mentions
          - [ ] Version history

 1. [OSEM](https://osem.seagl.org/) (note [confusing fields](https://github.com/openSUSE/osem/issues/1410)):
     1. Administration → Users → Edit:
          - [ ] Name
          - [ ] Nickname
          - [ ] Email
          - [ ] Biography
     1. Administration → *Conference* → Events → *Event* → Edit:
          - [ ] Miscellaneous mentions in the session description
     1. Rails console:
          - [ ] Username
          - [ ] PaperTrail versions

 1. [Internet Archive](https://archive.org/details/seagl):
     1. Identifier of upload:
          - [ ] Name
     1. Metadata of upload:
          - [ ] Name
          - [ ] Miscellaneous mentions in the session description

 1. [SeaGL website](https://github.com/SeaGL/seagl.github.io):
     1. Archived sessions in `_archive-sessions/*/*.md`:
          - [ ] Name
          - [ ] Pronouns
          - [ ] Gravatar ID
          - [ ] Biography
          - [ ] Linked resources
          - [ ] Miscellaneous mentions in the session description
     1. Blog posts in `_posts/*.md`:
          - [ ] Names in posted schedules
          - [ ] Names, images, and links in presenter features
     1. Git:
          - [ ] Version history

 1. [Public issue tracker](https://github.com/SeaGL/organization/issues):
      - [ ] Miscellaneous mentions

 1. [Meeting notes](https://github.com/SeaGL/organization/tree/main/meetings):
      - [ ] Miscellaneous mentions
