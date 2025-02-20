import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating ComboBox"

    Column {
        anchors.centerIn:parent
        spacing: 40
        ComboBox {
            id:comboBox
            width: 200
            model: ["Python", "C++", "Java", "Kotlin"]
            font.pixelSize: 18
            onActivated: {
                mylabel.text = comboBox.currentText + " is selected"
            }
        }

        Label {
            id:mylabel
            text: "---[]----[]---"
            font.pixelSize: 20
            font.bold: true
        }
    }

}