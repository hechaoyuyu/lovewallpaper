import QtQuick 1.0
Rectangle{
	anchors.fill:parent
	color:"transparent"
	z:1
	opacity:1
//////////////////////////////////////
	Rectangle{
		id:navbar
		color:"black"
		width:parent.width
		height:50
		opacity:0.6
	}
	Image{
		id:backimg
		source:"return.png"
		anchors.left:navbar.left
		anchors.leftMargin:5
		anchors.verticalCenter:navbar.verticalCenter

		MouseArea{
			anchors.fill:parent

			onClicked:controller.go_back()
		}
	}
	Text{
		id:viewtext
		anchors.left:backimg.right
		anchors.verticalCenter:navbar.verticalCenter
		text:"预览"
		font.pointSize: 18
		color:'white'
	}
	Text{

		anchors.left:viewtext.right
		anchors.leftMargin:10
		anchors.verticalCenter:navbar.verticalCenter
		text:"(您可以可以使用键盘方向键左右切换图片)"
		font.pointSize: 11
		color:'white'
	}
//////////////////////////////////////
	NavCricle{
		id:navicon_right
		anchors.rightMargin:20
		 anchors.right:parent.right
		 source:"right.png"

		states: [State {
			name: "enter"; when: mouseArea_right.containsMouse
			PropertyChanges { target: navicon_right;  width:50 ; height:50}
			
 		},
 		State{
 			name:"pressed";when:  mouseArea_right.pressed
 			PropertyChanges { target: navicon_right;  width:50;height:50}
			
 		}]

		 MouseArea {
		 	id:mouseArea_right
			anchors.fill: parent
			hoverEnabled: true
			onClicked: { 
				controller.nextPicture()
			 }
			
		}
	}
	NavCricle{
		id:navicon_left
		anchors.leftMargin:20
		 anchors.left:parent.left
		 source:"left.png"

		states: [State {
			name: "enter"; when: mouseArea_left.containsMouse
			PropertyChanges { target: navicon_left;  width:50 ; height:50}
			
 		},
 		State{
 			name:"pressed";when:  mouseArea_left.pressed
 			PropertyChanges { target: navicon_left;  width:50;height:50}
			
 		}]

		 MouseArea {
		 	id:mouseArea_left
			anchors.fill: parent
			hoverEnabled: true
			onClicked: { 
				controller.prevPicture()
			 }
			
		}
	}
//////////////////////////////////////
	

}