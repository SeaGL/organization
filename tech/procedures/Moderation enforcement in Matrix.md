# Moderation enforcement in Matrix

When a [decision has been made][code of conduct] to expel a user from SeaGL’s community spaces, the decision can be enforced by the Matrix bot [mjolnir]. This is controlled from within an invite-only Matrix room.

## Commands

### List existing bans

```
!mjolnir rules
```

### Ban a user for a code of conduct violation

```
!mjolnir ban coc user <ID> [reason]
```

Examples:

- `!mjolnir ban coc user @spammer:example.com spam`
- `!mjolnir ban coc user @harasser:example.com targeted harassment`

### Unban a user

```
!mjolnir unban coc user <ID>
```

## Escalation

If these commands aren't enough and you can't figure out the solution quickly, or you otherwise need more help, call AJ over the phone network or Signal (phone number is in the control room description).

## Reference

- [Moderator's guide to Mjolnir]

[code of conduct]: https://seagl.org/code_of_conduct
[mjolnir]: https://github.com/matrix-org/mjolnir
[Moderator's guide to Mjolnir]: https://github.com/matrix-org/mjolnir/blob/main/docs/moderators.md
