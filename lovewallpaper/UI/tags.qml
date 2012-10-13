import QtQuick 1.0



Rectangle{

	id: tagsWindow
	anchors.centerIn : parent
	color:"#f3f3f3"

	
	GridView {
	        id: textgrid
	       
	        anchors.fill:parent
	        anchors.centerIn : tagsWindow
	        cellWidth:(tagsWindow.width )/ 4 -1
        	        cellHeight:55
        	        model:tagsmodel

        	        	Rectangle{
        	       		id:bottombar
		    height:55
		    width:parent.width
		    color:"black"
		    opacity:0.6
		    anchors.bottom:parent.bottom

                            }

                            FreshButton{
                            	z:1
                            	anchors.centerIn:bottombar
                                    text:"再试一次"
                                    MouseArea{
                                    	anchors.fill:parent
                                    	
                                    	onClicked:{
                                    		controller.randomTag()
                                    	}
                                    }
                            }
	        

        	        delegate:Component{

	         		Rectangle{
	         			width:textgrid.cellWidth
				height:textgrid.cellHeight
				color:"transparent"

				Tag{
					anchors.centerIn : parent
					
				}

		}
		}

	                
	             
	        



	        
	     }
	    
}
