import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating Labels & handling Events"

    Column {
        anchors.centerIn:parent
        spacing: 10
        Label {
            id:label1
            text:"This is a Label"
            font.pixelSize: 20
            color:"blue"
            font.bold: true
            font.italic: true

        }
        Button {
            text:"Click Me"
            height: 40
            width: 150
            onClicked: {
                label1.text = "Button Clicked"
            }
        }
    }

}