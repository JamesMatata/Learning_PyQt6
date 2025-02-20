import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Rows and Columns in QtQuick"

    Row {
        spacing: 10
        Rectangle {
            width: 100
            height: 50
            color: "red"
        }

        Rectangle {
            width: 100
            height: 50
            color: "blue"
        }

        Rectangle {
            width: 100
            height: 50
            color: "black"
        }
    }

    Column {
        spacing: 10
        Rectangle {
            width: 100
            height: 50
            color: "red"
        }

        Rectangle {
            width: 100
            height: 50
            color: "blue"
        }

        Rectangle {
            width: 100
            height: 50
            color: "black"
        }
    }

}