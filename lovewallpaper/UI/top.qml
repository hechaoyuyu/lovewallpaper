import QtQuick 1.0
import "randombg.js" as Random
Rectangle {
    id: mainWindow
    anchors.centerIn : parent
    color:"#f3f3f3"
    Component.onCompleted: {
        nav_bar.topstate = "pressed";
        
        
        }
     Categorybar{
            id:nav_bar
    }

    Rectangle{
        anchors.top:nav_bar.bottom
        width:mainWindow.width
        height:mainWindow.height - nav_bar.height
        color:"transparent"

                

    GridView {
        id: imagegrid
        model: datamodel
        anchors.fill:parent
        cellWidth:(imagegrid.width  )/ imagenum - 1
        cellHeight:(imagegrid.cellWidth) *bili
        anchors.centerIn : mainWindow
        anchors.topMargin:5
        delegate: picture_component
        onFlickEnded: atYEnd ?  controller.nextPage():console.log(" NotEnd ")
    
        

        Component {
                id:picture_component

                Rectangle{
                    id:skin_cup
                    width:imagegrid.cellWidth
                    height:imagegrid.cellHeight
                    color:"transparent"

                    Rectangle {

                    id:picturecup
                    width:(imagegrid.cellWidth) * 0.95
                    height:picturecup.width*bili
                    anchors.centerIn : skin_cup

                    ShadowRectangle {
                            anchors.centerIn: parent; width: picturecup.width; height: picturecup.height
                            color: "black"
                        }

                    NumberAnimation {
                             id: animation
                             target: skin_cup
                             property: "y"
                             to:Random.getInt(skin_cup.y) - 5
                             duration: 200;
                         }
                        NumberAnimation {
                             id: animation_small
                             target: skin_cup
                             property: "y"
                             to: Random.getInt(skin_cup.y) + 5
                             duration: 200;
                         }

                   Image{
                        id:img
                        width:picturecup.width
                        height:picturecup.height
                        asynchronous :true
                        smooth: true
                        source:model.small
                        anchors.centerIn: parent
                        opacity: 0

                        states:State { name: 'loaded'; when: img.status == Image.Ready
                             PropertyChanges { target: img; opacity: 1 }
                         }

                        
                        transitions: Transition {
                             PropertyAnimation { target: img; properties: "opacity";duration: 500;}
                         }
                        
                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: { controller.thingSelected(model.buddy, model.key, model.small, model.big, model.original, model.detail, place) }
                            onEntered:{
                                animation_small.complete()
                                animation.start()
                            }
                            

                            onExited:{
                                animation.complete()
                                animation_small.start()
                            }

                        }
                   }


                }
             }
        }



        
     }
 }
 }