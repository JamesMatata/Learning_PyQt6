import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Switch Button in QtQuick"

    Column {
        anchors.centerIn:parent
        spacing: 40

        Label {
            id:mylabel
            text: "---[]----[]---"
            font.pixelSize: 20
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Switch {
            id:switchbutton
            checked: true
            font.pixelSize: 18
            anchors.horizontalCenter: parent.horizontalCenter
            onCheckedChanged: {
                if (switchbutton.checked) {
                    mylabel.text = "Switch Button is ON"
                } else {
                    mylabel.text = "Switch Button is OFF"
                }
            }
        }
    }

}