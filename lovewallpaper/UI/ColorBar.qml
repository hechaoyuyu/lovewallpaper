import QtQuick 1.0
Rectangle{
	width:parent.width
	height:45
	anchors.bottom:parent.bottom
	z:1
	color:"transparent"
	Rectangle{
		width:parent.width
		height:45
		anchors.bottom:parent.bottom
		color:"black"
		opacity:0.6
	  

	}
	Row{
		anchors.verticalCenter:parent.verticalCenter
		spacing:10
		Text{
			text:"颜色筛选："
			color:"white"
			font.pointSize: 18

			anchors.verticalCenter:parent.verticalCenter
			anchors.left:parent.left
			anchors.leftMargin:10
		}

		ColorButton{
			source:"coloricon/quanse.png"
	                        MouseArea {
				anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("quanse") }
	                        }
		}
		ColorButton{
			source:"coloricon/duocai.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("duocai") }
	                        }
		}
		ColorButton{
			source:"coloricon/heibai.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("heibai") }
	                        }
		}
		ColorButton{
			source:"coloricon/hongse.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("hongse") }
	                        }
		}

		ColorButton{
			source:"coloricon/chengse.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("chengse") }
	                        }
		}
		ColorButton{
			source:"coloricon/huangse.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("huangse") }
	                        }
		}
		ColorButton{
			source:"coloricon/lvse.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("lvse") }
	                        }
		}
		ColorButton{
			source:"coloricon/qingse.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("qingse") }
	                        }
		}
		ColorButton{
			source:"coloricon/lanse.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("lanse") }
	                        }
		}
		ColorButton{
			source:"coloricon/zise.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("zise") }
	                        }
		}
		ColorButton{
			source:"coloricon/fense.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("fense") }
	                        }
		}
		ColorButton{
			source:"coloricon/zongse.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("zongse") }
	                        }
		}
		ColorButton{
			source:"coloricon/heise.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("heise") }
	                        }
		}
		ColorButton{
			source:"coloricon/baise.png"
	                        MouseArea {
	                        	anchors.fill: parent
				hoverEnabled: true
	                            onClicked: { controller.colorSelected("baise") }
	                        }
		}		
	}
}