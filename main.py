list2: List[number] = []
def opretor(_1: List[any], _2: number, _3: Image, bool2: bool):
    return bool2

def on_forever():
    global list2
    opretor(list2,
        1,
        images.create_big_image("""
            . # . # . # . # . #
            . # . # . # . # . #
            . # . # . # . # . #
            . # . # . # . # . #
            # # # # # # # # # #
            """),
        True)
    list2 = [0, 1, 0, 0, 1, 0, 1, 8.584798666836784e+24]
    datalogger.log(datalogger.create_cv("3455", pins.digital_read_pin(DigitalPin.P0)),
        datalogger.create_cv("7878698598698",
            pins.map(radio.received_packet(parse_float(opretor(list2,
                            1,
                            images.create_big_image("""
                                # # # # # # # # # #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                """),
                            True))),
                radio.received_packet(parse_float(opretor(list2,
                            1,
                            images.create_big_image("""
                                # # # # # # # # # #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                """),
                            True))),
                radio.received_packet(parse_float(opretor(list2,
                            1,
                            images.create_big_image("""
                                # # # # # # # # # #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                """),
                            True))),
                radio.received_packet(parse_float(opretor(list2,
                            1,
                            images.create_big_image("""
                                # # # # # # # # # #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                """),
                            True))),
                radio.received_packet(parse_float(opretor(list2,
                            1,
                            images.create_big_image("""
                                # # # # # # # # # #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                . # . # . # . # . #
                                """),
                            True))))))
    record.start_recording(record.BlockingState.BLOCKING)
    pins.set_audio_pin(DigitalPin.P0)
    serial.write_value(serial.read_until(serial.delimiters(Delimiters.NEW_LINE)),
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
    datalogger.include_timestamp(FlashLogTimeStampFormat.DAYS)
    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    control.raise_event(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH),
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
basic.forever(on_forever)
