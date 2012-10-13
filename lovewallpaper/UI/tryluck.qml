import QtQuick 1.0

Rectangle {
    id: mainWindow
    anchors.centerIn : parent
    color:"#f3f3f3"
        Rectangle{
            id:bottombar
            height:55
            width:parent.width
            color:"black"
            opacity:0.6
            anchors.bottom:parent.bottom
            z:1

                            }

            FreshButton{
                z:2
                anchors.centerIn:bottombar
                    text:"再试一次"
                    MouseArea{
                        anchors.fill:parent
                        
                        onClicked:{
                            controller.tryAgain()
                        }
                    }
            }

    GridView {
        id: imagegrid
        model: datamodel
        anchors.fill:parent
        
        anchors.topMargin:5
        anchors.bottomMargin:60
        height :parent.height
        cellWidth:(imagegrid.width  )/ imagenum - 1
        cellHeight:(imagegrid.cellWidth) * bili
        anchors.centerIn : mainWindow
        onFlickEnded: atYEnd ?  controller.nextPage():console.log(" NotEnd ")



        delegate: Component {

                    Rectangle{
                        id:skin_cup
                        width:imagegrid.cellWidth
                        height:imagegrid.cellHeight
                        color:"transparent"
                        
                      
                        CustomImage{
                            id:picturecup
                        }

                 }
        }



        
     }
 
 }