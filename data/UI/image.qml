import QtQuick 1.0

Rectangle{
	id: mainWindow
	anchors.centerIn : parent
	color:"white"
	anchors.fill:parent
	focus: true
	    Component.onCompleted: {
       hideDetail.start()
        
        
        }
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
		id:loading
		source:"loading.png"
		anchors.centerIn:parent
		z:1
		smooth:true
		opacity:1
		  SequentialAnimation {
		         running: true
		         loops: Animation.Infinite
		         NumberAnimation { target: loading; property:"rotation";from: 0; to:360; duration: 200;}
		       
		     }
	   	transitions: Transition {
				 PropertyAnimation { target: loading; properties: "opacity";duration: 300;}
			 }

	}


	DetailForm{
		id:detailcontainer
		PropertyAnimation { id: showDetail; target:detailcontainer; property: "opacity"; to: 1 ; duration: 300 }
		PropertyAnimation { id: hideDetail; target:detailcontainer; property: "opacity"; to: 0 ; duration: 300 }
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
			text:"下载壁纸"
			MouseArea{
				anchors.fill:parent
				onClicked: { 
					
					controller.download(myimage.key, myimage.original)
							
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
					
					controller.setWallpaper(myimage.key, myimage.original)
							
				}
			}
		}
		ImageBtn{
			text:"图片详情"
			MouseArea{
				anchors.fill:parent
				onClicked: { 
					
					if (detailcontainer.opacity == 1){
						hideDetail.start()
					}
					else{
						controller.showDetail(myimage.detail)
						showDetail.start()

					}
							
				}
			}
		}
	}
	}


	Image{
	   	id:small_img
	   	source:myimage.small
	   	anchors.fill:parent
	   	asynchronous :true
		smooth: true
		
		anchors.centerIn: parent
		fillMode: Image.PreserveAspectCrop
	   	opacity:0

	   	states:State{
			 	name:'small_loaded';when:small_img.status == Image.Ready

			 	 PropertyChanges { target: small_img; opacity: 1 ;}

			 }

	   	 transitions: Transition {
				 PropertyAnimation { target: small_img; properties: "opacity";duration: 300;}
			 }

	   	Image{
			id:img
			asynchronous :true
			smooth: true
			source:myimage.big
			anchors.centerIn: parent
			fillMode: Image.PreserveAspectCrop
			anchors.fill:parent
			opacity:0
			states:State { name: 'loaded'; when: img.status == Image.Ready
				 PropertyChanges { target: img; opacity: 1;}
				 PropertyChanges { target: loading; opacity: 0;}
			 }

			transitions: Transition {
				 PropertyAnimation { target: img; properties: "opacity";duration: 300;}
			 }

			
			MouseArea {
				id:msarea
				anchors.fill: img
				hoverEnabled: true
						onDoubleClicked:{
		
			controller.lookit(myimage.original)
			
		}
		onClicked: {
				
			hideDetail.start()	
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
		}

		
	   }
	 
 }