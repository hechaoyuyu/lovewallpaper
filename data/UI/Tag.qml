import QtQuick 1.0
import "randombg.js" as Random

Rectangle{
	id:tagrectangle
	property alias text : tag.text
	anchors.centerIn : parent
	color:Random.randomBg()
	height:parent.height - 10
	width:parent.width - 10
	border.color:"grey"
	states: [State {
				name: "enter"; when: mouseArea.containsMouse
				PropertyChanges { target: cover;  opacity:0.3}
				
	 		},
	 		State{
	 			name:"pressed";when: mouseArea.pressed
	 			PropertyChanges { target: cover;  opacity:0.8}
				
	 		}]

	Rectangle{

		id:cover
		anchors.fill:parent
		color:"black"
		opacity:0
	}
	Text{
		id:tag
		font.pointSize:16
		color:"white"
		text:model.name
		anchors.centerIn : parent
		wrapMode: Text.WordWrap
		elide:Text.ElideRight


		
	}
	Image{
		source:"tag_bg.png"
		anchors.right:tagrectangle.right
		anchors.bottom:tagrectangle.bottom
	}
	 MouseArea {
	 	    id:mouseArea
                            anchors.fill: tagrectangle
                            hoverEnabled: true
                            onClicked: { controller.thingSelected(model.name, model.name, model.bgimage, model.url) }
                            onEntered: {
                          
                               console.log("Right mouse button pressed " + model.name )
                          }

              }
}