import QtQuick 1.0

Rectangle{
		id:detailcontainer
		anchors.centerIn:parent
		width:parent.width*0.6
		height:parent.height*0.6
		z:1
		color:"transparent"
		opacity:0



	Rectangle{
		id:detailform
		anchors.centerIn:parent
		width:parent.width
		height:parent.height
		color:"black"
		z:1
		opacity:0.6
	}

	Rectangle{
		id:detailform_header
		width:detailform.width
		height:detailform.height/9
		anchors.top:detailform.top
		anchors.left:detailform.left
		color:"black"
		z:2
	}

	Text{
		anchors.left:detailform_header.left
		anchors.leftMargin:20
		anchors.verticalCenter:detailform_header.verticalCenter 
		color:"white"
		text:detailtitle
		font.pointSize: 18
		z:2
	}


	GridView {
	        id: kvgrid
	       
	       anchors.top:detailform_header.bottom
	       anchors.left:detailform_header.left
	       anchors.leftMargin:20
	       anchors.topMargin:20
	        width:detailform.width
	        height:150
	        cellWidth:detailform.width
        	        cellHeight:30
        	        model:kvmodel
        	        z:2
        	        delegate:Component{
        	        			Row{
        	        				Text{
        	        					font.pointSize: 16
        	        					color:"white"
        	        					text:model.key
        	        					}

        	        				Text{
        	        					font.pointSize: 16
        	        					color:"white"
        	        					text:model.value
        	        				}

        	        			}
        	        		


        	        }
        	    }

        	    GridView {
	        id: tagsgrid
	       
	       anchors.top:kvgrid.bottom
	       anchors.left:detailform.left
	        width:detailform.width
	        height:(detailform.height - detailform_header.height) /2
	        cellWidth:detailform.width / 4
        	        cellHeight:40
        	        model:tagsmodel
        	        z:2
        	        delegate:Component{

        	        			Rectangle{
        	        				width:tagsgrid.cellWidth
        	        				height:tagsgrid.cellHeight
        	        				color:"transparent"
        	        				Tag{
        	        					
        	        					
        	        					text:model.name
        	        					
        	        					MouseArea{
        	        						anchors.fill:parent
        	        						onClicked:{
        	        							hideDetail.start()
        	        							hideDetail.complete()
        	        							controller.toTag(model.name,model.url)
        	        						}
        	        					}
        	        					}
        	        				}
        	        				
        	        }
        	    }
 }