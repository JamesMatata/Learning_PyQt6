import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating MenuBar"

    MenuBar {
        Menu {
            title: "File"
            Action {text: "New"}
            Action {text: "Open"}
            Action {text: "Save"}
            Action {text: "Exit"}
        }
        Menu {
            title: "Edit"
            Action {text: "Cut"}
            Action {text: "Copy"}
            Action {text: "Paste"}
        }

        Menu {
            title: "Help"
            Action {text: "About"}
        }
    }

}