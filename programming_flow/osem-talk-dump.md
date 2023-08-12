# SQL for dumping proposal information from OSEM

Having a spreadsheet of the proposals is invaluable for scheduling. That requires a dump of more information than we're able to get from the OSEM csv export.

**Note:** This is currently affected by [SeaGL/organization#165](https://github.com/SeaGL/organization/issues/165).

```sql
   SELECT events.id                                                                     AS `Event ID`,
          events.title                                                                  AS `Title`,
          event_schedules.start_time                                                    AS `Start time`,
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
          GROUP_CONCAT(CONCAT(vote_users.username, ":", votes.rating) SEPARATOR "\n")   AS `Votes`,
          SUM(votes.rating)                                                             AS `Vote Sum`,
          AVG(votes.rating)                                                             AS `Vote Average`
     FROM events
LEFT JOIN event_types
       ON event_types.id                    = events.event_type_id
LEFT JOIN event_schedules
       ON event_schedules.event_id          = events.id
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
    WHERE conferences.short_title           = "seagl2023"
 GROUP BY events.id
```

## Example usage

Open the Rails console:

```bash
RAILS_ENV='production' bundle exec rails console
```

Run the query and export to CSV:

```ruby
sql = File.read('list-proposals.sql')
result = ActiveRecord::Base.connection.exec_query(sql)

CSV.open('proposals.csv', 'w', headers: result.columns, write_headers: true) do |csv|
  result.each { |row| csv << row }
end
```
