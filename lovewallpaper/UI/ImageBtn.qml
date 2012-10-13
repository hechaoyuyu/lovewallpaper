import QtQuick 1.0
Rectangle{
	id:button
	width:200
	height:40
	property alias text : btn_text.text
	color:"transparent"
	border.color:"transparent"
	states:State {
		name: "enter"; when: mouseArea.containsMouse
		PropertyChanges { target: button;  color:"#b60400"}
		PropertyChanges { target: button;  border.color:"white"}
	 }

 	 transitions:Transition {
	             
	             ColorAnimation { target: button; duration: 150}
	         }
	Text{
		id:btn_text
		font.pointSize: 13
		anchors.centerIn: parent
		text:""
		color:"white"
	}
	MouseArea {
		id:mouseArea
		anchors.fill:button
		hoverEnabled: true
			 
	}
}