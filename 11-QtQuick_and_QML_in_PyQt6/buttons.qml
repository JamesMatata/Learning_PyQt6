import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Button Example"

    Button {
        text:"Click Me"
        id:mybutton
        //y:70
        //x:70
        //height:40
        //width:150
        anchors.centerIn:parent
        background:Rectangle {
            implicitWidth: 150
            implicitHeight: 40
            color:button.down ? "lightblue" : "lightgray"
            border.color: "blue"
            border.width: 1
            radius: 4
        }
        onClicked: {
            window.hello()
        }

    }
}