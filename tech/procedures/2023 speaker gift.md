# 2023 speaker gift

The 2023 speaker gift was a SeaGL-branded programmable USB macropad with three keyboard keys and a push-button rotary encoder.

## Preparation

1. Discard the printed instruction pamphlet; it’s primarily for a different product and promotes proprietary software.
1. Peel the protective adhesive layer off of the bottom. Temporarily loosening the screws with a Phillips #1 screwdriver can make this easier.
1. Apply the adhesive rubber feet around the bottom screws. Each foot is a ring with a discardable core.
1. Program a key layout; the factory configuration is `c` on all keys.

## Programming

The macropad uses the popular [CH552] microcontroller. A variety of open source projects are available for programming it, and we’ve found [ch57x-keyboard-tool] by Mikhail Trishchenkov to be a straightforward and reliable choice.

Configure buttons and knob:

```yaml
# config.yml

orientation: normal
rows: 1
columns: 3
knobs: 1
layers:
  - buttons:
      - - play
        - previous
        - next
    knobs:
      - press: mute
        ccw: volumedown
        cw: volumeup
```

```console
$ sudo ch57x-keyboard-tool upload < 'config.yml'
```

Configure LEDs:

- `0` off
- `1` follow button presses
- `2` dance

```console
$ sudo ch57x-keyboard-tool led '1'
```

[CH552]: https://hackaday.com/2023/03/03/all-the-usb-you-can-do-with-a-ch552/
[ch57x-keyboard-tool]: https://github.com/kriomant/ch57x-keyboard-tool
