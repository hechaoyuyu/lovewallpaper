import QtQuick 1.0
import "randombg.js" as Random

Rectangle {
    id: mainWindow
    anchors.centerIn : parent
    color:"#f3f3f3"
    


    Rectangle{
        anchors.fill:parent
        
        color:"transparent"                

    GridView {
        id: imagegrid
        model: datamodel
        anchors.fill:parent
        cellWidth:(imagegrid.width  )/ imagenum - 1
        cellHeight:imagegrid.cellWidth * bili
        anchors.centerIn : mainWindow

        delegate: picture_component

    
        

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



                   Image{
                        id:img
                        width:picturecup.width
                        height:picturecup.height
                        asynchronous :true
                        smooth: true
                        source:"file:"+model.url
                        anchors.centerIn: parent
                        fillMode: Image.PreserveAspectFit
                        opacity: 0

                        ShotCut{
                            id:shotcut
                            opacity:0
                            z:1
                            states:State{
                              name: 'showshotcut'; when: mouseArea.containsMouse
                             PropertyChanges { target: shotcut; opacity: 1 }
                             }
                        }

                        states:State { name: 'loaded'; when: img.status == Image.Ready
                             PropertyChanges { target: img; opacity: 1 }
                           
                         }

                        
                        transitions: Transition {
                             PropertyAnimation { target: img; properties: "opacity";duration: 500;}
                         }
                        
                        MouseArea {
                            id:mouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: { controller.thingSelected(model.index, model.url) }
                            onEntered:{

                            }
                            

                            onExited:{

                            }

                        }
                   }


                }
             }
        }



        
     }
 }
 }