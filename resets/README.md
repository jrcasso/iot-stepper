Reset Procedure:

1. Unplug the Raspberry Pi Pico W
1. Hold the reset button and continue to hold it.
1. Plug in the Raspberry Pi Pico W to the computer.
1. Observe the Raspberry Pi Pico W is handled as removable file storage.
1. Place one of the following `.uf2` files:
    - `flash_nuke.uf2` does a hard reset of the file system and any files you've placed here.
    - `RPI_PICO_W*` flashes MicroPython onto the controller, which may be necessary after flash nuking.
