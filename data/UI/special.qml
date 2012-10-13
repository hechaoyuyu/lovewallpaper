import QtQuick 1.0

Rectangle {
    id: mainWindow
    anchors.centerIn : parent
    color:"#f3f3f3"
    Component.onCompleted: {
        nav_bar.spstate = "pressed";
        
        
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
        model: specials_model
        anchors.fill:parent
        cellWidth:(imagegrid.width )/ titlenum -1
        cellHeight:(imagegrid.cellWidth) * 0.3
        

        delegate:  Component {
       

            Rectangle{
                
                width:imagegrid.cellWidth 
                height:imagegrid.cellHeight 
                color:"transparent"
              
                 MouseArea {
                            id:mouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: { controller.thingSelected(model.name, model.description, model.big, model.detail) }
                            }
                Rectangle{
                    id:specialframe
                    width:parent.width - 5
                    height:parent.height -5
                    anchors.centerIn:parent
                    color:"transparent"
                      states: State {
                        name: "enter"; when: mouseArea.containsMouse 
                        PropertyChanges { target: specialframe;  color:"#d8d8d8"}
                     
                        }
                     Row{
                        width:parent.width
                        height:parent.height

                        Rectangle{
                            border.color:"grey"
                            border.width:2
                            height:parent.height
                            width:parent.height


                            Image{
                                id:img
                                opacity: 0
                                source:model.big
                                width:parent.width
                                height:parent.height
                                       states:State { name: 'loaded'; when: img.status == Image.Ready
                                         PropertyChanges { target: img; opacity: 1 }
                                     }

                                    
                                    transitions: Transition {
                                         PropertyAnimation { target: img; properties: "opacity";duration: 300;}
                                     }
                            }

                        }

                         Column{
                            height:parent.height
                            width:parent.width- parent.height
                                Text{
                                    anchors.left:parent.left
                                    anchors.leftMargin:10
                                    color:"black"
                                    font.pointSize:16
                                    text:model.name
                                }

                                Text{
                                    anchors.left:parent.left
                                    anchors.leftMargin:10
                                    color:"grey"

                                    font.pointSize:11
                                    width:parent.width - 10
                                    text:model.description
                                    
                                    wrapMode:Text.WordWrap
                                }
                            }




                     }   



                }


              }

        }



        
     }
 }
 }