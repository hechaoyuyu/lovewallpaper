import QtQuick 1.0
 
Item {
	property alias color : button.color
	property alias text : button_text.text
	property alias idtext : target_id.text
	property alias btn_state : button.state
	MouseArea {
			id:mouseArea
			anchors.fill: parent
			hoverEnabled: true
			onClicked: { 
				controller.NavClicked(target_id.text) 
			}
	  }
	Text{
		id:button_text
		color:"black"
		text:"Text"
		font.pointSize: 18
		anchors.centerIn:button
		z:1
		Text{
			id:target_id
			text:"None"
			opacity:0
		}
	}

	Rectangle { id: button ; anchors.fill: parent ;color:"#d9d9d9"
		states: [State {
				name: "enter"; when: mouseArea.containsMouse && button.state != "pressed"
				PropertyChanges { target: button;  color:"#b60400"}
				PropertyChanges { target: button_text;  color:"white"}
	 		},
	 		State{
	 			name:"pressed";
	 			PropertyChanges { target: button;  color:"#b60400"}
				PropertyChanges { target: button_text;  color:"white"}
	 		}]

	 	 transitions:Transition {
		             
		             ColorAnimation { target: button; duration: 0}
		         }
	}
}