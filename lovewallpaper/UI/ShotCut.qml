import QtQuick 1.0

Rectangle{
    id:father
    height:parent.height/3
    width:parent.width
    color:"transparent"
    anchors.bottom:parent.bottom
    anchors.left:parent.left

    Rectangle{
    	anchors.fill:parent
    	color:"black"
    	opacity:0.4
    }

    Row{
    	spacing:10
    	anchors.centerIn:parent
        Rectangle{
            id:setpaper
            anchors.verticalCenter:parent.verticalCenter
            width:father.width / 3 -1
            height:20
            color:"transparent"
            
            states:State {
                name: "enter"; when: mouseArea.containsMouse
                PropertyChanges { target: setpaper;  color:"#b60400"}
            }
              MouseArea{
                    z:1
                   
                    id:mouseArea
                    anchors.fill:parent
                    onClicked: { controller.setWallpaper(model.url) }
                }
            Text{
                anchors.centerIn:parent
                text:"设置壁纸"
                color:"white"
                font.pointSize: 16
              
        }
        }
        Rectangle{
            id:delpapaer
            anchors.verticalCenter:parent.verticalCenter
            width:father.width / 3 -1
            height:20
            color:"transparent"
            states:State {
                name: "enter"; when: mouseAreadel.containsMouse
                PropertyChanges { target: delpapaer;  color:"#b60400"}
            }

            Text{
                anchors.centerIn:parent
                text:"删除"
                color:"white"
                font.pointSize: 16
            }
            MouseArea{
                    id:mouseAreadel
                    z:1
                    
                    anchors.fill:parent
                    onClicked: { controller.deleteWallapper( model.url) }
                }

        }


    }
}