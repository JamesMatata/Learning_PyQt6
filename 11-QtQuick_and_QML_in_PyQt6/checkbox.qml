import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating Checkboxes"

    Column {
        anchors.centerIn:parent
        spacing: 10
        CheckBox {
            checked:true
            id:python
            text:"Python"
            font.pixelSize: 20
        }

        CheckBox {
            id:cplusplus
            text:"C++"
            font.pixelSize: 20
        }

        CheckBox {
            id:java
            text:"Java"
            font.pixelSize: 20
        }

        CheckBox {
            id:kotlin
            text:"Kotlin"
            font.pixelSize: 20
        }
        
    }
}