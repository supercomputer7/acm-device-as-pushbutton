# What is repository for?

This is mainly a fast way for me to generate everything needed for setting-up a push button
using a CH340/FTDI ACM device on a Linux machine.

I've used this method for building a dispatching mechanism for a wireless 433MHz doorbell.
I also use this for a push button which sends an MQTT message to one of my IoT gadgets.

## What do I need for this to work?

You will need:
- A USB-to-serial device, which can be an FTDI device or a CH340-based adapter.
- A machine with USB port and Linux-based OS.

It can be valuable to acquire:
- A soldering equipment, if you plan to build something permanent.
- Some sort of enclosure for the serial device, especially if it's a CH340 USB to serial TTL adapter.
- A push button, if you don't plan on connecting to an external microcontroller.

## How do I make this to work then?

Simple, either install a momentary push button between ground and the RX input,
or just connect the RX input to some microcontroller output pin that pulls itself to ground when
you do something interesting with it.

Be aware! that if you use a momentary push button, you don't need to worry about
voltage levels, but if you connect the serial adapter to a microcontroller, you will need
to ensure that you work on the same TTL voltage level.

## How is this even working?

An ordinary UART communication starts with an RX input digital line (doesn't matter which device is considered here, as both have RX and TX pins) being set to HIGH and then pulled to LOW. While my method works because of this, as the serial device thinks that something is transmitting to it, it is not considered an actual UART communication by any means, so proper testing should always be done to ensure the push button actually works.

## But I can use an ESP32 or a Raspberry Pi with its GPIO pins, so what is the actual advantage?

Frankly, if you really want to build a push button for some IoT automation, an ESP32 or a Raspberry Pi
is sufficient for this type of task.

However, if you have an FTDI device or some other USB-to-serial TTL adapter and you need a quick and dirty solution,
this should set you up quite quickly.

# Installation

## Hardware

The simplest approach is to connect a push button between the RX input pin on USB-to-TTL adapter and its ground.
Since it should be easy to do with a breadboard and a couple of jumpers, I'll leave this for you to decide
on the exact shape.

As for using an external microcontroller, make sure you connect the RX input pin to a GPIO of the device which has
the same voltage levels, to avoid damaging your device or the microcontroller.

## Software

### Python script

First, change the command you want to run in `pushbutton.py`:

```python
os.system("/bin/sh -c 'echo hello world!'") # change this to be used for invoking a command upon push button being pressed!
```

to your desired command.

Then, install a new python virtual environment

```sh
python3 -m venv .venv
```

Then install `pyserial`:
```sh
.venv/bin/python3 -m pip install pyserial
```

### Systemd service

Change the settings in `systemd-service.template`:
```
YOUR_DESIRED_PROGRAM_PATH/.venv/bin/python3 YOUR_DESIRED_PROGRAM_PATH/pushbutton.py
```
Then copy that file into the `/etc/systemd/system/` directory. Any name with `.service` will be good here.
Don't forget to enable the service.

### Udev rules

Don't forget to find the serial number of your ACM device and adjusting with `udev-rules.template`.
You will need to copy that file to `/etc/udev/rules.d/`. Give it a name like `10-local.rules` in that directory.
