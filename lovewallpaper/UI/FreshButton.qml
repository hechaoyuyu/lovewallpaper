import QtQuick 1.0

            Rectangle{
                id:try_again
                width:110
                height:40
             
                border.color:"grey"
                border.width:2
                color:"#b60400"
                property alias text : button.text
                states: State {
                        name: "enter"; when: mouseArea.containsMouse
                        PropertyChanges { target: try_again;  color:"lightgrey"}
                        PropertyChanges { target: button;  color:"black"}
                    }

                MouseArea{
                    id:mouseArea
                    anchors.fill:parent
                    hoverEnabled: true

                }

                 transitions:Transition {
                             
                             ColorAnimation { target: button; duration: 0}
                         }



                Text{
                    id:button
                    text:""
                    color:"white"
                    font.pointSize: 18
                    anchors.centerIn:parent

                }

            }
        