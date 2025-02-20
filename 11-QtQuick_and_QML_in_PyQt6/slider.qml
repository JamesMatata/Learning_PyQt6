import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating Slider"

    Column {
        anchors.centerIn:parent
        spacing: 40

        Label {
            id:mylabel
            text: "---[]----[]---"
            font.pixelSize: 20
            font.bold: true
        }

        Slider {
            id:slider
            value:50
            from:1
            to:100
            stepSize:5
            font.pixelSize: 18
            onMoved: {
                mylabel.text = "Slider Value: " + slider.value
            }
        }
    }

}