let list: number[] = []
function opretor (_1: any[], _2: number, _3: Image, bool: boolean) {
    return bool
}
basic.forever(function () {
    opretor(list, 1, images.createBigImage(`
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        # # # # # # # # # #
        `), true)
    list = [
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    8.584798666836784e+24
    ]
    datalogger.log(
    datalogger.createCV("3455", pins.digitalReadPin(DigitalPin.P0)),
    datalogger.createCV("7878698598698", pins.map(
    radio.receivedPacket(parseFloat(opretor(list, 1, images.createBigImage(`
        # # # # # # # # # #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        `), true))),
    radio.receivedPacket(parseFloat(opretor(list, 1, images.createBigImage(`
        # # # # # # # # # #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        `), true))),
    radio.receivedPacket(parseFloat(opretor(list, 1, images.createBigImage(`
        # # # # # # # # # #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        `), true))),
    radio.receivedPacket(parseFloat(opretor(list, 1, images.createBigImage(`
        # # # # # # # # # #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        `), true))),
    radio.receivedPacket(parseFloat(opretor(list, 1, images.createBigImage(`
        # # # # # # # # # #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        . # . # . # . # . #
        `), true)))
    ))
    )
    record.startRecording(record.BlockingState.Blocking)
    pins.setAudioPin(DigitalPin.P0)
    serial.writeValue(serial.readUntil(serial.delimiters(Delimiters.NewLine)), radio.receivedPacket(RadioPacketProperty.SerialNumber))
    datalogger.includeTimestamp(FlashLogTimeStampFormat.Days)
    serial.redirect(
    SerialPin.P0,
    SerialPin.P1,
    BaudRate.BaudRate115200
    )
    control.raiseEvent(
    radio.receivedPacket(RadioPacketProperty.SignalStrength),
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
    )
})
