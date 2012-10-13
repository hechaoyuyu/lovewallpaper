import QtQuick 1.0

Rectangle {
    id: mainWindow
    anchors.fill:parent
    color:"#f3f3f3"
    
    Component.onCompleted: {
        nav_bar.cgstate = "pressed";
        
        
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
        model: category_model
        anchors.fill:parent
        anchors.topMargin:5
        cellWidth:(imagegrid.width )/ titlenum -1
        cellHeight:(imagegrid.cellWidth) * 0.17
        delegate: picture_component


        Component {
                id:picture_component

                Rectangle{
                    id:skin_cup
                    width:imagegrid.cellWidth
                    height:imagegrid.cellHeight
                    color:"#f3f3f3"

                    Rectangle {

                    id:picturecup
                    width:(imagegrid.cellWidth) * 0.98 -1
                    height:picturecup.width*0.17 - 2
                    color:"#e8e8e8"
                    border.color:"grey"
                    border.width:2
                    anchors.centerIn : skin_cup


                   Image{
                        id:img
                      
                        asynchronous :true
                        smooth: true
                        source:model.bgimage
                        anchors.fill: parent
                        opacity: 0

                        Rectangle{
                            id:cover
                            anchors.fill:parent
                            color:"black"
                            opacity:0
                            states: State{
                              name: 'showit'; when: mouseArea.containsMouse
                             PropertyChanges { target: cover; opacity: 0.3 }
                             }
                        }

                        states:State { name: 'loaded'; when: img.status == Image.Ready
                             PropertyChanges { target: img; opacity: 1 }

                         }

                        
                        transitions: Transition {
                             PropertyAnimation { target: img; properties: "opacity";duration: 200;}
                         }
                        

                        MouseArea {
                            id:mouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: { controller.thingSelected(model.tid, model.name, model.total, model.url) }
                            onEntered: {
                          
                               console.log("Right mouse button pressed " + model.name )
                          }

                        }
                   }
                    Text{
                            color:"black"
                            font.pointSize:28
                            text:model.name
                            
                            anchors.verticalCenter:img.verticalCenter
                            x:40
                            style:Text.Outline
                            styleColor: "white"
                        
                        }


                }
             }
        }



        
     }
 }
 }