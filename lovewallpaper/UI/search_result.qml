import QtQuick 1.0
import "randombg.js" as Random


Rectangle{

	id: tagsWindow
	anchors.centerIn : parent
	color:"white"

	
	GridView {
	        id: textgrid
	       
	        anchors.fill:parent
	        anchors.centerIn : tagsWindow
	        cellWidth:(tagsWindow.width )/ 4 -1 
        	        cellHeight:55
        	        model:tagsmodel
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
