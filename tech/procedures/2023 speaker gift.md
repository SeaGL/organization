# 2023 speaker gift

The 2023 speaker gift was a SeaGL-branded programmable USB macropad with three keyboard keys and a push-button rotary encoder.

## Programming

The macropad uses the popular [CH552] microcontroller. A variety of open source projects are available for programming it, and we’ve found [ch57x-keyboard-tool] by Mikhail Trishchenkov to be a straightforward and reliable choice.

Example usage:

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

[CH552]: https://hackaday.com/2023/03/03/all-the-usb-you-can-do-with-a-ch552/
[ch57x-keyboard-tool]: https://github.com/kriomant/ch57x-keyboard-tool
