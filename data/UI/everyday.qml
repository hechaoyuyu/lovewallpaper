import QtQuick 1.0

Rectangle {
    id: mainWindow
    anchors.centerIn : parent
    color:"#f3f3f3"
        Component.onCompleted: {
        nav_bar.daystate = "pressed";
        
        
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
        model: everymodel
        anchors.fill:parent
        cellWidth:(imagegrid.width )/ imagenum -1
        cellHeight:(imagegrid.cellWidth)
        anchors.centerIn : mainWindow
        delegate: picture_component


        Component {
                id:picture_component

                Rectangle{
                    id:skin_cup
                    width:imagegrid.cellWidth
                    height:imagegrid.cellHeight
                    color:"#D8D8D8"

                    Rectangle {

                    id:picturecup
                    width:(imagegrid.cellWidth) * 0.95
                    height:picturecup.width
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
                        source:model.image
                        anchors.centerIn: parent
                        opacity:0
                          states:State { name: 'loaded'; when: img.status == Image.Ready
                             PropertyChanges { target: img; opacity: 1 }
                         }

                        
                        transitions: Transition {
                             PropertyAnimation { target: img; properties: "opacity";duration: 500;}
                         }


                        Rectangle {
                            id:about_the_day
                            width:img.width
                            height:img.height * 0.25
                            color:"black"
                            anchors.bottom:img.bottom
                            opacity:0.30



                        }
                            Column{
                                anchors.left:about_the_day.left
                                anchors.leftMargin:5
                                anchors.verticalCenter:about_the_day.verticalCenter

                                Text{
                                    text:model.name
                                    color:"white"
                                    font.pointSize:18



                                }
                                Text{
                                    text:model.total + "张"
                                    color:"white"
                                    font.pointSize:15
                                }
                            }

                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: { controller.thingSelected(model.image, model.name, model.total, model.url) }
                            onEntered: {
                          
                               console.log("Right mouse button pressed " + model.key )
                          }

                        }
                   }


                }
             }
        }



        
     }
 }
 }