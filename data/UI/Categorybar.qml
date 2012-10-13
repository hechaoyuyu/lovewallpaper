import QtQuick 1.0


Rectangle{
            id:nav_bar

            property alias cgstate : cgbtn.btn_state
            property alias spstate : spbtn.btn_state
            property alias daystate : daybtn.btn_state
            property alias topstate : topbtn.btn_state

            width:parent.width
            anchors.top:parent.top
            height:50
            color:"#d9d9d9"
            z:1

            Row{
                spacing:20
                anchors.left:nav_bar.left
                anchors.leftMargin:20
                height:nav_bar.height

                    Button {
                            id:cgbtn
                            width: 60; height: 40
                            text:"分类"
                            idtext:"Category"
                            anchors.verticalCenter:parent.verticalCenter

                        }
                

                    Button {
                            id:daybtn
                            width: 60; height: 40
                            text:"每日"
                            idtext:"Everyday"
                            anchors.verticalCenter:parent.verticalCenter

                        }
                    Button {
                            id:topbtn
                            width: 60; height: 40
                            text:"排行"
                            idtext:"Top"
                            anchors.verticalCenter:parent.verticalCenter

                        }
                    Button {
                            id:spbtn
                            width: 60; height: 40
                            text:"专题"
                            idtext:"Special"
                            anchors.verticalCenter:parent.verticalCenter

                        }
            }

        }
