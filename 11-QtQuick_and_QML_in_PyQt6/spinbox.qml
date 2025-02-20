import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating SpinBox"

    Column {
        anchors.centerIn:parent
        spacing: 40

        Label {
            id:mylabel
            text: "---[]----[]---"
            font.pixelSize: 20
            font.bold: true
        }

        SpinBox {
            id:spinbox1
            value: 50
            from: 0
            to: 100
            stepSize: 1
            editable: true
            validator: IntValidator { bottom: 0; top: 100 }
            font.pixelSize: 18
            padding: 10
            onValueModified: {
                mylabel.text = "SpinBox Value: " + spinbox1.value
            }
        }
    }
}