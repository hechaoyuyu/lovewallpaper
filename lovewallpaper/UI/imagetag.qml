import QtQuick 1.0

Rectangle {
    id: mainWindow
    anchors.centerIn : parent
    color:"#D8D8D8"
    

                

    GridView {
        id: imagegrid
        model: datamodel
        anchors.fill:parent
        cellWidth:(imagegrid.width )/ 5
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
                            height:img.height * 0.4
                            color:"black"
                            anchors.bottom:img.bottom
                            opacity:0.65

                            Column{
                                anchors.left:about_the_day.left
                                anchors.leftMargin:5
                                anchors.verticalCenter:about_the_day.verticalCenter

                                Text{
                                    text:model.name
                                    color:"white"
                                    font.pointSize:24

                                }
                            }

                        }


                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: { controller.thingSelected(model.image, model.name, model.url) }
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