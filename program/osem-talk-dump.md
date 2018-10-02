# SQL for dumping proposal information from OSEM

Having a spreadsheet of the proposals is invaluable for scheduling. That requires a dump of more information than we're able to get from the OSEM csv export.

This is valid as of the OSEM installation in August, 2018.

This SQL includes several fields that aren't used in the scheduling process and make it tricky to import the csv. The fields we can drop the next time around are:

* abstract
* comments

```sql
   SELECT events.id                                                                     AS `Event ID`,
          events.title                                                                  AS `Title`,
          events.abstract                                                               AS `Abstract`,
          events.start_time                                                             AS `Start time`,
          speaker_user.name                                                             AS `Speaker`,
          speaker_user.email                                                            AS `Speaker Email`,
          events.proposal_additional_speakers                                           AS `Additional Speakers`,
          submitter_user.name                                                           AS `Submitter`,
          submitter_user.email                                                          AS `Submitter Email`,
          event_types.title                                                             AS `Event Type`,
          event_types.length                                                            AS `Event Length (Minutes)`,
          tracks.name                                                                   AS `Track`,
          difficulty_levels.title                                                       AS `Difficulty Level`,
          rooms.name                                                                    AS `Room`,
          events.state                                                                  AS `State`,
          ( SELECT GROUP_CONCAT(CONCAT(users.name, ":", comments.body) SEPARATOR "\n")
              FROM comments
              JOIN users
                ON users.id = comments.user_id
             WHERE comments.commentable_type        = "Event"
               AND comments.commentable_id          = events.id
          )                                                                             AS `Comments`,
          events.diversity                                                              AS `Diversity`,
          events.first_time                                                             AS `First Time Speaker`,
          GROUP_CONCAT(CONCAT(vote_users.name, ":", votes.rating) SEPARATOR "\n")       AS `Votes`,
          SUM(votes.rating)                                                             AS `Vote Sum`,
          AVG(votes.rating)                                                             AS `Vote Average`
     FROM events
LEFT JOIN event_types
       ON event_types.id                    = events.event_type_id
LEFT JOIN tracks
       ON tracks.id                         = events.track_id
LEFT JOIN difficulty_levels
       ON difficulty_levels.id              = events.difficulty_level_id
LEFT JOIN programs
       ON programs.id                       = events.program_id
LEFT JOIN conferences
       ON conferences.id                    = programs.conference_id
LEFT JOIN rooms
       ON rooms.id                          = events.room_id
LEFT JOIN votes
       ON votes.event_id                    = events.id
LEFT JOIN users                             AS vote_users
       ON vote_users.id                     = votes.user_id
LEFT JOIN event_users                       AS event_users_speaker
       ON event_users_speaker.event_id      = events.id
      AND event_users_speaker.event_role    = "speaker"
LEFT JOIN users                             AS speaker_user
       ON speaker_user.id                   = event_users_speaker.user_id
LEFT JOIN event_users                       AS event_users_submitter
       ON event_users_submitter.event_id    = events.id
      AND event_users_submitter.event_role  = "submitter"
LEFT JOIN users                             AS submitter_user
       ON submitter_user.id                 = event_users_submitter.user_id
    WHERE conferences.short_title           = "seagl2018"
 GROUP BY events.id
```
