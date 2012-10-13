import QtQuick 1.0

Rectangle {
	id: mainWindow
	color:"black"
	anchors.fill:parent
	focus: true
	Keys.onPressed: {
	         if (event.key == Qt.Key_Left) {
	             controller.prevPicture()
	             event.accepted = true;
	         }
	         else if (event.key == Qt.Key_Right){
                 	controller.nextPicture()
                 }
                 	
	 }

	   Image{
	   	id:img
	   	source:"file:"+ myimage.url
	   	anchors.fill:parent
	   	asynchronous :true
		smooth: true
		anchors.centerIn: parent
		fillMode: Image.PreserveAspectCrop

		
	}
		MouseArea {
		id:msarea
		anchors.fill: img
		hoverEnabled: true
		onDoubleClicked:{
		
			controller.lookit(myimage.url)
			
		}
		onClicked: {
				
			
			if (lotswidget.opacity == 1){
					shownav.complete()	
					hidenav.start()
				}
			else{
					hidenav.complete()
					shownav.start()

				}
					

		}
	  }

	   NavWidget{
		id:lotswidget
		PropertyAnimation { id: shownav; target:lotswidget; property: "opacity"; to: 1 ; duration: 300 }
		PropertyAnimation { id: hidenav; target:lotswidget; property: "opacity"; to: 0 ; duration: 300 }
	
	Rectangle{
		id:buttonbar
		color:"black"
		width:parent.width
		height:50
		opacity:0.6
		anchors.bottom:parent.bottom
	}

	Row{
		spacing:10
		anchors.centerIn:buttonbar

		ImageBtn{
			text:"预览壁纸"
			MouseArea{
				anchors.fill:parent
				onClicked: { 
					
					controller.lookit(myimage.url)
					
				}
			}

		}
		ImageBtn{
			text:"设置壁纸"
			color:"darkgreen"
			border.color:"white"
			MouseArea{
				anchors.fill:parent
				onClicked: { 
					
					controller.puresetWallpaper(myimage.url)
							
				}
			}
		}
		ImageBtn{
			text:"删除壁纸"
			MouseArea{
				anchors.fill:parent
				onClicked: { 
					
					controller.deleteWallapper(myimage.url)
							
				}
			}
		}
	}
	}


				   
				  
		
	 
 }