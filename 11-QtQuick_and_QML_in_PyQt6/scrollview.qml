import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating A ScrollView"

    ScrollView {
        width:400
        height:250

        Label {
            text: "Python"
            font.pixelSize: 224
        }
    }

}