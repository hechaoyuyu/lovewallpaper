import QtQuick 1.0
import "randombg.js" as Random
Rectangle {

                    id:picturecup
                    width:parent.width * 0.95
                    height:parent.height * 0.95
                    anchors.centerIn : parent

                    ShadowRectangle {
                            anchors.centerIn: parent; width: picturecup.width; height: picturecup.height
                            color: "black"
                        }
                    NumberAnimation {
                             id: animation
                             target: parent
                             properties: "y"
                             to:Random.getInt(skin_cup.y) - 7
                             duration: 200;
                         }
                        NumberAnimation {
                             id: animation_small
                             target: parent
                             property: "y"
                             to: Random.getInt(skin_cup.y) + 7
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

                        states:[State { name: 'loaded'; when: img.status == Image.Ready
                             PropertyChanges { target: img; opacity: 1 }
                         }]

                        
                        transitions: Transition {
                             PropertyAnimation { target: img; properties: "opacity";duration: 500;}
                             
                         }
                        
                        MouseArea {
                            id:mouseArea
                            anchors.fill: parent
                            hoverEnabled: true
                            z:1
                            onClicked: { controller.thingSelected(model.buddy, model.key, model.small, model.big, model.original, model.detail) }
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